# Widgets Reference

Termella v0.0.3 includes a suite of UI components to make your CLI tools professional.

## 1. Tables (`tables`)

Render tabular data with automatic column sizing and alignment.

```python
from termella import table

headers = ["Item", "Qty", "Price"]
data = [
    ["Apple", 5, "$1.20"],
    ["Banana", 12, "$0.80"]
]

# Simple
table(data, headers=headers)

# Advanced (Alignment)
# Item: left, qty: center, price: right
table(data, headers=headers, align=["left", "center", "right"], border_color="blue")
```

---

## 2. Spinners (`Spinner`)
Include background work without blocking the main thread. Use as a Context Manager.
```python
from termella import Spinner
import time

# Success case
with Spinner("Querying Database..."):
    time.sleep(2) # Your heavy logic here

# Failure case (Automatic)
try:
    with Spinner("Connecting..."):
        raise ConnectionError("Timeout")
except ConnectionError:
    pass # Spinner automatically prints "Connecting... Failed!"
```
---
## 3. Progress Bars (`progress_bar`)
Visualize loops.
```python
from termella import progress_bar

for i in range(101):
    progress_bar(i, 100, color="green")
```
---
## 4. Panels (`panel`)
Frame your text.
```python
from termella import panel
panel("Crucial Information", color="red", title="Alert")
```