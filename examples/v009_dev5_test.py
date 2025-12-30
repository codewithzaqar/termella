import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Button, VBox, Label, panel

class MouseApp(App):
    def on_start(self):
        self.btn1 = Button("Top Button", on_click=lambda: self.log("Top Clicked"))
        self.btn2 = Button("Bottom Button", on_click=lambda: self.log("Bot Clicked"))
        self.msg = "Click buttons!"

        self.add_focusable(self.btn1)
        self.add_focusable(self.btn2)

        self.btn1.set_rect(1, 5, 20, 1)
        self.btn2.set_rect(1, 7, 20, 1)

    def log(self, t): self.msg = t

    def render(self):
        header = panel("Mouse Test", render=True)

        layout = VBox(
            Label(header),
            self.btn1,
            Label(""),
            self.btn2,
            Label(""),
            Label(f"Status: {self.msg}")
        )
        return layout
    
if __name__ == "__main__":
    MouseApp(refresh_rate=0.1, mouse=True).run()