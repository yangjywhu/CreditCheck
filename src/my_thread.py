import time
from PySide6.QtCore import QThread, Signal
from modules import change_edit_type
from credit_check import schedule_convert
from credit_check import transcript_to_text
from credit_check import parse_transcript

class MyThread(QThread):
    signal_phase = Signal(str)
    signal_pct = Signal(int)
    signal_now = Signal(str)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
    
    def workflow(self):
        self.signal_phase.emit('')
        self.signal_now.emit('')
        
        check_boxes = [
            self.ui.xkjck,
            self.ui.sjbxk,
            self.ui.tsxxk,
            self.ui.zybxk,
            self.ui.zyxxk,
            self.ui.tsk,
        ]

        level_score = {
            self.ui.yx_label.text(): self.ui.yx_score.text(),
            self.ui.lh_label.text(): self.ui.lh_score.text(),
            self.ui.zd_label.text(): self.ui.zd_score.text(),
            self.ui.jg_label.text(): self.ui.jg_score.text(),
            self.ui.bjg_label.text(): self.ui.bjg_score.text(),
            self.ui.hg_label.text(): self.ui.hg_score.text(),
            self.ui.bhg_label.text(): self.ui.bhg_score.text()
        }

        pass_score = int(self.ui.pass_score.text())
        must_types = [i.text() for i in check_boxes if i.isChecked()]
        now_grade = int(self.ui.now_grade.currentText())
        now_semester = int(self.ui.now_semester.currentText())

        schedule_dir = self.ui.schedule_dir.text()
        transcript_file = self.ui.transcript_file.text()
        template_file = self.ui.notice_template.text()
        enter_year = int(self.ui.enter_year.text())
        out_dir = self.ui.notice_dir.text()

        same_course = self.ui.same_course.toPlainText()
        same_course = [i.split() for i in same_course.strip().split('\n')]
        discard_course = self.ui.discard_course.toPlainText().split()

        transcript_dir = transcript_file.replace(".pdf", "_txt")
                        
        self.signal_phase.emit("(1/3)从培养方案中提取课程信息...")
        major_course = schedule_convert(
            schedule_dir,
            must_types,
            enter_year,
            now_grade,
            now_semester,
            self.signal_pct,
            self.signal_now
        )

        self.signal_phase.emit("(2/3)将成绩单转换为文本...")
        transcript_to_text(
            transcript_file,
            transcript_dir,
            level_score,
            self.signal_pct,
            self.signal_now
        )

        self.signal_phase.emit("(3/3)从成绩单中提取课程信息...")
        parse_transcript(
            major_course,
            must_types,
            enter_year,
            transcript_dir,
            template_file,
            out_dir,
            pass_score,
            same_course,
            discard_course,
            self.signal_pct,
            self.signal_now,
        )
        self.signal_phase.emit("完成")
        self.signal_now.emit('')

    def run(self):
        try:
            change_edit_type(self.ui, False)
            self.workflow()

        except PermissionError:
            self.signal_phase.emit("错误: Word文档被占用")
        
        except FileNotFoundError as e:
            self.signal_phase.emit("错误: 输入文件或文件夹不存在")
            self.signal_now.emit(str(e))

        except Exception:
            text = self.ui.progress_phase.text()
            self.signal_phase.emit(text + "错误: 请联系管理员。")
    
        finally:
            change_edit_type(self.ui, True)

        # # test
        # change_edit_type(self.ui, False)
        # self.workflow()
        # change_edit_type(self.ui, True)