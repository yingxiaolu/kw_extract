"""
Import textbook raw data in data/raw_data_textbook into MongoDB
"""
import os


def load_data():
    contents = []
    d = "./data/raw_data_textbook"
    for file in os.listdir(d):
        with open(os.path.join(d, file)) as fin:
            text = fin.read()
        contents.append({"file_name": file, "text": text})
    for i in range(len())