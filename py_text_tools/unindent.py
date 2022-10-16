from .utils import find_index
import re


def unindent(text):
    assert type(text) == str, "`text` must be a string!"

    whitespace = re.compile("\s")
    lines = text.split("\n")

    indentations = list(
        map(
            lambda line: find_index(
                lambda char: not whitespace.match(char), list(line)
            ),
            list(filter(lambda line: len(line.strip()) > 0, lines)),
        )
    )

    min_indentation = min(indentations)
    return ("\n").join(list(map(lambda line: line[min_indentation:], lines)))
