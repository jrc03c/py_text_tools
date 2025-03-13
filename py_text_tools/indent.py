def indent(x, chars=""):
    return ("\n").join(
        [chars + line if len(line.strip()) > 0 else line for line in x.split("\n")]
    )
