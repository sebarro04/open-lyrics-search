from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from decouple import config
import pipelines

mongodb_connection_string = config('MONGODB_URI')

class MongoDB:
    def __init__(self):
        self.client = MongoClient(mongodb_connection_string, server_api=ServerApi('1'))
        try:
            self.client.server_info()
            print('MongoDB connected')
        except Exception as ex:
            print(ex)
             
    def __del__(self):
        try:
            self.client.close()
        except Exception as ex:
            print(ex)

    def read_song_by_id(self, id: str) -> dict | Exception:
        try:
            collection = self.client['open_lyrics_search']['songs']
            query = { '_id': ObjectId(id) }
            result = collection.find_one(query)
            if result == {}:
                return result
            result['_id'] = str(result['_id'])
            return result
        except Exception as ex:
            print(ex)
            return Exception('Can not read the song by id')

    def songs_text_search(self, query: dict) -> dict:
        try:
            pipeline = pipelines.generate_search_pipeline(query)
            collection = self.client['open_lyrics_search']['songs']
            result = collection.aggregate(pipeline=pipeline)
            matched_songs = []
            for song in result:
                song['_id'] = str(song['_id'])
                matched_songs.append(song)
            return {'songs': matched_songs}
        except Exception as ex:
            print(ex)
            return Exception('Error doing the full text search in songs')
        
    def songs_text_search_facets(self, query: dict) -> dict:
        try:
            pipeline = pipelines.generate_search_meta_pipeline(query)
            collection = self.client['open_lyrics_search']['songs']
            result = collection.aggregate(pipeline=pipeline)
            facets = []
            for document in result:
                facets.append(document)
            print(facets)
            return {'facets': facets[0]}
        except Exception as ex:
            print(ex)
            return Exception('Error generating the facets over full text search in songs')


if __name__ == '__main__':
    mongodb = MongoDB()
    del mongodb
    