import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, select, panel

def main():
    cprint("--- Termella v0.0.4a Alpha (Interactive) ---", styles="bold")
    print()

    # 1. Simple Selection
    languages = ["Python", "JavaScript", "Rust", "Go", "C++"]

    choice = select(
        languages,
        prompt="Which language is your favorite?",
        color="green"
    )

    if choice:
        print()  # Spacer
        cprint(f"Excellent! You chose: {choice}", color="bright_green", styles="bold")

        # 2. Conditional Logic based on choice
        if choice == "Python":
            panel("Termella is built with Python!", color="blue")
        elif choice == "Rust":
            panel("Blazingly fast choice!", color="red")
    else:
        print()
        cprint("Selection cancelled.", color="red")
    
if __name__ == "__main__":
    main()