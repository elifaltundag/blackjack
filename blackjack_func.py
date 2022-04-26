# IMPORTED MODULES
import random


# VARIABLES
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
# The whole deck of 52 cards
deck = []
for card in cards:
    for i in range(4):
        deck.append(card)

players = []
winners = []
losers = []

# FUNCTIONS
# Opening greeting at the beginning
def greeting():
    print("\n---   Welcome to the Blackjack Casino by Elif!   ---\n")


# Explaination of the possible moves
def explain_moves():
    print("Now let's start playing!\nThere are 2 possible moves you can play:\nHit   : Take another card\nStand : Take no more cards\n\n(Lower and upper cases are ignored)")


# Get the number of players and their names
def get_players_names():
    num_players = int(input("Enter number of players: "))
    
    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Player{i+1}, enter your name: ").strip())
    return player_names


# Each player is dealt 2 cards at the beginning
def deal_first_cards():
    num_first_cards = 2
    first_cards = []
    for i in range(num_first_cards):  
        random_card = random.choice(deck)
        first_cards.append(random_card)
        deck.remove(random_card)
    return first_cards


def calculate_sum(cards):
    sum_cards = 0
    for card in cards:
        if card != "A":
            if isinstance(card, int):
                sum_cards += card
            elif isinstance(card, str):
                sum_cards += 10
        elif card == "A":
            if sum_cards + 11 > 21:
                sum_cards += 1
            elif sum_cards + 11 <= 21:
                sum_cards += 11
    return sum_cards



def get_next_move(player):
    next_move = input(f"{player.name}'s next move: ").strip().lower()
    return next_move


def play_round(player, move):
    if move == "hit":
        random_card = random.choice(deck)
        player.cards.append(random_card)
        deck.remove(random_card)
        player.sum_cards = calculate_sum(player.cards)    
        
    elif move == "stand":
        pass

    print(f"{player.name}'s cards: {player.cards} => total: {player.sum_cards}")

def status(player):
    if player.sum_cards == 21:
        player.won = True
        # winners.append(player.name)
        print(f"Yeay {player.name} you won!")

    elif player.sum_cards > 21:
        player.lost = True
        # losers.append(player.name)
        print(f"Sorry {player.name}, you lost...")
