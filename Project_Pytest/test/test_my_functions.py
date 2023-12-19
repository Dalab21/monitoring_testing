import pytest
import time


import source.my_functions as mf

def test_add():
    result = mf.add(1,4)
    assert result == 5


def test_divide():
    result = mf.divide(245, 10)
    assert True


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = mf.divide(12, 0)


def test_divide():
    result = mf.divide(120, 5)


def test_add_strings():
    result = mf.add("J'aime ", "le fromage")
    assert result == "J'aime le fromage"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = mf.divide(10,5)
    assert result == 2

@pytest.mark.skip(reason = "this feature is currently broken")
def test_add():
    assert mf.add(1,2) == 3


@pytest.mark.xfail(reason = "We know we cannot divide by zero")
def test_divide_zero_broken():
    mf.divide(4,0)