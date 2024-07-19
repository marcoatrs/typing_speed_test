from PySide6 import QtCore as qc
from PySide6 import QtGui as qg


class LoadScreen:
    def __init__(self):
        self.current_rotation = 0
        self._step = 30
        self.data = qg.QPixmap(":/icons/icons/sand_clock.ico")
        self.transform = qg.QTransform()
        self.timer = qc.QTimer()

    def step(self) -> qg.QPixmap:
        self.transform.rotate(self._step)
        rotated_pixmap = self.data.transformed(self.transform)
        return rotated_pixmap
