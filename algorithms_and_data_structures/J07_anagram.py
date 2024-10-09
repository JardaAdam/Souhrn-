from typing import List
#Napište funkci, která najde všechny anagramy (přesmyčky) daného slova z uvedeného seznamu.
#Nalezená slova by měla být vrácena jako seznam.
#Co je to anagram? Jedná se o dvě různá slova, která se skládají ze stejných písmen.

def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    sorted_word = (sorted(word))
    return [w for w in lst_of_words if sorted(w) == sorted_word]
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))# => ['aabb', 'bbaa']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))# => ['carer', 'racer']

print(anagrams('laser', ['lazing', 'lazy', 'lacer']))# => []