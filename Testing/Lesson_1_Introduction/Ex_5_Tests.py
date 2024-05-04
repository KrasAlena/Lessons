from Ex_5 import Rectangle


def test_set_width_positive_number():
    rectangle = Rectangle(4, 2)
    rectangle.set_width(5)
    assert rectangle.width == 5


def test_set_width_negative_number():
    rectangle = Rectangle(4, 2)
    rectangle.set_width(-4)
    assert rectangle.width == -4


def test_set_width_zero():
    rectangle = Rectangle(4, 2)
    rectangle.set_width(0)
    assert rectangle.width == 0


def test_set_width_float():
    rectangle = Rectangle(4, 2)
    rectangle.set_width(4.5)
    assert rectangle.width == 4.5


def test_set_width_string():
    rectangle = Rectangle(4, 2)
    try:
        rectangle.set_width('test')
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_set_width_no_value():
    try:
        rectangle = Rectangle(4, 2)
        rectangle.set_width()
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_set_height_positive_number():
    rectangle = Rectangle(4, 2)
    rectangle.set_height(5)
    assert rectangle.height == 5


def test_set_height_negative_number():
    rectangle = Rectangle(4, 2)
    rectangle.set_height(-2)
    assert rectangle.height == -2


def test_set_height_zero():
    rectangle = Rectangle(4, 2)
    rectangle.set_height(0)
    assert rectangle.height == 0


def test_set_height_float():
    rectangle = Rectangle(4, 2)
    rectangle.set_height(2.5)
    assert rectangle.height == 2.5


def test_set_height_string():
    rectangle = Rectangle(4, 2)
    try:
        rectangle.set_height('test')
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_set_height_no_value():
    try:
        rectangle = Rectangle(4, 2)
        rectangle.set_height()
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_set_height_same_value():
    rectangle = Rectangle(4, 2)
    rectangle.set_height(2)
    assert rectangle.height == 2


def test_get_area_numbers():
    rectangle = Rectangle(4, 2.5)
    assert rectangle.get_area() == 10.0


def test_get_area_strings():
    rectangle = Rectangle('test', 'test')
    try:
        rectangle.get_area()
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_get_area_string_and_number():
    rectangle = Rectangle('test', 2)
    try:
        rectangle.get_area()
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_get_area_no_values():
    rectangle = Rectangle()
    try:
        rectangle.get_area()
        assert False, 'Should raise TypeError'
    except TypeError:
        pass