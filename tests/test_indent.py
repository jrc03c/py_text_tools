from unittest import TestCase

from py_text_tools import indent


class IndentTestCase(TestCase):
    def test(self):
        a = "Hello, world!"
        b_true = "    Hello, world!"
        b_pred = indent(a, "    ")
        self.assertEqual(b_true, b_pred)

        c = "Hello, world!"
        d_true = "\t\t\t\tHello, world!"
        d_pred = indent(c, "\t\t\t\t")
        self.assertEqual(d_true, d_pred)

        e = ("\n").join(
            ["  Hello, world!", "\t\t  My name is Josh!", "    \t\t  What's your name?"]
        )

        f_true = ("\n").join(list(map(lambda line: "!!!!!!" + line, e.split("\n"))))
        f_pred = indent(e, "!!!!!!")
        self.assertEqual(f_true, f_pred)

        g = """
            *question: What's your name?
                Alice
                Bob
                Charlie
                Denise
                Something else...
        """

        h_true = ("\n").join(
            list(
                map(
                    lambda line: "\t\t" + line if len(line.strip()) > 0 else line,
                    g.split("\n"),
                )
            )
        )

        h_pred = indent(g, "\t\t")
        self.assertEqual(h_true, h_pred)
