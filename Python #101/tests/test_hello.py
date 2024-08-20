from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Bu", "Bi", "Zim"]:
        assert hello(name) == f"hello, {name}"