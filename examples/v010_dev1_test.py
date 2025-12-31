import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, HBox, panel, Screen

class LayoutTest(App):
    def on_start(self):
        self.sidebar = Label("Sidebar", style="white bg_blue", width=15)
        self.main = Label("Main Content (50%)", style="white bg_green", align="center", width="50%")
        self.extra = Label("Auto", style="white bg_magenta", align="right")
        self.layout = HBox(self.sidebar, self.main, self.extra, padding=0)
        self.set_screen(Screen(self.layout))

    def on_resize(self, w, h):
        pass

if __name__ == "__main__":
    LayoutTest(refresh_rate=0.1).run()