class HtmlParser:

    def __init__(self, text: str):
        self.text = text
        self.registry: list[list[bool, str, str]] = []
        self.count = 0

    def parse_html(self, text: str, ok: bool) -> str:
        color = "#00FF00" if ok else "#FF0000"
        return f'<span style="color:{color};">{text}</span>'

    def push(self, ok: bool = True):
        char = self.text[self.count]
        self.count += 1
        # Nuevo registro
        if (len(self.registry) == 0) or (self.registry[-1][0] != ok):
            self.registry.append([ok, char, self.parse_html(char, ok)])
            return
        # Añadir a ultimo registro
        self.registry[-1][1] += char
        self.registry[-1][2] = self.parse_html(self.registry[-1][1], ok)

    def pop(self):
        if len(self.registry) == 0:
            return
        self.count -= 1
        if len(self.registry[-1][1]) == 1:
            return self.registry.pop()
        self.registry[-1][1] = self.registry[-1][1][:-1]
        self.registry[-1][2] = self.parse_html(self.registry[-1][1],
                                               self.registry[-1][0])

    def __str__(self) -> str:
        html_list = list(map(lambda item: item[2], self.registry))
        html = "".join(html_list)
        html += f'<span>{self.text[self.count:]}</span>'
        return html
