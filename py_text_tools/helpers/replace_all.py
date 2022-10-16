def replace_all(text, a, b):
    assert type(text) == str, "The `text` argument must be a string!"
    assert type(a) == str, "The `a` argument must be a string!"
    assert type(b) == str, "The `b` argument must be a string!"
    return b.join(text.split(a))

