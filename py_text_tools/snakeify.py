from .utils import strip


def snakeify(text):
    assert type(text) == str, "`text` must be a string!"

    words = strip(text).split(" ")

    if len(words) == 0:
        return ""

    if len(words) == 1:
        return words[0]

    return ("_").join(words)

