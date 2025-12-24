import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag, add_alias

def main():
    print("--- Termella v0.0.7.dev4 (Themes) ---")
    print()

    print_tag("[error]Critical Failure[/]: Database disconnected.")
    print_tag("[success]Restore Complete[/]: All systems go.")

    add_alias("heading", "magenta bold underline")
    add_alias("highlight", "black bg_yellow")

    print()
    print_tag("[heading]Chapter 1: The Beginning[/]")
    print_tag("Make sure to [highlight]read this carefully[/].")

    print_tag("[dim]Ignoring [error]bad sector[/] in drive...[/]")

if __name__ == "__main__":
    main()