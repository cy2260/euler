def smallestMultiple(n):
    result = 0
    isFound = False
    while not isFound:
        result += n
        i = n
        while i > 1:
            if result%i != 0:
                isFound = False
                break
            else:
                isFound = True
            i -= 1
    
    return result
