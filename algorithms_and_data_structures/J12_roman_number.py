"""Převod římských číslic na arabské
Napište funkci, která převede římské číslo na arabské (běžné celé číslo).
Římské číslice jsou I, V, X, L, C, D, M a mají hodnoty 1, 5, 10, 50, 100, 500, 1000.

Tip:
Při převodu je třeba mít na paměti, že pokud menší číslice předchází větší,
hodnota menší číslice se odečítá (např. IV = 4, IX = 9).

rom2dec('MMXXIV') -> 2024
"""
ROMAN = \
    {'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000}


def rom2dec(romstr: str):
    result = 0
    for i in range(len(romstr)):
        result += ROMAN[romstr[i]]
        if i < len(romstr) - 1:
            if ROMAN[romstr[i]] < ROMAN[romstr[i + 1]]:
                result -= 2 * ROMAN[romstr[i]]
    return result

# Petrovo verze 


def rom2decII(rom):
    reversed_rom = reversed(rom)
    arab = 0
    last_number = 0
    for character in reversed_rom:
        roman = ROMAN[character]
        if roman < last_number:
            arab -= roman
        else:
            arab += roman
        last_number = roman
    return arab

if __name__ == '__main__':
    print(f"'{rom2dec('MMXXVI')}'")
    print(rom2dec('MMXLI'))

    roman_numbers = ["MMXXIV", "DCIX", "IL", "VIII", "XIX"]
    for roman_number in roman_numbers:
        print(f"{roman_number} -> {rom2dec(roman_number)}")
    print("rom2decII")
    roman_numbers = ["MMXXIV", "DCIX", "IL", "VIII", "XIX"]
    for roman_number in roman_numbers:
        print(f"{roman_number} -> {rom2decII(roman_number)}")
        
# TODO testy
