"""
Implementujte funkci is_prime(n), která vrátí True, pokud je číslo prvočíslo, jinak vrátí False.
Implementujte funkci factorial(n), která vrátí faktoriál čísla n.
"""
import pytest
from p08_Exercise import is_prime, factorial


def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(1217) == True

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(7) == 5040
    # assert factorial(-5) == ValueError


if __name__ == "__main__":
    pytest.main()
