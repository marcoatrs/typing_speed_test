from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from PySide6.QtWebEngineWidgets import QWebEngineView


class GuiChart:

    def __init__(self, webview: QWebEngineView, title: str = 0, xlabel: str = "x", ylable: str = "y"):
        self.figure = figure(title=title,
                             x_axis_label=xlabel,
                             y_axis_label=ylable)
        self.webview = webview

    def get_bokeh_html(self):
        return file_html(self.figure, CDN, self.figure.title)

    def plot(self, wpm_list: list):
        x = list(range(len(wpm_list)))
        self.figure.line(x, wpm_list, legend_label="WPM", line_width=2)
        html = self.get_bokeh_html()
        self.webview.setHtml(html)

    def update_webview_size(self):
        """Ajustar el tamaño del visor web según el tamaño de la ventana principal."""
        rect = self.webview.geometry()
        self.figure.width = rect.width()
        self.figure.height = rect.height()

    def on_webview_resize(self, event):
        """Manejar el evento de redimensionamiento del visor web."""
        # super().resizeEvent(event)
        self.update_webview_size()
        html = self.get_bokeh_html()
        self.webview.setHtml(html)