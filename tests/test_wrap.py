from numpy.random import random
from py_text_tools import wrap
from unittest import TestCase


def make_key(n):
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
    out = ""

    while len(out) < n:
        out += alpha[int(random() * len(out))]

    return out


class WrapTestCase(TestCase):
    def test_length_constraints(self):
        text = (" ").join(list(map(lambda i: make_key(8), list(range(0, 1000)))))
        max_line_lengths = [40, 80, 120]

        for max_line_length in max_line_lengths:
            wrapped = wrap(text, max_line_length=max_line_length)

            for line in wrapped.split("\n"):
                self.assertLessEqual(len(line), max_line_length)

    def test_indentation_preservation(self):
        text = "\t\tLorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mollis tellus eu mi condimentum, a congue ipsum luctus. Donec vel suscipit dolor, vitae faucibus massa. Curabitur rhoncus semper tortor et mattis. Nullam laoreet lobortis nibh eget viverra. Nam molestie risus vitae ante placerat convallis. Pellentesque quis tristique dui. Vivamus efficitur mi erat, nec gravida felis posuere at. Donec sapien ipsum, viverra et aliquam quis, posuere ac ligula. Aenean egestas tincidunt mauris, in hendrerit tortor malesuada id. Proin viverra sodales ex eu fermentum. Aenean nisl ipsum, tristique venenatis massa eget, tempor facilisis felis. Praesent aliquam sem vitae arcu porta commodo. Aliquam tempor sollicitudin dapibus. Nulla ullamcorper orci eu ultricies cursus."

        wrapped = wrap(text, 40)
        lines = wrapped.split("\n")

        for line in lines:
            self.assertEqual("\t\t", line[:2])
            self.assertLessEqual(len(line), 40)
