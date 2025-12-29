import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, panel, Text

class HybridApp(App):
    def on_start(self):
        self.x = 2
        self.counter = 0

    def on_key(self, key):
        if key == 'RIGHT': self.x += 1
        elif key == 'LEFT': self.x -= 1
        elif key == 'q' or key == 'ESC': self.exit()

        self.x = max(0, min(30, self.x))

    def on_update(self):
        self.counter += 1

    def render(self):
        pad = " " * self.x
        move_box = f"{pad}[yellow]█[/]"
        info = f"Update Count: {self.counter}"

        from termella import parse
        return panel(parse(move_box + "\n\n" + info), title="Hybrid Loop Test", render=True)
    
if __name__ == "__main__":
    print("Launching Hybrid Loop Test...")
    print("Press LEFT/RIGHT to move instantly.")
    print("Do nothing to see slow updates.")
    time.sleep(1)

    HybridApp(refresh_rate=1.0).run()