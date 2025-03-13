from .camelify import camelify


def test():
    assert camelify("foobarbaz") == "foobarbaz"
    assert camelify("Hello, world! My name is Josh!") == "helloWorldMyNameIsJosh"

    assert (
        camelify("'42 is the number thou shalt count!'")
        == "42IsTheNumberThouShaltCount"
    )

    assert camelify("I don't like you.") == "iDontLikeYou"
    assert camelify("howAboutNow") == "howAboutNow"

    assert (
        camelify("heresAnotherOne_YesOrNo-orMaybeSo")
        == "heresAnotherOneYesOrNoOrMaybeSo"
    )
