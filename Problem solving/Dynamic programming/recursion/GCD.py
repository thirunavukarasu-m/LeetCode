

def gcd(a):
    li = []
    for i in range(1,a+1):
        if a % i == 0:
            li.append(i)
            
    return li


print(gcd(10))
    


