import re


def unindent(text):
    assert type(text) == str, "`text` must be a string!"

    def find_index(fn, x):
        for i in range(0, len(x)):
            if fn(x[i]):
                return i

        return None

    whitespace = re.compile("\s")
    lines = text.split("\n")
    lines = list(filter(lambda line: len(line.strip()) > 0, lines))

    indentations = list(
        map(
            lambda line: find_index(
                lambda char: not whitespace.match(char), line.split("")
            ),
            lines,
        )
    )

    min_indentation = min(indentations)
    return ("\n").join(list(map(lambda line: line[min_indentation:], lines)))
