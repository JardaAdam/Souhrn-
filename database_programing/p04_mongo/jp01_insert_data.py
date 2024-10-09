from connect_mongo import mydb


mycol = mydb["test_collection"]

response = mycol.insert_one({"street_name": "Podzimni", "number": 5, "city": "Brno"})   # vlozeni jednoho zaznamu
""" radek = dokument (slovnik) """
print(response.inserted_id)