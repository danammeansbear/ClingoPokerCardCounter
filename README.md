Texas Hold'em Hand Strength Evaluator
A Python program designed to help players evaluate their hand strength in Texas Hold'em poker, factoring in the cards they've been dealt, community cards, and the betting behavior of other players. The tool can assess the likelihood of the player's hand being stronger than the other players' hands.

Features
Hand Evaluation: Evaluates the strength of your hand based on Texas Hold'em hand rankings.
Card Counting Simulation: Simulates other players' hands based on the remaining deck and community cards.
Betting Influence: Considers the bet sizes of other players to estimate their hand strength.
Player Feedback: Gives you feedback on whether your hand is likely to be the strongest at the table.
Requirements
Python 3.x
python-poker library for hand evaluation
To install the required libraries, use the following command:

bash
Copy code
pip install poker
Installation
Clone the repository to your local machine:

bash
git clone https://github.com/yourusername/texas-holdem-hand-strength-evaluator.git
Navigate to the project directory:

bash
cd texas-holdem-hand-strength-evaluator
Install the required Python dependencies:

bash
pip install -r requirements.txt
Usage
Run the Python script:

bash
python texas_holdem_poker.py
Follow the prompts to input your hand, the community cards, and the bet amounts of other players.

Example prompts:

Enter the number of players: 3
Enter your hand (e.g., 'A of hearts, 10 of spades'): A of hearts, 10 of spades
Enter the community cards (e.g., '2 of hearts, 5 of spades, K of diamonds'): 2 of hearts, 5 of spades, K of diamonds
Enter the bet for Player 1 (chips): 100
Enter the bet for Player 2 (chips): 150
Enter the bet for Player 3 (chips): 200
The program will output the strength of each player's hand, betting influence, and determine if your hand is the best.

Example Output
bash
Welcome to the Texas Hold'em Hand Strength Evaluator!
Enter the number of players: 3
Enter your hand (e.g., 'A of hearts, 10 of spades'): A of hearts, 10 of spades
Enter the community cards (e.g., '2 of hearts, 5 of spades, K of diamonds'): 2 of hearts, 5 of spades, K of diamonds
Enter the bet for Player 1 (chips): 100
Enter the bet for Player 2 (chips): 150
Enter the bet for Player 3 (chips): 200

Hand Strengths (from weakest to strongest):
player_3: Four of a Kind
player_1: Two Pair
user: High Card

Betting Influences:
player_1: 20.00%
player_2: 30.00%
player_3: 50.00%

You do not have the best hand. Be careful!
How It Works
1. Hand Evaluation
The program uses the python-poker package to evaluate the strength of hands. It checks for common poker hand rankings such as Royal Flush, Straight Flush, Four of a Kind, etc., based on the cards the player holds and the community cards on the table.

2. Simulating Other Players' Hands
The program simulates the hands of other players by drawing cards from the remaining deck (excluding the user’s and community cards). Each simulated hand is evaluated, and the strength of the hand is compared to the user's hand.

3. Betting Influence
The program considers the amount of chips each player has bet. It assumes that players who bet more may have stronger hands, though this is a simplified assumption and can be adjusted for more complex strategies. It calculates the percentage of total bets for each player to gauge the relative strength of their bets.

4. Feedback
After simulating all player hands and calculating the betting influence, the program will tell you whether your hand is the best at the table and if you need to be cautious with your betting.

Contributing
Contributions are welcome! If you'd like to improve this project, you can fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
python-poker for hand evaluation functionality.
Texas Hold'em rules and community-driven strategies for poker.
Inspired by poker strategy tools and resources.
