from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from decouple import config

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

    def generate_search_pipeline(self, text_search: str, *params):
        pipeline = [
            {
                '$search': {
                    'compound': {
                        'must': [
                        {
                            'text': {
                            'query': text_search,
                            'path': { 'wildcard': '*' }
                            }
                        }
                        ],
                        'filter': [
                        {
                            'text': {
                            'query': ['Rap'],
                            'path': 'artist.genres'
                            }
                        },
                        {
                            'text': {
                            'query': ['$uicideboy$'],
                            'path': 'artist.name'
                            }
                        }
                        ]
                    },
                    'highlight': {
                        'path': { 'wildcard': '*' }
                    }
                }
            }
        ]
        for param in params:
            pass
        
    # def search_songs(self):
    #     collection = self.client['open_lyrics_search']['songs']
        
    #     result = collection.aggregate(pipeline=pipeline)
    #     for document in result:
    #         print(document)
        
        
    def generate_facets(self, search: str, query: dict | None = None):
        collection = self.client['open_lyrics_search']['songs']
        pipeline = [
            {
                '$searchMeta': {
                    'facet': {
                        'facets': {
                            'artist_name': {
                                'type': 'string',
                                'path': 'artist.name'
                            },
                            'genres_facet': {
                                'type': 'string',
                                'path': 'artist.genres'
                            },
                            'popularity_facet': {
                                'type': 'number',
                                'path': 'artist.popularity',
                                'boundaries': [0, 50, 100, 150, 200],
                                'default': 'others'
                            },
                            'songs_facet': {
                                'type': 'number',
                                'path': 'artist.songs',
                                'boundaries': [0, 200, 400, 600, 800, 1000],
                                'default': 'others'
                            },
                            'language_facet': {
                                'type': 'string',
                                'path': 'language'
                            }
                        }
                    }
                }
            }                        
        ]
        result = collection.aggregate(pipeline=pipeline)
        for document in result:
            print(document)

    
if __name__ == '__main__':
    mongodb = MongoDB()
    #print(mongodb.read_song_by_id('6471c3de55b8c9931ee61e9b'))
    #mongodb.search_songs()
    pipeline = [
        {
            '$search': {
                'facet': {
                    'operator': {
                        'compound': {
                            'must': [
                            {
                                'phrase': {
                                    'query': 'Today',
                                    'path': { 'wildcard': '*' }
                                }
                            }
                            ],
                            'filter': [
                            {
                                'text': {
                                    'query': ['Rap', 'Rock'],
                                    'path': 'artist.genres'
                                }
                            },
                            {
                                'text': {
                                    'query': ['$uicideboy$', 'Slipknot'],
                                    'path': 'artist.name'
                                }
                            }
                            ]
                        }
                    },
                    'facets': {
                        'artist_name': {
                            'type': 'string',
                            'path': 'artist.name'
                        },
                        'genres_facet': {
                            'type': 'string',
                            'path': 'artist.genres'
                        },
                        'popularity_facet': {
                            'type': 'number',
                            'path': 'artist.popularity',
                            'boundaries': [0, 50, 100, 150, 200],
                            'default': 'others'
                        },
                        'songs_facet': {
                            'type': 'number',
                            'path': 'artist.songs',
                            'boundaries': [0, 200, 400, 600, 800, 1000],
                            'default': 'others'
                        },
                        'language_facet': {
                            'type': 'string',
                            'path': 'language'
                        }
                    }
                },
                'highlight': {
                    'path': { 'wildcard': '*' }
                }
            }
        }
    ]
    result = mongodb.client['open_lyrics_search']['songs'].aggregate(pipeline=pipeline)
    for i in result:
        print(i)
    del mongodb
    