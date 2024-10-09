""" Problém osmi dam
Problém osmi dam je šachová úloha, respektive kombinatorický problém umístit na šachovnici osm dam tak,
aby se podle pravidel šachu navzájem neohrožovaly, tedy vybrat osm polí tak, aby žádná dvě nebyla ve stejné řadě,
sloupci, ani diagonální linii. Obecněji jde o to nalézt všechna možná taková rozmístění nebo určit jejich počet.
"""
# urcit pocet reseni pro 8 dam
#chess = [[0] * 8] * 8


"""def print_chess(ch):
    for row in chess:
        print(row)
"""

"""
def is_save(arr, row, col):
    for i in range(row):
        if arr[i] == col or arr[i] - i == col - row or arr[i] + i == col + row:
            return False
    return True


def solve_count(ch, row):
    if row == 8:
        return 1
    n_solution = 0
    for col in range(8):
        if is_save(ch, row, col):
            ch[row] = col
            n_solution += solve_count(ch, row+1)
    return n_solution


def queens_eight():
    chess = [0] * 8
    return solve_count(chess, 0)


print(f"Počet řešení problému pro 8 dam je {queens_eight()}")
"""


# řešení pro n dam
def is_save(arr, row, col):
    for i in range(row):
        if arr[i] == col or arr[i] - i == col - row or arr[i] + i == col + row:
            return False
    return True


def solve_count(ch, row, n):
    if row == n:
        return 1
    n_solution = 0
    for col in range(n):
        if is_save(ch, row, col):
            ch[row] = col
            n_solution += solve_count(ch, row+1, n)
    return n_solution


def queens_eight():
    chess = [0] * n
    return solve_count(chess, 0)



def queens_n(n):
    chess = [0] * n
    return solve_count(chess, 0, n)

for i in range(4,15):
    print(f"Pocet reseni pro problem {i} dam je {queens_n(i)} ")
