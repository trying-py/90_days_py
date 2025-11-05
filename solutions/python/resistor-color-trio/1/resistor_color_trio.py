def label(colors):
    combined = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    first_two = colors[:2]
    com = int("".join([str(combined[color])
                       for color in first_two if color in combined]))
    multi = 10 ** combined[colors[2]]
    total = multi * com

    if total > 1000000000:
        return f"{total // 1000000000} gigaohms"
    if total > 1000000:
        return f"{total // 1000000} megaohms"
    elif 1000 <= total <= 1000000:
        return f"{total // 1000} kiloohms"
    elif total < 1000:
        return f"{total} ohms"
    else:
        raise ValueError("not correct")


