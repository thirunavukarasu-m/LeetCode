'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
 
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
# In this logic if we pass dvdf as arg we will get 2 but the answer is 3. Cause the set will have d,v and when we get d again set and re initialized.
# We can't remove it blindly as we have to maintain order.
# 
def longest_substring_unique_1(s):
    unique_set = set()
    unique_count = 0
    result = 0
    for i in s:
        if i not in unique_set:
            unique_count += 1
            unique_set.add(i)
            result = max(result, unique_count)
            
        else:
            unique_set.remove(i)
            unique_set.add(i)
            result = max(result, unique_count)
            unique_count = 1
            
    print(unique_set)
    return result
    
# print(longest_substring_unique_1('dvdf'))

def longest_substring_unique_2(s):
    if not s:
        return 0
    
    if len(s) == 1:
        return 1
    
    pointer_one = 0
    pointer_two = 0
    buffer = set()
    max_length = 0
    
    while pointer_one < len(s) and pointer_two < len(s):
        if s[pointer_two] not in buffer:
            buffer.add(s[pointer_two])
            pointer_two += 1
            max_length = max(max_length,len(buffer))
            
        else:
            max_length = max(max_length,len(buffer))
            pointer_one += 1
            pointer_two = pointer_one
            buffer = set()
    
    print(buffer)
    return max_length
    
    
# print(longest_substring_unique_2('dvdf'))

def longest_substring_unique_3(s):
    max_length = 0
    if not s:
        return max_length
    
    pointer_one = 0
    contains = set()
    
    for pointer_two, char in enumerate(s):
        while char in contains:
            contains.remove(s[pointer_one])
            pointer_one += 1
        
        contains.add(char)
        max_length = max(max_length, pointer_two - pointer_one + 1)
    return max_length
        
print(longest_substring_unique_3('pwwkew'))
