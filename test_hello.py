from hello import more_hello, more_goodbye


def test_more_hello():
    assert more_hello() == "Hello, World!"


def test_more_goodbye():
    assert (
        more_goodbye() == "Goodbye, World!"
    )  # This will fail since more_hello returns "Hello, World!"
