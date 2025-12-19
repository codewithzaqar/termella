import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, grid, columns

def main():
    cprint("--- Termella v0.0.5.dev2 RC Test ---", styles="bold")
    print()

    cprint("[1] Vvrical Alignment (Center)", color="cyan")
    short = panel("Short", render=True)
    tall = panel("Tall\nPanel\nWith\nHeight", render=True)

    columns(short, tall, padding=4, align="center")
    print()

    cprint("[2] Grid Layout (3 Columns)", color="cyan")

    my_widgets = []
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

    for i in range(6):
        p = panel(f"Item #{i+1}", color=colors[i], title=f"Box {i+1}", render=True)
        my_widgets.append(p)

    grid(my_widgets, cols=3, padding=2)

if __name__ == "__main__":
    main()