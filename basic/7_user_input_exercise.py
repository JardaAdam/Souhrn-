#1 Accept numbers from a user
"""Write a program to accept two numbers from the user and calculate multiplication"""

# print("Ahoj zadej cisla do kalkulacky")
# a = int(input("zadej a:"))
# b = int(input("zadej b:"))
# print(f"tvuj vysledek je:{a * b}")

"""2 Display three string “Name”, “Is”, “James” (which you obtain from program argument)
# as “Name**Is**James” 
# Use the print() function to format the given words in the mentioned format.
# Display the ** separator between each string.
# Expected Output:
# For example: python myprogram Name Is James will display Name**Is**James"""
# TODO vsechno co tu delam delam v terminalu!!
"""zacnu tim ze si napisu data za tuto slozku v prikazovem radku a spustim to entrem"""
# import sys
# print(sys.argv)
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# arg3 = sys.argv[3]
# print(arg1, arg2, arg3, sep="**")


# TODO 3 Accept any three string from one input() call
"""Write a program to take three names as input from a user in the single input() function call.
Expected Output:
Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
"""

name1, name2, name3 = input("zadej tri jmena:").split()
print(f"jmeno1: {name1}")
print(f"jmeno2: {name2}")
print(f"jmeno3: {name3}")