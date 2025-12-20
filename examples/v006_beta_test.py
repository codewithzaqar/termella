import sys
import os
import time
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel

def main():
    print("--- Termella v0.0.6.dev1 (Artifact Test) ---")
    print("The box below will shrink and grow.")
    print("If successful, no 'ghost lines' will appear below it.")
    print()

    # Create a spacer to ensure we aren't at the very bottom of terminal
    print("\n" * 2)

    try:
        with Live(refresh_rate=0.2) as live:
            # Oscillate height between 3 and 10 lines
            for i in range(30):
                height = 3 + (i % 7)

                content = "Line\n" * (height - 2) + "Bottom"
                view = panel(content, title=f"Height: {height}", color="magenta", render=True)

                live.update(view)
    
    except KeyboardInterrupt:
        pass

    print("Test Complete.")

if __name__ == "__main__":
    main()