import unittest
from unittest import mock
from flask import Flask, jsonify
from __init__ import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('MongoDB.MongoDB.read_song_by_id')
    def test_search_song_by_id(self, mock_read_song_by_id):
        mock_read_song_by_id.return_value = {'song': 'lyrics'}
        response = self.app.get('/open-lyrics-search/songs/6471c3de55b8c9931ee61e9b')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'song': 'lyrics'})
        mock_read_song_by_id.assert_called_once_with('6471c3de55b8c9931ee61e9b')
    
    

if __name__ == '__main__':
    unittest.main()

