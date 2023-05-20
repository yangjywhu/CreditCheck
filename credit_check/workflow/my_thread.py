from PySide6.QtCore import QThread, Signal, Slot

from .schedule_convert import run as schedule_convert
from .transcript_to_text import run as transcript_to_text
from .parse_transcript import run as parse_transcript

class MyThread(QThread):
    signal_phase = Signal(str)
    signal_pct = Signal(int)
    signal_now = Signal(str)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
    
    def change_edit_type(self, enable = True):
        self.ui.xkjck.setEnabled(enable)
        self.ui.sjbxk.setEnabled(enable)
        self.ui.tsxxk.setEnabled(enable)
        self.ui.zybxk.setEnabled(enable)
        self.ui.zyxxk.setEnabled(enable)
        self.ui.tsxxk.setEnabled(enable)
        self.ui.tsk.setEnabled(enable)
        self.ui.pass_score.setEnabled(enable)
        self.ui.yx_score.setEnabled(enable)
        self.ui.lh_score.setEnabled(enable)
        self.ui.zd_score.setEnabled(enable)
        self.ui.jg_score.setEnabled(enable)
        self.ui.bjg_score.setEnabled(enable)
        self.ui.hg_score.setEnabled(enable)
        self.ui.bhg_score.setEnabled(enable)
        self.ui.now_grade.setEnabled(enable)
        self.ui.now_semester.setEnabled(enable)
        self.ui.schedule_dir.setEnabled(enable)
        self.ui.transcript_file.setEnabled(enable)
        self.ui.notice_template.setEnabled(enable)
        self.ui.enter_year.setEnabled(enable)
        self.ui.notice_dir.setEnabled(enable)
        self.ui.schedule_dir_view.setEnabled(enable)
        self.ui.notice_template_view.setEnabled(enable)
        self.ui.transcript_view.setEnabled(enable)
        self.ui.notice_dir_view.setEnabled(enable)
        self.ui.notice_create.setEnabled(enable)
    
    def run(self):
        self.change_edit_type(False)

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

        parse_transcript(
            major_course,
            must_types,
            transcript_dir,
            template_file,
            out_dir,
            self.signal_pct,
            self.signal_now,
            int(self.ui.pass_score.text())
        )

        self.signal_phase.emit("完成")
        self.signal_now.emit('')
        self.change_edit_type(True)