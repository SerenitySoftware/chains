from chains import Chain


def test_raw_object():
    assert Chain(0) == 0
    assert Chain(False) == False
    assert Chain({"key": "value"}) == {"key": "value"}
    assert Chain([1, 2, 3]) == [1, 2, 3]


def test_dict_access():
    assert Chain({"key": "value"}).key == "value"


def test_dict_access_missing():
    assert Chain({"key": "value"}).missing() is None
    assert not Chain({"key": "value"}).missing


def test_dict_access_nested():
    assert Chain({"nested": {"key": "value"}}).nested.key == "value"
    assert Chain({"nested": {"deeper": {"key": "value"}}}).nested.deeper == {"key": "value"}


def test_dict_access_nested_missing():
    assert Chain({"nested": {"key": "value"}}).nested.missing() is None


def test_list_access():
    assert Chain([1, 2, 3])[0] == 1
    assert Chain([1, 2, 3])[1] == 2
    assert Chain([1, 2, 3])[2] == 3


def test_list_access_missing():
    assert Chain([1, 2, 3])[3]() is None


def test_list_access_nested():
    assert Chain([{"key": "value"}])[0] == {"key": "value"}
    assert Chain({"items": [55, 8, 59]}).items[1] == 8
    assert Chain({"items": [{"hello": "world"}]}).items[0].hello == "world"
