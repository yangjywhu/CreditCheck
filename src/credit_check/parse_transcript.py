import os
import re
from collections import OrderedDict
from docxtpl import DocxTemplate
from openpyxl import Workbook

from modules import Student, create_dir, list_to_course


def extract_course(text):
    """
    Extract the course from transcript.
    """
    pattern = re.compile(r"(\S+)\s(\S{2,3})\s(\d\S{,2})\s(\d{1,3})")
    courses = pattern.findall(text)
    courses = list_to_course(courses)

    return courses


def run(
    major_course,
    must_types,
    transcript_dir,
    template_file,
    out_dir,
    signal_pct,
    signal_now,
    pass_score
):
    sep = '，'
    create_dir(out_dir)
    out_xlsx = out_dir + "/Summary.xlsx"
    file_names = os.listdir(transcript_dir)
    total_len = len(file_names)
    
    col_names = [
        "班级", "姓名", "学号", # 0 - 2
        "专业必完成科目", "专业必GPA", # 3 - 4
        "专业选完成科目", "转换课程", # 5 - 6
        "必须完成的类型", "必修未完成数目", "必修未完成科目", # 7 - 9
        "专业选应", "专业选实", "通识选应", "通识选实", # 10 - 13
    ]

    # create a excel workbook
    wb = Workbook()
    sheet = wb.active
    sheet.append(col_names)
    
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

        stu.course = extract_course(text)

        # Set the schedule of the stu's major
        major_info = major_course["20" + stu.id[:2] + stu.major]
        must_now = major_info["must_now"]
        must_all = must_now + major_info["must_later"]
        course_all = must_all + major_info["select"]

        # Mark the course for other major's class
        stu.check_convert(course_all, ignore = ["通识选"])
        remind_change =  stu.converted_course()
        fail_or_absent = stu.check_must(must_now, pass_score)

        # Set the key information
        stu_info = OrderedDict({
            col_names[0]: stu.classid,
            col_names[1]: stu.name,
            col_names[2]: "'" + stu.id,
            col_names[3]: sep.join(stu.type_names(["专业必"])),
            col_names[4]: stu.gpa("专业必")["gpa"],
            col_names[5]: sep.join(stu.type_names(["专业选", "fail"])),
            col_names[6]: sep.join(remind_change),
            col_names[7]: sep.join(must_types),
            col_names[8]: len(fail_or_absent),
            col_names[9]: sep.join(fail_or_absent),
            col_names[10]: major_info["credi"]["专业选修课"],
            col_names[11]: stu.gpa(["专业选", "fail"])["credi"],
            col_names[12]: major_info["credi"]["通识选修课"],
            col_names[13]: stu.gpa(["通识选"])["credi"]
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