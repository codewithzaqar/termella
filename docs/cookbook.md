# 🍳 Cookbook

## The Calculator (v0.0.9)

A grid of buttons.

```python
from termella import App, Button, Label, VBox, grid, panel

class CalcApp(App):
    def on_start(self):
        self.display = "0"
        self.buttons = []
        
        # Create Keypad
        keys = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]
        
        for k in keys:
            btn = Button(f" {k} ", on_click=lambda x=k: self.press(x))
            self.buttons.append(btn)
            self.add_focusable(btn)

    def press(self, key):
        if key == "C": self.display = "0"
        elif key == "=":
            try: self.display = str(eval(self.display))
            except: self.display = "Error"
        else:
            if self.display == "0": self.display = key
            else: self.display += key

    def render(self):
        screen = panel(
            Label(f"[right]{self.display}[/]", align="right"), 
            width=20, render=True
        )
        
        # Convert Button objects to strings for the 'grid' functional layout
        # (Future versions will have OOGrid container)
        keypad_str = grid([str(b) for b in self.buttons], cols=4, render=True)
        
        return VBox(Label(screen), Label(keypad_str), padding=1)

CalcApp().run()
```