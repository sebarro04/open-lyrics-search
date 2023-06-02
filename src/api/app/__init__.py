from flask import Flask, jsonify, request
import MongoDB

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return 'Open Lyrics Search'

@app.route('/open-lyrics-search/songs')
def songs_text_search():
    query = request.args.to_dict(flat=False)
    if 'search' not in query:
        response = jsonify('You must enter a text search')
        response.status_code = 400
        return response
    query['search'] = query['search'][0]
    if 'popularity' in query:
        if len(query['popularity']) != 2:
            response = jsonify('You must enter a popularity range')
            response.status_code = 400
            return response
        query['popularity'] = [float(x) for x in query['popularity']]
        query['popularity'].sort()
    if 'songs' in query:
        if len(query['songs']) != 2:
            response = jsonify('You must enter a songs range')
            response.status_code = 400
            return response
        query['songs'] = [int(x) for x in query['songs']]
        query['songs'].sort()
    print(query)
    mongodb = MongoDB.MongoDB()
    songs = mongodb.songs_text_search(query)
    if isinstance(songs, Exception):
        response = jsonify(str(songs))
        response.status_code = 500
        return response
    facets = mongodb.songs_text_search_facets(query)
    if isinstance(facets, Exception):
        response = jsonify(str(facets))
        response.status_code = 500
        return response
    result = songs | facets
    response = jsonify(result)
    response.status_code = 200
    return response

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

