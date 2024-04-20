import unittest

from chains import Chain


class TestNavigation(unittest.TestCase):

    def test_add_number(self):
        assert Chain(1) + 1 == 2
        assert Chain(1) + 1.1 == 2.1
        assert Chain(1.1) + 1 == 2.1
        assert Chain(1.1) + 1.1 == 2.2
        assert Chain(None) + 10 == 10

    def test_add_string(self):
        assert Chain("hello") + " world" == "hello world"
        assert Chain("hello") + " " + Chain("world") == "hello world"

    def test_add_list(self):
        assert Chain([1, 2, 3]) + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
        assert Chain([1, 2, 3]) + Chain([4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_subtract_number(self):
        assert Chain(1) - 1 == 0
        assert Chain(0) - 1 == -1
        assert Chain(2) - 1 == 1
        assert Chain(1.1) - 1.1 == 0
        assert Chain(10) - Chain(5) == 5
        assert Chain(0) - Chain(10) == -10
        assert Chain(None) - 10 == -10

    def test_multiply_number(self):
        assert Chain(1) * 1 == 1
        assert Chain(1) * 2 == 2
        assert Chain(2) * 2 == 4
        assert Chain(5) * 10 == 50
        assert Chain(5) * 0 == 0
        assert Chain(5) * -1 == -5
        assert Chain(5) * Chain(10) == 50

    def test_divide_number(self):
        assert Chain(1) / 1 == 1
        assert Chain(2) / 1 == 2
        assert Chain(2) / 2 == 1
        assert Chain(10) / 5 == 2
        assert Chain(5) / 10 == 0.5
        assert Chain(5) / 0 == 0
        assert Chain(5) / -1 == -5
        assert Chain(5) / Chain(10) == 0.5

        # Yes Chain lets you divide by 0
        assert Chain(10) / 0 == 0
        assert Chain(10) / Chain(0) == 0

    def test_modulo_number(self):
        assert Chain(1) % 1 == 0
        assert Chain(2) % 1 == 0
        assert Chain(2) % 2 == 0
        assert Chain(10) % 5 == 0
        assert Chain(5) % 10 == 5
        assert Chain(5) % 0 == 0
        assert Chain(5) % -1 == 0
        assert Chain(5) % Chain(10) == 5

    def test_power_number(self):
        assert Chain(1) ** 1 == 1
        assert Chain(2) ** 1 == 2
        assert Chain(2) ** 2 == 4
        assert Chain(10) ** 5 == 100000
        assert Chain(5) ** 0 == 1
        assert Chain(5) ** -1 == 0.2
        assert Chain(5) ** Chain(10) == 9765625
        assert Chain(None) ** 10 == 0

    def test_floor_div(self):
        assert Chain(1) // 1 == 1
        assert Chain(2) // 1 == 2
        assert Chain(2) // 2 == 1
        assert Chain(17) // 5 == 3
        assert Chain(5) // 10 == 0
        assert Chain(4) // Chain(3) == 1
        assert Chain(5) // 0 == 0
