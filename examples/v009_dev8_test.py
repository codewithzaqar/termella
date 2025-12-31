import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, panel, Text, VBox

class RenderTestApp(App):
    def on_start(self):
        self.mode = 0
        self.modes = [
            "Single Widget (Label)",
            "List of Widgets (Auto-Grid)",
            "Raw String",
            "Rich Text Object"
        ]

    def on_key(self, key):
        if key == 'SPACE' or key == 'ENTER':
            self.mode = (self.mode + 1) % len(self.modes)
        elif key == 'q' or key == 'ESC':
            self.exit()

    def render(self):
        header = Label(f"[bold reverse] Render Mode: {self.modes[self.mode]} [/] (Press Space)")

        if self.mode == 0:
            content = Label("[green]I am a Label Object[/]\nThe App class converts me via __str__.")
            return VBox(header, Label(""), content)
        
        elif self.mode == 1:
            items = [
                panel("Item 1", color="red", render=True),
                panel("Item 2", color="blue", render=True),
                panel("Item 3", color="yellow", render=True)
            ]
            return [header, Label("")] + items
        
        elif self.mode == 2:
            return f"{header}\n\nThis is just a [dim]standard python string[/]."
        
        elif self.mode == 3:
            from termella import parse
            t = parse(f"{header}\n\n[rgb(255,0,255)]I am a rich Text object![/]")
            return t
        
if __name__ == "__main__":
    RenderTestApp(refresh_rate=0.1).run()