from .kebabify import kebabify


def test():
    assert kebabify("foobarbaz") == "foobarbaz"
    assert kebabify("Hello, world! My name is Josh!") == "hello-world-my-name-is-josh"

    assert (
        kebabify("'42 is the number thou shalt count!'")
        == "42-is-the-number-thou-shalt-count"
    )

    assert kebabify("I don't like you.") == "i-don-t-like-you"
    assert kebabify("how-about-now") == "how-about-now"
