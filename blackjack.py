"""
Basic terminal program of the game Blackjack
"""

# PLAYER CLASS
class Player:
    def __init__(self, name = "PlayerX", sum_cards = 0):
        self.name = name
        self.sum_cards = sum_cards

    def __repr__(self):
        return self.name + " has a total of " + str(self.sum_cards)

# FUNCTIONS
def get_players():
    print("Welcome to Blackjack Casino by Elif!")
    num_players = int(input("Enter number of players: "))
    
    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Player{i+1}, enter your nickname: "))
    print(player_names)
    return player_names


        



# CONTROL FLOW
get_players()
elifing = Player()
print(elifing)