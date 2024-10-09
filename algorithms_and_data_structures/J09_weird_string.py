#Napište funkci to_weird_case, která přijme řetězec a vrátí jej se všemi znaky na sudých pozicích
# převedenými na velké znaky a všemi znaky na lichých pozicích převedenými na malé znaky. Uvažujte,
# že každé slovo by mělo být považováno za samostatný řetězec tak, aby první znak každého slova měl
# vždy index 0, viz příklady níže. Nulu považujte za sudé číslo.
#```python
# to_weird_case('String')
## => return 'StRiNg'
# to_weird_case('Algorithms and data structures')
## => return 'AlGoRiThMs AnD DaTa StRuCtUrEs

# def to_weird_case(string: str) -> str:
#     new_str = string.split()
#     result = ''
#     for words in new_str:
#         index = 0
#         for char in words:
#             if index % 2:
#                 # print(char.lower(), end='')
#                 result += char.lower()
#             else:
#                 # print(char.upper(), end='')
#                 result += char.upper()
#             index += 1
#         # print(' ', end='')
#         result += ' '
#     return result.strip()  # strip() = odstranuje prebytecne mezery
# TODO veta neni uzavrena '' podle J08
def to_weird_case(string: str) -> str:
    words = string.split()
    new_words = []

    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        new_words.append(new_word)

    return ' '.join(new_words)


print(to_weird_case('Algorithms and data structures'))
# => return 'AlGoRiThMs AnD DaTa StRuCtUrEs'
