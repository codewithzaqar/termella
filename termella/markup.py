import re
from .core import Text

TAG_RE = re.compile(r'\[(.*?)\]')

def parse(text):
    """
    Parses a string with inline markup tags a styled Text object.

    Example:
        parse("Hello [red]World[/]!")

    Limitations (dev0):
        - No nested tags yet (e.g. [red][bold]Hi[/][/])
    """
    if "[" not in text:
        return Text(text)
    
    parts = TAG_RE.split(text)

    final_output = Text("")
    style_stack = []

    for i, part in enumerate(parts):
        if i % 2 == 0:
            if not part: continue
            chunk = Text(part)
            for style_def in style_stack:
                tokens = style_def.split()
                chunk.style(color=tokens[0], styles=tokens[1:])
                c_val = None
                bg_val = None
                s_vals = []

                from .ansi import COLORS, BG_COLORS, STYLES
                for token in tokens:
                    if token in COLORS: c_val = token
                    elif token in BG_COLORS: bg_val = token
                    elif token in STYLES: s_vals.append(token)

                chunk.style(color=c_val, bg=bg_val, styles=s_vals)

            final_output += chunk

        else:
            tag = part.strip()
            if tag == "/":
                if style_stack:
                    style_stack.pop()
            else:
                style_stack.append(tag)

    return final_output

def print_tag(text, end="\n"):
    """
    Helper to parse and print immediately.
    """
    t = parse(text)
    print(t, end=end)