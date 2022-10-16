alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
double_space = "  "
single_space = " "


def strip(text):
    assert type(text) == str, "`text` must be a string!"

    out = ""

    for char in list(text):
        char = char.lower()

        if char in alpha:
            out += char

        elif char == "'" or char == "’" or char == "❜":
            out += ""

        else:
            out += single_space

    while double_space in out:
        out = replace_all(out, double_space, single_space)

    return out.strip()


def find_index(fn, x):
    for i in range(0, len(x)):
        if fn(x[i]):
            return i

    return None


def replace_all(text, a, b):
    assert type(text) == str, "`text` must be a string!"
    assert type(a) == str, "`a` must be a string!"
    assert type(b) == str, "`b` must be a string!"
    return b.join(text.split(a))
