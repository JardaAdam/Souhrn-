import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

# 1.factorial
n = int(input("Enter positive number: "))

i = 1
s = 1

while i <= n:
    s = s * i
    i = i +1

print(f"{n}! = {s}")

#TODO prepsat na forciclus

if __name__ == '__main__':
    unittest.main()
#TODO dodelat testy