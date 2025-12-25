import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag

def main():
    print("--- Termella v0.0.7.dev7 (Hyperlinks) ---")
    print()

    print_tag("Visit [link=https://www.google.com]Google[/] search.")
    print_tag("Check out [link=https://github.com][blue underline]GitHub[/][/]!")
    print_tag("Click [link=https://example.com][red]Here[/][/] for more.")

if __name__ == "__main__":
    main()