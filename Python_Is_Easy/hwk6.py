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

def drawPlayboard(rows, columns):
    dash = "-"
    bar = " |"
    # This if will add the appropriate number of rows to ensure the
    # playboard has the requested number of rows
    if rows % 2 == 0:
        if rows > 3:
            rows += 3
        else:
            rows += 1
    else:
        if rows > 3:
            rows += 4
        else:
            rows += 2
    # One bar creates 2 columns, so subtracting 1 from columns generates
    # playboard with requested number of columns
    columns -= 1

    for row in range(rows):
        if row%2 == 0:
            print(bar*columns)
        else:
            # adding one to finish row
            print(dash*(columns*2+1))


drawPlayboard(6,4)