def replace_all(text, a, b):
    assert type(text) is str, (
        "The first value passed into the `replace_all` function must be a string!"
    )

    assert type(a) is str, (
        "The second value passed into the `replace_all` function must be a string!"
    )

    assert type(b) is str, (
        "The third value passed into the `replace_all` function must be a string!"
    )

    return b.join(text.split(a))
