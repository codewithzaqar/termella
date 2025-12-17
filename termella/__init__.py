"""
Termella - Rich text and beautiful formatting in the terminal.
Version: 0.0.3c
"""

from .printer import cprint, cinput
from .core import Text
from .widgets import panel, progress_bar, table, Spinner

__version__ = "0.0.3c"
__all__ = ["cprint", "cinput", "Text", "panel", "progress_bar", "table", "Spinner"]