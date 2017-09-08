# -*- coding: utf-8 -*-
__author__  = 'joshua9889'

import logging

while(True):
    try:
        width = input("Please input width: ")
        length = input("Please input length: ")
        
        area = width * length
        
        print "Area: " + str(area) + " square inches"
        
        break
    except:
        logging.warning("Must be two numbers") # Make sure both input values are numbers
