from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


if __name__ == '__main__':
    # Replace the placeholder with your Atlas connection string
    uri = "mongodb+srv://geraldnc88:GNCia2002#@cluster0.ibhh1cq.mongodb.net/"
    # Set the Stable API version when creating a new client
    client = MongoClient(uri, server_api=ServerApi('1'))
                            
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as exeption:
        print(exeption)