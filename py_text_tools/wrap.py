import re

whitespace = re.compile("\\s")


def get_line_start_whitespace(line):
    for i in range(0, len(line)):
        if not whitespace.match(line[i]):
            return line[:i]

    return ""


def wrap(x, max_line_length=80, wrapped_line_prefix=""):
    assert type(x) is str, (
        "The first value passed into the `wrap` function must be a string!"
    )

    assert type(max_line_length) is int and max_line_length > 0, (
        "The `max_line_length` value passed into the `wrap` function must be a positive integer!"
    )

    assert type(wrapped_line_prefix) is str, (
        "The `wrapped_line_prefix` value passed into the `wrap` function must be a string!"
    )

    out = []
    lines = x.split("\n")

    for line in lines:
        if len(line.strip()) == 0:
            out.append("")
            continue

        indentation = get_line_start_whitespace(line)
        words = line.replace(indentation, "").split(" ")
        temp = (wrapped_line_prefix if len(out) > 0 else "") + indentation

        for word in words:
            new_temp = temp + (" " if len(temp.strip()) > 0 else "") + word

            if len(new_temp) > max_line_length:
                out.append(temp)

                temp = (
                    (wrapped_line_prefix if len(out) > 0 else "") + indentation + word
                )

            else:
                temp = new_temp

        if len(temp) > 0:
            out.append(temp)

    return ("\n").join(out)
