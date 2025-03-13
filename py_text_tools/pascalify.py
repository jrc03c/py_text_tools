from .camelify import camelify


def pascalify(x):
    assert type(x) is str, (
        "The value passed into the `pascalify` function must be a string!"
    )

    out = camelify(x)
    return out[0].upper() + out[1:]
