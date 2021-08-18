from termcolor import colored, cprint
import numpy as np

# # termcolor example
# text = colored(' ', 'red', attrs=['reverse','blink'])
# print(text)

boardsize = [6,7]
player1 = 1
player2 = 2
game_state = np.zeros(boardsize, dtype=int)
# game_state = np.array(
#     [
#         ["c0,r0","c0,r1","c0,r2"],
#         ["c1,r0","c1,r1","c1,r2"],
#         ["c2,r0","c2,r1","c2,r2"]
#     ])

def draw_Playboard(game_state):
    rows, columns = game_state.shape
    dash = "-"
    bar = "|"
    space = " "

    # reversing this range of how many rows draws the board top to bottom
    for rows in reversed(range(boardsize[1])):
        for columns in range(boardsize[0]):
            print(game_state[columns][rows], end="")
        print()

def nextMove(game_state, selected, player):
    # loop iterates through selected column array
    # enumerate returns the index and value at that index
    for index, val in enumerate(game_state[selected]):
        if val == 0:
            game_state[selected,index] = player
            break

def whoseTurn(player):
    if player == player1:
        return player2
    else: 
        return player1

# game_state[0,0] = player1
nextMove(game_state,1,player1)
nextMove(game_state,1,player2)
draw_Playboard(game_state)

# print(game_state)