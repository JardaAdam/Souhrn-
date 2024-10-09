import pymongo
# pip install pymongo
# vytvoření klienta
#mongo_client = pymongo.MongoClient("127.0.0.1", 27017)
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")  # pripojeni k serveru


# vytvoření databáze
mydb_test = mongo_client.test_db24
mydb = mongo_client["PythonRemoteCZ24"]    # pripojeni , vytvoreni database


if __name__ == '__main__':
    print(f"mongo_client: {mongo_client}")
    print(f"mydb_test24: {mydb_test}")
    print(f"mydb_pr24: {mydb}")

    databases = mongo_client.list_database_names()
    print(f"databases: {databases}")

    # Vytvoreni kolekce
    customers_collection = mydb["customers"]