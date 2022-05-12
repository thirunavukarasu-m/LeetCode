



# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?




# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



# n = 0
# dp = {}
# def climbing_stairs(i):
#     if i == n:
#         return 1
#     if i > n:
#         return 0
#     if i == 0:
#         return
    
#     dp[(i)] = climbing_stairs(i+1) + climbing_stairs(i+2)
#     return dp[(i)]

# print(climbing_stairs(0))

# print(dp)




def climbing_stairs(n):
    
    
    if n <= 1:
        return n
    if n == 2:
        return 1
    return climbing_stairs(n-1) + climbing_stairs(n-2)


print(climbing_stairs(5 + 1))