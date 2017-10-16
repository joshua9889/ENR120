def f(x):
    return x%3==0. or x%5==0.

#print filter(f, range(1, 1000))

def cube(x):
    return x*x*x

#print(map(cube, range(1, 11)))

def add(x,y):
    print str(x)+'|' +str(y)
    return x+y

#print(reduce(add, range(1,11)))

def squares():
    squares = []
    for x in range(10):
        squares.append(x**2)

    print squares

    squares = [x**2 for x in range(10)]
    print squares

def FormattedPrints():
    for x in range(1, 11):
        print repr(x).rjust(2), repr(x*x).rjust(3),
        # Note trailing comma on previous line
        print repr(x*x*x).rjust(4)
