
from flask import Flask
from search_flask import SEARCH_BLUEPRINT

app = Flask(__name__)

app.register_blueprint(SEARCH_BLUEPRINT)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return 'Proyecto 02 - Bases De Datos 2'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)


""" 
client = pymongo.MongoClient("mongodb+srv://geraldnc88:GNCia2002#@cluster0.ibhh1cq.mongodb.net/") """
""" result = client['open_lyrics_search']['songs'].aggregate([
    {
        '$search': {
            'index': 'default',
            'text': {
                'query': "Fim de baile, fim de noite",
                'path': 'lyric'
            }
        }
    }, {
        '$limit': 5
    },
    {
        '$project': {
            '_id': 1,
            'song_name': 1,
            'lyric': 1
        }
    }
]) """
""" result = client['open_lyrics_search']['songs'].aggregate([
    {
        '$match': {
            '_id': ObjectId("646c1870246a303032cea3c5")
        }
    }
])


for i in result:

    print(i)
    print("\n"+"\n")

 """
