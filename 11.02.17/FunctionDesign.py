# Takes two numbers and returns the larger one
def returnLarger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Takes two numbers and returns the lower one
def returnSmaller(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Takes a list and returns Average and Total
def sumList(list):
    total = 0
    length = len(list)
    for i in range(length):
        total += float(list[i])
    average = total/length
    return average, total

def roundup(num):
    outputNum = int(num)
    remainder = num - outputNum

    if remainder > 0.5: # Greater then
        outputNum += 1
    elif remainder < 0.5: # Less then
        outputNun = outputNum
    else: # Equal
        if outputNum%2 == 1:
            outputNum -= 1
    return outputNum

def crazyfunction2000(x):
    import random as rand
    r = rand.randint(0, 100)
    if r == x:
        return "Good Job"
    else:
        return "Ur wrong"
