import random
import statistics
from time import perf_counter

from PySide6 import QtCore as qc
from PySide6 import QtWidgets as qw

from src.controller.events import set_ui_events
from src.controller.graphs import GuiChart
from src.controller.language import set_languages
from src.controller.load_screen import LoadScreen
from src.controller.screen import TypingTest
from src.controller.type_test import Typing
from src.db.read_db import get_db


class Controller:

    def __init__(self):
        self._app = qw.QApplication([])
        self.view = TypingTest()
        self.load_screen = LoadScreen()
        self.typing = Typing()
        self.results_graph = GuiChart(self.view.web_view_results,
                                      "Speed Test Results", "", "WPM")
        self.db = []
        set_ui_events(self)
        self.total_time = 0
        self.test_active = False  # Ya inicio
        self.can_start = False  # Puede iniciar
        self.test_finish = False  # Ya termino

    def run(self):
        set_languages(self.view)
        self.view.show()
        self._app.exec_()

    def load_db_info(self):
        language = self.view.combo_language.currentText()
        self.get_db(language)
        if not self.db:
            return
        self.view.stackedWidget.setCurrentWidget(self.view.page_load_screen)
        self.load_screen.timer.start(50)
        qc.QTimer.singleShot(1000, self.show_typing_screen)

    def load_screen_step(self):
        image = self.load_screen.step()
        self.view.label_load.setPixmap(image)

    def show_typing_screen(self):
        self.set_text()
        self.view.stackedWidget.setCurrentWidget(self.view.page_test)
        self.load_screen.timer.stop()
        self.can_start = True

    def get_db(self, language) -> list[tuple[str]]:
        self.db = get_db(language)

    def set_text(self):
        if not self.db:
            print("No data")
            return
        text = random.choice(self.db)[0]
        self.view.text_test.setText(text.replace(" ", "_"))
        self.typing.load_text(text)

    def test_show_timer(self):
        time = perf_counter() - self.total_time

        # Lo que tu escribes
        self.typing.get_element()
        self.view.label_test.setText(str(self.typing))

        # Indicadores
        # WPM
        self.typing.calculate_wpm(time)
        self.view.label_wpm.setText(f"    WPM: {self.typing.wpm}")
        # Fallos
        self.view.label_failures.setText(f"    Failures: {self.typing.fails}")
        # Tiempo Total
        self.view.label_time.setText(f"    Time: {int(time)} seconds")

    def key_press_event(self, event):
        if self.test_finish or not self.can_start:
            return

        #  | alt | crtl | windows | tab
        if event.key() in [16777248, 16777251, 16777249, 16777250, 16777217]:
            return

        # Backspace
        if (event.key() == 16777219):
            if self.test_active:
                self.typing.pop_element()
                self.view.text_test.setHtml(str(self.typing.html))
            return

        if not self.typing.get_timer.isActive():
            self.typing.get_timer.start(1000)
            self.total_time = perf_counter()
            self.test_active = True

        if not self.test_active:
            return

        self.typing.push_element(event.text())
        self.view.label_test.setText(str(self.typing))

        if self.typing.current == (len(self.typing.text) - 1):
            self.typing.get_timer.stop()
            self.show_results()
            self.view.stackedWidget.setCurrentWidget(self.view.page_results)
            self.test_active = False
            self.can_start = False
            self.test_finish = True
            return

        self.typing.compare_char()
        self.view.text_test.setHtml(str(self.typing.html))

    def show_results(self):
        wpm = statistics.median(self.typing.wpm_list)
        total_success = list(
            filter(lambda item: item, self.typing.type_results))
        success_per = round(
            len(total_success) / len(self.typing.type_results) * 100, 2)

        self.view.label_wpm_result.setText(f"WPM: {wpm}")
        self.view.label_success_per.setText(
            f"Success percentage: {success_per}%")
        self.results_graph.plot(self.typing.wpm_list)
