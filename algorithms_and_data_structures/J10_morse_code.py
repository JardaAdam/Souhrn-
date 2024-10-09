#Ačkoli Morseova abeceda je v současné době většinou nahrazena jinými metodami přenosu dat, stále se používá
#v některých aplikacích po celém světě.
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str) -> str:
    #print(f"morse_code: {morse_code}")

    # odstanit zbytecne mezery na zacatku a na konci kodu
    morse_code = morse_code.strip()
    #print(f"morse_code.strip(): '{morse_code}'")

    # rozdelim si zadani na jednotlive slova
    morse_word_list = morse_code.split('   ')
    result = ''
    for morse_word in morse_word_list:
        # Rozsekám si slova na jednotlivá písmena
        morse_char_list = morse_word.split()
        #    print(f"morse_char_list: {morse_char_list}")
        # FIXME: osetrit tri mezery => oddelovac slov

        # kazdy znam prevedu podle slovniku MORSE_CODE na pismeno
        for morse_char in morse_char_list:
            result += MORSE_CODE[morse_char]

        result += ' '

    # vratim vysledek
    return result.strip()


if __name__ == "__main__":
    print(f"'{decode_morse('.... . -.--   .--- ..- -.. .')}'")  ## => 'HEY JUDE'
    print(f"'{decode_morse(' . ')}'")  ## => 'E'
    print(f"'{decode_morse('...   ---   ...')}'")  ## => 'S O S'
