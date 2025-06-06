from pymongo import MongoClient

def upload_to_mongodb(data, db_name='log_data', collection_name='user_history'):
    client = MongoClient('mongodb+srv://assassinken2:password@mydatabase1.g4l8k7x.mongodb.net/')
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(data)
    print(f"{len(data)} records uploaded to MongoDB collection '{collection_name}'.")
