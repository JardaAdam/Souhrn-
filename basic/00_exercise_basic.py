#variables and operators
#Task 1

#Given 1
number1 = 20
number2 = 30
print(number1*number2)


#Given 2
number1 = 40
number2 = 30
print(number1 + number2)

#Task 2
number = 23
print(number ** 4)

#Task 3
mam_hlad = True
mam_penize = True
mam_cas = False
print(mam_penize and mam_hlad)
print(mam_penize and mam_cas)
print(mam_penize or mam_cas)
print(mam_penize or mam_hlad)
print(not mam_hlad)
print(not mam_cas)


#Task 4

a = 10
b = 5
print(a / b)
print (a // b)
b = 4
print(a / b)
print(a // b)

#Utf8 compliance
#Task 1
#Zjistit, jaký znak reprezentuje v utf-8 pozice 128123.
print(chr(128123))    #👻

#Task 2
#Zakódovat do utf-8 řetězec “Nejneobhospodářovávatelnější” a znovu dekódovat.

text = "Nejneobhospodářovávatelnější"
encode_text = text.encode()
print(encode_text) # b'Nejneobhospod\xc3\xa1\xc5\x99ov\xc3\xa1vateln\xc4\x9bj\xc5\xa1\xc3\xad'
original_text = encode_text.decode()
print(original_text)   # Nejneobhospodářovávatelnější

# Task 3
#Převést číslo 255 na binární a hexadecimální podobu.
number = 255
print(bin(255))   #0b11111111
print(hex(255))   #0xff
# Task 4
#Najít binární reprezentaci čísla 169
print(bin(169))      #0b10101001
