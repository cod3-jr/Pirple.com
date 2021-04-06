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
    # write output
    # change to use writeLines
    
    if len(notes) > 0:
        for line in notes[:-1]:
            file.write('%s\n' %line)
        file.write('%s' %notes[-1])
    file.close()

def handle_file_exists(fileName):
    message = "Enter 'r' or 'read' to read file\n"
    message += "Enter 'ow' or 'overwrite' to overwrite\n"
    message += "Enter 'a' or 'append' to append to file\n"
    message += "Enter 'e' or 'edit' to edit a line of the file\n"
    option = input(message)

    if option == 'r' or option == 'read':
        file = open(fileName)
        for line in file:
            print('%s\n' %line)
    elif option == 'ow' or option == 'overwrite':
        writer(fileName)
    elif option == 'a' or option == 'append':
        print('append file')

def note_taker():
    fileName = input("Input filename:\n")
    if os.path.isfile(fileName):
        # TODO: Handle File exists
        # Maybe create "ask" method that returns value 
        # that indicates what to do when file exists
        # Or handle_file_exists to handle decision and writing
        # Would be nice to reuse writer...
        # print(fileName,"exists")
        handle_file_exists(fileName)
    else: # i.e. New FileName passed
        writer(fileName)

if __name__ == "__main__":
    note_taker()