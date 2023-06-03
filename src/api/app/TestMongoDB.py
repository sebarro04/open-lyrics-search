import unittest
from unittest.mock import MagicMock, patch
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from flask import Flask
import __init__
from MongoDB import MongoDB

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock(MongoClient)
        self.mock_client.server_info.return_value = {}
        self.mock_client.close.return_value = None
        self.mock_db = self.mock_client['open_lyrics_search']
        self.mock_collection = self.mock_db['songs']
        self.mock_result = MagicMock()

    def test_read_song_by_id(self):
        self.mock_collection.find_one.return_value = {'_id': ObjectId('6471c3de55b8c9931ee61e9b'), 'title': 'Lose Yourself'}
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            song = mongodb.read_song_by_id('6471c3de55b8c9931ee61e9b')
            self.mock_collection.find_one.assert_called_once_with({'_id': ObjectId('6471c3de55b8c9931ee61e9b')})
            self.assertEqual(song, {'_id': '6471c3de55b8c9931ee61e9b', 'title': 'Lose Yourself'})

    def test_songs_text_search(self):
        self.mock_collection.aggregate.return_value = self.mock_result
        self.mock_result.__iter__.return_value = [{'_id': ObjectId('6471c3de55b8c9931ee61e9b'), 'title':'Lose Yourself'}]
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            result = mongodb.songs_text_search({'query': 'Love'})
            self.mock_collection.aggregate.assert_called_once()
            self.assertEqual(result, {'songs': [{'_id': '6471c3de55b8c9931ee61e9b', 'title':'Lose Yourself'}]})

    
    def test_songs_text_search_facets(self):
        self.mock_collection.aggregate.return_value = self.mock_result
        self.mock_result.__iter__.return_value = [{'language': 'en'}]
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            result = mongodb.songs_text_search_facets({'query': 'search query'})
            self.mock_collection.aggregate.assert_called_once()
            self.assertEqual(result, {'facets': {'language': 'en'}}) 


if __name__ == '__main__':
    unittest.main()

