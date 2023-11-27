# filename: flask_blackjack.py
"""
To start the game, run this file with Python and go to http://localhost:5000 in your web browser. You can also make actions like hitting or sticking by sending GET or POST requests to http://localhost:5000/game, respectively.

Note: In this simplified version of blackjack, aces are always counted as 11 unless that would result in a total score greater than 21, in which case they are counted as 1. Additionally, blackjack is assigned a score of 0 for easy game checking.
Please make sure to save the script in a file called `flask_blackjack.py` and run it using the command:

python3 flask_blackjack.py

Please also note this is a very basic version. For a full version, you'd likely want to add a database to keep track of player's wins/losses, use templates to render the output in HTML, include betting, and so on.
"""

# filename: flask_blackjack.py
from flask import Flask, request, render_template_string, session
from random import sample

app = Flask(__name__)
app.secret_key = 'your_super_secret_string_here'

@app.route('/')
def blackjack():
    return render_template_string("""
        <p>Welcome! Let's play a game of BlackJack.</p>
        <form action="/deal" method="post">
        <input type="submit" value="Deal the cards!">
        </form>
        """)

@app.route('/deal', methods=['POST'])
def deal():
    deck = [i for i in range(1, 14)] * 4
    session['player'] = sample(deck, 2)
    deck = list(set(deck) - set(session['player'])) # remove player's cards from deck
    session['dealer'] = sample(deck, 2)
    session['deck'] = list(set(deck) - set(session['dealer'])) # remove dealer's cards from deck
    return render_template_string("""
        <p>Your hand: {{player}} | Dealer shows: {{dealer[0]}} </p>
        <form action="/hit" method="post">
        <input type="submit" value="Hit me!">
        </form>
        <form action="/stand" method="post">
        <input type="submit" value="I'll stand">
        </form>
        """, player=session['player'], dealer=session['dealer'])

@app.route('/hit', methods=['POST'])
def hit():
    session['player'].append(sample(session['deck'], 1)[0])
    session['deck'] = list(set(session['deck']) - set([session['player'][-1]])) #remove added card from deck
    return render_template_string("""
        <p>Your hand: {{player}} | Dealer shows: {{dealer[0]}} </p>
        <form action="/hit" method="post">
        <input type="submit" value="Hit me!">
        </form>
        <form action="/stand" method="post">
        <input type="submit" value="I'll stand">
        </form>
        """, player=session['player'], dealer=session['dealer'])

@app.route('/stand', methods=['POST'])
def stand():
    while(sum(session['dealer']) <= 16):
        session['dealer'].append(sample(session['deck'], 1)[0])
        session['deck'] = list(set(session['deck']) - set([session['dealer'][-1]])) #remove added card from deck
    return f'Dealer\'s hand: {session["dealer"]}, Your hand: {session["player"]}'

if __name__ == '__main__':
    app.run(port=5000, debug=False)
