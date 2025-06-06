
from src.extractor import extract_email_date_pairs
from src.mongodb_uploader import upload_to_mongodb
from src.sqlite_uploader import upload_to_sqlite
from src.analysis import run_queries
from pymongo import MongoClient
import os

log_file = "data/mbox.txt"
print(f"Checking if log file exists at: {log_file}")
print("Exists:", os.path.exists(log_file))

with open(log_file, 'r') as f:
    print("First 5 lines of mbox.txt:")
    for i in range(5):
        print(f.readline().strip())


if __name__ == "__main__":
    # Task 1 & 2: Extract and Transform
    log_file = "data/mbox.txt"
    cleaned_data = extract_email_date_pairs(log_file)

    # Task 3: Upload to MongoDB
    upload_to_mongodb(cleaned_data)

    # Task 4: Fetch from MongoDB and insert to SQLite
    client = MongoClient('mongodb+srv://assassinken2:password@mydatabase1.g4l8k7x.mongodb.net/')
    mongo_data = list(client['log_data']['user_history'].find({}, {'_id': 0}))
    upload_to_sqlite(mongo_data)

    # Task 5: Analysis
    run_queries()
