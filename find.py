import pymongo 

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['myfirstdb']
    collection = db['sampledata']
    

    one_data = collection.find_one({"_id": 1})
    print(one_data)
