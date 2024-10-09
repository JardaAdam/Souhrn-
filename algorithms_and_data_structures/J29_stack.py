"""zásobník = data vkládané do zasobníku > se vkládají a odebírají y vrchu
polsední vložená je první vyjmutá
LIFO = Last in, First out
push = přidávání položky
pop = odebírání yhora zásobníku"""

"""Využítí -> zálohování dat ( poslední uložení je první na řadě v případě 
vzvolání dat"""

# úloha
""" Závorky
Napište funkci, která má jako parametr string obsahující závorky.
Funkce vrátí True, pokud jsou závorky "správně", jinak False

()
(())
)( -> ()
(()
(()))(
(()))((())
1210-   vysledek je False!! protoze v prubehu kontroli jsm se dostal do zaporu
((()())())
1232321210  vysledek je True v prubehu kontroli jsem se nedostal do zapornych cisel
-> takze zavorky jsou ve spravnem poradi 
"""


def brackets(word):
    count = 0
    for c in word:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


"""
([)] -> False
([]) -> True
([][{}]) -> True

({[]<[]>}()) -> True
Zásobník: []

({[][<]>}()) -> False
Zásobník: ['(', '{', '[', '<'] - False
"""
""" v tomto pripade pouzivam zasobnik kdy vkladam leve zavorky a 
v pripade ze narazim pravou zavorku tak odstranim parovou levou. 
pokud jsou zavorky spatne skoncim na miste kde nelze odebirat """


def brackets2(word):
    stack = []
    for c in word:
        if c in "([{<":
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif c == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif c == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif c == '>':
            if len(stack) == 0 or stack.pop() != '<':
                return False
        print(stack)
    if len(stack) > 0:  # dulezite na konci nesmi zustat nic v zasobniku aby
        # mohl byt vysledek True
        return False
    return True


if __name__ == '__main__':
    words = ["()", "(())", "(()", ")(", "(()))((())", "((()())())"]
    for w in words:
        print(f"{w} -> {brackets(w)} -> {brackets2(w)}")

    words = ["([)]", "([])", "([][{}])", "({[]<[]>}())", "({[][<]>}())", ")}", "([)]"]
    for w in words:
        print(f"{w} -> {brackets2(w)}")
