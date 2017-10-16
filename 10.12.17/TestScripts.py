def f(x):
    return x%3==0. or x%5==0.

def c(x):

    return x<=100

print filter(c, range(1, 1000))
