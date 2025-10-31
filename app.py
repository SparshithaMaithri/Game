from flask import Flask, render_template, request, session, jsonify # type: ignore
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Start a new game: list with pairs of numbers, randomized
    numbers = [1, 1, 2, 2, 3, 3, 4, 4]
    random.shuffle(numbers)
    session['numbers'] = numbers
    session['matched'] = []
    session['score'] = 0
    return render_template('game.html', numbers=enumerate(numbers), score=0)

@app.route('/match', methods=['POST'])
def match():
    data = request.get_json()
    idx1 = int(data['first'])
    idx2 = int(data['second'])
    numbers = session.get('numbers')
    matched = session.get('matched', [])
    score = session.get('score', 0)
    res = {'matched': False, 'score': score}
    if numbers[idx1] == numbers[idx2] and idx1 != idx2 and idx1 not in matched and idx2 not in matched:
        matched.extend([idx1, idx2])
        score += 1
        res['matched'] = True
        session['matched'] = matched
        session['score'] = score
        res['score'] = score
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
