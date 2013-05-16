import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False

    return True
    
def sumOfPrimes(n):
    if n < 3:
       return 2
    sum = 2
    for i in range(3, n, 2):
        if isPrime(i) == True:
            sum += i
    return sum
