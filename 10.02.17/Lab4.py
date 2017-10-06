# -*- coding: utf-8 -*-
import string

def firstEx():
    my_str = "my cat is a dog but my dog is a mouse"

    my_list = string.split(my_str)
    print my_list

    for i in range(len(my_list)):
        print(my_list[i])

def secondEx():
    mylist = []
    for i in range(10):
        x = input('Please enter your number: ')
        mylist.append(x)
    print mylist

def thirdEx():
    Sum = 0
    for i in range(len(mylist)):
        Sum += mylist[i]
    print Sum

def _2_1_1():
    x = [3,4]
    Sum =0
    for i in range(len(x)):
        Sum += x[i]

    print Sum

def _2_2():
    unknownEntries = [4, 1, 0]

    for i in range(len(unknownEntries)):
         if unknownEntries[i] == 0:
             print "invalid number at array " + str(i)

def average(timesRun=4):
    running = True
    unknownNumbers = []

    while running== True:
        w = input("Enter Number: ")
        if w == 0:
            break
        else:
            timesRun += 1
            unknownNumbers.append(w)

        running = timesRun != 10

    average = 0
    for i in range(len(unknownNumbers)):
        average += unknownNumbers[i]

    average /= len(unknownNumbers)
    print average
    return average
