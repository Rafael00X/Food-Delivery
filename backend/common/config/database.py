from pymongo import MongoClient


def create_db_connection(url: str, db_name: str):
    try:
        client = MongoClient(url)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client[db_name]
    except Exception as e:
        print(e)
        return None
