import unittest
from unittest.mock import MagicMock, patch
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from flask import Flask
import __init__
from MongoDB import MongoDB

""" class TestMongoDB(unittest.TestCase):
    def setUp(self):
        # Configurar un objeto Mock para MongoClient
        self.mock_client = MagicMock(MongoClient)
        self.mock_client.server_info.return_value = {}  # Simular conexión exitosa
        self.mock_client.close.return_value = None
        self.mock_db = self.mock_client['open_lyrics_search']
        self.mock_collection = self.mock_db['songs']
        self.mock_result = MagicMock()

    def test_read_song_by_id(self):
        # Configurar el objeto Mock para la colección y el resultado
        self.mock_collection.find_one.return_value = {'_id': ObjectId('6471c3de55b8c9931ee61e9b'), 'title': 'Lose Yourself'}
        
        # Crear una instancia de MongoDB con el cliente mock
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            song = mongodb.read_song_by_id('6471c3de55b8c9931ee61e9b')

            # Verificar que se haya llamado a los métodos y obtener los argumentos pasados
            self.mock_collection.find_one.assert_called_once_with({'_id': ObjectId('6471c3de55b8c9931ee61e9b')})

            # Verificar los resultados
            self.assertEqual(song, {'_id': '6471c3de55b8c9931ee61e9b', 'title': 'Lose Yourself'})

    def test_songs_text_search(self):
        # Configurar el objeto Mock para la colección y el resultado
        self.mock_collection.aggregate.return_value = self.mock_result
        self.mock_result.__iter__.return_value = [{'_id': ObjectId('6471c3de55b8c9931ee61e9b'), 'title':'Lose Yourself'}]

        # Crear una instancia de MongoDB con el cliente mock
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            result = mongodb.songs_text_search({'query': 'Love'})

            # Verificar que se haya llamado a los métodos y obtener los argumentos pasados
            self.mock_collection.aggregate.assert_called_once()

            # Verificar los resultados
            self.assertEqual(result, {'songs': [{'_id': '6471c3de55b8c9931ee61e9b', 'title':'Lose Yourself'}]})

    def test_songs_text_search_facets(self):
        # Configurar el objeto Mock para la colección y el resultado
        self.mock_collection.aggregate.return_value = self.mock_result
        self.mock_result.__iter__.return_value = [{'language': 'en'}]

        # Crear una instancia de MongoDB con el cliente mock
        with patch('MongoDB.MongoClient', return_value=self.mock_client):
            mongodb = MongoDB()
            result = mongodb.songs_text_search_facets({'query': 'search query'})

            # Verificar que se haya llamado a los métodos y obtener los argumentos pasados
            self.mock_collection.aggregate.assert_called_once()

            # Verificar los resultados
            self.assertEqual(result, {'facets': {'language': 'en'}}) """

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Open Lyrics Search')

    @patch('__init__.MongoDB')
    def test_songs_text_search(self, mock_mongodb):
        mock_mongodb_instance = MagicMock(MongoDB)
        mock_mongodb_instance.songs_text_search.return_value = {'songs': [{'title': 'Lose Yourself'}]}
        mock_mongodb.return_value = mock_mongodb_instance

        response = self.client.get('/open-lyrics-search/songs?search=query')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'songs': [{'title': 'Lose Yourself'}]})

        mock_mongodb_instance.songs_text_search.assert_called_once_with({'search': 'query'})

    @patch('__init__.MongoDB')
    def test_search_song_by_id(self, mock_mongodb):
        mock_mongodb_instance = MagicMock(MongoDB)
        mock_mongodb_instance.read_song_by_id.return_value = {'title': 'Lose Yourself'}
        mock_mongodb.return_value = mock_mongodb_instance

        response = self.client.get('/open-lyrics-search/songs/6471c3de55b8c9931ee61e9b')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'title': 'Lose Yourself'})

        mock_mongodb_instance.read_song_by_id.assert_called_once_with('6471c3de55b8c9931ee61e9b')

if __name__ == '__main__':
    unittest.main()

