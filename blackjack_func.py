# IMPORTED MODULES
import random


# -------------------- #
# VARIABLES ---------- #
# -------------------- #

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = [] # The whole deck of 52 cards
for card in cards:
    for i in range(4):
        deck.append(card)

players = []



# -------------------- #
# FUCNTIONS ---------- #
# -------------------- #

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

# Calculate the sum of the cards in hand
def calculate_sum(cards):
    sum_cards = 0
    for card in cards:
        if card != "A":
            if isinstance(card, int):   # 2 - 10 : their own values 
                sum_cards += card
            elif isinstance(card, str): # J, Q, K : 10
                sum_cards += 10
        elif card == "A":               # A: 1 or 11 depending on the sum of the other cards 
            if sum_cards + 11 > 21:
                sum_cards += 1
            elif sum_cards + 11 <= 21:
                sum_cards += 11
    return sum_cards


# Get the move of the player
def get_next_move(player):
    next_move = input(f"{player.name}'s next move: ").strip().lower()
    return next_move

# Play a round depending on the house's card's total sum 
def get_next_move_house(player): 
    if player.sum_cards < 15:
        player.move = "hit"
    elif player.sum_cards >= 15:
        player.move = "stand"
    print(f"{player.name}'s next move: {player.move}")



# Play a round depending on the player's move
def play_round(player): 
    if player.move == "hit": # Deal a random and remove it from the deck
        random_card = random.choice(deck)
        player.cards.append(random_card)
        deck.remove(random_card)
        player.sum_cards = calculate_sum(player.cards)    
        
    elif player.move == "stand": # Do nothing
        pass

    print(f"{player.name}'s cards: {player.cards} => total: {player.sum_cards}")


# Check the status for winners and losers
def status(player):
    if player.sum_cards == 21:
        player.won = True
        print(f"Yeay {player.name} you won!")

    elif player.sum_cards > 21:
        player.lost = True
        print(f"Sorry {player.name}, you lost...")
