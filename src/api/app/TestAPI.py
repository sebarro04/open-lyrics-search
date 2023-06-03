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
    
    @mock.patch('MongoDB.MongoDB.songs_text_search')
    def test_songs_text_search(self, mock_songs_text_search):
        mock_songs_text_search.return_value = {'song': 'lyrics', 'facets': {'count': {'lowerBound': 2139}}}
        response = self.app.get('/open-lyrics-search/songs?search=test')
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()

