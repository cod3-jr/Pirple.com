from termcolor import colored, cprint
import numpy as np

# # termcolor example
# text = colored(' ', 'red', attrs=['reverse','blink'])
# print(text)

boardsize = [6,7]
current = ""
game_state = np.zeros(boardsize, dtype=int)
player1 = 1
player2 = 2

def draw_Playboard(game_state):
    rows, columns = game_state.shape
    dash = "-"
    bar = "|"
    space = " "

    # reversing this range of how many rows draws the board top to bottom
    for rows in reversed(range(boardsize[1])):
        for columns in range(boardsize[0]):
            cell = game_state[columns][rows]
            if (cell != 0):
                if (cell == player1):
                    cprint("☉","red",attrs=["bold"],end="")
                    # print(game_state[columns][rows], end="")
                else:
                    cprint("☉","grey",attrs=["bold"],end="")
            else:
                print(space,end="")
            if (columns != boardsize[0]-1):
                print(bar,end="")
        print()
        print(dash*(boardsize[0]*2-1))

    for i in range(boardsize[0]):
        print(i,end=" ")
    
    print("\n")

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

nextMove(game_state,1,player1)

nextMove(game_state,1,player2)
nextMove(game_state,2,player1)
draw_Playboard(game_state)

# print(game_state)