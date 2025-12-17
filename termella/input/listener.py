import sys
import os

class InputListener:
    """
    Reads a single keypress from STDIN without blocking line buffering.
    Returns normalized key names: 'UP', 'DOWN', 'ENTER', or the char.
    """

    def read_key(self):
        """Waits for a single keypress and returns it."""
        if os.name == 'nt':
            return self._read_windows()
        else:
            return self._read_unix()
        
    def _read_windows(self):
        import msvcrt

        key = msvcrt.getch()
        if key == b'\r': return 'ENTER'
        if key == b'\xe0': # Special keys (arrows)
            key = msvcrt.getch()
            if key == b'H': return 'UP'
            if key == b'P': return 'DOWN'
            if key == b'K': return 'LEFT'
            if key == b'M': return 'RIGHT'
        return key.decode('utf-8', 'ignore')
    
    def _read_unix(self):
        import tty
        import termios
        
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)

            # Handle Escape Sequences (Arrows)
            if ch == '\x1b':
                seq = sys.stdin.read(2)
                if seq == '[A': return 'UP'
                if seq == '[B': return 'DOWN'
                if seq == '[C': return 'RIGHT'
                if seq == '[D': return 'LEFT'
                return 'ESC'
            
            if ch == '\r' or ch == '\n': return 'ENTER'
            if ch == '\x03': raise KeyboardInterrupt # Handle Ctrl+C
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)