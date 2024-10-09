from connect_mongo import mydb

mycol = mydb["customers"]

myquery = {"surname": "Daniel"}
print(f"Vysledek dotazu: {myquery}")
for response in mycol.find(myquery):
    print(response)
mycol.delete_one(myquery)  # smaze jeden zaznam
# pro kontrolu vypiseme jeste jednou
for response in mycol.find(myquery):
    print(response)

print('-' * 80)
print("Smazeme vsechny zakazniky z Ostravy:")
myquery = {"address": {"$regex": "Ostrava"}}
for response in mycol.find(myquery):
    print(response)
response = mycol.delete_many(myquery)
print(f"Bylo smazano {response.deleted_count} zaznamu.")

print('-' * 80)
print("Smazeme vsechny zaznamy:")
response = mycol.delete_many({})
print(f"Bylo smazano {response.deleted_count} zaznamu.")  # delete_count pocita smazane zaznamy

print('-' * 80)
print("Databaze je prazdna:")
for response in mycol.find():
    print(response)

print('-' * 80)
print("Smazeme celou kolekci")
mycol.drop()  # smazeme celou kolekci
