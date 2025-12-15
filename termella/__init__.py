"""
Termella - Rich text and beautiful formatting in the terminal.
Version: 0.0.1a
"""

from .printer import cprint
from .core import Text
from .widgets import panel

__version__ = "0.0.1a"
__all__ = ["cprint", "Text", "panel"]