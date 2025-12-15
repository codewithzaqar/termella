# Cookbook

Common patterns for using Termella v0.0.2

## 1. The CLI Login Form
Use `cinput` to create a professional prompt.

```python
from termella import cprint, cinput, panel

panel("Secure System v1.0", color="blue")

username = cinput("Username >", color="yellow")
if not username:
    cprint("\nLogin Cancelled.", color="red")
    exit()

# Note: For passwords, use Python's built-in getpass module,
# Termella cinput is for visible text.
cprint(f"Welcome, {username}!", color="green", styles="bold")
```
## 2. The File Downloader
Combine `panel` for status and `progress_bar` for visualization.

```python
import time
from termella import panel, progress_bar, cprint

# 1. Hander
panel("Downloading update_v2.zip\nSource: remote-server", color="magenta", title="Download Manager")

# 2. Progress Loop
total_size = 50
for i in range(total_size + 1):
    time.sleep(0.05) # Simulate network lag

    # Change color based on progress
    color = "red" if i < 25 else "green"

    progress_bar(i, total_size, color=color, length=40)

# 3. Completion
cprint("Download verified.", color="bright_green", styles="bold")
```
## 3. Custom Error Logs
Create a consistent logging style using `Text`.
```python
from termella import Text

def log_error(code, message):
    # Build the timestamp
    ts = Text("[ERROR] ").style(color="red", styles="bold")

    # Build the code
    err_code = Text(f"({code}) ").style(color="yellow")

    # Build the message
    msg = Text(message).style(color="white")

    print(ts + err_code + msg)

log_error(500, "Internal Server Error")
log_error(404, "Resource not found")
```