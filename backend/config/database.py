from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Food-Delivery"]