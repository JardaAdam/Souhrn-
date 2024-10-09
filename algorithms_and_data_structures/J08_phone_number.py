from typing import List
#Napište funkci, která přijme seznam 12 celých čísel a vrátí řetězec ve formátu telefonního čísla.
#Struktura funkce by měla vypadat takto:

def create_phone_number(n: List[int]) -> str:
    # return f"(+{n[0]}{n[1]}) {n[2]}{n[3]}{n[4]}-{n[5]}{n[6]}{n[7]}-{n[8]}{n[9]}{n[10]}"
    str1 = ''.join(str(x) for x in n[0:2])
    str2 = ''.join(str(x) for x in n[2:5])
    str3 = ''.join(str(x) for x in n[5:8])
    str4 = ''.join(str(x) for x in n[8:])
    return '(+{}) {}-{}-{}'.format(str1, str2, str3, str4)


if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    print(f'"{create_phone_number(n)}"')
# => returns "(+12) 345-678-901"
