def replace_all(text, a, b):
    assert type(text) == str, "`text` must be a string!"
    assert type(a) == str, "`a` must be a string!"
    assert type(b) == str, "`b` must be a string!"
    return b.join(text.split(a))

