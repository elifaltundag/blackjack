# IMPORT MODULES
import random
import blackjack_func as bj

# -------------------- #
# VARIABLES ---------- #
# -------------------- #

players = []
winners = []
losers = []



# -------------------- #
# FUCNTIONS ---------- #
# -------------------- #

# Skip a line when going from one task to another to improve readability in the termianl
def skip_line():
    print("")
def skip_2_lines():
    print("")
    print("")



# -------------------- #
# PLAYER CLASS ------- #
# -------------------- #

class Player:
    def __init__(self, name = "PlayerX", sum_cards = 0, move_chosen = None, won = False, lost = False):
        self.name = name
        self.cards = bj.deal_first_cards()
        self.sum_cards = bj.calculate_sum(self)
        self.move_chosen = move_chosen
        self.won = won
        self.lost = lost

    def __repr__(self):
        return f"{self.name}'s cards: {self.cards} => total: {self.sum_cards}"

house = Player("House")
players.append(house)



# --------------------------------------- #
# ONE FUNCTION FOR THE WHOLE CONTROL FLOW #
# --------------------------------------- #

def play_blackjack():
    
    # Introduce the game 
    bj.greeting()
    
    # Get the number of players and their names 
    players_names = bj.get_players_names()
    
    # Get each player as a class instance with their names, deal them each 2 random cards
    # Dealing each player 2 cards at the beginning is define in the class initiation
    for player_name in players_names:
        player_name = Player(player_name)
        players.append(player_name)
    skip_line() 

    # Print each players cards and the total sum 
    for player in players:
        print(player)
    skip_2_lines()

    bj.explain_moves()
    skip_2_lines()

    # Get each player's move, play accordingly
    # Unless there is a winner o loser, keep playing
    while (len(winners) == 0 and len(losers) == 0):
        # if SOMEONE NOT STANDING
            for player in players:
                if player == house: 
                    player.move_chosen = bj.get_next_move_house(player)
                else: 
                    player.move_chosen = bj.get_next_move(player)
                
                bj.play_round(player)
                bj.status(player)
                skip_line()

                if player.won == True:
                    winners.append(player.name)
                elif player.lost == True:
                    losers.append(player.name)
        
        # elif EVERYONE IS STANDING:



# -------------------- #
# PLAY THE GAME ------ #
# -------------------- #
play_blackjack()

