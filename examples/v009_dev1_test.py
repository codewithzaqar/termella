import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, HBox, panel

class LayoutApp(App):
    def render(self):
        header = Label("[bold white bg_blue]  My Application v0.9  [/]")

        sidebar = VBox(
            Label("[cyan]Dashboard[/]"),
            Label("[dim]Settings[/]"),
            Label("[dim]Logout[/]"),
            padding=1
        )
        sidebar_panel = panel(str(sidebar), title="Menu", render=True)

        content = Label("This is the main content area.\nIt sits next to the sidebar.")
        content_panel = panel(str(content), title="View", render=True)

        middle = HBox(
            Label(sidebar_panel),
            Label(content_panel),
            padding=2
        )

        root = VBox(
            header,
            middle,
            padding=1
        )

        return root
    
if __name__ == "__main__":
    LayoutApp(refresh_rate=0.5).run()