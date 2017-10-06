# -*- coding: utf-8 -*-
# Computes the area of a retangle, right triangle, and circle
# Written by Joshua H. on 9.11.2017
# Lab Number 1

from math import pi
import sys
import logging
  
def retangle():
    try:
        width = input("Please input width: ")
        length = input("Please input length: ")
        
        area = width * length # Calculate Area
        
        print "Area: " + str(area) + " square inches"
        
    except:
        logging.warning("Must be two numbers") # Make sure both input values are numbers

def rightTriangle():
    try:
        base = input("Please input the base of the triangle: ")
        height = input("Please input the height of the triangle: ")
        
        area = 1./2 * base * height # Calculate Area
        
        print "Area: " + str(area) + " square inches"
    except:
        logging.warning("Must be two numbers") # Make sure both input values are numbers

def circle():
    d = 'd'
    r = 'r'
    goodValues = True

    # loop in ensure correct values
    while(goodValues):
        print "To calcutate the circle with diameter, type 'd'."
        print "To calcutate the circle with radius, type 'r'."
        diameterOrRadius = input('>')

        try: 
            if diameterOrRadius == r:
                goodValues = False
                radiusInput = input('Please enter radius: ')/1. 
            elif diameterOrRadius == 'r':
                goodValues = False
                radiusInput = input('Please enter radius: ')/1.
            elif diameterOrRadius == d:
                goodValues = False
                radiusInput = input('Please enter diameter: ')/2.#Convert diameter to radius
            elif diameterOrRadius == 'd':
                goodValues = False
                radiusInput = input('Please enter diameter: ')/2.#Convert diameter to radius
        except:
            print "Try again."
            goodValues = True

    areaOfCircle = (pi*(radiusInput**2)) # Calculate Area
    print 'Anwser: '+ str(areaOfCircle)
    
def main():
    c = 'c'
    r = 'r'
    t = 't'
    e = 'e'
    exitProgram = True
        
    while(exitProgram):
        try:
            print 'Choose what to calculate'
            print "Type in 'c' to calcutate a circle"
            print "Type in 'r' to calcutate a retangle"
            print "Type in 't' to calcutate a right triangle"
            print "Type in 'e' to exit"

            typeOfCal = input('>')

            # Determine what type of calculation to preform.
            if typeOfCal == 'c':
                circle()
            elif typeOfCal == 'r':
                retangle()
            elif typeOfCal == 't':
                rightTriangle()
            elif typeOfCal == 'e':
                exitProgram = False

            print ''
        except:
            print "Please try again"

    sys.exit()
        
main() # Run program
