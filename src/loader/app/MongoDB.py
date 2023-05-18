from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

class MongoDB:
    def __init__(self):
        try:
            connection_string = config('MONGO_CONNECTION_STRING')
            self.client = MongoClient(connection_string, server_api=ServerApi('1'))
            self.client.server_info()
            self.db = self.client['open_lyrics_search']
            print('MongoDB connected')
        except:
            print('Error connecting to MongoDB')

    def create_processed_archive(self, data: dict) -> str | None:
        try:
            collection = self.db['processed_archives']
            result = collection.insert_one(data)
            return str(result.inserted_id)
        except:
            print('Error creating the document in the processed archives collection')
            return None
        
    def create_songs(self, data: list[dict]) -> str | None:
        try:
            collection = self.db['songs']
            result = collection.insert_many(data)
            return str(result.inserted_ids)
        except:
            print('Error creating the songs in the collection songs')
            return None
        
    def read_processed_archives(self) -> list | None:
        try:
            collection = self.db['processed_archives']            
            result = collection.find()
            processed_archives = []
            for document in result:
                processed_archives.append(document)
            return processed_archives
        except:
            print('Error reading the processed archives')

if __name__ == '__main__':
    mongodb = MongoDB()