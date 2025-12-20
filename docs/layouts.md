# Layouts and Composition

Termella v0.0.5 introduces a Layout Engine allowing you to arrange text blocks side-by-side.

## 1. Columns (`columns`)
Places widgets horizontally.

```python
columns(*widgets, padding=2, align="top", render=False)
```
* **padding**: Number of spaces between columns.
* **align**: Vertical alignment of shorter columns (`"top"`,`"center"`,`"bottom"`).
* **render**: If `True`, returns the resulting string instead of printing.

### Example:
```python
from termella import panel, columns

p1 = panel("Short", render=True)
p2 = panel("Tall\nPanel\nHere", render=True)

columns(p1, p2, align="center")
```
## 2. Grids (`grid`)
Arranges a list of widgets into rows and columns automatically.
```python
grid(widgets, cols=3, padding=2, render=False)
```

### Example:
```python
from termella import panel, grid

# Create 6 panels
items = [panel(f"Box {i}", render=True) for i in range(6)]

# Print in 3x2 grid
grid(items, cols=3)
```

### 3. Trees (`tree`)
Visualizes nested dictionaries.
```python
tree(data, root_name=".", render=False)
```
* **data**: A nested dictionary. Keys are branches, values are leaves (or nested dicts).
* **root_name**: The title of the root node.

## 4. Composition (Nesting)
All Termella widgets (`panel`, `table`, `columns`, `tree`, etc.) now accept `render=True`. This allows you to build complex interfaces by nesting them.

### Pattern:
1. Create inner widgets with `render=True`.
2. Pass them into a layout (`columns` or `grid`) with `render=True`.
3. Pass that result into a container (`panel`) or print it.
```python
# Tree inside a Panel
t_str = tree(data, render=True)
p = panel(t_str, title="File Browser")
```