import sys
import time
from .ansi import CURSOR_HIDE, CURSOR_SHOW, CURSOR_UP, CURSOR_DOWN, CLEAR_LINE, CARRIAGE_RETURN

class Live:
    """
    Context manager for live-updating terminal output.
    Prevents screen flickering by only overwriting the necessary lines.

    Usage:
        with Live() as live:
            while True:
                live.update(render_function())
                time.sleep(1)
    """
    def __init__(self, refresh_rate=None):
        self.last_height = 0
        self.refresh_rate = refresh_rate
        self.is_running = False

    def start(self):
        self.is_running = True
        sys.stdout.write(CURSOR_HIDE)
        sys.stdout.flush()

    def stop(self):
        self.is_running = False
        sys.stdout.write(CURSOR_SHOW)
        print()

    def update(self, renderable):
        """
        Replaces the previous output with the new renderable.
        Args:
            renderable (str): The multi-line string to display.
        """
        text = str(renderable)
        lines = text.split('\n')
        new_height = len(lines)

        if self.last_height > 0:
            sys.stdout.write(CURSOR_UP * self.last_height)
            for _ in range(self.last_height):
                sys.stdout.write(CLEAR_LINE)
                sys.stdout.write(CURSOR_DOWN)

            sys.stdout.write(CURSOR_UP * self.last_height)
            sys.stdout.write(CARRIAGE_RETURN)

        sys.stdout.write(text)

        if not text.endswith('\n'):
            sys.stdout.write('\n')

        sys.stdout.flush()
        self.last_height = new_height + (0 if text.endswith('\n') else 1)
        if self.refresh_rate:
            time.sleep(self.refresh_rate)

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_valm, exc_tb):
        self.stop()
        return False