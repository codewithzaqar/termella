# API Reference

## 1. High-Level Functions

### `cprint(text, color=None, bg=None, styles=None, end="\n")`
Prints styled text to the console directly.

*   **text** *(str)*: The content to print.
*   **color** *(str)*: Foreground color name (e.g., `'red'`).
*   **bg** *(str)*: Background color name (e.g., `'bg_white'`).
*   **styles** *(str or list)*: A single string or a list of styles (e.g., `'hold'` or `['bold', 'underline']`).
*   **end** *(str)*: String appended after the last value, default is a newline.

---

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

### `panel(text, color="white", title=None)`
Prints a multi-line string enclosed in an ASCII box.

*   **text** *(str)*: The content to display inside the box. Handles `\n` automatically.
*   **color** *(str)*: The color of the border/box lines.
*   **title** *(str)*: Optional text to display embedded in the top border.