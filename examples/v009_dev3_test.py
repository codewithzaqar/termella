import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, TextInput, Button, panel

class LoginApp(App):
    def on_start(self):
        self.user_input = TextInput(placeholder="Username", width=15)
        self.pass_input = TextInput(placeholder="Password", width=15, password=True)
        self.btn = Button("Login", on_click=self.login)
        self.status = "Please login."

        self.add_focusable(self.user_input)
        self.add_focusable(self.pass_input)
        self.add_focusable(self.btn)

    def login(self):
        u = self.user_input.value
        p = self.pass_input.value
        self.status = f"[green]Logged in as: {u}[/]"

    def render(self):
        form = VBox(
            Label("User:"),
            self.user_input,
            Label("Pass:"),
            self.pass_input,
            Label(""),
            self.btn
        )

        p = panel(str(form), title="Login", render=True)
        return VBox(Label(p), Label(self.status), padding=1)

if __name__ == "__main__":
    LoginApp(refresh_rate=0.05).run()