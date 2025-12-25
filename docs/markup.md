# Markup Guide (v0.0.7)

Termella v0.0.7 introduces a tag-based markup language inspired by BBCode.

## Basic Syntax
Wrap text in square brackets to apply styles. Use `[/]` to close the most recent tag.

```text
[style]Text[/]
```
Multiple styles can be space-separated inside a tag:
```text
[red bold underline]Urgent Message[/]
```

## Nesting
Tags can be nested. Inner tags add to or override outer tags.
```text
[blue]Outer [white]Inner[/] Outer[/]
```
- "Outer" is Blue
- "Inner" is White (Blue is overridden/mixed depending on attribute).

## Macros
Macros are special tags that take arguments.

### 1. RGB Colors
Use TrueColor (24-bit) if your terminal supports it.
- **Foreground**: `[rgb(r,g,b)]`
- **Background**: `bg_rgb(r,g,b)]`

```text
[rgb(255,100,50)]Coral Color[/]
[bg_rgb(0,0,100)]Deep Blue BG[/]
```
### 2. Hyperlinks
Create clickable text (supported in iTerm2, VSCode, Windows Terminal, etc).
```text
[link=https://example.com]Click Here[/]
```
## Theming (Aliases)
You can register custom tags to semanticize your output.
```python
from termella import add_alias

add_alias("h1", "magenta bold underline")
add_alias("warn", "black bg_yellow")
```
Now you can use `[h1]` and `[warn]` in your strings:
```python
print_tag("[h1]Chapter 1[/]")
```

## Escaping
If you need to print a literal bracket `[` or `]`, escape it with a backslash.
**Note**: Use Python raw strings `r"..."` to avoid warnings.
```python
print_tag(r"This is a literal \[tag\]")
# Output: This is a literal [tag]
```

## Parsing
If you need the `Text` object (e.g., to pass into a Widget), use `parse()`.
```python
from termella import parse, panel

text_obj = parse("[bold]Title[/]")
panel(text_obj)
```