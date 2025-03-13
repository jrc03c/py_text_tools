from .pascalify import pascalify


def test():
    assert pascalify("foobarbaz") == "Foobarbaz"
    assert pascalify("Hello, world! My name is Josh!") == "HelloWorldMyNameIsJosh"

    assert (
        pascalify("'42 is the number thou shalt count!'")
        == "42IsTheNumberThouShaltCount"
    )

    assert pascalify("I don't like you.") == "IDontLikeYou"
    assert pascalify("howAboutNow") == "HowAboutNow"

    assert (
        pascalify("heresAnotherOne_YesOrNo-orMaybeSo")
        == "HeresAnotherOneYesOrNoOrMaybeSo"
    )
