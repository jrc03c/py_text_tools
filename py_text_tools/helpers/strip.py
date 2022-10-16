from .replace_all import replace_all

alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
double_space = "  "
single_space = " "


def strip(text):
    assert type(text) == str, "`text` must be a string!"

    out = ""

    for char in text.split(""):
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
