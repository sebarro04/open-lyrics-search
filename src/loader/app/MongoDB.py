from pymongo import MongoClient
from decouple import config

class MongoDB:
    def __init__(self):
        try:
            connection_string = config('MONGO_CONNECTION_STRING')
            self.client = MongoClient(connection_string)
            self.client.server_info()
            self.db = self.client['open_lyrics_search']
            print('MongoDB connected')
        except Exception as ex:
            print(f'Error connecting to MongoDB')
            raise

    def __del__(self):
        self.client.close()

    def create_processed_file(self, processed_file: dict) -> str | None:
        try:
            collection = self.db['processed_files']
            result = collection.insert_one(processed_file)
            return str(result.inserted_id)
        except Exception as ex:
            print(f'Error creating the processed files in the processed files collection: {ex}')
            return None
        
    def create_song(self, song: dict) -> str | None:
        try:
            collection = self.db['songs']
            result = collection.insert_one(song)
            return str(result.inserted_id)
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
    #mongodb.db['songs'].delete_many({'artist.name': {'$not': {'$eq': '$uicideboy$'}}})
    del mongodb