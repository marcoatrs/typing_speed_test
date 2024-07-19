from collections import deque

from PySide6 import QtCore as qc

from src.controller.text_html import HtmlParser

class Typing:

    def __init__(self):
        self.writes = deque(maxlen=15)
        self.get_timer = qc.QTimer()
        self.text = ""
        self.current = 0
        self.words = 0
        self.fails = 0
        self.type_results: list[bool] = []
        self.wpm_list = []
        self.wpm = 0


    def get_element(self):
        if self.writes:
            return self.writes.popleft()
        # if self.get_timer.isActive():
        #     self.get_timer.stop()

    def push_element(self, element: str):
        self.writes.append(element)

    def pop_element(self):
        if len(self.writes) == 0:
            return
        self.html.pop()
        self.current -= 1
        self.current = max(self.current, 0)
        self.words = len(self.text[:self.current].split(" "))
        if len(self.type_results) == 0:
            return
        if not self.type_results.pop():
            self.fails -= 1

    def calculate_wpm(self, total_time: int):
        self.wpm = 60 * self.words // total_time
        self.wpm_list.append(self.wpm)

    def __str__(self) -> str:
        return "".join(self.writes)

    def load_text(self, text: str):
        self.text = text
        self.html = HtmlParser(self.text.replace(" ", "_")) # ·
        self.current = 0

    def compare_char(self) -> bool:
        r = self.text[self.current] == self.writes[-1]
        self.html.push(r)
        self.type_results.append(r)
        self.current += 1
        self.words = len(self.text[:self.current].split(" "))
        if not r:
            self.fails += 1
        return r
