## This is a function
def myFunc(x):  # The function's name is "myFunc"
    try:
        eval(x)
        print "x is a number"
    except:
        print "x is not a number"
