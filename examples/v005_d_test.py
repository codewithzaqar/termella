import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, columns, grid

def main():
    cprint("--- Termella v0.0.5.dev3 RC2 Test ---", styles="bold")
    print()

    cprint("[1] Empty Widget in Middle:", color="yellow")
    p1 = panel("Left", render=True)
    p2 = ""
    p3 = panel("Right", render=True)

    columns(p1, p2, p3, padding=4)
    print()

    cprint("[2] Grid Remainder (7 items / 3 cols):", color="yellow")
    items = [panel(str(i), render=True) for i in range(1, 8)]
    grid(items, cols=3)

if __name__ == "__main__":
    main()