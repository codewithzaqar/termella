from ..core import visible_len

def columns(*widgets, padding=2, align="top"):
    """
    Prints strings/widgets side-by-side.
    Args:
        *widgets: Strings (output from panel(render=True), etc)
        padding (int): Spaces between columns.
    """
    cols_data = []
    for w in widgets:
        if not w: cols_data.append([])
        else: cols_data.append(str(w).split('\n'))
    
    if not cols_data: return
    max_height = max(len(c) for c in cols_data)
    col_widths = []
    for col in cols_data:
        w = max(visible_len(line) for line in col) if col else 0
        col_widths.append(w)

    pad_str = " " * padding

    aligned_cols = []
    for col in cols_data:
        diff = max_height - len(col)
        if diff > 0:
            if align == "bottom":
                new_col = ([""] * diff) + col
            elif align == "center":
                top_pad = diff // 2
                bot_pad = diff - top_pad
                new_col = ([""] * top_pad) + col + ([""] * bot_pad)
            else:
                new_col = col + ([""] * diff)
            aligned_cols.append(new_col)
        else:
            aligned_cols.append(col)

    for i in range(max_height):
        line_parts = []
        for j, col in enumerate(cols_data):
            content = col[i] if i < len(col) else ""
            v_len = visible_len(content)
            fill = " " * (col_widths[j] - v_len)
            line_parts.append(content + fill)

        print(pad_str.join(line_parts))

def grid(widgets, cols=3, padding=2):
    """
    Arranges a list of widgets into a grid structure.
    """
    for i in range(0, len(widgets), cols):
        chunk = widgets[i : i + cols]
        columns(*chunk, padding=padding)
        print()