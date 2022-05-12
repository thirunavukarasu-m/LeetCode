# Python Program to Find the Sum of Natural Numbers Using Recursion 



def sum_natural(n):
    
    if n == 1:
        return n
    if n <= 0:
        return "Enter valid number"

    return n + sum_natural(n-1)


print(sum_natural(2))















































