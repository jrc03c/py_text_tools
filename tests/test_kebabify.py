from unittest import TestCase

from py_text_tools import kebabify


class KebabifyTestCase(TestCase):
    def test(self):
        self.assertEqual(kebabify("foobarbaz"), "foobarbaz")

        self.assertEqual(
            kebabify("Hello, world! My name is Josh!"), "hello-world-my-name-is-josh"
        )

        self.assertEqual(
            kebabify("'42 is the number thou shalt count!'"),
            "42-is-the-number-thou-shalt-count",
        )

        self.assertEqual(kebabify("I don't like you."), "i-dont-like-you")
        self.assertEqual(kebabify("how-about-now"), "how-about-now")

        self.assertEqual(
            kebabify("heresAnotherOne_YesOrNo-orMaybeSo"),
            "heresanotherone-yesorno-ormaybeso",
        )
