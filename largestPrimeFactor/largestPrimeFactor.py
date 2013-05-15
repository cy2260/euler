import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False

    return True

def largestPrimeFactor(n):
    maxFactor = 0

    for i in range(1, int(math.sqrt(n)+1)):
        if n%i == 0 and isPrime(i):
            maxFactor = i

    return maxFactor

