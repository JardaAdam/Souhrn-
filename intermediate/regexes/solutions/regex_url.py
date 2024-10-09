import re
# Task 4
# Napis funkciu, ktora vrati vsetky webove adresy zo stringu vo formate
# https://{hocico}<whitespace>
# alebo
# http://{hocico}<whitespace>
# Ak mas cas navyse, mozes si skusit napisat taky regex, ktory korektne validuje celu URL.

def find_urls_easy(text):
    return re.findall(r"https?://[A-Za-z0-9-]+\.[A-Za-z]{2,6}\s", text)


def find_urls(text):
    return [match.group() for match in re.finditer(r"(https?://)?(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})", text)]


if __name__ == "__main__":
    print(find_urls_easy("http://example.com nonsense asdf $@ https: https://asdf.jkl.cz test.com test"))
    print(find_urls("http://example.com nonsense asdf $@ https: https://asdf.jkl.cz test.com test"))
