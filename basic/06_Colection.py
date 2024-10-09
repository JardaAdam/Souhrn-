

# TODO List-
# v prubehu programu se meni obsah

abeceda = ["a"]

abeceda.append("b")
abeceda.append("c")
print(abeceda)                       # ['a', 'b', 'c']



abeceda.extend(["z","p","v"])
print(abeceda)                      # ['a', 'b', 'c', 'z', 'p', 'v']


print("sorted")
print(sorted(abeceda))              # ['a', 'b', 'c', 'p', 'v', 'z']
print(abeceda)                      # ['a', 'b', 'c', 'z', 'p', 'v']


abeceda.sort()
print(abeceda)                      # ['a', 'b', 'c', 'p', 'v', 'z']

print(abeceda.count(True))          # 0

print(abeceda.index("z"))           # 5
abeceda.insert(3,False)
print(abeceda)              # ['a', 'b', 'c', False, 'p', 'v', 'z']

#pop

abeceda.pop(3)
print(abeceda)              # ['a', 'b', 'c', 'p', 'v', 'z']
abeceda.pop()
print(abeceda)              # ['a', 'b', 'c', 'p', 'v', 'z']

abeceda.remove("v")
print(abeceda)

abeceda.reverse()
print(abeceda)

abeceda.clear()
print(abeceda)


"""tu jsem zkoncil """
users = ["Alice", "Honza" , "Tereza", "Vasek"]
print(users)            # ['Alice', 'honza', 'Tereza', 'Vasek']
print(users[0:3])          # ['Alice', 'honza', 'Tereza']
print(users[1:2])           # ['Honza']
print(users[2])             # Tereza
print(users[1:])            # ['Honza', 'Tereza', 'Vasek']

# list listu
matice_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(matice_2d)        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matice_2d[1])     # [4, 5, 6]
print(matice_2d[1][0])  # 4

# Slovnik Dictionary- (Dict)


phonebook = {"Honza" : 12345,
             "Marek" : 67890,
             "deda" : 98765}
print(phonebook)            # {'Honza': 12345, 'Marek': 67890, 'deda': 98765}
phonebook["Adela"] = 23456
print(phonebook)    # {'Honza': 12345, 'Marek': 67890, 'deda': 98765, 'Adela': 23456}
print(phonebook["Adela"])       # 23456
phonebook.pop("Honza")
print(phonebook)        # {'Marek': 67890, 'deda': 98765, 'Adela': 23456}
del phonebook["Adela"]
print(phonebook)        # {'Marek': 67890, 'deda': 98765}
print(phonebook.get("Honza", "nenasel jsem ho"))

phonebook.items()
print(phonebook)

# TODO N-tice (tuple) () neprepsatelny list


tupple3 = (2,5,8,7,)

w,x,y,z = tupple3
print(tupple3)

# TODO Mnozina (set)  {}  data kde nas nezajima duplicitni ( stejne) hodnoty
# neidentifikovatelne a neusporadane kolekce

animals = {"pes", "kocka","slon"}
animals.add("mys")
print(animals)

animals.update(["tygr","lev","zirafa"])
print(animals)

print(len(animals))


