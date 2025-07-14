from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Load mock movie data
def load_movies():
    with open(os.path.join('data', 'movies.json'), 'r') as f:
        return json.load(f)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the DevFlix Catalogue Service. Visit /movies to see the list."})

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = load_movies()
    return jsonify(movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
