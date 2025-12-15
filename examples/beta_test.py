import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, progress_bar, cinput, panel

def main():
    cprint("--- Termella v0.0.2b Beta Test ---", styles="bold")

    cprint("Test: Try pressing Ctrl+C inside the input:", color="yellow")
    res = cinput("Input >")
    if res is None:
        cprint("\nCaught KeyboardInterrupt gracefully!", color="green")
    else:
        cprint(f"You typed: {res}", color="green")

    print("\n[Testing Type Safety]")
    panel(12345, color="red", title="Integer Input")

    print("\n[Testing Zero Division Protection]")
    progress_bar(0, 0)
    print(" (Survived 0 total)")

    print("\n[Testing Cursor Hiding]")
    total = 30
    for i in range(total + 1):
        time.sleep(0.05)
        progress_bar(i, total, color="bright_blue")

    cprint("\nBeta Test Complete.", color="green", styles="bold")

if __name__ == "__main__":
    main()