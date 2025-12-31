import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, Label, VBox, CheckBox, Button, panel

class SettingsApp(App):
    def on_start(self):
        self.cb_sound = CheckBox("Enable Sound", checked=True)
        self.cb_notif = CheckBox("Notifications")
        self.cb_theme = CheckBox("Dark Mode", checked=True)

        self.btn_save = Button("Save", on_click=self.save)
        self.status = "Change settings..."

        self.add_focusable(self.cb_sound)
        self.add_focusable(self.cb_notif)
        self.add_focusable(self.cb_theme)
        self.add_focusable(self.btn_save)

    def save(self):
        s = "ON" if self.cb_sound.checked else "OFF"
        n = "ON" if self.cb_notif.checked else "OFF"
        t = "Dark" if self.cb_theme.checked else "Light"
        self.status = f"[green]Saved: Sound={s}, Notif={n}, Theme={t}[/]"

    def render(self):
        form = VBox(
            Label("[bold]Preferences[/]"),
            Label(""),
            self.cb_sound,
            self.cb_notif,
            self.cb_theme,
            Label(""),
            self.btn_save
        )

        p = panel(str(form), title="Settings", render=True)

        return VBox(Label(p), Label(self.status), padding=1)
    
if __name__ == "__main__":
    SettingsApp(refresh_rate=0.1).run()