"""Exercise 5

Write a class that will represent the magazine.
Storage capacity (float value reflecting cubic meters) is defined by the constructor.
Create a class that will reflect the product.
The product volume is defined by the constructor.
The magazine will have a method "add", which will take a Product object as its argument
and return the remaining free space, or -1 if you can't add a new item since it won't fit in the warehouse anymore.

Use fixture to prepare a set of products that flow into warehouses every month
and create tests that will check whether warehouses respond correctly to adding more products.
Accuracy should be implemented to two decimal places.
"""


class Product:
    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume


class Warehouse:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.products = []

    def __calculate_free_space(self):
        sum_od_products = sum([x.volume for x in self.products])
        return self.capacity - sum_od_products

    def add(self, *products: Product):
        for product in products:
            rest_space = self.__calculate_free_space()
            if rest_space >= product.volume:
                self.products.append(product)
                print(
                    f"Položka {product.name} byla přidána do skladu. Zbývající volné místo: {rest_space - product.volume}")
            else:
                print(f"Nedostatek místa pro položku {product.name}. Nemohla být přidána.")


if __name__ == "__main__":
    warehouse1 = Warehouse(100)

    karabina1 = Product("triplelock", 1)
    karabina2 = Product("twistlock", 1)
    smyce1 = Product("opensling", 1)
    smyce2 = Product("eye", 1)
    pulley1 = Product("single_pulley", 1)
    pulley2 = Product("double_pulley", 1)
    helmet1 = Product("work_helmet", 2)
    helmet2 = Product("climbing_helmet", 2)
    harness1 = Product("work_harness", 3)
    harness2 = Product("climbing_harness", 2)

    result = warehouse1.add(helmet1, helmet2, harness1)
