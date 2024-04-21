import unittest

from chains import Chain


class TestBuiltins(unittest.TestCase):

    def test_repr(self):
        assert repr(Chain(1)) == "1"
        assert repr(Chain("hello")) == "'hello'"
        assert repr(Chain([1, 2, 3])) == "[1, 2, 3]"
        assert repr(Chain({"a": 1, "b": 2})) == "{'a': 1, 'b': 2}"

    def test_str(self):
        assert str(Chain(1)) == "1"
        assert str(Chain("hello")) == "hello"
        assert str(Chain([1, 2, 3])) == "[1, 2, 3]"
        assert str(Chain({"a": 1, "b": 2})) == "{'a': 1, 'b': 2}"
        assert str(Chain(None)) == "None"

    def test_hash(self):
        assert hash(Chain(None)) == hash(None)
        assert hash(Chain(1)) == hash(1)
        assert hash(Chain("hello")) == hash("hello")
