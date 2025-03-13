def string_to_array(x):
    assert type(x) is str, (
        "The value passed into the `string_to_array` function must be a string!"
    )

    out = []

    for i in range(0, len(x)):
        out.append(x[i])

    return out
