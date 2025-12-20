import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from termella import cprint, panel, table, columns, grid, Text

# 1. Server Stats Table
stats_data = [
    ["CPU", "12%", "Cool"],
    ["RAM", "4.2GB", "OK"],
    ["Disk", "85%", "Warn"]
]
# Render to string
stats_tbl = table(
    stats_data,
    headers=["Metric", "Value", "Status"],
    border_color="blue",
    render=True
)
# Wrap in Panel
stats_panel = panel(stats_tbl, title="Hardware", color="blue", render=True)

# 2. Network Info Panel
net_info = "IO: 192.168.1.50\nPort: 8080\nSSL: Enabled"
net_panel = panel(net_info, title="Network", color="green", render=True)

# 3. Recent Logs Panel
logs = "10:00 - Login Success\n10:05 - Upload Complete\n10:12 - Error: Timeout"
log_panel = panel(logs, title="System Logs", color="yellow", render=True)

# 4. Compose: Top Row (Status + Network)
top_row = columns(stats_panel, net_panel, align="top", padding=1, render=True)

# 5. Compose: Full Dashboard (Top Row over Logs)
dashboard = grid([top_row, log_panel], cols=1, padding=0, render=True)

# 6. Final Frame
cprint(Text(" --- ADMIN CONSOLE --- ").style(styles=["bold", "reverse"]))
print(dashboard)