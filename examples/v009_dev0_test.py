import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, panel

class ComponentApp(App):
    def on_start(self):
        self.lbl_status = Label("Status: [green]Active[/]")
        self.lbl_info = Label("Press [bold]C[/] to toggle", style="dim")

    def on_key(self, key):
        if key == 'c':
            if "Active" in self.lbl_status.raw_text:
                self.lbl_status = Label("Status: [red]Offline[/]")
            else:
                self.lbl_status = Label("Status: [green]Active[/]")
        elif key == 'q':
            self.exit()

    def render(self):
        combined = str(self.lbl_status) + "\n\n" + str(self.lbl_info)
        return panel(combined, title="Component System", render=True)

if __name__ == "__main__":
    ComponentApp(refresh_rate=0.1).run()