"""
Import textbook raw data in data/raw_data_textbook into MongoDB
"""
import os
import sys
sys.path.append("./")
from lib.db.mongo import MongoClient


def load_data():
    contents = []
    d = "./data/raw_data_textbook"
    for file in os.listdir(d):
        with open(os.path.join(d, file)) as fin:
            text = fin.read()
        contents.append({"file_name": file, "text": text})
    for i in range(len(contents)):
        contents[i]["order_id"] = f"textbook_{i}"
        contents[i]["sub_code"] = 0
    return contents


def import_data():
    mongo_client = MongoClient()
    for content in load_data():
        status, msg = mongo_client.insert_raw_document(**content)
        if status != 0:
            print(status, msg)


def check_data():
    mongo_client = MongoClient()
    for content in mongo_client.raw_document_table.find():
        print(content)
        break


if __name__ == '__main__':
    check_data()
