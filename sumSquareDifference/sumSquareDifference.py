def sumSquareDiff(n):
    a = sum( x**2 for x in range(1,n+1) )
    b = sum( x for x in range(1,n+1) )**2
    return abs(a-b)
