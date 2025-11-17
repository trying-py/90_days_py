def flatten(iterable):
    lst = []

    for i in iterable:
        if i is None:
            continue
        if isinstance(i, int):
            lst.append(i)
        if isinstance(i, list):
            lst.extend(flatten(i))

    return lst