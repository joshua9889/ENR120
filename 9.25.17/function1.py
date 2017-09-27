# -*- coding: utf-8 -*-
def say_hello():
    # block belonging to the function
    print('hello world')

def print_max(a, b):
     if a > b:
         print a, 'is maximum'
     elif a == b:
         print a, 'is equal to', b
     else:
         print b, 'is maximum'

def maximum(x, y):
     if x > y:
         return x
     elif x == y:
         return 'The numbers are equal'
     else:
         return y

def func(x):
     print 'x is', x
     x = 2
     print 'Changed local x to', x
