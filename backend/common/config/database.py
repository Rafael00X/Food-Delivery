from pymongo import MongoClient

url = "mongodb://127.0.0.1:27017/"
db_name = "Food-Delivery"

def create_db_connection():
    try:
        client = MongoClient(url)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client[db_name]
    except Exception as e:
        print(e)
        return None
