import re

alphanumeric = re.compile("[A-Za-z0-9]")


def camelify(x):
    assert type(x) is str, (
        "The value passed into the `camelify` function must be a string!"
    )

    x = x.trim()
    out = ""
    should_capitalize_next_character = False

    for i in range(0, len(x)):
        char = x[i]

        if alphanumeric.match(char):
            if len(out) == 0:
                out += char.lower()

            elif should_capitalize_next_character:
                out += char.upper()

            else:
                out += char

            should_capitalize_next_character = False

        elif "'" not in char and "’" not in char and "❜" not in char:
            should_capitalize_next_character = True

        should_capitalize_next_character = False

    return out
