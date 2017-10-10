import math
import string

myList = []
running_Total = 0

numFlg = False
print "This program will ask the user to enter a list of numbers "
print "Once entered the program will return the average value for the list"

while not numFlg: # Changed "while numFlg == False" to "while not numFlg"
    print "Please enter the next number or type 'q' to stop"
    num = str(raw_input("The entry must be a number "))

    try:
        num = eval(num)
        myList.append(num)
        running_Total += num
    except:
        if string.upper(num) == "Q" and len(myList) > 0:
            average = float(running_Total)/len(myList)
            print "The average = {0:.2f}".format(average)
            numFlg = True
        else:
            print "Please enter at least one valid number "
