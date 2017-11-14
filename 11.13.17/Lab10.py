import VectorAdder, VectorSubtracter, VectorMultiplier
import string

# Allowed Choices
validChoices = 'asmq'

while True:
    # Menu
    print "'a' for Adding\n's' for Subtracting\n'm' for Multipling\n'q' to quit"
    userChoice = str(raw_input(""))

    # Make it an input we can read easily
    userChoice = userChoice.strip()
    userChoice = userChoice.lower()
    userChoice = userChoice[0]

    print "==============++=============="  # Easier for user to read
    if userChoice == validChoices[0]:  # Add two vectors
        VectorAdder.main()
    elif userChoice == validChoices[1]:  # Subtract two vectors
        VectorSubtracter.main()
    elif userChoice == validChoices[2]:  # Multiply two vectors
        VectorMultiplier.main()
    elif userChoice == validChoices[3]:  # Quit the program
        break
    else:  # Not a va
        print "Invalid Input"

    print "==============++=============="  # Easier for user to read
