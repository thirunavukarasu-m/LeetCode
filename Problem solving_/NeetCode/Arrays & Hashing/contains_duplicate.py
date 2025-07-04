'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

https://leetcode.com/problems/contains-duplicate/
'''


def contains_duplicate(nums):
    if not nums:
        return False
    
    # Method 1: Very slow
    # nums.sort()
    
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i-1]:
    #         return True
    
    # return False
    # 
    # Method 2: Mid fast
    # return len(set(nums)) != len(nums)
    
    # Method 3: Fast
    seen_nums = set()
    for i in nums:
        if i not in seen_nums:
            seen_nums.add(i)
        else:
            return True
    
    return False