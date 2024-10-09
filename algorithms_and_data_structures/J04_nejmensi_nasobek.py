# def nsn(a, b):
#     i = max(a, b)
#     while True:
#         if i % a == 0 and i % b == 0:
#             return i
#         i += max(a, b)
#
# print(nsn(5, 12))


# dalsi reseni

def nsn(a, b):
    maximum = max(a, b)

    while True:
        print(maximum)
        if maximum % a == 0 and maximum % b == 0:
            return maximum

        maximum += max(a, b)

print(nsn(23, 50))

#TODO dodelat testy