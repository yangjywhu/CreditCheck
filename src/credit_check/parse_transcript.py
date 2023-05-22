import os
import re
from collections import OrderedDict
from docxtpl import DocxTemplate
from openpyxl import Workbook

from modules import Student, create_dir, list_to_course


def extract_course(text, discard_course):
    """
    Extract the course from transcript.
    """
    pattern = re.compile(r"(\S+)\s(\S{2,3})\s(\d\.?\d?)\s(\d{1,3})")
    courses = pattern.findall(text)
    courses = list_to_course(courses)
    courses = [i for i in courses if i.name not in discard_course]
    
    return courses


def run(
    major_course,
    must_types,
    enter_year,
    transcript_dir,
    template_file,
    out_dir,
    pass_score,
    same_course,
    discard_course,
    signal_pct,
    signal_now,
):
    create_dir(out_dir)
    out_xlsx = out_dir + "/Summary.xlsx"
    file_names = os.listdir(transcript_dir)
    total_len = len(file_names)
    
    cols = [
        "班级", "姓名", "学号", # 0 - 2
        "专业必完成科目", "专业必GPA", "必修课转换", # 3 - 5
        "专业选完成科目", "选修课转换", # 6 - 7
        "必须完成的类型", "必修未完成数目", "必修未完成科目", # 8 - 10
        "专业选应", "专业选实", "通识选应", "通识选实", # 11 - 14
    ]

    # create a excel workbook
    wb = Workbook()
    sheet = wb.active
    sheet.append(cols)
    
    for i, file_name in enumerate(file_names):
        # Set the file path
        stu_str, _ = os.path.splitext(file_name)
        in_file = transcript_dir + '/' + file_name
        
        # Set progress bar
        progress_pct = int(i / total_len * 100)
        signal_pct.emit(progress_pct)
        signal_now.emit(stu_str)

        # Read the transcript of text
        with open(in_file, 'r', encoding = "UTF-8") as f:
            text = f.read()
        
        # Create Student object from transcript
        stu = Student(*stu_str.split('-'))
        stu.course = extract_course(text, discard_course)

        # Set the schedule of the stu's major
        major_info = major_course[str(enter_year) + stu.major]
        must_now = major_info["must_now"]
        must_all = must_now + major_info["must_later"]
        course_all = must_all + major_info["select"]

        # Mark the course for other major's class
        stu.check_convert(course_all, same_course, ignore = ["通识选"])
        for course in stu.course:
            if course.warning == "fail":
                course.type = "专业选"
        fail_or_absent = stu.check_must(must_now, pass_score)


        # Set the key information
        stu_info = OrderedDict({
            cols[0]: stu.classid,
            cols[1]: stu.name,
            cols[2]: "'" + stu.id,
            cols[3]: stu.get_course(types = ["专业必"]),
            cols[4]: stu.gpa("专业必")["gpa"],
            cols[5]: stu.get_course(must_types, ["diff"]),
            cols[6]: stu.get_course(types = ["专业选"]),
            cols[7]: stu.get_course(warnings = ["fail"]),
            cols[8]: " / ".join(must_types),
            cols[9]: len(fail_or_absent),
            cols[10]: " / ".join(fail_or_absent),
            cols[11]: major_info["credi"]["专业选修课"],
            cols[12]: stu.gpa(["专业选"])["credi"],
            cols[13]: major_info["credi"]["通识选修课"],
            cols[14]: stu.gpa(["通识选"])["credi"]
        })

        # Output the docx and xlsx for each stu
        docx_file = out_dir + '/' + stu.classid + '_' + stu.name + ".docx"
        tpl = DocxTemplate(template_file)
        tpl.render(stu_info)
        tpl.save(docx_file)
        sheet.append(list(stu_info.values()))

    # Save xlsx file
    wb.save(out_xlsx)
    signal_pct.emit(100)

if __name__ == "__main__":
    pass