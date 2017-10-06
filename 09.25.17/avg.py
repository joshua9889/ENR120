arrayscores = (100, 50, 50, 50, 100)

def avg(array):
    totalScore = 0.
    for i in range(len(array)):
        totalScore += array[i]

    avgScore = totalScore / len(array)
    return avgScore

print(avg(arrayscores))
