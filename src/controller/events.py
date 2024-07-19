from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controller.controller import Controller


def set_ui_events(self: "Controller"):
    view = self.view
    typing = self.typing
    graph = self.results_graph

    # Teclado
    view.keyReleaseEvent = self.key_press_event

    # Combo boxes
    view.combo_language.currentTextChanged.connect(view.enable_start)

    # Push Buttons
    view.push_start.clicked.connect(self.load_db_info)

    # Timers
    self.load_screen.timer.timeout.connect(self.load_screen_step)
    typing.get_timer.timeout.connect(self.test_show_timer)

    # Plots
    view.web_view_results.resizeEvent = graph.on_webview_resize
