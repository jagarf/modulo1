import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017, username='root', password='Cic1234*', authSource="admin")
db = client["todaslasnoticias"]
collection = db["data"]


app = Flask(__name__)

@app.route('/getData/<www_categoria>')
def getData(www_categoria):

    docs = collection.find({categoria:www_categoria})

    return jsonify(docs)

if __name__ == "__main__":
  app.run(host='localhost', port=5000, debug=True)