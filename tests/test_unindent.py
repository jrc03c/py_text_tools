from unittest import TestCase

from py_text_tools import unindent


class UnindentTestCase(TestCase):
    def test(self):
        a = "Hello, world!"
        b_true = a
        b_pred = unindent(a)
        self.assertEqual(b_true, b_pred)

        c = ("\n").join(
            [
                "    Hello, world!",
                "        My name is Josh.",
                "  What's your name?",
            ]
        )

        d_true = ("\n").join(list(map(lambda line: line[2:], c.split("\n"))))
        d_pred = unindent(c)
        self.assertEqual(d_true, d_pred)

        e = ("\n").join(
            [
                "\t         \t  Hello, world!",
                "\tMy name is Josh",
                "\t  \t\t    Yep, that's all!",
            ]
        )

        f_true = ("\n").join(list(map(lambda line: line[1:], e.split("\n"))))
        f_pred = unindent(e)
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
            [
                "*question: What's your name?",
                "    Alice",
                "",
                "    Bob",
                "",
                "    Charlie",
                "",
                "    Denise",
                "",
                "    Something else...",
            ]
        )

        h_pred = unindent(g).strip()
        self.assertEqual(h_true, h_pred)
