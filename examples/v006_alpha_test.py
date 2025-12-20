import sys
import os
import time
import random
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel, columns, table, Text

def generate_dashboard():
    # 1. Clock Panel
    now = datetime.now().strftime("%H:%M:%S")
    clock = panel(
        Text(now).style(color="green", styles="bold"),
        title="Current Time",
        render=True
    )

    # 2. Random Data Table
    data = [
        ["Server A", f"{random.randint(20, 90)}%", "Active"],
        ["Server B", f"{random.randint(10, 50)}%", "Active"],
        ["Server C", f"{random.randint(0, 5)}%", "Idle"]
    ]
    tbl = table(
        data,
        headers=["Host", "CPU", "State"],
        border_color="blue",
        render=True
    )

    # 3. Combine Side-by-Side
    return columns(clock, tbl, align="center", render=True)

def main():
    print("--- Termella v0.0.6.dev0 Live Engine ---")
    print("Press Ctrl+C to stop.")
    print()

    try:
        with Live(refresh_rate=0.5) as live:
            for _ in range(20):
                view = generate_dashboard()
                live.update(view)
    
    except KeyboardInterrupt:
        pass

    print("Live view stopped.")

if __name__ == "__main__":
    main()