import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, columns, tree, Text

def main():
    cprint("--- Termella v0.0.5.dev4 RC3 Test (Nesting) ---", styles="bold")
    print()

    my_data = {"src": {"api.py": "File"}, "config": {"settings.json": "File"}}
    tree_str = tree(my_data, root_name="Project", render=True)

    left_panel = panel(tree_str, title="File System", color="blue", render=True)
    stats_panel = panel("Status: OK\nPing: 12ms", title="Network", color="green", render=True)
    layout_block = columns(left_panel, stats_panel, padding=2, render=True)
    cprint("[Master Dashboard]", color="yellow")
    master_view = panel(layout_block, title="Main Dashboard", color="white")

if __name__ == "__main__":
    main()