Catchflg = 1  # Variable Catchflg equals 1
while Catchflg == 1:  # Repeat code in this loop til Catchflg does not equal 1
    trialBalloon = raw_input("enter a type of animal") # User input
    if trialBalloon == 'cat':  # If trialBalloon equals 'cat'
        print "Good choice"  # Print "Good choice"
        Catchflg = 0  # Set Catchflg to 0 (stop the loop)
    else: # If trialBallon does not equal 'cat'
        print "Try again"  # Print "Try again"
print "Done"  # Print "Done" When the code is finished
