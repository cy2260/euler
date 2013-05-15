def isPalindrome(n):
    return str(n) == str(n)[::-1]
    
def largetPalindromeProduct(numOfDigits):
    start = 10**(numOfDigits)-1
    end   = 10**(numOfDigits-1)-1
    i = j = start
    maxNum = 0
    print start, end
    while i > end:
        while j > end:
            if isPalindrome(i*j):
              maxNum = max(maxNum, i*j)
            j -= 1
        j = start
        i -= 1
    return maxNum
