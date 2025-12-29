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

## 4. Live Display (`termella.live`)

### `class Live(refresh=None, auto_refresh=None)`
Contect manager for dynamic output.

#### `update(renderable)`
Updates the display.
*   **renderable**: String, Widget (rendered string), or List of widgets.
*   Moves cursor up, clears old content, prints new content.

#### `log(*objects, sep=" ", end="\n")`
Prints a message above the current live display.
*   Temporarily clears live view, prints log, resets internal height tracker.

#### `start()` / `stop()`
Manually control the live display lifecycle (hide/show cursor).

## 5. Markup (`termella.markup`)

### `print_tag(text, end="\n")`
**[New in v0.0.7]**
Parses a markup string and prints it immediately.
*   **text**: String containing tags like `[red]...[/]`.

### `parse(text)`
**[New in v0.0.7]**
Parses a markup string into a `Text` object.
*   **Returns**: `termella.core.Text`
*   **Robustness**: Handles unclosed tags automatically.

### `add_alias(name, style_str)`
**[New in v0.0.7]**
Registers a global alias for the markup parser.
*   **name**: The tag name (e.g., "alert").
*   **style_str**: The styles to apply (e.g., "red bold").

## 6. 🖥️ Application (`termella.app`)

### `class App(refresh_rate=0.1, mouse=False)`
Base class for TUI apps.

#### `run()`
Starts the application loop. Blocks until `exit()` is called.

#### `exit()`
Signals the loop to stop.

#### `render()` -> `str | Widget | list`
**Abstract**. Must be overridden to define the UI.

#### `on_key(key: str)`
Hook for keyboard events.

#### `on_click(x: int, y: int, btn: str)`
Hook for mouse events.

#### `on_resize(width: int, height: int)`
Hook for resize events. Also updates `self.width` and `self.height`.