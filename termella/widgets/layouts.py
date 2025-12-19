from ..core import visible_len

def columns(*widgets, padding=2):
    """
    Prints strings/widgets side-by-side.
    Args:
        *widgets: Strings (output from panel(render=True), etc)
        padding (int): Spaces between columns.
    """
    cols_data = []
    for w in widgets:
        if not w:
            cols_data.append([])
        else:
            cols_data.append(str(w).split('\n'))
    
    if not cols_data: return
    max_height = max(len(c) for c in cols_data)
    col_widths = []
    for col in cols_data:
        if not col:
            w = 0
        else:
            w = max(visible_len(line) for line in col)
        col_widths.append(w)

    pad_str = " " * padding

    for i in range(max_height):
        line_parts = []
        for j, col in enumerate(cols_data):
            content = col[i] if i < len(col) else ""
            v_len = visible_len(content)
            fill_amount = col_widths[j] - v_len
            line_parts.append(content + (" " * fill_amount))
        print(pad_str.join(line_parts)) 