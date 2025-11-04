def value(colors):
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
    combined_list = [str(combined[color])
                     for color in first_two if color in combined]
    return int("".join(combined_list))