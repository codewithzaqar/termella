import sys
from ..core import Text
from ..input.listener import InputListener
from ..ansi import CURSOR_HIDE, CURSOR_SHOW, CURSOR_UP, CLEAN_LINE

def select(options, prompt="Select an option:", color="cyan", marker=">"):
    """
    Interactive selection menu using arrow keys.

    Args:
        options (list): List of string options.
        prompt (str): The question to ask.

    Returns:
        str: The selected option string.
    """
    listener = InputListener()
    idx = 0
    n_options = len(options)

    sys.stdout.write(CURSOR_HIDE)
    print(Text(prompt).style(styles="bold"))

    try:
        while True:
            # Render Options
            for i, option in enumerate(options):
                # Clear line to ensure clean redraw
                sys.stdout.write(CLEAN_LINE)

                if i == idx:
                    # Highlight selected
                    prefix = f"{marker} "
                    styled = Text(f"{prefix}{option}").style(color=color, styles="bold")
                    print(styled)
                else:
                    # Dim unselected
                    prefix = "  "
                    styled = Text(f"{prefix}{option}").style(styles="dim")
                    print(styled)
                
            # Wait for Input
            key = listener.read_key()

            if key == 'UP':
                idx = (idx - 1) % n_options
            elif key == 'DOWN':
                idx = (idx + 1) % n_options
            elif key == 'ENTER':
                break

            # Move Cursor Back Up to redraw
            # We move up 'n_options' lines
            sys.stdout.write(f"\r{CURSOR_UP * n_options}")

    except KeyboardInterrupt:
        sys.stdout.write(CURSOR_SHOW)
        print()
        return None
    finally:
        sys.stdout.write(CURSOR_SHOW)

    return options[idx]