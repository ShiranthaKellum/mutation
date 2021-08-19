
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

def mutateString (text, position, character):
    sList = list(text)                              # convert string into a list
    sList [position] = character                    # replcing
    text = ''.join (sList)                          # updated list convert into a string
    print (text)


string = input ()

command = list (input ().split ())          # get the position and the character into a list

position = int (command [0])                # convert char type position in the command list into an integer

mutateString (string, position, command [1])
