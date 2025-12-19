import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, columns, Text

def main():
    cprint("--- Termella v0.0.5.dev1 (Alignment Test) ---", styles="bold")
    print()

    p1 = panel(
        "Line 1\nLine 2 is longer",
        title="Plain",
        render=True
    ) 

    colored_content = (
        str(Text("Red").style(color="red")) + " vs " +
        str(Text("Blue").style(color="blue")) + "\n" +
        str(Text("Green Background").style(bg="bg_green", color="black"))
    )

    p2 = panel(
        colored_content,
        title="Colors",
        color="yellow",
        render=True
    )

    cprint("Below should be perfectly aligned:", color="cyan")
    print("-" * 40)

    columns(p1, p2, padding=5)

    print("-" * 40)
    cprint("If the boxes look broken, ANSI sizing is wrong.", color="dim")

if __name__ == "__main__":
    main()