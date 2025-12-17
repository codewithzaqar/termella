import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, checkbox, panel

def main():
    cprint("--- Termella v0.0.4b RC Test ---", styles="bold")
    print()

    # Define Options
    packages = [
        "React",
        "Vue",
        "Svelte",
        "Angular",
        "HTMX",
        "jQuery"
    ]

    # Run Checkbox Menu
    selected = checkbox(
        packages,
        prompt="Select Frontend Frameworks (Space to toggle, Enter to confirm):",
        color="bright_green"
    )

    print()

    if selected:
        # Display results
        msg = "You selected:\n" + "\n".join(f"- {s}" for s in selected)
        panel(msg, color="magenta", title="Installation Plan")
    else:
        cprint("Np packages selected.", color="yellow")

if __name__ == "__main__":
    main()