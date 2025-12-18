import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, select, checkbox

def main():
    cprint("--- Termella v0.0.4d Pagination Test ---", styles="bold")
    print()

    # Generate 50 items
    countries = [f"Country #{i}" for i in range(1, 51)]

    # 1. Text Select with Limit
    cprint("[1] Scrolling Select (Limit 5 of 50):", color="yellow")

    choice = select(
        countries,
        prompt="Choose a destination:",
        color="magenta",
        limit=5
    )

    if choice:
        cprint(f">> You chose: {choice}", color="green")

    print()

    # 2. Test Checkbox with Limit
    cprint("[2] Scrolling Checkbox (Limit 8 of 50):", color="yellow")

    selections = checkbox(
        countries,
        prompt="Select multiple destinations:",
        color="blue",
    )

    if selections:
        cprint(f">> Selected {len(selections)} countries.", color="green")

if __name__ == "__main__":
    main()