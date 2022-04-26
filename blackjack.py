"""
Basic terminal program of the game Blackjack
"""
import random

# CARDS 
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = []
for card in cards:
    for i in range(4):
        deck.append(card)

winners = []
losers = []

# FUNCTIONS
def get_players_names():
    print("Welcome to Blackjack Casino by Elif!")
    num_players = int(input("Enter number of players: "))
    
    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Player{i+1}, enter your nickname: ").strip())
    return player_names


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


def explain_moves():
    print("\nNow let's start playing!\nThere are 2 possible moves you can play:\nHit   : Take another card\nStand : Take no more cards\n\n(Lower and upper cases are ignored)\n")


def get_next_move(player):
    next_move = input(f"{player}'s next move: ").strip().lower()
    return next_move


def play_round(move):
    if move == "hit":
        random_card = random.choice(deck)
        player.cards.append(random_card)
        deck.remove(random_card)
        player.sum_cards = calculate_sum(player.cards)    
        
    elif move == "stand":
        pass

    print(f"{player.name}'s cards: {player.cards} => total: {player.sum_cards}")

    if player.sum_cards == 21:
        player.won = True
        winners.append(player.name)
        print(f"Yeay {player.name} you won!")

    elif player.sum_cards > 21:
        player.lost = True
        losers.append(player.name)
        print(f"Sorry {player.name}, you lost...")
    
    print("")



# PLAYER CLASS
class Player:
    def __init__(self, name = "PlayerX", won = False, lost = False):
        self.name = name
        self.cards = deal_first_cards()
        self.sum_cards = calculate_sum(self.cards)
        self.won = won
        self.lost = lost

    def __repr__(self):
        return f"{self.name}'s cards: {self.cards} => total: {self.sum_cards}"  





# CONTROL FLOW
# print(len(deck))
players_names = get_players_names()

players = []
for player_name in players_names:
    player_name = Player(player_name)
    players.append(player_name)

# print(len(deck))

print("")
for player in players:
    print(player)

explain_moves()

for player in players:
    player_move = get_next_move(player.name)
    play_round(player_move)


