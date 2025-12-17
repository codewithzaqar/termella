import sys
import time
import threading
from ..ansi import CURSOR_HIDE, CURSOR_SHOW

class Spinner:
    """
    A context manager for a loading spinner.
    Usage:
        with Spinner("Loading..."):
            time.sleep(2)
    """
    def __init__(self, message="Loading...", delay=0.1):
        self.message = message
        self.delay = delay
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.running = False
        self.thread = None

    def _spin(self):
        idx = 0
        while self.running:
            frame = self.frames[idx % len(self.frames)]
            sys.stdout.write(f"\r{CURSOR_HIDE}{frame} {self.message}")
            sys.stdout.flush()
            idx += 1
            time.sleep(self.delay)

    def __enter__(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.running = False
        self.thread.join()
        sys.stdout.write(f"\r{CURSOR_SHOW}✔ {self.message} Done.\n")
        sys.stdout.flush()