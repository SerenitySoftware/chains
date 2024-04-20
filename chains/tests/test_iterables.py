from chains import Chain


def test_dict_keys():
    chainable = Chain({"key": "value", "nested": {"key": "value"}})
    assert list(chainable.keys()) == ["key", "nested"]
    assert list(chainable.nested.keys()) == ["key"]
    assert "key" in chainable.keys()
    assert "nested" in chainable
    assert "missing" not in chainable


def test_lists():
    chainable = Chain([1, 2, 3])
    assert chainable[0] == 1
    assert chainable[1] == 2
    assert chainable[2] == 3
    assert 1 in chainable
    assert 4 not in chainable
    assert 1 in chainable[0:2]

    assert sorted(chainable, reverse=True) == [3, 2, 1]
    assert sorted(chainable, reverse=False) == [1, 2, 3]
    assert sorted(chainable[0:2], reverse=True) == [2, 1]
    assert sorted(chainable[0:2], reverse=False) == [1, 2]

    for index, item in enumerate(chainable):
        assert index + 1 == item


def test_sets():
    assert Chain(set()) == set()
    assert Chain({1, 2, 3}) == {1, 2, 3}
    assert 1 in Chain({1, 2, 3})


def test_strings():
    chainable = Chain("abcdefghijklmnopqrstuvwxyz")
    assert chainable[0] == "a"
    assert chainable[1] == "b"
    assert chainable[0:5] == "abcde"

    assert "a" in chainable
    assert "z" in chainable
    assert "abc" in chainable
    assert "xyz" in chainable


def test_generators():
    chainable = Chain(range(5))

    for index, item in enumerate(chainable):
        assert index == item
