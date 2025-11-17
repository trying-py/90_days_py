def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    diff = 0
    for i, ch in enumerate(strand_a):
        if ch != strand_b[i]:
            diff += 1

    return diff
    