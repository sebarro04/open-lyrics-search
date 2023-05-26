from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from decouple import config

mongodb_connection_string = config("MONGODB_URI")

class MongoDB:
    def __init__(self):
        self.client = MongoClient(mongodb_connection_string, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as exeption:
            print(exeption)
             
    def __del__(self):
        try:
            self.client.close()
        except Exception as ex:
            print(ex)

    def read_song_by_id(self, id: str) -> int | Exception:
        try:
            collection = self.client['open_lyrics_search']['songs']
            query = { '_id': ObjectId(id) }
            result = collection.find_one(query)
            result['_id'] = str(result['_id'])
            return result
        except Exception as ex:
            print(ex)
            return Exception('Can not read the song by id')

if __name__ == '__main__':
    mongodb = MongoDB()
    del mongodb
    