from .helpers import strip


def kebabify(x):
    assert type(x) is str, (
        "The value passed into the `kebabify` function must be a string!"
    )

    words = strip(x).split(" ")

    if len(words) == 0:
        return ""

    if len(words) == 1:
        return words[0]

    return ("-").join(words)
