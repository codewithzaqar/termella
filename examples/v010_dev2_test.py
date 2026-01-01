import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, HBox, Screen

class GrailApp(App):
    def on_start(self):
        header = Label("[bold white bg_blue] HEADER [/]", align="center", width="100%")
        nav = Label("Nav\nItem 1\nItem 2", style="white bg_red", width=15)
        main = Label("Main Content Area\n(Resizes automatically)", style="black bg_white", align="center")
        aside = Label("Aside", style="white bg_red", width=15)
        middle = HBox(nav, main, aside, padding=0)
        footer = Label("Footer", style="white bg_blue", align="center", width="100%")
        
        self.layout = Screen(
            header,
            middle,
            footer
        )
        self.set_screen(self.layout)

if __name__ == "__main__":
    GrailApp(refresh_rate=0.1).run()