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

# db = create_db_connection()
# client = MongoClient("mongodb://127.0.0.1:27017/")
#
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
#
# db = client["Food-Delivery"]
