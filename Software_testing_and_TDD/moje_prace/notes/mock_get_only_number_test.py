from unittest.mock import patch, MagicMock
from mock_get_only_numbers import get_only_numbers, API
# protoze nemuzu delat upravy v mock_get_only_numbers.py na radku 1 - 4 tak si vytvorim
# fake_api abych ziskal data pro metody teto tridy

def test_read_only_numbers():

    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]
    #test_data = open('bb').readline()  # dalsi moznost zadani dat

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  mockovani get_data metody
    with patch('mock_get_only_numbers.API', fake_api):  # vytvorim zaplatu ktera nahradi radky
                                                        # 1-4 v mock_get_only_numbers.py
        # patch nahrazuje originální objekty a správce kontextu definuje rozsah použití mocku
        result = get_only_numbers()
        assert result == expected