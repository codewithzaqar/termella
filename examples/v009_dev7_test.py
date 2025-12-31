import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Screen, Label, VBox, panel

class ScreenApp(App):
    def on_start(self):
        self.header = Label("[bold reverse] Termella App [/]")
        self.body = Label("Resize the window to see updates.")

        root = Screen(
            self.header,
            Label(""),
            self.body
        )
        self.set_screen(root)

    def on_resize(self, width, height):
        self.body.raw_text = f"Screen Size: {width}x{height}"
        super().on_resize(width, height)

if __name__ == "__main__":
    ScreenApp(refresh_rate=0.1).run()