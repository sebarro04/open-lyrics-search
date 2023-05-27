from flask import Flask, jsonify, request
import MongoDB

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return 'Open Lyrics Search'

@app.route('/open-lyrics-search/songs')
def song_search_text():
    search = request.args.get('search', None)
    if search == None:
        response = jsonify('You must enter a text search')
        response.status_code = 400
        return response
    artists = request.args.getlist('artist')
    genres = request.args.getlist('genre')
    popularity = request.args.getlist('popularity')
    songs = request.args.getlist('songs')
    return 'Songs search'

@app.route('/open-lyrics-search/songs/<string:id>', methods=['GET'])
def search_song_by_id(id: str):
    mongodb = MongoDB.MongoDB()
    result = mongodb.read_song_by_id(id)
    if isinstance(result, Exception):
        response = jsonify(str(result))
        response.status_code = 500
        return response
    response = jsonify(result)
    response.status_code = 200
    return response
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)

