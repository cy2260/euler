def evenFibSum(limit):
    fib0 = 0
    fib1 = 1
    fib  = 0
    sum  = 0
    while(True):
        if fib > limit:
            break
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
        if fib%2 == 0:
            sum += fib
    return sum
