import os

"""
    2021-04-04
    Requirements:
        On start, prompt user for filename
        If filename doesn't exist, prompt user to enter text
            that will be written to the file.
            After entering the text, it should save the file and exit
        If the filename does exist, prompt user to:
            a. read file
                then: print file to terminal
            b. overwrite file
                then: delete file and create new file
            c. append the file
                then: add input to existing file
    Bonus: 
        implement 4th option: replace a single line
        prompt for:
            line to replace
            text that should replace the line
"""
def writer(fileName, opt='w'):
    print("Write \'!wq\' on a new line to finish editing the file:")
    file = open(fileName, opt)
    done = "!wq"
    line = ""
    notes = []
    # Capture input
    while line != done:
        line = input()
        if line == done:
            break
        else:
            notes.append(line)
    
    if opt == 'a':
        file.write('\n')
    # write output
    if len(notes) > 0:
        for line in notes[:-1]:
            file.write('%s\n' %line)
        file.write('%s' %notes[-1])
    file.close()

def inserter(fileName):
    try:
        line = int(input("Select line number to replace. First line of file is 1\n"))
    except ValueError:
        line = 1
        print('Valid number not entered. Defaulting to 1\n')

    text = input("Replace line %i with:" %line) + '\n'
    file = open(fileName, 'r+')
    notes = file.readlines()
    notes[line-1] = text
    file.seek(0,0)
    file.writelines(notes)

def handle_file_exists(fileName):
    message = "File %s already exists:\n\n"
    message += "Enter 'r' or 'read' to read file\n"
    message += "Enter 'o' or 'overwrite' to overwrite\n"
    message += "Enter 'a' or 'append' to append to file\n"
    message += "Enter 'e' or 'edit' to edit a single line of the file:\n"
    option = input(message %fileName)

    if option == 'r' or option == 'read':
        file = open(fileName)
        for line in file.readlines():
            print('%s' %line,end="")
    elif option == 'ow' or option == 'overwrite':
        writer(fileName)
    elif option == 'a' or option == 'append':
        writer(fileName, 'a')
    elif option == 'e' or option == 'edit':
        inserter(fileName)

def note_taker():
    fileName = input("Input filename:\n")
    if os.path.isfile(fileName): 
    # i.e. FileName exists
        handle_file_exists(fileName)
    else: 
    # i.e. New FileName passed
        writer(fileName)

if __name__ == "__main__":
    note_taker()