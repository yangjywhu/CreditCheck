# -*- coding: utf-8 -*-

import re
import pdfplumber
from modules import Student, create_dir

def run(transcript_file, transcript_dir, level_score, signal_pct, signal_now):
    create_dir(transcript_dir)

    with pdfplumber.open(transcript_file) as pdf:
        total_len = len(pdf.pages)

        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            info = map(
                lambda key: re.compile(f"{key}\s?:\s?(\S+)").findall(text)[0],
                ["班级", "学号", "姓名", "专业"]
            )
            stu = Student(*info)

            progress_pct = int(i / total_len * 100)
            signal_pct.emit(progress_pct)
            signal_now.emit(str(stu))
            
            text = re.sub(r"(\S+) ([A-Z])", "\\1\\2", text)
            for key, value in level_score.items():
                text = text.replace(key, value)

            text_file = transcript_dir + '/' + str(stu) + ".txt"
            with open(text_file, 'w', encoding = "UTF-8") as f:
                f.write(text)

    signal_pct.emit(100)

if __name__ == "__main__":
    pass
    # run(transcript_file, transcript_dir)