'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Earlier I had not target in the if condition so if 0 is given it fails.
# I also had the max and min functions while calculating the diff which created problems as what if there are negative numbers.
def two_sum(nums, target):
    if not nums:
        return []
        
    temp_dict = {}
    
    for index, number in enumerate(nums):
        diff = target - number
        if diff not in temp_dict:
            temp_dict[number] = index
        else:
            return [temp_dict[diff], index]
    return []
print(two_sum([3,2,95,4,-3], 92))


