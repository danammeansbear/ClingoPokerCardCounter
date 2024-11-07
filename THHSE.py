import random
from poker import Card, Deck, Hand
from collections import defaultdict

# Define poker hand rankings
HAND_RANKS = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10,
}

# Helper function to evaluate hands
def evaluate_hand(hand_cards, community_cards):
    hand = Hand(hand_cards + community_cards)
    return hand.best_hand()

# Function to simulate the deck and determine the best hand for the player
def simulate_player_hands(num_players, user_hand, community_cards):
    # Create a deck and remove cards that are already dealt
    deck = Deck()
    all_dealt_cards = user_hand + community_cards
    for card in all_dealt_cards:
        deck.cards.remove(Card(card[0] + ' of ' + card[1]))
    
    # Deal hands to other players
    player_hands = []
    for _ in range(num_players - 1):
        player_hand = [deck.draw() for _ in range(2)]  # Each player gets 2 cards
        player_hands.append(player_hand)
    
    # Evaluate the user's hand strength
    user_best_hand = evaluate_hand(user_hand, community_cards)
    
    # Now evaluate other players' hands and compare
    player_strengths = defaultdict(int)
    player_strengths["user"] = HAND_RANKS[user_best_hand[0]]

    for i, player_hand in enumerate(player_hands, start=1):
        best_hand = evaluate_hand(player_hand, community_cards)
        player_strengths[f"player_{i}"] = HAND_RANKS[best_hand[0]]
    
    return player_strengths

# Function to calculate likelihood of winning based on betting behavior
def calculate_betting_influence(bets):
    # Example: Use bet size as an indicator of strength (simplified)
    total_bet = sum(bets.values())
    max_bet = max(bets.values())
    betting_influence = {player: bet / total_bet for player, bet in bets.items()}
    return betting_influence

# Main game loop
def main():
    print("Welcome to the Texas Hold'em Hand Strength Evaluator!")
    
    # Number of players (including the user)
    num_players = int(input("Enter the number of players: "))
    
    # Get user input for their hand
    user_hand_input = input("Enter your hand (e.g., 'A of hearts, 10 of spades'): ").split(',')
    user_hand = [(card.split(' of ')[0].strip(), card.split(' of ')[1].strip()) for card in user_hand_input]
    
    # Get community cards
    community_cards_input = input("Enter the community cards (e.g., '2 of hearts, 5 of spades, K of diamonds'): ").split(',')
    community_cards = [(card.split(' of ')[0].strip(), card.split(' of ')[1].strip()) for card in community_cards_input]
    
    # Handle bets for multiple players
    bets = {}
    for i in range(1, num_players + 1):
        bet = int(input(f"Enter the bet for Player {i} (chips): "))
        bets[f"player_{i}"] = bet

    # Simulate the game and evaluate hands
    player_strengths = simulate_player_hands(num_players, user_hand, community_cards)
    betting_influence = calculate_betting_influence(bets)
    
    # Display hand strengths and betting influences
    print("\nHand Strengths (from weakest to strongest):")
    for player, strength in sorted(player_strengths.items(), key=lambda item: item[1], reverse=True):
        print(f"{player}: {list(HAND_RANKS.keys())[strength - 1]}")

    print("\nBetting Influences:")
    for player, influence in betting_influence.items():
        print(f"{player}: {influence * 100:.2f}%")

    # Determine if the user has the best hand
    if player_strengths["user"] == max(player_strengths.values()):
        print("\nYou have the best hand!")
    else:
        print("\nYou do not have the best hand. Be careful!")

if __name__ == "__main__":
    main()
