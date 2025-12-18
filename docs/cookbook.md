# Cookbook

## Interactive Installation Wizard (v0.0.4)

Combine `cinput`, `select`, `checkbox`, and `Spinner` to create a full CLI tool.

```python
import time
from termella import cprint, cinput, select, checkbox, Spinner, panel

# 1. Welcome
panel("Termella Setup Wizard", color="blue")

# 2. Get User Info
username = cinput("Enter your name >", color="yellow")
if not username: exit()

# 3. Choose Environment
env = select(
    ["Development", "Staging", "Production"],
    prompt=f"Hi {username}, select environment:",
    color="cyan"
)
if not env: exit()

# 4. Choose Components
components = checkbox(
    ["Database", "Redis", "Nginx", "Docker"],
    prompt="Select components to install:",
    color="green"
)

# 5. Execute
print()
if components:
    msg = f"Deploying to {env}..."
    with Spinner(msg):
        time.sleep(2)
    
    cprint("Deployment Successful!", color="bright_green", styles="bold")
else:
    cprint("No components selected.", color="yellow")
```