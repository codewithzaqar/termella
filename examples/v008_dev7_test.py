import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, panel, Text

class ResizeApp(App):
    def on_start(self):
        self.msg = "Resize Me!"

    def on_resize(self, width, height):
        self.msg = f"Resized to {width}x{height}"

    def render(self):
        content = f"Current Size: [green bold]{self.width}x{self.height}[/]\n{self.msg}"

        from termella import parse
        p = panel(parse(content), title="Responsive App", render=True)

        p_lines = str(p).split('\n')
        p_h = len(p_lines)
        p_w = len(p_lines[0]) if p_lines else 0

        top_pad = (self.height - p_h) // 2
        left_pad = (self.width - p_w) // 2

        top_pad = max(0, top_pad)
        left_pad = max(0, left_pad)

        output = []
        output.append("\n" * top_pad)
        for line in p_lines:
            output.append((" " * left_pad) + line)

        return "\n".join(output)
    
if __name__ == "__main__":
    ResizeApp(refresh_rate=0.2).run()