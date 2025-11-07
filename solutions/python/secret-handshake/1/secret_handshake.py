def commands(binary_str):
    actions = []

    # جدول حرکات بر اساس بیت‌ها از راست به چپ
    moves = ["wink", "double blink", "close your eyes", "jump"]

    # از راست به چپ بررسی می‌کنیم (بیت 1 تا 4)
    for i in range(4):
        # اگه بیت iام از راست 1 بود، حرکت مربوطه رو اضافه کن
        if binary_str[-(i+1)] == "1":
            actions.append(moves[i])

    # بیت پنجم (از راست پنجمین کاراکتر) بررسی می‌کنه آیا باید معکوس کنیم یا نه
    if len(binary_str) >= 5 and binary_str[-5] == "1":
        actions.reverse()

    return actions
