import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel, cprint

def main():
    cprint("--- Termella v0.0.6.dev4 Manual Mode ---", styles="bold")
    print()

    with Live() as live:
        for i in range(5):
            live.update(panel(f"Manual Update #{i+1}", color="magenta", render=True))

            time.sleep(0.2)

            time.sleep(0.2)

    cprint("Finished.", color="green")

if __name__ == "__main__":
    main()