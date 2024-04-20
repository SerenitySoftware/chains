from chains import sniff


def test_isdictlike():
    assert sniff.isdictlike({}) is True
    assert sniff.isdictlike([]) is False
    assert sniff.isdictlike(set()) is False
    assert sniff.isdictlike(1) is False
    assert sniff.isdictlike("hello") is False


def test_islistlike():
    assert sniff.islistlike([]) is True
    assert sniff.islistlike(set()) is True
    assert sniff.islistlike({}) is False
    assert sniff.islistlike(1) is False
    assert sniff.islistlike("hello") is False


def test_isiterable():
    assert sniff.isiterable([]) is True
    assert sniff.isiterable(set()) is True
    assert sniff.isiterable({}) is True
    assert sniff.isiterable(1) is False
    assert sniff.isiterable("hello") is True


def test_isnestable():
    assert sniff.isnestable([]) is True
    assert sniff.isnestable(set()) is True
    assert sniff.isnestable({}) is True
    assert sniff.isnestable(1) is False
    assert sniff.isnestable("hello") is False
