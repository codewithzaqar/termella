import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import print_tag

def main():
    print("--- Termella v0.0.7.dev5 (RGB Macros) ---")
    print()

    print_tag("This is [rgb(255,165,0)]Orange Text[/] using TrueColor.")

    print_tag("This has a [bg_rgb(80,0,80)]Deep Purple Background[/].")

    print_tag("[rgb(0,255,255)]Cyan Bold[/] mixed with standard styles.")

if __name__ == "__main__":
    main()