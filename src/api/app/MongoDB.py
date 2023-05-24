
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://geraldnc88:GNCia2002#@cluster0.ibhh1cq.mongodb.net/", server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as exeption:
            print(exeption)

    # Try to close the connection 
    # def __del__(self):
    #     try:
    #         self.client.close()
    #     except Exception as ex:
    #         print(ex)

if __name__ == '__main__':
    db = MongoDB()