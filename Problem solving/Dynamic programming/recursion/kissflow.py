# 1/1    +     1/2 + 1/4 + 1/8 + 1/16

# 1/2**0  +    1/2**1


def kissflow(n,val=0):
    
    if n == 0:
        return val
    if n < 0:
        return
    n -= 1
    print(n)
    return kissflow(n,val+1/2**n)
    
print(kissflow(5))


# def kissflow(n,val="1/1",i=1):
#     n -= 1
#     if n == 0:
#         return val
    
#     if n < 0:
#         return
    
    
#     val = val + f' + 1/{2**i}' 
    
#     return kissflow(n,val,i+1)
    
# print(kissflow(5))





# def kissflow(n,i,val=0):
#     i = i + 1/2**val
#     if n == 0:
#         return i
#     else:
#         return kissflow(n-1,i,val+1)

# print(kissflow(5,0))