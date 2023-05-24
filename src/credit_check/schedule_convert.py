# -*- coding: utf-8 -*-

import re
import pdfplumber
from modules.course import Course
from modules.dir_operate import list_format_file
from modules.settings import convert_text

def course_type_credit(text):
    """
    For each course type, extract its name and credit
    e.g. "1. 通识课 32.5 学分"
    """
    pattern_list = [
        r"\d\.(\S{3,5})", # course name
        r"(\d{1,2}\.?\d?)" # course credit
    ]
    pattern = '\s?'.join(pattern_list)
    target = re.compile(pattern).findall(text)
    course_dict = {key: float(value) for key, value in target}
    
    return course_dict

def every_course(text):
    """
    For each course, extract its name, semester. Semester is the smaller year
    and semester id (1 or 2).
    Normal e.g. "16330060 会计制度设计 2.0 2023-2024 2 考查 专业选修课"

    Note1: If name starts with English letter, there is no space between id and
    name.
    e.g. "16340076RPA智能财务机器人 1.0 2024-2025 1 考查 实践必修课"

    Note2: Some courses don't have exam form, so i can't to extract course type 
    directly. Extract the exam form and course type together, and then split by
    space.
    e.g. "04332021 高等数学B(Ⅱ) 4.0 2021-2022 2 学科基础课"
    """

    for key, value in convert_text.items():
        text = text.replace(key, value)
    pattern_list = [
        r"(\d{8})", # course accession number
        r"(\S+)", # course name
        r"(\d{1,2}\.?\d?)", # credit
        r"(\d{4}\-\d{4})", # year
        r"(\d)", # semester
        r"(.*)\n" # exam (may not) and course type
    ]
    pattern = '\s?'.join(pattern_list)
    target = re.compile(pattern).findall(text)
    course_list = []

    for line in target:
        course = Course(
            name = line[1],
            type = line[-1].split()[-1],
            credit = line[2],
            score = 0,
            semester = line[3].split('-')[0] + '_' + line[4]
        )
        course_list.append(course)
        
    return course_list


def run(
    schedule_dir,
    must_types,
    enter_year,
    now_grade,
    now_semester,
    signal_pct,
    signal_now
):
    """
    main function
    """
    # Get semesters form enter_year, now_grade, now_semester
    years = range(enter_year, enter_year + now_grade)
    semesters = ["%d_%d" % (i, j) for i in years for j in [1, 2]]

    # If semester is 1, remove the last semester.
    if now_semester == 1:
        semesters.pop()

    major_course = {}
    file_names = list_format_file(schedule_dir, "pdf")
    total_len = len(file_names)

    for i, file_name in enumerate(file_names):
        # get pdf full name, and change to yaml name to store course info
        pdf_file = schedule_dir + '/' + file_name
        major_name = file_name.replace(".pdf", '')

        progress_pct = int(i / total_len * 100)
        signal_pct.emit(progress_pct)
        # signal_now.emit(major_name)
        signal_now.emit("(%d/%d)%s" % (i + 1, total_len, major_name))
        
        # parse pdf into text
        with pdfplumber.open(pdf_file) as pdf:
            text = '\n'.join(i.extract_text() for i in pdf.pages)
            text = re.sub(r"(\S+) ([A-Z])", "\\1\\2", text)

        # match the courses' name and semester
        course_dict = {
            "credit": course_type_credit(text),
            "must_now": {},
            "must_later": {},
            "select": {},
        }

        for course in every_course(text):
            if course.type not in must_types:
                course_dict["select"][course.name] = course
            elif course.semester in semesters:
                course_dict["must_now"][course.name] = course
            else:
                course_dict["must_later"][course.name] = course
        
        major_course[major_name] = course_dict

    signal_pct.emit(100)
    return major_course


if __name__ == "__main__":
    pass
    # run(
    #     schedule_dir = schedule_dir,
    #     yaml_dir = yaml_dir,
    #     must_types = must_types,
    #     enter_year = enter_year,
    #     now_grade = now_grade,
    #     now_semester = now_semester
    # )