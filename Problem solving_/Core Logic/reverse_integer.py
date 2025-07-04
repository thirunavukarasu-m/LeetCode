"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


def reverse(x):
    if not x:
        return 0
    x = str(x)
    if not str(x)[0].isalnum():
        print(x[0] + x[1:][::-1])
        return 0
    else:
        x = int(x[:: -1])
    
    if x >= -2**31 and x <= 2**31:
        return x
    else:
        return 0

print(reverse(1534236469))