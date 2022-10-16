from .utils import find_index
import os
import re


def wrap(raw, max_line_length=None):
    assert (
        type(raw) == str
    ), "The first argument to the `wrap` function must be a string!"

    if max_line_length is None:
        max_line_length = min(80, os.get_terminal_size().columns)

    assert (
        type(max_line_length) == int
    ), "The second argument to the `wrap` function must be an integer or None!"

    out = []
    lines = raw.split("\n")
    whitespace = re.compile("\s")

    for line in lines:
        if len(line.strip()) == 0:
            out.append("")

        first_important_character_index = find_index(
            lambda char: not whitespace.match(char), list(line)
        )

        indentation = line[:first_important_character_index]
        words = line.replace(indentation, "").split(" ")
        temp = indentation

        for word in words:
            new_line = temp + (" " if len(temp.strip()) > 0 else "") + word

            if len(new_line) > max_line_length:
                out.append(temp)
                temp = indentation + word

            else:
                temp = new_line

        if len(temp) > 0:
            out.append(temp)

    return ("\n").join(out)
