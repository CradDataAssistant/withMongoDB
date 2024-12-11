from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection URI
client = MongoClient("mongodb://192.168.0.18:27017/")

# Access the database and collection
db = client['Nikita']
collection = db['Test']

@app.route('/')
def index():
    # Fetch titles from MongoDB collection
    documents = collection.find()
    titles = [doc.get('Title') for doc in documents]  # Assuming 'title' field exists
    return render_template('index3.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)