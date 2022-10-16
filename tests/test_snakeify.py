from py_text_tools import snakeify
from unittest import TestCase


class SnakeifyTestCase(TestCase):
    def test(self):
        self.assertEqual(snakeify("foobarbaz"), "foobarbaz")

        self.assertEqual(
            snakeify("Hello, world! My name is Josh!"), "hello_world_my_name_is_josh"
        )

        self.assertEqual(
            snakeify("'42 is the number thou shalt count!'"),
            "42_is_the_number_thou_shalt_count",
        )

        self.assertEqual(snakeify("I don't like you."), "i_dont_like_you")
        self.assertEqual(snakeify("how_about_now"), "how_about_now")

        self.assertEqual(
            snakeify("heresAnotherOne_YesOrNo-orMaybeSo"),
            "heresanotherone_yesorno_ormaybeso",
        )
