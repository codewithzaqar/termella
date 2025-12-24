import re
from .core import Text
from .ansi import COLORS, BG_COLORS, STYLES

# Use raw string for regex pattern
TAG_RE = re.compile(r'(?<!\\)\[(.*?)(?<!\\)\]')

THEME = {
    "error": "red bold",
    "warn": "yellow",
    "info": "cyan",
    "success": "green bold"
}

def add_alias(name, style_str):
    """
    Registers a custom tag alias.
    Usage: add_alias("alert", "white bg_red bold")
    """
    THEME[name] = style_str

def unescape(s):
    r"""
    Replaces \[ with [ and \] with ].
    """
    # Use raw strings for the replacement arguments
    return s.replace(r'\[', '[').replace(r'\]', ']')

def parse(text):
    """
    Parses nested markup tags with escape support.
    """
    if "[" not in text:
        return Text(unescape(text))

    parts = TAG_RE.split(text)
    
    final_output = Text("")
    style_stack = [] 

    for i, part in enumerate(parts):
        if i % 2 == 0:
            if not part: continue
            clean_text = unescape(part)
            chunk = Text(clean_text)
            
            for style_key in style_stack:
                style_def = THEME.get(style_key, style_key)
                tokens = style_def.split()
                c_val = None
                bg_val = None
                s_vals = []
                
                for token in tokens:
                    if token in COLORS: c_val = token
                    elif token in BG_COLORS: bg_val = token
                    elif token in STYLES: s_vals.append(token)
                
                chunk.style(color=c_val, bg=bg_val, styles=s_vals)

            final_output += chunk
            
        else:
            tag = part.strip()
            tag = unescape(tag)
            
            if tag == "/":
                if style_stack: style_stack.pop()
            else:
                style_stack.append(tag)
                
    return final_output

def print_tag(text, end="\n"):
    t = parse(text)
    print(t, end=end)