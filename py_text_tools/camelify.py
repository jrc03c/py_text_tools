import re


def camelify(text):
    assert type(text) == str, "`text` must be a string!"

    alphanumerics = re.compile("[A-Za-z0-9]")
    text = text.strip()
    out = ""
    should_capitalize_next_character = False

    for char in list(text):
        if alphanumerics.match(char):
            if len(out) == 0:
                out += char.lower()

            elif should_capitalize_next_character:
                out += char.upper()

            else:
                out += char

            should_capitalize_next_character = False

        elif "'" not in char and "’" not in char and "❜" not in char:
            should_capitalize_next_character = True

    return out
