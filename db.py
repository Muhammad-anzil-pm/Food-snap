import os

from pymongo import MongoClient
from dotenv import load_dotenv

class Food_data():
    def __init__(self):
        load_dotenv()
        self.mongo_url = os.getenv("mongo_url")
        self.db_name = os.getenv("db_name")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]
        self.food_list = self.db["food_list"]

    def finder(self,id):
        food = self.food_list.find_one({"class_id" : id}) 
        return food



