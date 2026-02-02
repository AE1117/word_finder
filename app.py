from flask import Flask, render_template, jsonify
from generator import get_puzzle_data
from word_finder import find_childs, find_parent
import json
import os

LEVEL_FILE = 'database/level.json'

# Generating level file
def get_level():
    if not os.path.exists(LEVEL_FILE): return 1
    with open(LEVEL_FILE, 'r') as f:
        return json.load(f).get('level', 1)

# Updating level data
def increment_level():
    level = get_level()
    with open(LEVEL_FILE, 'w') as f:
        json.dump({'level': level + 1}, f)

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    data = {"words": []}

    # If there is less than five words, code keep searching for it
    while not data.get("words") or len(data.get("words")) < 5:
        # Finding words
        words_list, letters_list = find_childs(find_parent())
        print(words_list)
        # Generating map with words
        data = get_puzzle_data(words_list, letters_list)

    data['level_number'] = get_level()
    return render_template('game.html', data=data)


@app.route('/api/next-level', methods=['POST'])
def next_level():
    increment_level()
    return jsonify({"success": True})


if __name__ == '__main__':

    app.run(debug=True, port=5000)
