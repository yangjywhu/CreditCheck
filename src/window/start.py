# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Slot
from ui.start import Ui_Form
from window.error import ErrorDialog
from thread.start import MyThread

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.schedule_dir_view.clicked.connect(self.choose_schedule)
        self.ui.notice_template_view.clicked.connect(self.choose_notice)
        self.ui.transcript_view.clicked.connect(self.choose_transcript)
        self.ui.notice_dir_view.clicked.connect(self.choose_output)

        self.ui.notice_create.clicked.connect(self.click_notice_create)
        self.ui.open_notice_dir.clicked.connect(self.open_dir)

    def choose_schedule(self):
        dir_path = QFileDialog.getExistingDirectory(
            parent = None,
            caption = "select directory",
            dir = ''
        )
        self.ui.schedule_dir.setText(dir_path)
    
    def choose_transcript(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent = None,
            caption = "select file",
            dir = '',
            filter = 'PDF(*.pdf)'
        )
        self.ui.transcript_file.setText(file_path)
    
    def choose_notice(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent = None,
            caption = "select file",
            dir = '',
            filter = 'Word(*.docx)'
        )
        self.ui.notice_template.setText(file_path)
    
    def choose_output(self):
        dir_path = QFileDialog.getExistingDirectory(
            parent = None,
            caption = "select directory",
            dir = ''
        )
        self.ui.notice_dir.setText(dir_path)
    
    def click_notice_create(self):
        self.thread = MyThread(self.ui)
        self.thread.signal_phase.connect(self.progress_phase)
        self.thread.signal_pct.connect(self.progress_pct)
        self.thread.signal_now.connect(self.progress_now)
        self.thread.signal_error.connect(self.error_dialog)
        self.thread.start()
    
    def open_dir(self):
        windows_dir = self.ui.notice_dir.text().replace('/', '\\')
        os.system('start %s' % windows_dir)
    
    @Slot(str)
    def progress_phase(self, string):
        self.ui.progress_phase.setText(string)    

    @Slot(int)
    def progress_pct(self, pct):
        self.ui.progress_bar.setValue(pct)
    
    @Slot(str)
    def progress_now(self, string):
        self.ui.progress_now.setText(string)
    
    @Slot(str)
    def error_dialog(self, string):
        self.error_win = ErrorDialog()
        self.error_win.show()
        self.error_win.ui.plainTextEdit.setPlainText(string)