# filename: flask_blackjack.py
"""
To start the game, run this file with Python and go to http://localhost:5000 in your web browser. You can also make actions like hitting or sticking by sending GET or POST requests to http://localhost:5000/game, respectively.

Note: In this simplified version of blackjack, aces are always counted as 11 unless that would result in a total score greater than 21, in which case they are counted as 1. Additionally, blackjack is assigned a score of 0 for easy game checking.
Please make sure to save the script in a file called `flask_blackjack.py` and run it using the command:

python3 flask_blackjack.py

Please also note this is a very basic version. For a full version, you'd likely want to add a database to keep track of player's wins/losses, use templates to render the output in HTML, include betting, and so on.
"""

from flask import Flask, request
import random

app = Flask(__name__)

# Global vars
player_cards = []
dealer_cards = []

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

@app.route('/')
def game_start():
    global player_cards, dealer_cards
    player_cards = []
    dealer_cards = []
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    return f"Welcome to Blackjack! Your cards: {player_cards}, dealer's first card: {dealer_cards[0]}"

@app.route('/game', methods=['GET', 'POST'])
def game_play():
    global player_cards, dealer_cards
    if calculate_score(player_cards) == 0 or calculate_score(dealer_cards) == 0:
        return f"Game over: {'Player win' if calculate_score(player_cards) == 0 else 'Dealer win'}"
    if request.method == 'POST':
        player_cards.append(deal_card())
        if calculate_score(player_cards) > 21:
            return f"Your cards: {player_cards}, Your score: {calculate_score(player_cards)}, You lose!"
        return f"Your cards: {player_cards}, Your score: {calculate_score(player_cards)}"
    else:
        while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
            dealer_cards.append(deal_card())
        return f"Your cards: {player_cards}, Your score: {calculate_score(player_cards)}, Dealer's cards: {dealer_cards}, Dealer's score: {calculate_score(dealer_cards)}, {'Player win' if calculate_score(player_cards) > calculate_score(dealer_cards) else 'Dealer win'}"

if __name__ == '__main__':
    app.run(debug=True)


