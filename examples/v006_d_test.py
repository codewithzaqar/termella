import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel, cprint

def main():
    cprint("--- Termella v0.0.6.dev3 RC2 Test ---", styles="bold")
    print()

    with Live(refresh_rate=0.5) as live:
        for i in range(5):
            p1 = panel(f"Count: {i}", title="Top", render=True)
            p2 = panel(f"Double: {i*2}", title="Bottom", render=True)

            live.update([p1, p2])

    cprint("Done.", color="green")

if __name__ == "__main__":
    main()