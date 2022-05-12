li =  [1, 2, [3,4], [5,6]]



# def list_sum(li,i=0):
#     sum = 0
#     if i == len(li):
#         return sum
#     if type(li[i]) == type([]):
#         sum +=  list_sum(li[i])
#     else:
#         sum = sum +li[i] +list_sum(li,i+1)
        
#     return sum
    
# print(list_sum(li))

li =  [1, 2, [3,4], [5,6]]
def list_sum(li):
    sum = 0
    for i in li:
        if type(i) == type([]):
            sum += list_sum(i)
        else:
            sum = sum+i
    return sum
print(list_sum(li))

