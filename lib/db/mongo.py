import pymongo


class MongoClient:
    def __init__(self, host="localhost", port=28000):
        self.mongo_client = pymongo.MongoClient(host=host, port=port)
        self.raw_document_table = self.mongo_client.db.raw_document_table

    def insert_raw_document(self, order_id, sub_code, file_name, text):
        insert_doc = {
            "_id": f"{order_id}::{sub_code}",
            "order_id": order_id,
            "sub_code": sub_code,
            "file_name": file_name,
            "text": text
        }
        if self.raw_document_table.find_one({"_id": insert_doc["_id"]}):
            return 1, f"order_id: {order_id}, sub_code: {sub_code} already exists"
        self.raw_document_table.insert_one(insert_doc)
        return 0, "succeed"

