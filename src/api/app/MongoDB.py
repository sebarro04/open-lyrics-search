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

    def read_song_by_id(self, id: str) -> dict | Exception:
        try:
            collection = self.client['open_lyrics_search']['songs']
            query = { '_id': ObjectId(id) }
            result = collection.find_one(query)
            result['_id'] = str(result['_id'])
            return result
        except Exception as ex:
            print(ex)
            return Exception('Can not read the song by id')
    
    def search_songs(self, query: list) -> list | Exception:
        try:
            term_to_search = query[0]
            filters = ["artist.genres", "artist.name"]
            pipeline = [
                            {
                                '$search': {
                                    'index': 'test', 
                                    'compound': {
                                        'must': [
                                            {
                                                'text': {
                                                    'query': term_to_search, 
                                                    'path': 'lyric'
                                                }
                                            }
                                        ], 
                                        'filter': [
                                            
                                        ]
                                    }, 
                                    'highlight': {
                                        'path': {
                                            'wildcard': '*'
                                        }
                                    }
                                }
                            },
                            {
                                '$project': {
                                    '_id': 1, 
                                    'song_name': 1, 
                                    'highlights': {
                                        '$meta': 'searchHighlights'
                                    }
                                }
                            }
                        ]
            position = 0
            for i in filters:
                if query[position + 1] == "null":
                    position = position + 1
                else: 
                    pipeline[0]["$search"]["compound"]["filter"].append({
                        "text": {
                            "query": query[position + 1],
                            "path": filters[position],
                        },
                    })
                    position = position + 1
            collection = self.client['open_lyrics_search']['songs']
            result = collection.aggregate(pipeline)
            return result
        except Exception as ex:
            print(ex)
            return ex
    
if __name__ == '__main__':
    mongodb = MongoDB()
    list = mongodb.search_songs(["full metal jacket kinda heavy", "Rap", "$uicideboy$"])
    for doc in list:
        print (doc)
        print ("\n")
    del mongodb
    