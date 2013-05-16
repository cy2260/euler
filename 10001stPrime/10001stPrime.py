import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False

    return True
    
def nthPrimeNum(n):
    if n == 1:
        return 2
    i = 2
    num = 3
    prime = 0
    while i <= n:
        if isPrime(num) == True:
            i += 1
            prime = num
        num += 1
    return prime
