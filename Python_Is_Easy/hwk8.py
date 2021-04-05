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
def writer(fileName):
    file = open(fileName, "w")
    line = ""
    done = "!wq"
    print("Write \'!wq\' to finish editing the file:")
    while line != done:
        line = input()
        if line == done:
            break
        else:
            file.writelines(line+"\n")
    file.close()

def noteTaker():
    fileName = input("Input filename:\n")
    if os.path.isfile(fileName):
        # TODO: Handle File exists
        # Maybe create "ask" method that returns value 
        # that indicates what to do when file exists
        # Or handle_file_exists to handle decision and writing
        # Would be nice to reuse writer...
        print(fileName,"exists")
    else: 
        writer(fileName)

if __name__ == "__main__":
    noteTaker()