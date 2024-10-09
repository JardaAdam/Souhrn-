import pytest
from p04_Exercise_2 import *

"""Exercise 2
You have the code:

def odd_indexes(string):
    return string[1::2]

For the given string it returns letters from odd indexes, e.g.

elephant -> lpat computer -> optr

Test this function for an argument that will be a string.

Run the function by passing an int. Observe what happens. 
Write tests for arguments that are int. 
Correct the function to make it work fully and make the tests pass.
"""


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


@pytest.mark.parametrize("input_, result", [("elephant", "lpat"), ("computer", "optr"), ("Petr", "er"),
                                           (123456789, "2468"), (0, ""), (1, ""), (11, "1"),
                                           (111, "1"), (1111, "11")])
def test_odd_indexes_param(input_, result):
    assert odd_indexes(input_) == result
