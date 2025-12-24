import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag

def main():
    print("--- Termella v0.0.7.dev2 (Nested Markup) ---")
    print()

    print_tag("[red]Hello [bold]World[/]![/]")
    print_tag("[blue]Outer [bg_white]Middle [red]Inner[/] Middle[/] Outer[/]")
    print_tag("[green]Green[/] Normal [yellow]Yellow[/]")
    print_tag("This is [unknown]ignored style[/].")

if __name__ == "__main__":
    main()