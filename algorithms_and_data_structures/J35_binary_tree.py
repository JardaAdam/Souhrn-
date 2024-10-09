from collections import deque


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:  # kdyz je hodnota mensi nez aktualni hodnota
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryTree(value)
        elif value > self.value:  # kdyz je hodnota vetsi nez aktualni hodnota
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryTree(value)

    def find(self, value) -> bool:
        """find
        :param value = hledana hodnota
        :return True pokud je hodnota v binarnim strome
        """
        if self.value == value:
            return True
        if self.left and value < self.value:
            return self.left.find(value)
        elif self.right and value > self.value:
            return self.right.find(value)
        return False

    def deep(self):
        """
        Vrati hloubku daneho stromu
        :return: hloubka
        """
        left_deep = 0
        if self.left:
            left_deep = self.left.deep()
        right_deep = 0
        if self.right:
            right_deep = self.right.deep()
        return 1 + max(left_deep, right_deep)

    # TODO projit a pochopit funkce nize
    """ 
    Homework:
    Napište metody, které provedou průchod binárním stromem v 
    - preorder, 
    - inorder,
    - postorder a
    - level order pořadí a vrátí seznam.
    """

    # Pre-order traversal (Kořen -> Levá větev -> Pravá větev)
    def preorder(self):
        """Pre-order průchod stromem. Nejprve navštívíme kořen, poté levý podstrom a nakonec pravý podstrom.
        :return: seznam hodnot v pre-order pořadí
        """
        result = [self.value]  # Začínáme s hodnotou aktuálního uzlu (kořene)
        if self.left:
            result += self.left.preorder()  # Rekurzivně přidáme levý podstrom
        if self.right:
            result += self.right.preorder()  # Rekurzivně přidáme pravý podstrom
        return result

    # In-order traversal (Levá větev -> Kořen -> Pravá větev)
    def inorder(self):
        """
        In-order průchod stromem. Nejprve navštívíme levý podstrom, poté kořen a nakonec pravý podstrom.
        :return: seznam hodnot v in-order pořadí
        """
        result = []
        if self.left:
            result += self.left.inorder()  # Rekurzivně přidáme levý podstrom
        result.append(self.value)  # Přidáme kořen
        if self.right:
            result += self.right.inorder()  # Rekurzivně přidáme pravý podstrom
        return result

        # Post-order traversal (Levá větev -> Pravá větev -> Kořen)

    def postorder(self):
        """
        Post-order průchod stromem. Nejprve navštívíme levý podstrom, poté pravý podstrom a nakonec kořen.
        :return: seznam hodnot v post-order pořadí
        """
        result = []
        if self.left:
            result += self.left.postorder()  # Rekurzivně přidáme levý podstrom
        if self.right:
            result += self.right.postorder()  # Rekurzivně přidáme pravý podstrom
        result.append(self.value)  # Přidáme kořen
        return result

        # Level-order traversal (průchod po vrstvách, tedy úroveň po úrovni)

    def level_order(self):
        """
        Level-order průchod stromem. Průchod po jednotlivých úrovních stromu pomocí fronty.
        :return: seznam hodnot v level-order pořadí
        """
        result = []
        queue = deque([self])  # Vytvoříme frontu a přidáme do ní kořen
        while queue:
            node = queue.popleft()  # Odebereme první prvek z fronty
            result.append(node.value)  # Přidáme hodnotu uzlu do výsledku
            if node.left:
                queue.append(node.left)  # Pokud existuje levý podstrom, přidáme ho do fronty
            if node.right:
                queue.append(node.right)  # Pokud existuje pravý podstrom, přidáme ho do fronty
        return result


# TODO doladit tuto funkci podle lektora
# funkce pro vypis stromu
    def __str__(self):
        result = str(self.value) + ', '
        result +=str(self.left) + ', '
        result +=str(self.right) + ', '
        return result


if __name__ == '__main__':
    # polopate popsany prubeh vytvareni stromu
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(7)
    root.left.left.left = BinaryTree(1)
    root.left.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(8)
    root.right = BinaryTree(12)
    # bezne vytvoreni BinaryTree

    binary_tree = BinaryTree(10)
    numbers = [10, 5, 3, 12, 11, 7, 15, 4, 8, 1]
    for number in numbers:
        binary_tree.add(number)
    print(binary_tree)

    for number in range(1, 20):
        print(f"{number} -> {binary_tree.find(number)}")

    binary_tree2 = BinaryTree(10)
    print(f"binary_tree has deep {binary_tree.deep()}")
    print(f"binary_tree2 has deep {binary_tree2.deep()}")

    numbers = range(1, 20)
    binary_tree3 = BinaryTree(0)
    for number in numbers:
        binary_tree3.add(number)
    print(f"binary_tree3 has deep {binary_tree3.deep()}")

    print(f"binary_tree.inorder(): {binary_tree.inorder()}")
    print(f"binary_tree.preorder(): {binary_tree.preorder()}")
    print(f"binary_tree.postorder(): {binary_tree.postorder()}")
    print(f"binary_tree.level_order(): {binary_tree.level_order()}")

    # TODO video 22/08/2024 3:05:45 pokracovani vysvetleni binarnich stromu
