from unittest import TestCase

from py_text_tools import camelify


class CamelifyTestCase(TestCase):
    def test(self):
        self.assertEqual(camelify("foobarbaz"), "foobarbaz")

        self.assertEqual(
            camelify("Hello, world! My name is Josh!"), "helloWorldMyNameIsJosh"
        )

        self.assertEqual(
            camelify("'42 is the number thou shalt count!'"),
            "42IsTheNumberThouShaltCount",
        )

        self.assertEqual(camelify("I don't like you."), "iDontLikeYou")
        self.assertEqual(camelify("howAboutNow"), "howAboutNow")

        self.assertEqual(
            camelify("heresAnotherOne_YesOrNo-orMaybeSo"),
            "heresAnotherOneYesOrNoOrMaybeSo",
        )
