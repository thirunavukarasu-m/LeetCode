# 0 1 1 2 3 5 8 13 21 
# a b c
#   a b c



def fibonacci(n):
    print(0,1,end=" ")
    def recur(n,a=0,b=1):
        if n == 0:
            return 0
        
        c = a + b
        
        print(c , end = " ")
        
        a,b = b,c
        return recur(n-1,a,b)
    return recur(n-2)
    

fibonacci(10)
    
    

# li = []

# def fibonacci(n,a=0,b=1):
    
#     c = a + b
#     if len(li) >= n:
#         return li
#     else:
#         li.append(c)
    
#     a,b = b,c
#     return fibonacci(n,a,b)
    
    
    
# print(fibonacci(10))

