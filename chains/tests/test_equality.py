from decimal import Decimal
import unittest

from chains import Chain


class TestEquality(unittest.TestCase):

    def test_none(self):
        chain_none = Chain(None)
        assert chain_none == None
        assert chain_none() is None
        assert chain_none != ""

        chain_empty = Chain("")
        assert chain_empty != None
        assert chain_empty() == ""
        assert chain_empty is not None

    def test_booleans(self):
        chain_true = Chain(True)
        chain_nested_true = Chain({"nested": True}).nested
        chain_false = Chain(False)
        chain_nested_false = Chain({"nested": False}).nested

        assert chain_true == True
        assert chain_true != False
        assert chain_true() is True
        assert chain_true() is not False

        assert chain_false == False
        assert chain_false != True
        assert chain_false() is False
        assert chain_false() is not True

        assert chain_nested_true == True
        assert chain_nested_true != False
        assert chain_nested_true() is True
        assert chain_nested_true() is not False

        assert chain_nested_false == False
        assert chain_nested_false != True
        assert chain_nested_false() is False
        assert chain_nested_false() is not True

    def test_strings(self):
        assert Chain("") == ""
        assert Chain("hello") == "hello"
        assert Chain("hello") != "world"

    def test_raw_number_equality(self):
        assert Chain(0) == 0
        assert Chain(1) == 1
        assert Chain(-1) == -1
        assert Chain(1.1) == 1.1
        assert Chain(-1.1) == -1.1

    def test_raw_number_inequality(self):
        assert Chain(1) != 0
        assert Chain(1) != 1.1
        assert Chain(1) != -1
        assert Chain(1) != -1.1
        assert Chain(1.1) != 0
        assert Chain(1.1) != 1
        assert Chain(1.1) != -1
        assert Chain(1.1) != -1.1
        assert Chain(-1) != 0
        assert Chain(-1) != 1
        assert Chain(-1) != 1.1
        assert Chain(-1) != -1.1
        assert Chain(-1.1) != 0
        assert Chain(-1.1) != 1
        assert Chain(-1.1) != 1.1
        assert Chain(-1.1) != -1

    def test_raw_number_greater_than(self):
        assert Chain(1) > 0
        assert Chain(1) > -1
        assert Chain(1) > 0.5
        assert Chain(1) > -0.5

        assert Chain(1) >= 1
        assert Chain(1) >= 0
        assert Chain(1) >= -1
        assert Chain(1) >= 0.5

        self.assertTrue(1 > Chain({"numeric": 5}).garbage)
        self.assertTrue(1 >= Chain({"numeric": 5}).garbage)

        self.assertFalse(Chain(None) > 1)
        self.assertFalse(Chain(None) >= 1)

    def test_raw_number_less_than(self):
        assert Chain(1) < 2
        assert Chain(1) < 1.1
        assert Chain(1) < 1.5
        assert Chain(-1) < 0

        assert Chain(1) <= 2
        assert Chain(1) <= 1.1
        assert Chain(1) <= 1
        assert Chain(-1) <= 0

        self.assertFalse(Chain({"numeric": 5}).garbage < 0)
        self.assertTrue(Chain({"numeric": 5}).garbage <= 0)
        self.assertTrue(Chain({"numeric": 5}).garbage < 1)
        self.assertTrue(Chain({"numeric": 5}).garbage <= 1)

        self.assertTrue(Chain(None) < 1)
        self.assertTrue(Chain(None) <= 1)

    def test_nested_numbers(self):
        assert Chain({"numeric": 5}).numeric == 5
        assert Chain({"numeric": 5}).numeric != 1
        assert Chain({"numeric": 5.5}).numeric == 5.5

    def test_floats(self):
        assert Chain(5.09245) == 5.09245
        assert Chain(5.09245) != 5.09246

    def test_decimals(self):
        assert Chain(Decimal("5.09245")) == Decimal("5.09245")
        assert Chain(Decimal("5.09245")) != Decimal("5.09246")

    def test_dicts(self):
        assert Chain({}) == {}
        assert Chain({"hello": "world"}) == {"hello": "world"}
        assert Chain({"foo": "bar"}) != {"baz": "qux"}
        assert Chain({"content": {"nested": "here"}}) == {"content": {"nested": "here"}}

    def test_lists(self):
        assert Chain([]) == []
        assert Chain([1, 2, 3]) == [1, 2, 3]
        assert Chain(["hello", "world"]) == ["hello", "world"]
        assert Chain([1, 2, 3]) != [3, 2, 1]
        assert Chain([1, 2, 3]) != [1, 2, 3, 4]
