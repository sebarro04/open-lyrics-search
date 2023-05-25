
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

