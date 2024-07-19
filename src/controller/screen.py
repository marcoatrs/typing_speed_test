from PySide6 import QtWidgets as qw

from src.view.gui import Ui_TypingTest


class TypingTest(qw.QMainWindow, Ui_TypingTest):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def enable_start(self):
        self.push_start.setEnabled(True)
