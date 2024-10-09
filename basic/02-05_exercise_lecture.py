# Task 1
# Given  1
# Vypsat číslo 1.23 jako procento
print("\nUkol1")
cislo = 1.25
print(f"{1.23: .2%}")           # 123.00%
# Given 2
# Bez proměnných vypočítat v f-formátu printu složitější výpočet. (9 * 25 + 47 / 65)
print("\nUkol2")
print(f"{9 * 25 + 47 / 65: .5}")      # 225.72
# Given 3
# Vytvořit si proměnné obsahující všechny datové typy (Str, Int, Float, Bool) a
# všechny je vypsat v jednom printu s f-formátem
print("\nUkol3")
Barva = "zelena"
Cislo = 23
Presne_cislo = 23.23
Rikam_jedine = True
print(f"{Barva} {Cislo} {Presne_cislo} {Rikam_jedine}")  # zelena 23 23.23 True

# Task 2

# Given 1
print("\nTask 2 \nGiven 1")

Jmeno = "James"

print(Jmeno[0::2])          # Jms

# Given 2
print("\nGiven 2")
s1 = "Ault"
s2 = "Kelly"
s3 = s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:] # prostredek stringu je 'len(s1) // 2'
print(s3)
print(s1[0:2], s2, s1[2:5], sep="")           # AuKellylt

# Given 3
print("\nGiven 3")
S1 = "America"
S2 = "Japan"
print(S1[0], S2[0], S1[3], S2[2], S1[-1], S2[-1], sep="")  # AJrpan

# Jednoducha kalkulacka
vstup1 = 10
vstup2 = 8
znamenko = "/"
print(f"{vstup1} / {vstup2} = {vstup1 / vstup2}")
