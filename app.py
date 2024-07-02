from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Choices available for the game
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'Player wins!'
    else:
        return 'Computer wins!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return render_template('result.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
