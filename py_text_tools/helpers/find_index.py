def find_index(fn, x):
    for i in range(0, len(x)):
        if fn(x[i]):
            return i

    return None
