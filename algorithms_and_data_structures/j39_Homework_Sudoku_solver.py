"""Sudoku Solver
Máte částečně vyplněnou mřížku Sudoku o velikosti 9x9.
Napište program, který tuto mřížku vyplní tak, aby byly splněny všechny pravidla Sudoku
(čísla 1-9 se v žádném řádku, sloupci ani 3x3 boxu neopakují)."""
# TODO dodelat

def solve_sudoku(board):
    pass


def print_sudoku(board):
    pass


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print_sudoku(board)
else:
    print("No solution for this sudoku.")
