def nthUglyNumber(n):
    ugly_number = [1]
    
    pos_2 = 0
    pos_3 = 0
    pos_5 = 0
    
    while n > 0:
        two = ugly_number[pos_2] * 2
        three = ugly_number[pos_3] * 3
        five = ugly_number[pos_5] * 5
        
        ugly_number_var = min(two,three,five)
        ugly_number.append(ugly_number_var)
        if ugly_number_var == two:
            pos_2 += 1
        if ugly_number_var == three:
            pos_3 += 1
        if ugly_number_var == five:
            pos_5 += 1
        n -= 1
    return ugly_number[-1]


print(nthUglyNumber(9))