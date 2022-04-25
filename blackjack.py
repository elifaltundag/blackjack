"""
Basic terminal program of the game Blackjack
"""

import random

# CARDS 
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
values = []
""" for card in cards:
    if isinstance(card, int):
        values.append(card)
    elif isinstance(card, str):
        values.append(11) """



# FUNCTIONS
def get_players_names():
    print("Welcome to Blackjack Casino by Elif!")
    num_players = int(input("Enter number of players: "))
    
    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Player{i+1}, enter your nickname: "))
    return player_names


def deal_first_cards():
    num_first_cards = 2
    first_cards = []
    for i in range(num_first_cards):   
        first_cards.append(random.choice(cards))
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


# PLAYER CLASS
class Player:
    def __init__(self, name = "PlayerX"):
        self.name = name
        self.cards = deal_first_cards()
        self.sum_cards = calculate_sum(self.cards)

    def __repr__(self):
        return f"{self.name}'s cards: {self.cards} => total: {self.sum_cards}"  



# CONTROL FLOW
starting = get_players_names()

players = []
for player_name in starting:
    player_name = Player(player_name)
    players.append(player_name)

for player in players:
    print(player)

