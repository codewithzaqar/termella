import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, Button, panel

class FormApp(App):
    def on_start(self):
        self.msg = "Waiting..."

        self.btn_ok = Button("Confirm", on_click=self.do_ok)
        self.btn_cancel = Button("Cancel", on_click=self.do_cancel)

        self.add_focusable(self.btn_ok)
        self.add_focusable(self.btn_cancel)

    def do_ok(self):
        self.msg = "[green]Confirmed![/]"

    def do_cancel(self):
        self.msg = "[red]Cancelled![/]"

    def render(self):
        form = VBox(
            Label("Do you want to proceed?"),
            Label(""),
            self.btn_ok,
            Label(""),
            self.btn_cancel
        )

        p = panel(str(form), title="Dialog", render=True)

        status = Label(f"Status: {self.msg}")

        return VBox(Label(p), status, padding=1)
    
if __name__ == "__main__":
    print("Use TAB or UP/DOWN to switch buttons. ENTER to click.")
    FormApp(refresh_rate=0.1).run()