import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from termella import cprint, table, Spinner

def main():
    cprint("--- Termella v0.0.3c RC Test ---", styles="bold")
    print()

    # Data: Product List
    headers = ["ID", "Product", "Price", "Stock"]
    data = [
        [1, "Widget A", "$10.50", 100],
        [2, "Widget B", "$5.99", 5000],
        [3, "Premium Kit", "$1,250.00", 2],
        [4, "Cheap Part", "$0.99", 150]
    ]

    # Test 1: Default Alignment (Left)
    cprint("[1] Default Alignment (Left):", color="cyan")
    table(data, headers=headers)
    print()

    # Test 2: Custom Alignment
    # ID: Center, Product: Left, Price: Right, Stock: Right
    cprint("[2] Financial Alignment (Center, Left, Right, Right):", color="cyan")
    
    custom_align = ["center", "left", "right", "right"]

    table(data, headers=headers, align=custom_align, border_color="green")

    print()
    cprint("v0.0.3c Release Candidate Verified.", color="green")

if __name__ == "__main__":
    main()