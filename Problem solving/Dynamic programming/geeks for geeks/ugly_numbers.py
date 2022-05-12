def UglyNumber(n):
    for i in [2,3,5]:
        while n % i == 0:
            n = n // i
            
    return n == 1

print(UglyNumber(14))
        