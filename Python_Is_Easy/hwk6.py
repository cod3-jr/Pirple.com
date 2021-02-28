"""
    Date:   2021-02-27

    Purpose: def function for drawing a playing board
         | | 
        -----
         | |
    arguments: row int, columns int
    return: if width and height <= maximum, return True
        else return False
"""
import math # only needed if printing row and / or column numbers
import os # needed to determine terminal window size

def drawPlayboard(rows, columns):
    dash = "-"
    bar = "|"
    space = " "

    # Handles printing small playboards
    if columns > 2:
        columns = columns * 2 -1
    else:
        columns += 1
    
    if rows > 2:
        rows = rows * 2 - 1
    else:
        rows += 1 

    for row in range(rows):
        # For printing row numbers
        # if row % 2 == 0:
        #     print(math.floor(row/2+1),end= " ")
        # else:
        #     print(" ", end= " ")

        for column in range(columns):
            if row % 2 == 0:
                if column == (columns - 1):
                    # For printing column number at end of row
                    # print(math.floor(column/2+1))
                    print(space)
                elif column % 2 == 1:
                    print(bar, end="")
                else:
                    # For printing column number
                    # print(math.floor(column/2+1), end= "")
                    print(space,end="")
            elif column == columns - 1:
                print(dash)
            else:
                print(dash,end= "")
    
    size = os.get_terminal_size()
    if rows <= size.lines and columns <= size.columns:
        return True
    else:
        return False
# For confirming terminal window size
# print(os.get_terminal_size())
success = drawPlayboard(12,48)
# For confirming function return value
# print(success)