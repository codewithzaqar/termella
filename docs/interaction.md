# Interaction Guide (v0.0.4)

Termella v0.0.4 introduces interactive widgets that respond to keyboard events (Arrow Keys, Enter, Space, Escape).

## 1. Single Selection (`select`)

The `select` function creates a vertical menu. The user navigates with `UP`/`DOWN` and confirms with `ENTER`.

### Signature
```python
select(options, prompt="Select:", color="cyan", marker=">", limit=5)
```
### Parameters
- **options** *(list)*: A list of strings to display.
- **prompt** *(str)*: The question displayed above the menu.
- **color** *(str)*: The color of the highlighted item (e.g., `"green"`, `"magenta"`).
- **marker** *(str)*: The character indicating the current selection (default `">"`).
- **limit** *(int)*: The maximum number of items to show at once. If `len(options) > limit`, the menu becomes scrollable.

### Returns
- **str**: The selected option string.
- **None**: If the user presses `ESC` or `Ctrl+C`.

---
## 2. Multi-Selection(`checkbox`)
The `checkbox` function allows selecting multiple items. The user toggles items with `SPACE` and confirms with `ENTER`.

### Signature
```python
checkbox(options, prompt="Select options:", color="green", marker=">", limit=5)
```

### Visuals
- **Unchecked**: `[ ] Option`
- **Checked**: `[x] Option` (Colored)
- **Focused**: `> [ ] Option` (Highlighted)

### Returns
- **list**: A list of the selected option strings.
- **[]**: An empty list if cancelled (`ESC` or `Ctrl+C`).

---
## 3. Keyboard Controls

| Key | Action |
| :-- | :-- |
| **Up/Down** | Navigate the list |
| **Enter** | Confirm selection |
| **Space** | Toggle checkbox (only in `checkbox`) |
| **Esc** | Cancel the menu (returns `None` or `[]`) |
| **Ctrl+C** | Interrupt/Cancel |

---
## 4. Input Listener Details
Termella uses a custom input listener located in `termella.input`.

- **Windows**: Uses `msvcrt` for non-blocking input.
- **Unix (Linux/Mac)**: Uses `termios` and `tty` to set raw mode, and `select` to handle escape sequences non-blockingly.