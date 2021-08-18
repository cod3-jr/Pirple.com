"""
    Date:   2021-02-16
    Dev:    Me
    Purpose: work with lists
    - Declare a variable that contains an empty list
    - Define a function takes 1 argument and compares it 
    to the elements in the list variable if new element is unique, 
    add to list

"""
myUniqueList = []
myLeftovers = []

def lister(newElement):
    try:
        myUniqueList.index(newElement)
        dupLister(newElement)
        return False
    except ValueError:
        myUniqueList.append(newElement)
        return True

def dupLister(dupe):
    myLeftovers.append(dupe)

added = lister('Hello')
print(added)

added = lister('World')
print(added)

added = lister('test1')
print(added)

added = lister('test1')
print(added)

added = lister(5)
print(added)

print(myUniqueList)
print(myLeftovers)