import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import App, cprint, panel

class MyApp(App):
    def on_start(self):
        cprint(panel("Welcome to Termella OS v0.0.8", color="green"))
        self.counter = 3

    def update(self):
        print(f"App shutting down in {self.counter}...")
        self.counter -= 1
        time.sleep(1)

        if self.counter < 0:
            self.exit()

if __name__ == "__main__":
    print("Launching Full-Screen App...")
    time.sleep(1)

    app = MyApp()
    app.run()

    print("App Finished. Notice how the terminal history was preserved!")