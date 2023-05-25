import os  
from flask import Blueprint, Flask, jsonify
import search

SEARCH_BLUEPRINT = Blueprint('SEARCH_BLUEPRINT', __name__)

@SEARCH_BLUEPRINT.route('/openlyrics/search-song/<song_id>', methods = ['GET'])
def search_id(song_id):
    result = search.search_song__by_id(song_id)
    if isinstance(result, Exception):
        return 'Error with the database', 500 
    response = jsonify(str(result))
    # response = jsonify(result)
    response.status_code = 200
    return response