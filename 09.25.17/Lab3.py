# -*- coding: utf-8 -*-
# Return the Fahrenheit value of a celsius value
def celsius2Fahrenheit(celsius):
    degreeF = celsius*9./5. +32 # Calculate Fahrenheit.
    return degreeF

# 2 Function that computes the factorial for a number.
# 2.1 For numbers that are zero or less, the function returns 0.
# 2.2 For number equal to one, it returns 1.
# 2.3 For any positive integer greater than one, it computes the product term of
#       the 'result' plus all of the integers between the number and one.
def factorial(number):
    if number <= 0: # 2.1
        return 0
    elif number == 1: # 2.2
        return number
    elif number < 1:
        return None
    elif number > 1: # 2.3
       result = 1;
       for i in range(1,number+1):
           result *= i;
       return result;
