# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(613, 460)
        self.notice_create = QPushButton(Form)
        self.notice_create.setObjectName(u"notice_create")
        self.notice_create.setGeometry(QRect(460, 390, 101, 21))
        self.open_notice_dir = QPushButton(Form)
        self.open_notice_dir.setObjectName(u"open_notice_dir")
        self.open_notice_dir.setGeometry(QRect(460, 420, 101, 21))
        self.must_group = QGroupBox(Form)
        self.must_group.setObjectName(u"must_group")
        self.must_group.setEnabled(True)
        self.must_group.setGeometry(QRect(340, 20, 241, 91))
        self.grade_group = QGroupBox(Form)
        self.grade_group.setObjectName(u"grade_group")
        self.grade_group.setGeometry(QRect(30, 19, 291, 91))
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(350, 41, 221, 57))
        self.must_type_layout = QGridLayout(self.layoutWidget1)
        self.must_type_layout.setObjectName(u"must_type_layout")
        self.must_type_layout.setHorizontalSpacing(0)
        self.must_type_layout.setVerticalSpacing(15)
        self.must_type_layout.setContentsMargins(0, 0, 0, 0)
        self.xkjck = QCheckBox(self.layoutWidget1)
        self.xkjck.setObjectName(u"xkjck")
        self.xkjck.setTabletTracking(False)
        self.xkjck.setChecked(True)

        self.must_type_layout.addWidget(self.xkjck, 0, 0, 1, 1)

        self.sjbxk = QCheckBox(self.layoutWidget1)
        self.sjbxk.setObjectName(u"sjbxk")
        self.sjbxk.setChecked(True)

        self.must_type_layout.addWidget(self.sjbxk, 0, 1, 1, 1)

        self.tsk = QCheckBox(self.layoutWidget1)
        self.tsk.setObjectName(u"tsk")
        self.tsk.setChecked(True)

        self.must_type_layout.addWidget(self.tsk, 0, 2, 1, 1)

        self.zybxk = QCheckBox(self.layoutWidget1)
        self.zybxk.setObjectName(u"zybxk")
        self.zybxk.setChecked(True)

        self.must_type_layout.addWidget(self.zybxk, 1, 0, 1, 1)

        self.zyxxk = QCheckBox(self.layoutWidget1)
        self.zyxxk.setObjectName(u"zyxxk")

        self.must_type_layout.addWidget(self.zyxxk, 1, 1, 1, 1)

        self.tsxxk = QCheckBox(self.layoutWidget1)
        self.tsxxk.setObjectName(u"tsxxk")
        self.tsxxk.setEnabled(True)
        self.tsxxk.setTabletTracking(False)
        self.tsxxk.setCheckable(True)
        self.tsxxk.setChecked(True)

        self.must_type_layout.addWidget(self.tsxxk, 1, 2, 1, 1)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 40, 271, 56))
        self.semester_layout = QGridLayout(self.layoutWidget2)
        self.semester_layout.setObjectName(u"semester_layout")
        self.semester_layout.setHorizontalSpacing(5)
        self.semester_layout.setVerticalSpacing(10)
        self.semester_layout.setContentsMargins(0, 0, 0, 0)
        self.enter_year = QLineEdit(self.layoutWidget2)
        self.enter_year.setObjectName(u"enter_year")

        self.semester_layout.addWidget(self.enter_year, 0, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.semester_layout.addWidget(self.label_5, 1, 2, 1, 1)

        self.now_grade = QComboBox(self.layoutWidget2)
        self.now_grade.addItem("")
        self.now_grade.addItem("")
        self.now_grade.addItem("")
        self.now_grade.addItem("")
        self.now_grade.setObjectName(u"now_grade")
        self.now_grade.setEnabled(True)

        self.semester_layout.addWidget(self.now_grade, 1, 1, 1, 1)

        self.college_name = QComboBox(self.layoutWidget2)
        self.college_name.addItem("")
        self.college_name.setObjectName(u"college_name")
        self.college_name.setEnabled(False)
        self.college_name.setEditable(False)

        self.semester_layout.addWidget(self.college_name, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.semester_layout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_21 = QLabel(self.layoutWidget2)
        self.label_21.setObjectName(u"label_21")

        self.semester_layout.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.semester_layout.addWidget(self.label_4, 1, 0, 1, 1)

        self.now_semester = QComboBox(self.layoutWidget2)
        self.now_semester.addItem("")
        self.now_semester.addItem("")
        self.now_semester.setObjectName(u"now_semester")

        self.semester_layout.addWidget(self.now_semester, 1, 3, 1, 1)

        self.semester_layout.setColumnStretch(0, 1)
        self.semester_layout.setColumnStretch(1, 1)
        self.semester_layout.setColumnStretch(2, 1)
        self.semester_layout.setColumnStretch(3, 1)
        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(30, 380, 411, 23))
        self.progress_bar.setCursor(QCursor(Qt.ArrowCursor))
        self.progress_bar.setValue(0)
        self.progress_phase = QLabel(Form)
        self.progress_phase.setObjectName(u"progress_phase")
        self.progress_phase.setGeometry(QRect(30, 400, 401, 20))
        self.progress_now = QLabel(Form)
        self.progress_now.setObjectName(u"progress_now")
        self.progress_now.setGeometry(QRect(30, 420, 401, 31))
        self.progress_now.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.grade_group_2 = QGroupBox(Form)
        self.grade_group_2.setObjectName(u"grade_group_2")
        self.grade_group_2.setGeometry(QRect(30, 120, 141, 241))
        self.crouse_group = QGroupBox(Form)
        self.crouse_group.setObjectName(u"crouse_group")
        self.crouse_group.setGeometry(QRect(190, 120, 391, 121))
        self.same_coures_label = QLabel(self.crouse_group)
        self.same_coures_label.setObjectName(u"same_coures_label")
        self.same_coures_label.setGeometry(QRect(10, 20, 181, 21))
        self.discard_coures_label = QLabel(self.crouse_group)
        self.discard_coures_label.setObjectName(u"discard_coures_label")
        self.discard_coures_label.setGeometry(QRect(240, 20, 131, 21))
        self.same_course = QPlainTextEdit(self.crouse_group)
        self.same_course.setObjectName(u"same_course")
        self.same_course.setGeometry(QRect(10, 40, 221, 71))
        self.same_course.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.same_course.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.discard_course = QPlainTextEdit(self.crouse_group)
        self.discard_course.setObjectName(u"discard_course")
        self.discard_course.setGeometry(QRect(240, 40, 141, 71))
        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(40, 140, 118, 212))
        self.gridLayout_2 = QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lh_score = QLineEdit(self.layoutWidget3)
        self.lh_score.setObjectName(u"lh_score")

        self.gridLayout_2.addWidget(self.lh_score, 2, 1, 1, 1)

        self.bhg_score = QLineEdit(self.layoutWidget3)
        self.bhg_score.setObjectName(u"bhg_score")

        self.gridLayout_2.addWidget(self.bhg_score, 7, 1, 1, 1)

        self.jg_label = QLabel(self.layoutWidget3)
        self.jg_label.setObjectName(u"jg_label")

        self.gridLayout_2.addWidget(self.jg_label, 4, 0, 1, 1)

        self.hg_label = QLabel(self.layoutWidget3)
        self.hg_label.setObjectName(u"hg_label")

        self.gridLayout_2.addWidget(self.hg_label, 6, 0, 1, 1)

        self.hg_score = QLineEdit(self.layoutWidget3)
        self.hg_score.setObjectName(u"hg_score")

        self.gridLayout_2.addWidget(self.hg_score, 6, 1, 1, 1)

        self.zd_label = QLabel(self.layoutWidget3)
        self.zd_label.setObjectName(u"zd_label")

        self.gridLayout_2.addWidget(self.zd_label, 3, 0, 1, 1)

        self.yx_score = QLineEdit(self.layoutWidget3)
        self.yx_score.setObjectName(u"yx_score")

        self.gridLayout_2.addWidget(self.yx_score, 1, 1, 1, 1)

        self.bjg_score = QLineEdit(self.layoutWidget3)
        self.bjg_score.setObjectName(u"bjg_score")

        self.gridLayout_2.addWidget(self.bjg_score, 5, 1, 1, 1)

        self.pass_label = QLabel(self.layoutWidget3)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.pass_label, 0, 0, 1, 1)

        self.jg_score = QLineEdit(self.layoutWidget3)
        self.jg_score.setObjectName(u"jg_score")

        self.gridLayout_2.addWidget(self.jg_score, 4, 1, 1, 1)

        self.zd_score = QLineEdit(self.layoutWidget3)
        self.zd_score.setObjectName(u"zd_score")

        self.gridLayout_2.addWidget(self.zd_score, 3, 1, 1, 1)

        self.yx_label = QLabel(self.layoutWidget3)
        self.yx_label.setObjectName(u"yx_label")

        self.gridLayout_2.addWidget(self.yx_label, 1, 0, 1, 1)

        self.bhg_label = QLabel(self.layoutWidget3)
        self.bhg_label.setObjectName(u"bhg_label")

        self.gridLayout_2.addWidget(self.bhg_label, 7, 0, 1, 1)

        self.pass_score = QLineEdit(self.layoutWidget3)
        self.pass_score.setObjectName(u"pass_score")

        self.gridLayout_2.addWidget(self.pass_score, 0, 1, 1, 1)

        self.lh_label = QLabel(self.layoutWidget3)
        self.lh_label.setObjectName(u"lh_label")

        self.gridLayout_2.addWidget(self.lh_label, 2, 0, 1, 1)

        self.bjg_label = QLabel(self.layoutWidget3)
        self.bjg_label.setObjectName(u"bjg_label")

        self.gridLayout_2.addWidget(self.bjg_label, 5, 0, 1, 1)

        self.layoutWidget4 = QWidget(Form)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(190, 250, 391, 112))
        self.gridLayout = QGridLayout(self.layoutWidget4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.schedule_dir = QLineEdit(self.layoutWidget4)
        self.schedule_dir.setObjectName(u"schedule_dir")

        self.gridLayout.addWidget(self.schedule_dir, 0, 1, 1, 1)

        self.schedule_dir_view = QPushButton(self.layoutWidget4)
        self.schedule_dir_view.setObjectName(u"schedule_dir_view")

        self.gridLayout.addWidget(self.schedule_dir_view, 0, 2, 1, 1)

        self.label_22 = QLabel(self.layoutWidget4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)

        self.transcript_file = QLineEdit(self.layoutWidget4)
        self.transcript_file.setObjectName(u"transcript_file")

        self.gridLayout.addWidget(self.transcript_file, 1, 1, 1, 1)

        self.transcript_view = QPushButton(self.layoutWidget4)
        self.transcript_view.setObjectName(u"transcript_view")

        self.gridLayout.addWidget(self.transcript_view, 1, 2, 1, 1)

        self.label_17 = QLabel(self.layoutWidget4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)

        self.notice_template = QLineEdit(self.layoutWidget4)
        self.notice_template.setObjectName(u"notice_template")

        self.gridLayout.addWidget(self.notice_template, 2, 1, 1, 1)

        self.notice_template_view = QPushButton(self.layoutWidget4)
        self.notice_template_view.setObjectName(u"notice_template_view")

        self.gridLayout.addWidget(self.notice_template_view, 2, 2, 1, 1)

        self.label_18 = QLabel(self.layoutWidget4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)

        self.notice_dir = QLineEdit(self.layoutWidget4)
        self.notice_dir.setObjectName(u"notice_dir")

        self.gridLayout.addWidget(self.notice_dir, 3, 1, 1, 1)

        self.notice_dir_view = QPushButton(self.layoutWidget4)
        self.notice_dir_view.setObjectName(u"notice_dir_view")

        self.gridLayout.addWidget(self.notice_dir_view, 3, 2, 1, 1)

        self.grade_group_2.raise_()
        self.layoutWidget3.raise_()
        self.layoutWidget4.raise_()
        self.crouse_group.raise_()
        self.must_group.raise_()
        self.grade_group.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget2.raise_()
        self.notice_create.raise_()
        self.open_notice_dir.raise_()
        self.progress_bar.raise_()
        self.progress_phase.raise_()
        self.progress_now.raise_()

        self.retranslateUi(Form)

        self.now_grade.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5b66\u5206\u6e05\u67e5\u5de5\u5177", None))
        self.notice_create.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u901a\u77e5\u4e66", None))
        self.open_notice_dir.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u901a\u77e5\u4e66\u76ee\u5f55", None))
        self.must_group.setTitle(QCoreApplication.translate("Form", u"\u5fc5\u4fee\u7c7b\u578b", None))
        self.grade_group.setTitle(QCoreApplication.translate("Form", u"\u5e74\u7ea7\u8bbe\u7f6e", None))
        self.xkjck.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u57fa", None))
        self.sjbxk.setText(QCoreApplication.translate("Form", u"\u5b9e\u8df5\u5fc5", None))
        self.tsk.setText(QCoreApplication.translate("Form", u"\u901a\u8bc6", None))
        self.zybxk.setText(QCoreApplication.translate("Form", u"\u4e13\u4e1a\u5fc5", None))
        self.zyxxk.setText(QCoreApplication.translate("Form", u"\u4e13\u4e1a\u9009", None))
        self.tsxxk.setText(QCoreApplication.translate("Form", u"\u901a\u8bc6\u9009", None))
        self.enter_year.setText(QCoreApplication.translate("Form", u"2021", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5b66\u671f", None))
        self.now_grade.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.now_grade.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.now_grade.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.now_grade.setItemText(3, QCoreApplication.translate("Form", u"4", None))

        self.now_grade.setCurrentText(QCoreApplication.translate("Form", u"2", None))
        self.college_name.setItemText(0, QCoreApplication.translate("Form", u"\u4f1a\u8ba1\u5b66\u9662", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u5165\u5b66\u5e74\u4efd", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u5b66\u9662", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5e74\u7ea7", None))
        self.now_semester.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.now_semester.setItemText(1, QCoreApplication.translate("Form", u"2", None))

        self.progress_phase.setText(QCoreApplication.translate("Form", u"\u5c31\u7eea\u3002", None))
        self.progress_now.setText(QCoreApplication.translate("Form", u"\u5c31\u7eea\u3002", None))
        self.grade_group_2.setTitle(QCoreApplication.translate("Form", u"\u5206\u6570\u8bbe\u7f6e", None))
        self.crouse_group.setTitle(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8bbe\u7f6e", None))
        self.same_coures_label.setText(QCoreApplication.translate("Form", u"\u76f8\u540c\u8bfe\u7a0b\uff08\u4e00\u884c\u4e00\u4e2a\uff0c\u7a7a\u683c\u5206\u9694\uff09", None))
        self.discard_coures_label.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6\u8bfe\u7a0b\uff08\u65e0\u6cd5\u8f6c\u6362\uff09", None))
        self.same_course.setPlainText(QCoreApplication.translate("Form", u"\u7a0e\u52a1\u4f1a\u8ba1A \u7a0e\u52a1\u4f1a\u8ba1I", None))
        self.discard_course.setPlainText(QCoreApplication.translate("Form", u"\u82f1\u8bed\u8bed\u8a00\u62d3\u5c55AI", None))
        self.lh_score.setText(QCoreApplication.translate("Form", u"85", None))
        self.bhg_score.setText(QCoreApplication.translate("Form", u"0", None))
        self.jg_label.setText(QCoreApplication.translate("Form", u"\u53ca\u683c", None))
        self.hg_label.setText(QCoreApplication.translate("Form", u"\u5408\u683c", None))
        self.hg_score.setText(QCoreApplication.translate("Form", u"80", None))
        self.zd_label.setText(QCoreApplication.translate("Form", u"\u4e2d\u7b49", None))
        self.yx_score.setText(QCoreApplication.translate("Form", u"95", None))
        self.bjg_score.setText(QCoreApplication.translate("Form", u"0", None))
        self.pass_label.setText(QCoreApplication.translate("Form", u"\u9884\u8b66\u5206\u6570", None))
        self.jg_score.setText(QCoreApplication.translate("Form", u"65", None))
        self.zd_score.setText(QCoreApplication.translate("Form", u"75", None))
        self.yx_label.setText(QCoreApplication.translate("Form", u"\u4f18\u79c0", None))
        self.bhg_label.setText(QCoreApplication.translate("Form", u"\u4e0d\u5408\u683c", None))
        self.pass_score.setText(QCoreApplication.translate("Form", u"60", None))
        self.lh_label.setText(QCoreApplication.translate("Form", u"\u826f\u597d", None))
        self.bjg_label.setText(QCoreApplication.translate("Form", u"\u4e0d\u53ca\u683c", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u57f9\u517b\u65b9\u6848", None))
        self.schedule_dir.setText(QCoreApplication.translate("Form", u"_data/\u57f9\u517b\u65b9\u6848", None))
        self.schedule_dir_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6210\u7ee9\u5355", None))
        self.transcript_file.setText(QCoreApplication.translate("Form", u"_data/2021\u6210\u7ee9\u5355.pdf", None))
        self.transcript_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u901a\u77e5\u4e66\u6a21\u677f", None))
        self.notice_template.setText(QCoreApplication.translate("Form", u"_data/\u5b66\u5206\u6e05\u67e5\u901a\u77e5\u4e66\u6a21\u677f.docx", None))
        self.notice_template_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u901a\u77e5\u4e66\u4fdd\u5b58", None))
        self.notice_dir.setText(QCoreApplication.translate("Form", u"_data/\u5b66\u5206\u6e05\u67e5\u7ed3\u679c", None))
        self.notice_dir_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
    # retranslateUi

