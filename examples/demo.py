import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, panel, Text

def main():
    print("--- Termella v0.0.1a Demo ---\n")

    # 1. Simple Color Printing
    cprint("Hello, Termella!", color="bright_green", styles="bold")
    cprint("This is an error message.", color="red", styles=["bold", "underline"])
    cprint("Highlight me!", color="black", bg="bg_yellow")

    print()

    # 2. Object Oriented Chaining
    t1 = Text("I am Blue ").style(color="blue")
    t2 = Text("and I am Magenta.").style(color="magenta", styles="italic")
    print(t1 + t2)

    print()

    # 3. Widgets (Panels)
    info_text = "Termella makes CLI tools\nlook professional\nwith minimal effort."
    panel(info_text, color="cyan", title="Info")

if __name__ == "__main__":
    main()