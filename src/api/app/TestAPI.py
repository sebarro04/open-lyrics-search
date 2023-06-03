import unittest
from unittest import mock
from flask import Flask, jsonify
from __init__ import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    '''@mock.patch('MongoDB.MongoDB.read_song_by_id')
    def test_search_song_by_id(self, mock_read_song_by_id):
        mock_read_song_by_id.return_value = {'song': 'lyrics'}
        self.app.get('/open-lyrics-search/songs/6471c3de55b8c9931ee61e9b')
        mock_read_song_by_id.assert_called_once_with('6471c3de55b8c9931ee61e9b')
    
    @mock.patch('MongoDB.MongoDB.songs_text_search')
    def test_songs_text_search(self, mock_songs_text_search):
        mock_songs_text_search.return_value = {'song1': 'Lyric1'}
        self.app.get('/open-lyrics-search/songs?search=love')
        mock_songs_text_search.assert_called_one_with({'search': 'love'})'''


if __name__ == '__main__':
    unittest.main()

