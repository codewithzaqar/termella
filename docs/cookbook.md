# Cookbook

## The Worker Monitor (v0.0.6)

A pattern for monitoring a long-running task.

```python
import time
import random
from termella import Live, panel, progress_bar, Text, grid

def get_progress_panel(percent):
    chars = int(20 * (percent / 100))
    bar = "█" * chars + "-" * (20 - chars)
    return panel(f"[{bar}] {percent}%", title="Progress", color="cyan", render=True)

def get_logs_panel(logs):
    content = "\n".join(logs[-5:])
    return panel(content, title="Recent Activity", color="dim", render=True)

def run_monitor():
    logs = []

    with Live(refresh=0.1) as live:
        for i in range(101):
            if random.random() < 0.1:
                msg = f"Processed batch #{i}"
                logs.append(msg)
                live.log(Text(f"[LOG] {msg}").style(color="green"))

            p_prog = get_progress_panel(i)
            p_logs = get_logs_panel(logs)

            live.update(grid([p_prog, p_logs], cols=1, render=True))

run_monitor()
```