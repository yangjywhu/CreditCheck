import os
import re
import pandas as pd
from rich.progress import track
from docxtpl import DocxTemplate
from modules import Student, create_dir, list_to_course, dict_to_course


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
    df_list = []
    
    for i, file_name in enumerate(file_names):

        # Set the file path
        stu_str, _ = os.path.splitext(file_name)
        in_file = transcript_dir + '/' + file_name
        
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
        stu_info = {
            "班级": stu.classid,
            "姓名": stu.name,
            "学号": "'" + stu.id,
            "专业必完成科目": sep.join(stu.type_names(["专业必"])),
            "专业选完成科目": sep.join(stu.type_names(["专业选", "fail"])),
            "专业必GPA": stu.gpa("专业必")["gpa"],
            "必须完成的类型": sep.join(must_types),
            "必修未完成数目": len(fail_or_absent),
            "必修未完成科目": sep.join(fail_or_absent),
            "专业选应": major_info["credi"]["专业选修课"],
            "专业选实": stu.gpa(["专业选", "fail"])["credi"],
            "通识选应": major_info["credi"]["通识选修课"],
            "通识选实": stu.gpa(["通识选"])["credi"],
            "转换课程": sep.join(remind_change)
        }

        # Output the docx for each stu
        docx_file = out_dir + '/' + stu.classid + '_' + stu.name + ".docx"
        tpl = DocxTemplate(template_file)
        tpl.render(stu_info)
        tpl.save(out_dir + '/' + docx_file)
        df_list.append(stu_info)

    # Output an excel file of summary
    signal_now.emit("生成汇总表")
    df = pd.DataFrame(df_list)
    df.to_excel(out_xlsx, index = False)
    signal_pct.emit(100)

if __name__ == "__main__":
    pass