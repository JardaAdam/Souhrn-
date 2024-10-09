"""Fibonacciho posloupnost
Implementujte funkci fibonacci(n), která vrátí n-tý prvek Fibonacciho posloupnosti.
"""
import pytest
from p10_Exercise_fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


if __name__ == "__main__":
    pytest.main()
