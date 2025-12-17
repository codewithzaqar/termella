import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, table, Spinner

def main():
    cprint("--- Termella v0.0.3a Preview ---", styles="bold")
    print()

    # 1. Test Spinner
    cprint("[1] Testing Async Spinner:", color="cyan")
    with Spinner("Connecting to database..."):
        time.sleep(2.5)  # Simulate work

    print()

    # 2. Test Table
    cprint("[2] Testing Table Renderer:", color="cyan")

    headers = ["ID", "Name", "Role"]
    data = [
        ["001", "Alice", "Admin"],
        ["002", "Bob", "Developer"],
        ["003", "Charlie", "Designer"]
    ]

    table(data, headers=headers, border_color="blue")

if __name__ == "__main__":
    main()