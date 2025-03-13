from .punctuation import punctuation
from .replace_all import replace_all

double_space = "  "
single_space = " "


def strip(text):
    assert type(text) is str, (
        "The value passed into the `strip` function must be a string!"
    )

    out = ""

    for i in range(0, len(text)):
        char = text[i].lower()

        if char in punctuation:
            out += single_space

        else:
            out += char

    while double_space in out:
        out = replace_all(out, double_space, single_space)

    return out.strip()
