import numpy as np

from .helpers import string_to_array
from .wrap import wrap


def make_key(n):
    alpha = "abcdef1234567890"
    out = ""

    for i in range(0, n):
        out += alpha[int(np.random.random() * len(alpha))]

    return out


def test1():
    text = (" ").join([make_key(8) for i in range(0, 1000)])
    max_line_lengths = [40, 80, 120]

    for max_line_length in max_line_lengths:
        wrapped = wrap(text, max_line_length=max_line_length)

        for line in wrapped.split("\n"):
            assert len(line) <= max_line_length


def test2():
    text = "\t\tLorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mollis tellus eu mi condimentum, a congue ipsum luctus. Donec vel suscipit dolor, vitae faucibus massa. Curabitur rhoncus semper tortor et mattis. Nullam laoreet lobortis nibh eget viverra. Nam molestie risus vitae ante placerat convallis. Pellentesque quis tristique dui. Vivamus efficitur mi erat, nec gravida felis posuere at. Donec sapien ipsum, viverra et aliquam quis, posuere ac ligula. Aenean egestas tincidunt mauris, in hendrerit tortor malesuada id. Proin viverra sodales ex eu fermentum. Aenean nisl ipsum, tristique venenatis massa eget, tempor facilisis felis. Praesent aliquam sem vitae arcu porta commodo. Aliquam tempor sollicitudin dapibus. Nulla ullamcorper orci eu ultricies cursus."

    wrapped = wrap(text, 40)

    for line in wrapped.split("\n"):
        assert line[:2] == "\t\t"
        assert len(line) <= 40


def test3():
    prefix = ">> "
    max_length = 80
    y_true = []

    for i in range(0, 10):
        line = string_to_array(
            ((prefix if i > 0 else "") + make_key(max_length))[:max_length]
        )

        for _ in range(0, int(0.25 * len(line))):
            index = int(np.random.random() * (len(line) - 1))

            if (
                index >= len(prefix)
                and line[index - 1] != " "
                and line[index + 1] != " "
            ):
                line = line[:index] + [" "] + line[index + 1 :]

        y_true.append(("").join(line))

    y_true = ("\n").join(y_true)
    x = (" ").join([line.replace(prefix, "") for line in y_true.split("\n")])
    y_pred = wrap(x, max_line_length=max_length, wrapped_line_prefix=prefix)
    assert y_pred == y_true


def test4():
    wrongs = [
        [234, 80],
        [True, 80],
        [False, 80],
        [None, 80],
        [{}, 80],
        [[], 80],
        [lambda x: x, 80],
        ["Hello, world!", "foobar"],
        ["Hello, world!", True],
        ["Hello, world!", False],
        ["Hello, world!", {}],
        ["Hello, world!", []],
        ["Hello, world!", lambda x: x],
    ]

    for pair in wrongs:
        failed = False

        try:
            wrap(pair[0], pair[1])

        except Exception:
            failed = True

        assert failed
