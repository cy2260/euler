def sumMultiplesOf3And5(start, end):
    sum = 0
    for i in range(start, end):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum


