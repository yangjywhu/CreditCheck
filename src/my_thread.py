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
        check_boxes = [
            self.ui.xkjck,
            self.ui.sjbxk,
            self.ui.tsxxk,
            self.ui.zybxk,
            self.ui.zyxxk,
            self.ui.tsk,
        ]

        level_score = {
            self.ui.pass_score.objectName(): self.ui.pass_score.text(),
            self.ui.yx_label.text(): self.ui.yx_score.text(),
            self.ui.lh_label.text(): self.ui.lh_score.text(),
            self.ui.zd_label.text(): self.ui.zd_score.text(),
            self.ui.jg_label.text(): self.ui.jg_score.text(),
            self.ui.bjg_label.text(): self.ui.bjg_score.text(),
            self.ui.hg_label.text(): self.ui.hg_score.text(),
            self.ui.bhg_label.text(): self.ui.bhg_score.text()
        }
        
        must_types = [i.text() for i in check_boxes if i.isChecked()]
        now_grade = int(self.ui.now_grade.currentText())
        now_semester = int(self.ui.now_semester.currentText())

        schedule_dir = self.ui.schedule_dir.text()
        transcript_file = self.ui.transcript_file.text()
        template_file = self.ui.notice_template.text()
        enter_year = int(self.ui.enter_year.text())
        out_dir = self.ui.notice_dir.text()

        transcript_dir = transcript_file.replace(".pdf", "_txt")
                        
        self.signal_phase.emit("从培养方案中提取课程信息...")
        major_course = schedule_convert(
            schedule_dir,
            must_types,
            enter_year,
            now_grade,
            now_semester,
            self.signal_pct,
            self.signal_now
        )

        self.signal_phase.emit("将成绩单转换为文本...")
        transcript_to_text(
            transcript_file,
            transcript_dir,
            level_score,
            self.signal_pct,
            self.signal_now
        )

        self.signal_phase.emit("从成绩单中提取课程信息...")
        parse_transcript(
            major_course,
            must_types,
            enter_year,
            transcript_dir,
            template_file,
            out_dir,
            self.signal_pct,
            self.signal_now,
            int(self.ui.pass_score.text())
        )
        self.signal_phase.emit("完成")
        self.signal_now.emit('')

    def run(self):
        # try:
        #     change_edit_type(self.ui, False)
        #     self.workflow()

        # # TODO: print information
        # except Exception as e:
        #     self.signal_phase.emit("发生错误，请联系管理员。" + str(e))
        #     # self.ui.note_text.setText(e.with_traceback())
    
        # finally:
        #     change_edit_type(self.ui, True)
        change_edit_type(self.ui, False)
        self.workflow()
        change_edit_type(self.ui, True)