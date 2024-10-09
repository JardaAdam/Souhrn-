class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


items = [Item(10, 60),
         Item(20, 100),
         Item(30, 120),
         Item(15, 70),
         Item(8, 45)]

capacity = 50


def sack(capacity, items):
    n = len(items)
    # Vytvoření 2D pole pro ukládání maximální hodnoty pro každou kombinaci kapacity a položek
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    # dp -> dinamicke programovani
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1].weight <= w:
                dp[i][w] = max(items[i-1].value + dp[i-1][w-items[i-1].weight], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


print(f"maximalni hodnota pro {capacity} v batohu je {sack(capacity, items)}")
