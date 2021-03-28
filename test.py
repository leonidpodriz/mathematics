from utils import get_composition, get_image, get_prototype


def test_get_composition():
    a = {(1, 2), (3, 4)}
    b = {(2, 3), (4, 5)}
    composition = get_composition(a, b)

    assert len(composition) == 2
    assert (1, 3) in composition
    assert (3, 5) in composition


def test_get_image():
    a = {(1, 2), (1, 4), (2, 3), (4, 5)}

    i1 = get_image(a, 1)
    i2 = get_image(a, 2)
    i3 = get_image(a, 5)

    assert len(i1) == 2
    assert len(i2) == 1
    assert len(i3) == 0

    assert 2 in i1
    assert 4 in i1

    assert 3 in i2


def test_get_prototype():
    b = {(4, 2), (1, 2), (5, 3), (7, 4)}

    i1 = get_prototype(b, 2)
    i2 = get_prototype(b, 3)
    i3 = get_prototype(b, 6)

    assert len(i1) == 2
    assert len(i2) == 1
    assert len(i3) == 0

    assert 4 in i1
    assert 1 in i1

    assert 5 in i2
