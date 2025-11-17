def flatten(iterable):
    def gen(it):
        for i in it:
            if i is None:
                continue
            if isinstance(i, list):
                yield from gen(i)
            else:
                yield i

    return list(gen(iterable)) 
