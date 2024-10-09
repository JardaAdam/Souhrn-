from unittest.mock import patch, MagicMock
from exercise4 import get_avg


def test_get_avg():
    fake_get_data = MagicMock(return_value="1")
    with patch("exercise4._get_data", fake_get_data):
        assert get_avg(1) == 1

    fake_get_data = MagicMock(return_value="12")
    with patch("exercise4._get_data", fake_get_data):
        assert get_avg(2) == 1.5

    fake_get_data = MagicMock(return_value="123")
    with patch("exercise4._get_data", fake_get_data):
        assert get_avg(3) == 2

    fake_get_data = MagicMock(return_value="1234")
    with patch("exercise4._get_data", fake_get_data):
        assert get_avg(4) == 2.5

# a tak dale az do vsech cisel 123456789