"""
    Date:   2021-02-11
    Dev:    Me
    Purpose: work with if statements
    Function takes 3 arguments and compares them 
    to determine if 2 or more are equivalent

"""

def comparer(a,b,c):
    # for string parameters
    if a == b or b == c or a == c:
        return True
    # for strings that can be interpreted as integers
    elif a == int(b) or b == int(c) or a == int(c) or int(a) == b or int(b) == c or int(a) == c:
        return True
    else:
        return False