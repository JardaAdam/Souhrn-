import re
# Task 6
# Napis funkciu, ktora dostane ako parameter string obsahujuci hashtagy z tweetu a vrati ich zoznam.
# Priklad:
# "Love the new features in #Python3! #coding #developer #regex"

def find_hashtags(text):
    return re.findall(r'#[^\s#]+', text)


if __name__ == "__main__":
    print(find_hashtags("# #a"))
    print(find_hashtags("Love the new features in #Python3.10! ## #coding #developer #regex"))
