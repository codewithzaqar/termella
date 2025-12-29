import sys
import os

# Ensure we import local termella
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import App, panel, columns, Text

class InputTester(App):
    def on_start(self):
        self.last_key = "None"
        self.last_click = "None"
        self.counter = 0

    def on_update(self):
        self.counter += 1

    def on_key(self, key):
        self.last_key = str(key)
        if key == 'q' or key == 'ESC':
            self.exit()

    def on_click(self, x, y, btn):
        self.last_click = f"{btn} at ({x}, {y})"

    def render(self):
        # 1. Info Panel
        info_text = (
            f"Frame: {self.counter}\n"
            f"Last Key: [green bold]{self.last_key}[/]\n"
            f"Last Click: [yellow bold]{self.last_click}[/]"
        )
        # We need to parse markup manually if using old panel style, 
        # but let's assume Text supports basic string content for now
        # Actually v0.0.7 added parsing.
        from termella import parse
        p_info = panel(parse(info_text), title="Input Monitor", render=True)

        # 2. Instructions Panel
        instr_text = (
            "1. Press Keys (Arrows, Enter)\n"
            "2. Click Mouse anywhere\n"
            "3. Press 'q' or 'ESC' to Quit"
        )
        p_instr = panel(instr_text, title="Instructions", color="blue", render=True)

        return columns(p_info, p_instr, render=True)

if __name__ == "__main__":
    print("Launching Input Tester...")
    # Enable Mouse!
    app = InputTester(refresh_rate=0.05, mouse=True)
    app.run()