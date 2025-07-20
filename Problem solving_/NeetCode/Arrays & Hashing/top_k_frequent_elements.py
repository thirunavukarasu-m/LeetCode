'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

https://leetcode.com/problems/top-k-frequent-elements/description/
'''
# Need to learn Heap
# I misunderstood the question and wrote the logic to get the repetations more than or equal to k
def k_freq_1(nums, k):
    if not nums:
        return []
    
    temp_dict = {}
    result = set()
    for i in nums:
        if i not in temp_dict:
            temp_dict[i] = 1
            if temp_dict[i] >= k:
                result.add(i)
        else:
            temp_dict[i] += 1
            if temp_dict[i] >= k:
                result.add(i)
    
    return list(result)
    
# print(k_freq_1([1,2], 2))


def k_freq_2(nums, k):
    if not nums:
        return []
        
    