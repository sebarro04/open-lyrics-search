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
        except Exception as ex:
            print(f'Error connecting to MongoDB')
            raise

    def __del__(self):
        self.client.close()

    def create_processed_files(self, processed_files: list[dict]) -> list | None:
        try:
            collection = self.db['processed_files']
            result = collection.insert_many(processed_files, ordered=False)
            return result.inserted_ids
        except Exception as ex:
            print(f'Error creating the processed files in the processed files collection: {ex}')
            return None
        
    def create_songs(self, songs: list[dict]) -> list | None:
        try:
            collection = self.db['songs']
            result = collection.insert_many(songs, ordered=False)
            return result.inserted_ids
        except Exception as ex:
            print(f'Error creating the song in the collection songs: {ex}')
            return None
        
    def read_processed_files(self) -> list[str] | None:
        try:
            collection = self.db['processed_files']            
            result = collection.find()
            processed_files = []
            for document in result:
                processed_files.append(document['filename'])
            return processed_files
        except Exception as ex:
            print(f'Error reading the processed files: {ex}')
            return None

if __name__ == '__main__':
    mongodb = MongoDB()
    del mongodb