from unittest import TestCase

from py_text_tools.helpers import strip


class StripTestCase(TestCase):
    def test(self):
        self.assertEqual(strip("foobarbaz"), "foobarbaz")

        self.assertEqual(
            strip("Hello, world! My name is Josh!"), "hello world my name is josh"
        )

        self.assertEqual(
            strip("'42 is the number thou shalt count!'"),
            "42 is the number thou shalt count",
        )

        self.assertEqual(strip("I don't like you."), "i dont like you")
        self.assertEqual(strip("how about now"), "how about now")

        self.assertEqual(
            strip("heresAnotherOne_YesOrNo-orMaybeSo"),
            "heresanotherone yesorno ormaybeso",
        )
