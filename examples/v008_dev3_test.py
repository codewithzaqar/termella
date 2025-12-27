import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, panel, columns

class FlickerTestApp(App):
    def on_start(self):
        self.val = 0

    def on_update(self):
        self.val += 1

    def render(self):
        noise = "".join([random.choice(" .:+*#") for _ in range(200)])
        noise_block = "\n".join([noise[i:i+20] for i in range(0, 200, 20)])

        p1 = panel(f"Frame: {self.val}\nNo Flicker!", title="Status", render=True)
        p2 = panel(noise_block, title="Static Noise", color="dim", render=True)

        return columns(p1, p2, render=True)
    
if __name__ == "__main__":
    FlickerTestApp(refresh_rate=0.02).run()