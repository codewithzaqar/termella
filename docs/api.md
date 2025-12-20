# API Reference

## 1. High-Level Functions

### `cprint(text, color=None, bg=None, styles=None, end="\n")`
Prints styled text to the console directly.

*   **text** *(str)*: The content to print.
*   **color** *(str)*: Foreground color name (e.g., `'red'`).
*   **bg** *(str)*: Background color name (e.g., `'bg_white'`).
*   **styles** *(str or list)*: A single string or a list of styles (e.g., `'hold'` or `['bold', 'underline']`).
*   **end** *(str)*: String appended after the last value, default is a newline.

### `cinput(prompt_text, color="cyan", styles="bold")`
**[New in v0.0.2]**
Displays a styled prompt and waits for user input.

- **Parameters:**
  - `prompt_text` (Any): The text to display as the prompt.
  - `color` (str): Color of the prompt text. Default is `"cyan"`.
  - `styles` (str | list): Styles for the prompt. Default is `"bold"`.
- **Returns:**
  - `str`: The user's input.
  - `None`: If the user presses `Ctrl+C` (KeyboardInput).
- **Behaior:**
  - The color resets automatically before the user begins typing, ensuring their input is standard terminal color.

---

## 1.1 Interactive Widgets (`termella.widgets`)

### `columns(*widgets, padding=2, align="top", render=False)`
**[New in v0.0.5]**
Renders multiple string blocks side-by-side. Robustly handles ANSI color codes to ensure correct alignment.
*   **align**: `'top'`, `'center'`, `'bottom'`.

### `grid(widgets, cols=3, padding=2, render=False)`
**[New in v0.0.5]**
Arranges a list of widget strings into a grid layout.

### `tree(data, root_name=".", render=False)`
**[New in v0.0.5]**
Recursively renders a dictionary as a tree structure.

### `select(options, prompt=..., color=..., marker=..., limit=...)`
**[New in v0.0.4]**
Renders an interactive menu for single choice selection.
*    Supports scrolling via `limit`.
*    Supports cancellation via `ESC`.

### `checkbox(options, prompt=..., color=..., marker=..., limit=...)`
**[New in v0.0.4]**
Renders an interactive menu for multiple choice selection.
*    Toggle with Spacebar.
*    Returns a list of strings.

## 2. Core Classes

### `class Text(content)`
Represents a styled string. Instances of this class are immutable regarding content but mutable regarding style codes.

#### `__init__(self, content)`
*   **content** *(str)*: The raw string text.

#### `style(self, color=None, bg=None, styles=None)`
Applies ANSI codes to the text object. Returns `self` to allow chaining.

*   **color**, **bg**, **styles**: Same arguments as `cprint`.

#### `__add__(self, other)`
Allows concatenation of two `Text` objects (or a `Text` object and a string).
*   **Example**: `Text("A") + Text("B")`

#### `__str__(self)`
Renders the final string with ANSI escape embedded.

---

## 3. Widgets

### `panel(text, color="white", title=None, render=False)`
Prints a multi-line string enclosed in an ASCII box.

**[Updated v0.0.5]**
Added `render` parameter. If `True`, returns the string.

- **Parameters**
  - `text` (str): The content to display inside the box. Handles `\n` automatically.
  - `color` (str): The color of the border/box lines.
  - `title` (str): Optional text to display embedded in the top border.

### `progress_bar(iternation, total, length=30, color="green", fill="█", empty="-")`
**[New in v0.0.2]**
Prints a dynamic progress bar.

- **Parameters:**
  - `iteration` (int): Current step (e.g., 5).
  - `total` (int): Total steps (e.g., 100).
  - `length` (int): Visual length of the bar in characters.
  - `color` (str): Color of the filled portion.
  - `fill` (str): Character used for the completed section.
  - `empty` (str): Character used for the remaining section.
- **Behavior:**
  - Hides the cursor while updating to prevent flickering.
  - Automatically handles `ZeroDivisionError` if `total` is 0.

### `table(data, headers=..., align="left", render=False)`
**[Updated v0.0.5]**
Added `render` parameter.

### `select(...)` / `checkbox(...)`
Iteractive menus (see [Interaction Guide](interaction.md)).