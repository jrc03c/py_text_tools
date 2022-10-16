from py_text_tools.utils import replace_all
from unittest import TestCase


class ReplaceAllTestCase(TestCase):
    def test(self):
        self.assertEqual(replace_all("foobar", "o", "z"), "fzzbar")
        self.assertEqual(replace_all("Hello, world!", "!", "?"), "Hello, world?")

