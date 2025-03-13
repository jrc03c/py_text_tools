from unittest import TestCase

from py_text_tools.utils import replace_all


class ReplaceAllTestCase(TestCase):
    def test(self):
        self.assertEqual(replace_all("foobar", "o", "z"), "fzzbar")
        self.assertEqual(replace_all("Hello, world!", "!", "?"), "Hello, world?")
