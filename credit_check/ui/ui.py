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
    QGroupBox, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 458)
        self.notice_create = QPushButton(Form)
        self.notice_create.setObjectName(u"notice_create")
        self.notice_create.setGeometry(QRect(430, 250, 101, 31))
        self.open_notice_dir = QPushButton(Form)
        self.open_notice_dir.setObjectName(u"open_notice_dir")
        self.open_notice_dir.setGeometry(QRect(430, 290, 101, 31))
        self.must_group = QGroupBox(Form)
        self.must_group.setObjectName(u"must_group")
        self.must_group.setEnabled(True)
        self.must_group.setGeometry(QRect(30, 120, 291, 91))
        self.grade_group = QGroupBox(Form)
        self.grade_group.setObjectName(u"grade_group")
        self.grade_group.setGeometry(QRect(30, 19, 291, 91))
        self.grade_group_2 = QGroupBox(Form)
        self.grade_group_2.setObjectName(u"grade_group_2")
        self.grade_group_2.setGeometry(QRect(340, 20, 211, 191))
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 141, 271, 57))
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
        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(350, 42, 191, 152))
        self.score_layout = QGridLayout(self.layoutWidget3)
        self.score_layout.setObjectName(u"score_layout")
        self.score_layout.setHorizontalSpacing(1)
        self.score_layout.setVerticalSpacing(10)
        self.score_layout.setContentsMargins(0, 0, 0, 0)
        self.hg_label = QLabel(self.layoutWidget3)
        self.hg_label.setObjectName(u"hg_label")

        self.score_layout.addWidget(self.hg_label, 4, 0, 1, 1)

        self.lh_label = QLabel(self.layoutWidget3)
        self.lh_label.setObjectName(u"lh_label")

        self.score_layout.addWidget(self.lh_label, 1, 3, 1, 1)

        self.bjg_label = QLabel(self.layoutWidget3)
        self.bjg_label.setObjectName(u"bjg_label")

        self.score_layout.addWidget(self.bjg_label, 3, 3, 1, 1)

        self.yx_score = QLineEdit(self.layoutWidget3)
        self.yx_score.setObjectName(u"yx_score")

        self.score_layout.addWidget(self.yx_score, 1, 1, 1, 1)

        self.bjg_score = QLineEdit(self.layoutWidget3)
        self.bjg_score.setObjectName(u"bjg_score")

        self.score_layout.addWidget(self.bjg_score, 3, 4, 1, 1)

        self.bhg_score = QLineEdit(self.layoutWidget3)
        self.bhg_score.setObjectName(u"bhg_score")

        self.score_layout.addWidget(self.bhg_score, 4, 4, 1, 1)

        self.yx_label = QLabel(self.layoutWidget3)
        self.yx_label.setObjectName(u"yx_label")

        self.score_layout.addWidget(self.yx_label, 1, 0, 1, 1)

        self.bhg_label = QLabel(self.layoutWidget3)
        self.bhg_label.setObjectName(u"bhg_label")

        self.score_layout.addWidget(self.bhg_label, 4, 3, 1, 1)

        self.lh_score = QLineEdit(self.layoutWidget3)
        self.lh_score.setObjectName(u"lh_score")

        self.score_layout.addWidget(self.lh_score, 1, 4, 1, 1)

        self.jg_score = QLineEdit(self.layoutWidget3)
        self.jg_score.setObjectName(u"jg_score")

        self.score_layout.addWidget(self.jg_score, 3, 1, 1, 1)

        self.hg_score = QLineEdit(self.layoutWidget3)
        self.hg_score.setObjectName(u"hg_score")

        self.score_layout.addWidget(self.hg_score, 4, 1, 1, 1)

        self.zd_score = QLineEdit(self.layoutWidget3)
        self.zd_score.setObjectName(u"zd_score")

        self.score_layout.addWidget(self.zd_score, 2, 1, 1, 1)

        self.pass_label = QLabel(self.layoutWidget3)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setWordWrap(False)

        self.score_layout.addWidget(self.pass_label, 0, 0, 1, 2)

        self.jg_label = QLabel(self.layoutWidget3)
        self.jg_label.setObjectName(u"jg_label")

        self.score_layout.addWidget(self.jg_label, 3, 0, 1, 1)

        self.zd_label = QLabel(self.layoutWidget3)
        self.zd_label.setObjectName(u"zd_label")

        self.score_layout.addWidget(self.zd_label, 2, 0, 1, 1)

        self.pass_score = QLineEdit(self.layoutWidget3)
        self.pass_score.setObjectName(u"pass_score")

        self.score_layout.addWidget(self.pass_score, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.score_layout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.score_layout.setColumnStretch(0, 1)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 231, 371, 131))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)

        self.notice_template = QLineEdit(self.layoutWidget)
        self.notice_template.setObjectName(u"notice_template")

        self.gridLayout.addWidget(self.notice_template, 2, 1, 1, 1)

        self.schedule_dir = QLineEdit(self.layoutWidget)
        self.schedule_dir.setObjectName(u"schedule_dir")

        self.gridLayout.addWidget(self.schedule_dir, 0, 1, 1, 1)

        self.notice_dir = QLineEdit(self.layoutWidget)
        self.notice_dir.setObjectName(u"notice_dir")

        self.gridLayout.addWidget(self.notice_dir, 3, 1, 1, 1)

        self.transcript_view = QPushButton(self.layoutWidget)
        self.transcript_view.setObjectName(u"transcript_view")

        self.gridLayout.addWidget(self.transcript_view, 1, 2, 1, 1)

        self.transcript_file = QLineEdit(self.layoutWidget)
        self.transcript_file.setObjectName(u"transcript_file")

        self.gridLayout.addWidget(self.transcript_file, 1, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)

        self.notice_template_view = QPushButton(self.layoutWidget)
        self.notice_template_view.setObjectName(u"notice_template_view")

        self.gridLayout.addWidget(self.notice_template_view, 2, 2, 1, 1)

        self.notice_dir_view = QPushButton(self.layoutWidget)
        self.notice_dir_view.setObjectName(u"notice_dir_view")

        self.gridLayout.addWidget(self.notice_dir_view, 3, 2, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)

        self.schedule_dir_view = QPushButton(self.layoutWidget)
        self.schedule_dir_view.setObjectName(u"schedule_dir_view")

        self.gridLayout.addWidget(self.schedule_dir_view, 0, 2, 1, 1)

        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(60, 390, 451, 23))
        self.progress_bar.setCursor(QCursor(Qt.ArrowCursor))
        self.progress_bar.setValue(0)
        self.progress_phase = QLabel(Form)
        self.progress_phase.setObjectName(u"progress_phase")
        self.progress_phase.setGeometry(QRect(60, 420, 161, 21))
        self.progress_now = QLabel(Form)
        self.progress_now.setObjectName(u"progress_now")
        self.progress_now.setGeometry(QRect(60, 440, 411, 21))
        self.must_group.raise_()
        self.grade_group.raise_()
        self.layoutWidget.raise_()
        self.grade_group_2.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget2.raise_()
        self.layoutWidget3.raise_()
        self.notice_create.raise_()
        self.open_notice_dir.raise_()
        self.progress_bar.raise_()
        self.progress_phase.raise_()
        self.progress_now.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5b66\u5206\u6e05\u67e5\u5de5\u5177", None))
        self.notice_create.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u901a\u77e5\u4e66", None))
        self.open_notice_dir.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u901a\u77e5\u4e66\u76ee\u5f55", None))
        self.must_group.setTitle(QCoreApplication.translate("Form", u"\u5fc5\u4fee\u7c7b\u578b", None))
        self.grade_group.setTitle(QCoreApplication.translate("Form", u"\u5e74\u7ea7\u8bbe\u7f6e", None))
        self.grade_group_2.setTitle(QCoreApplication.translate("Form", u"\u5206\u6570\u8bbe\u7f6e", None))
        self.xkjck.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u57fa\u7840\u8bfe", None))
        self.sjbxk.setText(QCoreApplication.translate("Form", u"\u5b9e\u8df5\u5fc5\u4fee\u8bfe", None))
        self.tsk.setText(QCoreApplication.translate("Form", u"\u901a\u8bc6\u8bfe", None))
        self.zybxk.setText(QCoreApplication.translate("Form", u"\u4e13\u4e1a\u5fc5\u4fee\u8bfe", None))
        self.zyxxk.setText(QCoreApplication.translate("Form", u"\u4e13\u4e1a\u9009\u4fee\u8bfe", None))
        self.tsxxk.setText(QCoreApplication.translate("Form", u"\u901a\u8bc6\u9009\u4fee\u8bfe", None))
        self.enter_year.setText(QCoreApplication.translate("Form", u"2021", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5b66\u671f", None))
        self.now_grade.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.now_grade.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.now_grade.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.now_grade.setItemText(3, QCoreApplication.translate("Form", u"4", None))

        self.now_grade.setCurrentText(QCoreApplication.translate("Form", u"1", None))
        self.college_name.setItemText(0, QCoreApplication.translate("Form", u"\u4f1a\u8ba1\u5b66\u9662", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u5165\u5b66\u5e74\u4efd", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u5b66\u9662", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5e74\u7ea7", None))
        self.now_semester.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.now_semester.setItemText(1, QCoreApplication.translate("Form", u"2", None))

        self.hg_label.setText(QCoreApplication.translate("Form", u"\u5408\u683c", None))
        self.lh_label.setText(QCoreApplication.translate("Form", u"\u826f\u597d", None))
        self.bjg_label.setText(QCoreApplication.translate("Form", u"\u4e0d\u53ca\u683c", None))
        self.yx_score.setText(QCoreApplication.translate("Form", u"95", None))
        self.bjg_score.setText(QCoreApplication.translate("Form", u"0", None))
        self.bhg_score.setText(QCoreApplication.translate("Form", u"0", None))
        self.yx_label.setText(QCoreApplication.translate("Form", u"\u4f18\u79c0", None))
        self.bhg_label.setText(QCoreApplication.translate("Form", u"\u4e0d\u5408\u683c", None))
        self.lh_score.setText(QCoreApplication.translate("Form", u"85", None))
        self.jg_score.setText(QCoreApplication.translate("Form", u"65", None))
        self.hg_score.setText(QCoreApplication.translate("Form", u"80", None))
        self.zd_score.setText(QCoreApplication.translate("Form", u"75", None))
        self.pass_label.setText(QCoreApplication.translate("Form", u"\u9884\u8b66\u5206\u6570", None))
        self.jg_label.setText(QCoreApplication.translate("Form", u"\u53ca\u683c", None))
        self.zd_label.setText(QCoreApplication.translate("Form", u"\u4e2d\u7b49", None))
        self.pass_score.setText(QCoreApplication.translate("Form", u"60", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6210\u7ee9\u5355", None))
        self.notice_template.setText(QCoreApplication.translate("Form", u"../\u5b66\u5206\u6e05\u67e5\u901a\u77e5\u4e66\u6a21\u677f.docx", None))
        self.schedule_dir.setText(QCoreApplication.translate("Form", u"../\u57f9\u517b\u65b9\u6848", None))
        self.notice_dir.setText(QCoreApplication.translate("Form", u"../new", None))
        self.transcript_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.transcript_file.setText(QCoreApplication.translate("Form", u"../2021\u6210\u7ee9\u5355\u6d4b\u8bd5.pdf", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u57f9\u517b\u65b9\u6848", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u901a\u77e5\u4e66\u4fdd\u5b58", None))
        self.notice_template_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.notice_dir_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u901a\u77e5\u4e66\u6a21\u677f", None))
        self.schedule_dir_view.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8...", None))
        self.progress_phase.setText(QCoreApplication.translate("Form", u"\u5c31\u7eea\u3002", None))
        self.progress_now.setText("")
    # retranslateUi

