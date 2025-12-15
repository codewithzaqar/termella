import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, progress_bar, cinput

def main():
    cprint("--- Termella v0.0.2a Alpha Test ---", styles="bold")

    username = cinput("Enter your username >", color="yellow")
    cprint(f"Welcome, {username}!", color="green")
    print()

    cprint("Initiating Alpha Sequence...", color="blue")
    items = 50
    for i in range(items + 1):
        time.sleep(0.02)
        progress_bar(i, items, color="magenta", length=40)

    cprint("Done.", color="green")

if __name__ == "__main__":
    main()