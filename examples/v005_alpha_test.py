import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, tree, columns, table

def main():
    cprint("--- Termella v0.0.5a Alpha (Layouts) ---", styles="bold")
    print()

    # 1. Create a Panel (Rendered, not printed)
    info_panel = panel(
        "System: Online\nCPU: 12%\nRAM: 4.2GB", 
        color="magenta", 
        title="Stats", 
        render=True
    )

    # 2. Create a Tree (Rendered)
    file_structure = {
        "src": {
            "main.py": "File",
            "utils.py": "File"
        },
        "tests": {
            "test_ui.py": "File"
        },
        "README.md": "File"
    }
    tree_view = tree(file_structure, root_name="Project", render=True)

    # 3. Display Side-by-Side using Columns
    cprint("[Layout: Panel + Tree]", color="yellow")
    columns(info_panel, tree_view, padding=4)

    print()

    # 4. Complex Layout (Table + Panel)
    cprint("[Layout: Table + Panel]", color="yellow")
    
    data = [["001", "Active"], ["002", "Offline"]]
    tbl = table(data, headers=["ID", "Status"], border_color="cyan", render=True)
    
    note = panel("Check ID 002\nConnection Timeout", color="red", title="Alerts", render=True)
    
    columns(tbl, note)

if __name__ == "__main__":
    main()