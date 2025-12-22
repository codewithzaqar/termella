# Live Display Engine (v0.0.6)

The `Live` class allows you to create flicker-free, dynamic terminal interfaces. It works by moving the cursor up and overwriting previous output rather then clearing the entine screen.

## Basic Usage

Wrap your loop in a `with Live()` block. Call `.update()` to change the display.

```python
from termella import Live
import time

with Live() as live:
    live.update("Loading...")
    time.sleep(1)
    live.update("Done!")
```
## Configuration
```python
Live(refresh=None, auto_refresh=None)
```
* **refresh** *(float)*: Number of seconds to sleep automatically after every `.update()`. If `None`, you must handle timing yourself.
* **auto_refresh** *(bool)*: If `True`, `update()` sleeps for `refresh` seconds. Defaults to `True` if `refresh` is provided.

## Logging
To print permanent text (like logs) while the Live display is running, use `.log()`. Do NOT use `print()`, as it will mess up the cursor position.
```python
live.log("This text stays.")
live.update("This text gets overwritten.")
```
## Rendering Layouts
`Live.update()` accepts:
1. **Strings** Direct text.
2. **Lists/Tuples**: Automatically stacks them vertically using `grid(cols=1)`.
3. **Widgets**: Results from `panel(..., render=True)`, `columns(..., render=True)`, etc.

## Best Practices
1. **Always use** `render=True` inside `live.update()`. Do not `print()` widgets directly.
2. **Handle Exit**: The `with` block ensures the cursor is shown again. If you don't use `with`, manually call `live.start()` and `live.stop()`.