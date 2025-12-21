import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel, cprint

def main():
    cprint("--- Termella v0.0.6.dev2 RC Test ---", styles="bold")
    cprint("This script will CRASH in 3 seconds.", color="red")
    cprint("Verify that your cursor reappears afterwards.", color="yellow")
    print()

    try:
        with Live(refresh_rate=1.0) as live:
            for i in range(3, 0, -1):
                live.update(panel(f"Crashing in {i}...", color="red", render=True))

            raise ValueError("Simulated User Code Crash")
        
    except ValueError as e:
        print()
        cprint(f"Caught Expected Error: {e}", color="green")
        cprint("Cursor should be visible now [ _ ]", color="cyan")

if __name__ == "__main__":
    main()