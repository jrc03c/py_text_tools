def indent(text, chars=""):
    return ("\n").join(
        list(
            map(
                lambda line: chars + line if len(line.strip()) > 0 else line,
                text.split("\n"),
            )
        )
    )

