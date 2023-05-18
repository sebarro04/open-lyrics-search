from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

class MongoDB:
    def __init__(self):
        try:
            connection_string = config('MONGO_CONNECTION_STRING')
            self.client = MongoClient(connection_string, server_api=ServerApi('1'))
            self.client.server_info()
            print('MongoDB connected')
        except:
            print('Error connecting to MongoDB')

    #def 

if __name__ == '__main__':
    mongodb = MongoDB()