from examples_class_based import Circle


def test_Circle():
    c = Circle(10)
    assert c.radius == 10