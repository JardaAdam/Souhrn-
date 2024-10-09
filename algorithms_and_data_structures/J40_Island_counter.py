"""Počet ostrovů
Máte dvourozměrné pole, kde 1 představuje zemi a 0 představuje vodu.
Napište funkci, která spočítá počet ostrovů.
Ostrov je souvislá oblast země, která je obklopena vodou a tvoří ji buňky,
které sousedí vodorovně nebo svisle."""


def number_of_islands(Grid):
    if not Grid:
        return 0

    rows, cols = len(Grid), len(Grid[0])
    island_count = 0

    def dfs(r, c):
        # Base condition to stop recursion if out of bounds or on water
        if r < 0 or c < 0 or r >= rows or c >= cols or Grid[r][c] == 0:
            return

        # Mark the cell as visited by setting it to 0
        Grid[r][c] = 0

        # Recursively call dfs on all adjacent cells
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for i in range(rows):
        for j in range(cols):
            if Grid[i][j] == 1:
                # Found an island, increment count and mark all its parts
                island_count += 1
                dfs(i, j)

    return island_count


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

print(f"Number if islands: {number_of_islands(grid)}")
