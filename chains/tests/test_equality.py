from decimal import Decimal

from chains import Chain


def test_none():
    chain_none = Chain(None)
    assert chain_none == None
    assert chain_none() is None
    assert chain_none != ""

    chain_empty = Chain("")
    assert chain_empty != None
    assert chain_empty() == ""
    assert chain_empty is not None


def test_booleans():
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


def test_strings():
    assert Chain("") == ""
    assert Chain("hello") == "hello"
    assert Chain("hello") != "world"


def test_raw_number_equality():
    assert Chain(0) == 0
    assert Chain(1) == 1
    assert Chain(-1) == -1
    assert Chain(1.1) == 1.1
    assert Chain(-1.1) == -1.1


def test_raw_number_inequality():
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


def test_raw_number_greater_than():
    assert Chain(1) > 0
    assert Chain(1) > -1
    assert Chain(1) > 0.5
    assert Chain(1) > -0.5

    assert Chain(1) >= 1
    assert Chain(1) >= 0
    assert Chain(1) >= -1
    assert Chain(1) >= 0.5

    assert 0 > Chain({"numeric": 5}).garbage


def test_raw_number_less_than():
    assert Chain(1) < 2
    assert Chain(1) < 1.1
    assert Chain(1) < 1.5
    assert Chain(-1) < 0

    assert Chain(1) <= 2
    assert Chain(1) <= 1.1
    assert Chain(1) <= 1
    assert Chain(-1) <= 0

    assert Chain({"numeric": 5}).garbage < 0


def test_nested_numbers():
    assert Chain({"numeric": 5}).numeric == 5
    assert Chain({"numeric": 5}).numeric != 1
    assert Chain({"numeric": 5.5}).numeric == 5.5


def test_floats():
    assert Chain(5.09245) == 5.09245
    assert Chain(5.09245) != 5.09246


def test_decimals():
    assert Chain(Decimal("5.09245")) == Decimal("5.09245")
    assert Chain(Decimal("5.09245")) != Decimal("5.09246")


def test_dicts():
    assert Chain({}) == {}
    assert Chain({"hello": "world"}) == {"hello": "world"}
    assert Chain({"foo": "bar"}) != {"baz": "qux"}
    assert Chain({"content": {"nested": "here"}}) == {"content": {"nested": "here"}}


def test_lists():
    assert Chain([]) == []
    assert Chain([1, 2, 3]) == [1, 2, 3]
    assert Chain(["hello", "world"]) == ["hello", "world"]
    assert Chain([1, 2, 3]) != [3, 2, 1]
    assert Chain([1, 2, 3]) != [1, 2, 3, 4]
