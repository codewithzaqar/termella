import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Text

class ClickApp(App):
    def on_start(self):
        self.clicks = []

    def on_click(self, x, y, btn):
        self.clicks.append((x, y))
        if len(self.clicks) > 10:
            self.clicks.pop(0)

    def render(self):
        rows = []
        for r in range(1, 15):
            row_str = ""
            for c in range(1, 40):
                char = "."
                if (c, r) in self.clicks:
                    char = "X"
                row_str += char
            rows.append(row_str)

        board = "\n".join(rows)
        return Text(board + "\n\nClick anywhere! (Unix Only)").style(color="green")
    
if __name__ == "__main__":
    ClickApp(refresh_rate=0.05, mouse=True).run()