"""
termella.ansi
Definitions for ANSI escape codes.
"""

RESET = "\033[0m"

# Foreground Colors
COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "bright_red": "91",
    "bright_green": "92",
    "bright_blue": "94",
}

# Background Colors
BG_COLORS = {
    "bg_black": "40",
    "bg_red": "41",
    "bg_green": "42",
    "bg_blue": "44",
    "bg_white": "47",
}

# Styles
STYLES = {
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "reverse": "7",
}