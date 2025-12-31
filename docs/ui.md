# Component System (v0.0.9)

Termella v0.0.9 introduces `termella.ui`, a set of Object-Oriented widgets.

## Base Class: `Widget`
All components inherit from `Widget`.
*   **render()**: Returns a list of strings representing the widget.
*   **on_focus() / on_blur()**: Called by the Focus Manager.
*   **is_focused**: Boolean state.

## Components

### `Label(text, style=None)`
Static text display. Supports markup.
```python
lbl = Label("Hello [red]World[/]")
```
### `Button(label, on_click=func)`
Clickable button. Focusable.

* Triggers on_click when Enter/Space pressed or clicked with mouse.

### `TextInput(value="", placeholder="", password=False)`
Single line input field. Focusable.

* value: Current text.
* password: If True, displays *.

### `CheckBox(label, checked=False, on_change=func)`
Toggle switch. Focusable.

## Containers
### `VBox(*children, padding=0)`
Stacks widgets vertically.

### `HBox(*children, padding=0)`
Places widgets horizontally.

### `Screen(*children)`
Root container that auto-sizes to the terminal dimensions.

## Focus Management
In your App:

1. Create widgets.
2. Call self.add_focusable(widget) to register them.
3. The user can navigate with Tab, Shift+Tab, Up/Down.