from .core import Text

def cprint(text, color=None, bg=None, styles=None, end="\n"):
    """
    Color Print: Prints text with specified formatting.

    Args:
        text (str): The text to print.
        color (str): Foreground color name (e.g., 'red', 'blue').
        bg (str): Background color name (e.g., 'bg_white').
        styles (list/str): Styles like 'bold', 'underline'.
    """
    styled_text = Text(text).style(color, bg, styles)
    print(styled_text, end=end)