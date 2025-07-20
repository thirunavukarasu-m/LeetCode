# Given a sorted array, find indices of the two numbers that add up to a target.
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# I tried doing this with a for loop. But made a blunder in not increasing the left pointer.


def two_sum_ii_1(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# li = [2,7,11,15]
# print(two_sum_ii_1(li, 9))


def two_sum_ii_2(numbers, target):
    if not numbers:
        return []
        
    left = 0
    right  = len(numbers) - 1
    
    result = []
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            if numbers[left] != numbers[right]:
                result.append([numbers[left] , numbers[right]])
            right -= 1
            left += 1
            continue
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    return result
    

# li = [0,1,1,2,2,2,3,4, 4.5, 4.5,5,6,7,8,9,11,15]
# print(two_sum_ii_2(li, 9))



'''
Input: arr[] = {1, 5, 7, -1, 5}, target = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input: arr[] = {1, 1, 1, 1}, target = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).

Input: arr[] = {10, 12, 10, 15, -1}, target = 125
Output:  0
'''

def two_sum_ii_3_1(numbers, target):
    if not numbers:
        return 0
    
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    result = 0
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        
        if curr_sum == target:
            result += 1
            left += 1
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
             right -= 1
    
    return result
    
    
li = [1, 5, 7, -1, 5]
print(two_sum_ii_3_1(li,6))


def two_sum_ii_3_2(numbers, target):
    if not numbers:
        return 0
        
    result = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                result += 1
    
    return result
    
li = [1, 5, 7, -1, 5]
print(two_sum_ii_3_2(li,6))
