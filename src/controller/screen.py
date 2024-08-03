from PySide6 import QtCore as qc
from PySide6 import QtGui as qg
from PySide6 import QtWidgets as qw

from src.controller.path import ROOT_PATH
from src.view.gui import Ui_TypingTest


class TypingTest(qw.QMainWindow, Ui_TypingTest):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def enable_start(self):
        self.push_start.setEnabled(True)

    def restart_cursor(self):
        self.text_test.textCursor().movePosition(qg.QTextCursor.Start)

    def move_cursor(self, column: int): # , line: int = 0
        cursor = self.text_test.textCursor()
        cursor.movePosition(qg.QTextCursor.Start)
        cursor.movePosition(qg.QTextCursor.Right, qg.QTextCursor.MoveAnchor, column - 1)
        self.text_test.setTextCursor(cursor)
        self.text_test.ensureCursorVisible()


class MyApp(qw.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        font_root = ROOT_PATH / "assets" / "SpaceMono-Regular.ttf"
        self.setFont(str(font_root))