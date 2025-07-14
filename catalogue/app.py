import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

def load_movies():
    # Always resolve path relative to app.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'data', 'movies.json')
    with open(data_path, 'r') as f:
        return json.load(f)

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = load_movies()
    return jsonify(movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
