from .helpers.replace_all import replace_all
from .kebabify import kebabify


def snakeify(x):
    assert type(x) is str, (
        "The value passed into the `snakeify` function must be a string!"
    )

    out = kebabify(x)
    return replace_all(out, "-", "_")
