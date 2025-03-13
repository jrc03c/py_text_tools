from .indent import indent


def test():
    a = "Hello, world!"
    b_true = "    Hello, world!"
    b_pred = indent(a, "    ")
    assert b_pred == b_true

    c = "Hello, world!"
    d_true = "\t\t\t\tHello, world!"
    d_pred = indent(c, "\t\t\t\t")
    assert d_pred == d_true

    e = ("\n").join(
        [
            "  Hello, world!",
            "\t\t  My name is Josh!",
            "    \t\t  What's your name?",
        ]
    )

    f_true = ("\n").join(["!!!!!!" + line for line in e.split("\n")])
    f_pred = indent(e, "!!!!!!")
    assert f_pred == f_true

    g = """
      *question: What's your name?
        Alice
        Bob
        Charlie
        Denise
        Something else...
    """

    h_true = ("\n").join(
        ["\t\t" + line if len(line.strip()) > 0 else line for line in g.split("\n")]
    )

    h_pred = indent(g, "\t\t")
    assert h_pred == h_true
