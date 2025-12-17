from ..core import Text

def table(data, headers=None, border_color="white"):
    """
    Renders a list of lists as a table.

    Args:
        data (list): list of rows (e.g. [['A', 'B'], ['C', 'D']])
        headers (list): List of column titles.
    """
    if not data: return

    # Calculate column widths
    cols = len(data[0])
    widths = [0] * cols

    all_rows = ([headers] if headers else []) + data

    for row in all_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # Formatting helpers
    def print_sep(left, mid, right, line):
        segments = [line * (w + 2) for w in widths]
        full_line = left + mid.join(segments) + right
        print(Text(full_line).style(border_color))

    # Top Border
    print_sep("┌", "┬", "┐", "─")

    # Headers
    if headers:
        row_str = "│"
        for i, cell in enumerate(headers):
            row_str += f" {str(cell).ljust(widths[i])} │"
        print(Text(row_str).style(border_color, styles="bold"))
        print_sep("├", "┼", "┤", "─")

    # Data
    for row in data:
        row_str = "│"
        for i, cell in enumerate(row):
            row_str += f" {str(cell).ljust(widths[i])} │"
        print(Text(row_str).style(border_color))

    # Bottom Border
    print_sep("└", "┴", "┘", "─")