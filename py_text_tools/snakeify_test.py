from .snakeify import snakeify


def test():
    assert snakeify("foobarbaz") == "foobarbaz"
    assert snakeify("Hello, world! My name is Josh!") == "hello_world_my_name_is_josh"

    assert (
        snakeify("'42 is the number thou shalt count!'")
        == "42_is_the_number_thou_shalt_count"
    )

    assert snakeify("I don't like you.") == "i_don_t_like_you"
    assert snakeify("how_about_now") == "how_about_now"
