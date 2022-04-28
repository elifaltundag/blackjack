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
def calculate_sum(player):
    player.sum_cards = 0
    for card in player.cards:
        if card != "A":
            if isinstance(card, int):   # 2 - 10 : their own values 
                player.sum_cards += card
            elif isinstance(card, str): # J, Q, K : 10
                player.sum_cards += 10
        elif card == "A":               # A: 1 or 11 depending on the sum of the other cards 
            if player.sum_cards + 11 > 21:
                player.sum_cards += 1
            elif player.sum_cards + 11 <= 21:
                player.sum_cards += 11
    return player.sum_cards


# Get the move of the player
def get_next_move(player):
    player.move_chosen = input(f"{player.name}'s next move: ").strip().lower()
    return player.move_chosen

# Get the House's move depending on the its' cards' total sum 
def get_next_move_house(player): 
    if player.sum_cards < 18:
        player.move_chosen = "hit"
    elif player.sum_cards >= 18:
        player.move_chosen = "stand"
    print(f"{player.name}'s next move: {player.move_chosen}")
    return player.move_chosen



# Play a round depending on the move
def play_round(player): 
    if player.move_chosen == "hit": # Deal a random and remove it from the deck
        random_card = random.choice(deck)
        player.cards.append(random_card)
        deck.remove(random_card)
        player.sum_cards = calculate_sum(player)    
        
    elif player.move_chosen == "stand": # Do nothing
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

# End the game if everyone is standing
def everyone_standing():
    print("Looks like everybody's standing so it's time to end game.")


def end_game(players): 
    print("Player: Points")
    for player in players:
        print(f"{player.name}: {player.sum_cards}")

