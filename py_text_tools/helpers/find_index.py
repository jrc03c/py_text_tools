def find_index(fn, x):
    for i, v in enumerate(x):
        if fn(v):
            return i

    return -1
