import pytest

from p01_BasicCalculator import BasicCalculator


class Test():

    def setup_method(self):
        print("\nEnvironment for test preparation")

    def test_addition(self):
        basic_calculator = BasicCalculator()
        assert basic_calculator.add(5, 7) == 12
        assert basic_calculator.add(7, 5) == 12
        assert basic_calculator.add(15, 0) == 15
        assert basic_calculator.add(9, -5) == 4
        assert basic_calculator.add("5", 2) is None
        assert basic_calculator.add(5, "ahoj") is None
        assert basic_calculator.add("hello", "world") is None

    def test_subtraction(self):
        basic_calculator = BasicCalculator()
        assert basic_calculator.subtract(7, 5) == 2
        assert basic_calculator.subtract(5, 7) == -2
        assert basic_calculator.subtract("5", 2) is None
        assert basic_calculator.subtract(5, "ahoj") is None
        assert basic_calculator.subtract("hello", "world") is None

    def test_multiply(self):
        basic_calculator = BasicCalculator()
        assert basic_calculator.multiply(5, 3) == 15
        assert basic_calculator.multiply(-1, 5) < 0
        assert basic_calculator.multiply(17, 0) == 0
        assert basic_calculator.multiply("5", 2) is None
        assert basic_calculator.multiply(5, "ahoj") is None
        assert basic_calculator.multiply("hello", "world") is None

    def test_divide(self):
        basic_calculator = BasicCalculator()
        assert basic_calculator.divide(10, 2) == 5
        assert basic_calculator.divide(15, 3) == 5
        assert basic_calculator.divide(10, 3) == 10 / 3
        # with pytest.raises(Exception):
        #    assert basic_calculator.divide(10, 0)
        assert basic_calculator.divide(10, 0) is None
        assert basic_calculator.divide(5, basic_calculator.add(10, -10)) is None
        assert basic_calculator.divide("5", 2) is None
        assert basic_calculator.divide(5, "ahoj") is None
        assert basic_calculator.divide("hello", "world") is None

    def teardown_method(self):
        print("\nEnd of test.")
