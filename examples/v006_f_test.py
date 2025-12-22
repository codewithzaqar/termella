import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import Live, panel, cprint, Text

def main():
    cprint("--- Termella v0.0.6.dev5 Logging Test ---", styles="bold")
    print()

    with Live(refresh=0.2) as live:
        for i in range(20):
            status_panel = panel(
                f"Processing Item #{i}\nActive Threads: {random.randint(1, 5)}",
                title="Worker Status",
                color="blue",
                render=True
            )
            live.update(status_panel)

            if i % 5 == 0:
                msg = Text(f"[INFO] Batch {i//5} completed successfully.").style(color="green")
                live.log(msg)

            if i == 12:
                live.log(Text("[WARN] High CPU usage detected").style(color="yellow"))

    cprint("Process Complete.", color="green")

if __name__ == "__main__":
    main()