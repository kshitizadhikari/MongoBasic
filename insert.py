import pymongo 

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['myfirstdb']
    collection = db['sampledata']
    data = {
        "name": "ram",
        "age": 12
    }

    multiple_data = [
        {"name": "sam", "age": 13},
        {"name": "dam", "age": 53},
        {"name": "ham", "age": 24},
        {"name": "bam", "age": 32},
    ]

    data_with_custom_id = {
        "_id": 1,
        "name": "bobobo",
        "age": 89
    }

    # collection.insert_one(data_with_custom_id)
    # collection.insert_many(multiple_data)
