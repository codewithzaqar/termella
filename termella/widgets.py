from .core import Text

def panel(text, color="white", title=None):
    """
    Greates a simple ASCII box around text.
    """
    lines = text.split("\n")
    width = max(len(line) for line in lines) + 2

    # Box characters
    tl, tr, bl, br = "┌", "┐", "└", "┘"
    h, v = "─", "│"

    # Build Top
    rendered_title = f" {title} " if title else ""
    top_bar = h * (width - len(rendered_title))
    print(Text(f"{tl}{rendered_title}{top_bar}{tr}").style(color))

    # Build Content
    for line in lines:
        padded = line.ljust(width)
        print(Text(f"{v}{padded}{v}").style(color))

    # Build Bottom
    print(Text(f"{bl}{h * width}{br}").style(color))