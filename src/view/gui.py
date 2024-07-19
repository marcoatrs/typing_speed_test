# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiBWczli.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTextEdit, QWidget)
from . import icons_rc

class Ui_TypingTest(object):
    def setupUi(self, TypingTest):
        if not TypingTest.objectName():
            TypingTest.setObjectName(u"TypingTest")
        TypingTest.setEnabled(True)
        TypingTest.resize(800, 602)
        icon = QIcon()
        icon.addFile(u":/icons/icons/key.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TypingTest.setWindowIcon(icon)
        TypingTest.setStyleSheet(u"QMainWindow{\n"
"	background-color: white;\n"
"}\n"
"\n"
"\n"
"/*\n"
"#FFC15E\n"
"#F7B05B\n"
"#F7934C\n"
"#CC5803\n"
"#1F1300\n"
"*/")
        self.centralwidget = QWidget(TypingTest)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_init = QWidget()
        self.page_init.setObjectName(u"page_init")
        self.stackedWidget.addWidget(self.page_init)
        self.page_select = QWidget()
        self.page_select.setObjectName(u"page_select")
        self.gridLayout_3 = QGridLayout(self.page_select)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gdl_select = QGridLayout()
        self.gdl_select.setSpacing(15)
        self.gdl_select.setObjectName(u"gdl_select")
        self.textEdit = QTextEdit(self.page_select)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	border: None;\n"
"}\n"
"\n"
"QTextEdit:disabled {\n"
"	border: None;\n"
"	background-color: white;\n"
"}")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.gdl_select.addWidget(self.textEdit, 1, 0, 4, 1)

        self.label_2 = QLabel(self.page_select)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-image: url(:/icons/image/letters.jpg);")

        self.gdl_select.addWidget(self.label_2, 1, 1, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_round = QLabel(self.page_select)
        self.label_round.setObjectName(u"label_round")
        self.label_round.setStyleSheet(u"background-color: #FFC15E;\n"
"border-top-right-radius: 50%;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_round)

        self.label_title1 = QLabel(self.page_select)
        self.label_title1.setObjectName(u"label_title1")
        font = QFont()
        font.setPointSize(36)
        self.label_title1.setFont(font)
        self.label_title1.setStyleSheet(u"color: #1F1300;")
        self.label_title1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_title1)

        self.label_title2 = QLabel(self.page_select)
        self.label_title2.setObjectName(u"label_title2")
        self.label_title2.setFont(font)
        self.label_title2.setStyleSheet(u"color: #FFC15E;")

        self.horizontalLayout_2.addWidget(self.label_title2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 10)

        self.gdl_select.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.combo_language = QComboBox(self.page_select)
        self.combo_language.setObjectName(u"combo_language")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.combo_language.setFont(font1)
        self.combo_language.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combo_language.setStyleSheet(u"QComboBox {\n"
"    padding: 1px 18px 1px 3px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: #F7934C;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #f6f7fa, stop:1 #dadbde);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/drop_down.ico);\n"
"}")

        self.horizontalLayout_3.addWidget(self.combo_language)


        self.gdl_select.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.push_start = QPushButton(self.page_select)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(18)
        self.push_start.setFont(font2)
        self.push_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.push_start.setStyleSheet(u"QPushButton:enabled{\n"
"	background-color: #F7B05B;\n"
"	padding: 5px;\n"
"	color: #1F1300;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"	background: #CC5803;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: gray;\n"
"    background-color: #1F1300;   \n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.push_start)


        self.gdl_select.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)

        self.gdl_select.setRowStretch(0, 1)
        self.gdl_select.setRowStretch(1, 3)
        self.gdl_select.setRowStretch(2, 3)
        self.gdl_select.setColumnStretch(0, 2)
        self.gdl_select.setColumnStretch(1, 2)

        self.gridLayout_3.addLayout(self.gdl_select, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_select)
        self.page_load_screen = QWidget()
        self.page_load_screen.setObjectName(u"page_load_screen")
        self.page_load_screen.setStyleSheet(u"background-color: #FFC15E;")
        self.gridLayout_4 = QGridLayout(self.page_load_screen)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gld_load = QGridLayout()
        self.gld_load.setObjectName(u"gld_load")
        self.label_load = QLabel(self.page_load_screen)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setStyleSheet(u"background-color: transparent;")
        self.label_load.setPixmap(QPixmap(u":/icons/icons/sand_clock.ico"))

        self.gld_load.addWidget(self.label_load, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gld_load.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gld_load.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gld_load.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gld_load.addItem(self.verticalSpacer_4, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gld_load, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_load_screen)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.page_test.setStyleSheet(u"background-color: #FFC15E;")
        self.gridLayout_5 = QGridLayout(self.page_test)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gdl_test = QGridLayout()
        self.gdl_test.setObjectName(u"gdl_test")
        self.text_test = QTextEdit(self.page_test)
        self.text_test.setObjectName(u"text_test")
        self.text_test.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(28)
        self.text_test.setFont(font3)
        self.text_test.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.gdl_test.addWidget(self.text_test, 1, 0, 1, 1)

        self.label_test = QLabel(self.page_test)
        self.label_test.setObjectName(u"label_test")
        self.label_test.setFont(font)
        self.label_test.setStyleSheet(u"background-color: #F7B05B;\n"
"color: rgb(163, 163, 163);")
        self.label_test.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gdl_test.addWidget(self.label_test, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.page_test)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-top-left-radius: 50%;")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/speed.ico"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.label_wpm = QLabel(self.page_test)
        self.label_wpm.setObjectName(u"label_wpm")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_wpm.setFont(font4)
        self.label_wpm.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-bottom-right-radius: 50%;")

        self.horizontalLayout_7.addWidget(self.label_wpm)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.page_test)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-top-left-radius: 50%;")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/fail.ico"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.label_failures = QLabel(self.page_test)
        self.label_failures.setObjectName(u"label_failures")
        self.label_failures.setFont(font4)
        self.label_failures.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-bottom-right-radius: 50%;")

        self.horizontalLayout_8.addWidget(self.label_failures)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.page_test)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-top-left-radius: 50%;")
        self.label_6.setPixmap(QPixmap(u":/icons/icons/time.ico"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.label_time = QLabel(self.page_test)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font4)
        self.label_time.setStyleSheet(u"background-color: #CC5803;\n"
"color: #1F1300;\n"
"border-bottom-right-radius: 50%;")

        self.horizontalLayout_9.addWidget(self.label_time)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.horizontalLayout_6)


        self.gdl_test.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gdl_test.setRowStretch(0, 1)
        self.gdl_test.setRowStretch(1, 5)
        self.gdl_test.setRowStretch(2, 1)

        self.gridLayout_5.addLayout(self.gdl_test, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_test)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.page_results.setStyleSheet(u"background-color: #CC5803;")
        self.gridLayout_6 = QGridLayout(self.page_results)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gdl_main_results = QGridLayout()
        self.gdl_main_results.setObjectName(u"gdl_main_results")
        self.gdl_results = QGridLayout()
        self.gdl_results.setObjectName(u"gdl_results")
        self.web_view_results = QWebEngineView(self.page_results)
        self.web_view_results.setObjectName(u"web_view_results")
        self.web_view_results.setUrl(QUrl(u"about:blank"))

        self.gdl_results.addWidget(self.web_view_results, 0, 0, 1, 1)


        self.gdl_main_results.addLayout(self.gdl_results, 1, 1, 1, 1)

        self.label_results_title = QLabel(self.page_results)
        self.label_results_title.setObjectName(u"label_results_title")
        self.label_results_title.setFont(font)
        self.label_results_title.setStyleSheet(u"background-color: #FFC15E;\n"
"color: #1F1300;\n"
"border-top-left-radius: 50%;\n"
"border-bottom-right-radius: 50%;")
        self.label_results_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gdl_main_results.addWidget(self.label_results_title, 0, 0, 1, 2)

        self.label_success_per = QLabel(self.page_results)
        self.label_success_per.setObjectName(u"label_success_per")
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        self.label_success_per.setFont(font5)
        self.label_success_per.setStyleSheet(u"background-color: #FFC15E;\n"
"border-radius: 50%;")
        self.label_success_per.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_success_per.setWordWrap(True)

        self.gdl_main_results.addWidget(self.label_success_per, 2, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.label_wpm_result = QLabel(self.page_results)
        self.label_wpm_result.setObjectName(u"label_wpm_result")
        self.label_wpm_result.setMinimumSize(QSize(150, 150))
        self.label_wpm_result.setFont(font5)
        self.label_wpm_result.setStyleSheet(u"background-color: #F7934C;\n"
"border-radius: 50%;")
        self.label_wpm_result.setTextFormat(Qt.TextFormat.PlainText)
        self.label_wpm_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_wpm_result.setWordWrap(True)

        self.gridLayout.addWidget(self.label_wpm_result, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)


        self.gdl_main_results.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gdl_main_results.setRowStretch(0, 1)
        self.gdl_main_results.setRowStretch(1, 10)
        self.gdl_main_results.setRowStretch(2, 3)
        self.gdl_main_results.setColumnStretch(0, 1)
        self.gdl_main_results.setColumnStretch(1, 1)

        self.gridLayout_6.addLayout(self.gdl_main_results, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_results)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        TypingTest.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(TypingTest)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setEnabled(True)
        self.menu_bar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menu_bar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_view = QMenu(self.menu_bar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        TypingTest.setMenuBar(self.menu_bar)
        self.statusbar = QStatusBar(TypingTest)
        self.statusbar.setObjectName(u"statusbar")
        TypingTest.setStatusBar(self.statusbar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.menu_bar.addAction(self.menu_view.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(TypingTest)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TypingTest)
    # setupUi

    def retranslateUi(self, TypingTest):
        TypingTest.setWindowTitle(QCoreApplication.translate("TypingTest", u"Typing Test", None))
        self.textEdit.setHtml(QCoreApplication.translate("TypingTest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700;\">Ready to </span><span style=\" font-size:36pt;\"><br /></span><span style=\" font-size:36pt; font-weight:700;\">measure your </span><span style=\" font-size:36pt;\"><br /></span><span style=\" font-size:36pt; font-weight:700; color:#cc5803;\">typing speed?</span><span style=\" font-size:36pt;\"><br /></span><span style=\" font-size:36pt; font-weight:70"
                        "0;\">Show off your </span><span style=\" font-size:36pt;\"><br /></span><span style=\" font-size:36pt; font-weight:700; color:#cc5803;\">skill</span><span style=\" font-size:36pt; font-weight:700;\"> with every<br />keystroke!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt;\"><br /></p></body></html>", None))
        self.label_2.setText("")
        self.label_round.setText("")
        self.label_title1.setText(QCoreApplication.translate("TypingTest", u"Typing ", None))
        self.label_title2.setText(QCoreApplication.translate("TypingTest", u"Speed Test", None))
        self.combo_language.setPlaceholderText(QCoreApplication.translate("TypingTest", u"Select a language", None))
        self.push_start.setText(QCoreApplication.translate("TypingTest", u"          Start  \u2192          ", None))
        self.label_load.setText("")
        self.text_test.setHtml(QCoreApplication.translate("TypingTest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt;\"><br /></p></body></html>", None))
        self.label_test.setText("")
        self.label_4.setText("")
        self.label_wpm.setText(QCoreApplication.translate("TypingTest", u"  WPM:", None))
        self.label_5.setText("")
        self.label_failures.setText(QCoreApplication.translate("TypingTest", u"  Failures:", None))
        self.label_6.setText("")
        self.label_time.setText(QCoreApplication.translate("TypingTest", u"  Time:", None))
        self.label_results_title.setText(QCoreApplication.translate("TypingTest", u"Results:", None))
        self.label_success_per.setText(QCoreApplication.translate("TypingTest", u"Success percentage:", None))
        self.label_wpm_result.setText(QCoreApplication.translate("TypingTest", u"WPM: 38", None))
        self.menu_file.setTitle(QCoreApplication.translate("TypingTest", u"File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("TypingTest", u"Edit", None))
        self.menu_view.setTitle(QCoreApplication.translate("TypingTest", u"View", None))
        self.menu_help.setTitle(QCoreApplication.translate("TypingTest", u"Help", None))
    # retranslateUi

