import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, table, Spinner

def main():
    cprint("--- Termella v0.0.3b Preview ---", styles="bold")
    print()

    # 1. Test Spinner
    cprint("[1] Testing Empty Table Handling:", color="cyan")
    table([], headers=["ID", "Name", "Status"], border_color="yellow")
    print()

    # 2. Test Table
    cprint("[2] Testing Spinner Success:", color="cyan")
    with Spinner("Loading assets..."):
        time.sleep(1)
    print()

    # 3. Test Spinner Failure (Exception Handling)
    cprint("[3] Testing Spinner with Exception (Crash Test):", color="cyan")
    try:
        with Spinner("Connecting to server..."):
            time.sleep(1)
            raise ValueError("Simulated Connection Error")
    except ValueError as e:
        cprint(f"Caught expected error: {e}", color="dim")

    print()
    cprint("Check cursor visibility: [  ok  ]", color="green")
    input("Press Enter to exit (cursor should be blinking...)")

if __name__ == "__main__":
    main()