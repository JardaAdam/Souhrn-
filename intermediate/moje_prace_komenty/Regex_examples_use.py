# Regulární výrazy
# Regulární výrazy jsou vzory, které popisují řetězce symbolů. Můžeme například vytvořit výraz, který bude odpovídat
# libovolné e-mailové adrese, libovolnému datu, telefonnímu číslu nebo číslu kreditní karty atd.

#V jazyce Python potřebujeme pro práci s regulárními výrazy modul re. Tento modul nám pomůže vyhledat v textu
# řetězce odpovídající vzoru nebo zkontrolovat, zda daný text přesně odpovídá danému vzoru.
# TODO jako prvni import!!
import re

# TODO Funkce search (vyhledej)
# Funkce přijímá dva argumenty, prvním je regulární výraz a druhým text, ve kterém hledáme řetězec odpovídající
# regulárnímu výrazu. Vrací objekt Match, který obsahuje informaci o tom, který řetězec byl nalezen a kde se nachází,
# nebo objekt None, pokud nebyl nalezen žádný odpovídající řetězec.

print(re.search(r"[A-Z]la", "ala Ola Ela"))

# vypis = <_sre.SRE_Match object; span=(4, 7), match='Ola'>


# TODO Funkce match (vyhledej na začátku)
# Tato funkce přijímá přesně stejné parametry jako funkce search. Rozdíl je v tom, že match vám řekne, zda výrazu
# odpovídá začátek textu, nikoliv jen jeho část.

print(re.match(r"[A-Z]la", "ala Ola Ela"))

# vypis =  None

# TODO Funkce fullmatch (vyhledej úplnou shodu)

# Tato funkce slouží k vyhledání výskytů, které přesně odpovídají zadanému vzoru. Jinými slovy
# - řetězec musí přesně odpovídat hledanému vzoru.

print(re.fullmatch(r"[A-Z]la", "Ela"))

# vypis = <_sre.SRE_Match object; span=(0, 3), match='Ela'>


# TODO Funkce findall (vyhledej všechny)
# Funkce vrátí všechny shody se vzorem z textu.

print(re.findall(r".la", "Ola ala Ela"))

# vypis = ['Ola', 'ala', 'Ela']

# TODO Funkce finditer
# Tato funkce funguje podobně jako findall, ale vrací iterátor, který umožňuje přistupovat k po sobě
# jdoucím položkám při jejich postupném procházení.

iter = re.finditer(r".la", "Ola ala Ela")
for elem in iter:
    print(elem)

#iter = re.finditer(r".la", "Ola ala Ela")
for elem in iter:
    print(elem)
# vypis =
# <_sre.SRE_Match object; span=(0, 3), match='Ola'>
# <_sre.SRE_Match object; span=(4, 7), match='ala'>
# <_sre.SRE_Match object; span=(8, 11), match='Ela'>


# TODO Funkce split (rozděl)
# Funkce split z modulu re pracuje podobně jako funkce split z modulu os s tím rozdílem, že zde můžeme zadat
# regulární výraz, podle kterého řetězec rozdělíme.


print(re.split(r",|\.", "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"))

# vypis = ['jablko', 'hruška', 'hrozny', 'mrkev', 'zelí', 'zelenina', 'ovoce', 'dvůr']

# TODO Funkce sub
#Funkce převede všechny řetězce popsané regulárním výrazem na zadaný řetězec.

print(re.sub(r"[a-z]{5}", "pes", "Alice má slona"))

# vypis = Alice má psa

# TODO Funkce subn
# Funkce funguje stejně jako sub, ale navíc vrací informaci o počtu provedených substitucí.

print(re.sub(r"[a-z]{5}", "pes", "Alice má slona"))

# vypis = ('Alice má psa', 1)

# TODO Seskupování
# Regulární výrazy mohou také extrahovat zajímavé části textu. K tomu se používá seskupování, tj. fragmenty vzorů
# zabalené do závorek.
print("seskpovani")


if __name__ == "__main__":
    text = "Thomas W. (33), last seen in Krakow"
    pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+)\)"
    match = re.search(pattern, text)
    print(match)
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

    text = "Thomas (33) i Eva (24) agreed to go shopping together tomorrow"
    pattern = r"([A-Z]{1}[a-z]+) \((\d+)\)"
    print(re.findall(pattern, text))

# vypis =
# <re.Match object; span=(0, 17), match='Thomas W. (33)'>
# ('Thomas W.', '33')
# Thomas W. (33)
# Thomas W.
# 33
# [('Thomas', '33'), ('Eva', '24')]
