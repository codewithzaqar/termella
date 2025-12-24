import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag

def main():
    print("--- Termella v0.0.7.dev6 (Syntax Fixes) ---")
    print()

    # 1. Literal Brackets using Raw Strings (Recommended)
    # The 'r' prefix prevents Python from warning about \[
    print_tag(r"[green]\[INFO\][/] System OK")
    
    # 2. Mixed Usage
    print_tag(r"[red]\[red\] is literal[/], [blue]this is blue[/]")
    
    # 3. Alternative: Double Backslashes
    # If you can't use raw strings, escape the backslash itself
    print_tag("[yellow]\\[WARNING\\][/] Double backslash works too")

    # 4. Pathological Case
    # Raw string handles this cleanly
    print_tag(r"Escaped open: \[ | Escaped close: \]")

if __name__ == "__main__":
    main()