import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, select, checkbox

def main():
    cprint("--- Termella v0.0.4c RC2 Test ---", styles="bold")
    print()

    # 1. Test ESC on Select
    cprint("[1] Test Canellation:", color="yellow")
    result = select(
        ["Confirm", "Deny"],
        prompt="Do you want to proceed? (Try pressing ESC)",
        color="red"
    )

    if result is None:
        cprint(">> Menu Canelled (Success)", color="green")
    else:
        cprint(f">> Selected: {result}", color="dim")

    print()

    # 2. Test ESC on Checkbox
    cprint("[2] Test Multi-Select Cancellation:", color="yellow")
    res_list = checkbox(
        ["File A", "File B", "File C"],
        prompt="Select files to delete (Try pressing ESC):",
        color="red"
    )

    if not res_list:
        cprint(">> No files selected or Cancelled (Success)", color="green")
    else:
        cprint(f">> Deleting: {res_list}", color="red")

if __name__ == "__main__":
    main()