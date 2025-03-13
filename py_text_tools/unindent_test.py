from .unindent import unindent


def test():
    a = "Hello, world!"
    b_true = a
    b_pred = unindent(a)
    assert b_pred == b_true

    c = ("\n").join(
        [
            "    Hello, world!",
            "        My name is Josh.",
            "  What's your name?",
        ]
    )

    d_true = ("\n").join([line[2:] for line in c.split("\n")])
    d_pred = unindent(c)
    assert d_pred == d_true

    e = ("\n").join(
        [
            "\t         \t  Hello, world!",
            "\tMy name is Josh",
            "\t  \t\t    Yep, that's all!",
        ]
    )

    f_true = ("\n").join([line[1:] for line in e.split("\n")])
    f_pred = unindent(e)
    assert f_pred == f_true

    g = ("\n").join(
        [
            "\t\t*question: What's your name?",
            "\t\t\tAlice",
            "\t\t\tBob",
            "\t\t\tCharlie",
            "\t\t\tDenise",
            "\t\t\tSomething else...",
        ]
    )

    h_true = "*question: What's your name?\n\tAlice\n\tBob\n\tCharlie\n\tDenise\n\tSomething else..."

    h_pred = unindent(g)
    assert h_pred == h_true
