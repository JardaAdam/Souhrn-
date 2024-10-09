from collections import Counter
import re


def word_count(texts: str) -> int:
    """prevod textu na mala pismena"""
    texts = texts.lower()
    """pouziti regularniho vyrazu k extrakci slow"""
    words = re.findall(r'\b\w+\b', texts)
    """pocitani vyskytu jednotlivych slov pomoci Counteru"""
    word_freq = Counter(words)
    """celokovy pocet slov spocitam pomoci"""
    total_words = sum(word_freq.values())

    return total_words


if __name__ == "__main__":
    text = "tak schvalne jestli to bude fungovat"
    i = word_count(text)
    print("pocet slov:", i)
