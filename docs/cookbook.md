# 🍳 Cookbook

## The File Navigator (v0.0.8)

A simple file browser using the App framework.

```python
import os
from termella import App, panel, select, grid

class FileManager(App):
    def on_start(self):
        self.path = os.getcwd()
        self.files = []
        self.selected_idx = 0
        self.refresh_files()

    def refresh_files(self):
        try:
            self.files = [".."] + [f for f in os.listdir(self.path)]
        except PermissionError:
            self.files = ["..", "(Access Denied)"]

    def on_key(self, key):
        if key == 'UP': 
            self.selected_idx = max(0, self.selected_idx - 1)
        elif key == 'DOWN': 
            self.selected_idx = min(len(self.files) - 1, self.selected_idx + 1)
        elif key == 'ENTER':
            chosen = self.files[self.selected_idx]
            new_path = os.path.normpath(os.path.join(self.path, chosen))
            if os.path.isdir(new_path):
                self.path = new_path
                self.selected_idx = 0
                self.refresh_files()
        elif key == 'q':
            self.exit()

    def render(self):
        # Build List View manually (or use future Layout widgets)
        lines = []
        start = max(0, self.selected_idx - 5)
        end = start + 10
        
        for i, f in enumerate(self.files[start:end]):
            real_idx = start + i
            if real_idx == self.selected_idx:
                lines.append(f"> [green bold]{f}[/]")
            else:
                lines.append(f"  {f}")
        
        from termella import parse
        p = panel(parse("\n".join(lines)), title=self.path, render=True)
        return p

FileManager().run()
```