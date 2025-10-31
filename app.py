from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # change to a real secret for production

@app.route('/')
def index():
    # Prepare a shuffled list of pairs
    numbers = [1,1,2,2,3,3,4,4]
    random.shuffle(numbers)
    session['numbers'] = numbers
    session['matched'] = []
    session['score'] = 0
    # pass enumerate(numbers) so template receives (idx, num)
    return render_template('game.html', numbers=list(enumerate(numbers)), score=0)

@app.route('/match', methods=['POST'])
def match():
    data = request.get_json() or {}
    try:
        idx1 = int(data.get('first', -1))
        idx2 = int(data.get('second', -1))
    except (ValueError, TypeError):
        return jsonify({'matched': False, 'score': session.get('score', 0)}), 400

    numbers = session.get('numbers', [])
    matched = session.get('matched', [])
    score = session.get('score', 0)
    res = {'matched': False, 'score': score}

    # validate indices
    if 0 <= idx1 < len(numbers) and 0 <= idx2 < len(numbers) and idx1 != idx2:
        if numbers[idx1] == numbers[idx2] and idx1 not in matched and idx2 not in matched:
            matched.extend([idx1, idx2])
            score += 1
            session['matched'] = matched
            session['score'] = score
            res['matched'] = True
            res['score'] = score

    return jsonify(res)

if __name__ == '__main__':
    # For local development only. In Docker/container, use host 0.0.0.0 as you had before.
    app.run(host='0.0.0.0', port=5000, debug=True)
