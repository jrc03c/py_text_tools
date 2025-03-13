import re

from .helpers.find_index import find_index
from .helpers.string_to_array import string_to_array

whitespace = re.compile("\\s")


def unindent(x):
    assert type(x) is str, (
        "The value passed into the `unindent` function must be a string!"
    )

    lines = x.split("\n")
    non_empty_lines = [line for line in lines if len(line.strip()) > 0]

    indentations = [
        find_index(lambda char: not whitespace.match(char), string_to_array(line))
        for line in non_empty_lines
    ]

    min_indentation = min(indentations)
    return ("\n").join([line[min_indentation:] for line in lines])
