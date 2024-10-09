import pytest

from exercise import *


@pytest.mark.parametrize("string, result", [("highline", "ihie"),
                                            ("policista", "oiit"),
                                            ((123456789), (2, 4, 6, 8))])
def test_odd_indexes(string, result):
    assert odd_indexes(string) == result


# Petrovo reseni

def test_odd_indexes_str():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"
    assert odd_indexes("Petr") == "er"


def test_odd_indexes_int():
    assert odd_indexes(123456789) == "2468"
    assert odd_indexes(3456) == "46"
    assert odd_indexes(159753) == "573"
    assert odd_indexes(0) == ""
    assert odd_indexes(1) == ""
    assert odd_indexes(11) == "1"
    assert odd_indexes(111) == "1"
    assert odd_indexes(1111) == "11"


"""Exercise 2a

Rewrite the previous tests to use pytest parameterization and remove code duplication.
"""


# TODO proc ma u inputu (input_) to _ ?
@pytest.mark.parametrize("input_, result", [("elephant", "lpat"), ("computer", "optr"), ("Petr", "er"),
                                            (123456789, "2468"), (0, ""), (1, ""), (11, "1"),
                                            (111, "1"), (1111, "11")])
def test_odd_indexes_param(input_, result):
    assert odd_indexes(input_) == result
