"""
Factorial:
5! = 5*4*3*2*1
0! = 1
1! = 1
2! = 2*1 = 2
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120
...
"""


def fact(n: int) -> int:
	if n < 0:
		raise ValueError
	if n == 0 or n == 1:
		return 1
	result = 1
	for i in range(2, n+1):
		result *= i
	return result



"""
Rekurzivní verze faktoriálu:
5! = 5*4!
4! = 4*3!
3! = 3*2!
2! = 2*1!
1! = 1
"""

# nevyhoda narocnost na pamet v mezipameti zustavaji vsechny predchozi Fact
def fact_r(n: int) -> int:
	print(f"Počítám faktoriál pro číslo {n}")  # radek ktery demonstruje jak pocita tato funkce
	if n < 0:
		raise ValueError
	if n == 0 or n == 1:
		return 1
	return n * fact_r(n-1)
# postup vypoctu n = 5        5 * 24 (fac_r(4))-> 120
#                             4 * 6  (fac_r(3))
#                             3 * 2  (fac_r(2))
#                             2 * 1  (fac_r(1))


if __name__ == '__main__':
	for i in range(10):
		print(f"{i}! = {fact(i)} = {fact_r(i)}")