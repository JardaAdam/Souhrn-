"""Počítání slov
Implementujte funkci word_count(s), která vrátí počet slov v daném řetězci.
"""
import pytest
from Jp09_Exercise_word_count import word_count


def test_word_count():
    assert word_count("Hello world") == 2
    assert word_count("This is a test") == 4
    assert word_count("One more test case") == 4
    assert word_count("") == 0
    assert word_count("Python is awesome!") == 3
    assert word_count("takze jeste upravim tuhle chybu") == 5


if __name__ == "__main__":
    pytest.main()
