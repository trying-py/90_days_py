def resistor_label(colors):
    digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tol = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }

    n = len(colors)
    if n not in (1, 4, 5):
        raise ValueError("bands must be 1, 4, or 5")

    # 1-band: فقط black
    if n == 1:
        if colors[0] != "black":
            raise ValueError("single-band resistor must be ['black']")
        return "0 ohms"

    # رنگ آخر باید تلورانس معتبر باشد
    tol_color = colors[-1]
    if tol_color not in tol:
        raise ValueError("invalid tolerance band color")
    tol_str = tol[tol_color]

    # تعداد ارقام اصلی و اندیس ضریب بر اساس ۴ یا ۵ باند
    digit_count = 3 if n == 5 else 2
    mult_idx = 3 if n == 5 else 2

    # مقدار اصلی (دو یا سه رقم)
    digits = [digit[colors[i]] for i in range(digit_count)]
    main = int("".join(map(str, digits)))

    # ضریب (توان ۱۰)
    value = main * (10 ** digit[colors[mult_idx]])

    # نمایش تمیز اعداد (حذف صفرهای اضافی اعشار)
    def tidy(x):
        return f"{x:.10f}".rstrip('0').rstrip('.')

    # انتخاب واحد
    if value >= 1_000_000_000:
        return f"{tidy(value / 1_000_000_000)} gigaohms {tol_str}"
    elif value >= 1_000_000:
        return f"{tidy(value / 1_000_000)} megaohms {tol_str}"
    elif value >= 1_000:
        return f"{tidy(value / 1_000)} kiloohms {tol_str}"
    else:
        return f"{value} ohms {tol_str}"
