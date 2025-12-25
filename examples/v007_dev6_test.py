import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag

def main():
    print("--- Termella v0.0.7.dev6 (Robustness) ---")
    print()

    print_tag("[red]Error: Something went wrong (Unclosed)")

    print_tag("This has an empty tag [] inside.")

    print_tag("[rgb(invalid)]This has broken color[/], but text remains.")

    print_tag("This tag is [bold incomplete")

if __name__ == "__main__":
    main()