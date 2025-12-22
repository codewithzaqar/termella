import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag, parse

def main():
    print("--- Termella v0.0.7.dev1 (Markup Prototype) ---")
    print()

    t = parse("[red]Red[/]")

    print("1. Text + Text:", t + t)

    print_tag("2. Text + Str: ", t + " suffix")

    try:
        res = "prefix " + t
        print("3. Str + Text: ", res)
    except TypeError as e:
        print("3. FAILED:", e)

    print(f"4. f-string:  val={t}")

if __name__ == "__main__":
    main()