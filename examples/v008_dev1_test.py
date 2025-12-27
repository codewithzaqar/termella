import sys
import os
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, panel, Text

class BouncingApp(App):
    def on_start(self):
        self.tick = 0

    def on_update(self):
        self.tick += 0.2
        if self.tick > 20: self.exit()

    def render(self):
        width = 40
        pos = int((math.sin(self.tick) + 1) / 2 * width)

        ball = "O"
        space_left = " " * pos
        space_right = " " * (width - pos)

        content = f"|{space_left}{ball}{space_right}|"

        return panel(
            Text(content).style(color="cyan", styles="bold"),
            title=f"Frame: {int(self.tick * 10)}",
            color="white",
            render=True
        )
    
if __name__ == "__main__":
    app = BouncingApp(refresh_rate=0.05)
    app.run()