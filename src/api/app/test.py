import unittest
from unittest.mock import MagicMock, patch
from bson import ObjectId
from pymongo.mongo_client import MongoClient

# Importar la clase MongoDB desde el archivo MongoDB.py
from MongoDB import MongoDB

class TestMongoDB(unittest.TestCase):
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
            self.assertEqual(result, {'facets': {'language': 'en'}})

if __name__ == '__main__':
    unittest.main()

