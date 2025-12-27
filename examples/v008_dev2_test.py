import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, panel, Text

class GameApp(App):
    def on_start(self):
        self.x = 5
        self.y = 5
        self.msg = "Use Arrow Keys to Move. 'q' to Quit."

    def on_key(self, key):
        if key == 'UP': self.y -= 1
        elif key == 'DOWN': self.y += 1
        elif key == 'LEFT': self.x -= 1
        elif key == 'RIGHT': self.x += 1
        elif key == 'q': self.exit()

        self.x = max(0, min(20, self.x))
        self.y = max(0, min(10, self.y))

    def render(self):
        rows = []
        for r in range(12):
            if r == self.y:
                row = " " * self.x + "@" + " " * (20 - self.x)
            else:
                row = " " * 21
            rows.append(row)

        board = "\n".join(rows)

        return panel(
            board + "\n\n" + self.msg,
            title=f"Pos: ({self.x}, {self.y})",
            render=True
        )
    
if __name__ == "__main__":
    GameApp(refresh_rate=0.05).run()