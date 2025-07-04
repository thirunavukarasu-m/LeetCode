'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]

Output: [[""]]

Example 3:
Input: strs = ["a"]

Output: [["a"]]

https://leetcode.com/problems/group-anagrams/description/
'''

def group_anagrams_1(strings):
    if not strings:
        return []
    temp_dict = {}

    for index, string in enumerate(strings):
        temp_string = ''.join(sorted(string))
        if temp_string not in temp_dict:
            temp_dict[temp_string] = [string]
        else:
           temp_dict[temp_string].append(string)
    return list(temp_dict.values())
print(group_anagrams_1(["eat","tea","tan","ate","nat","bat"]))
#
import collections
def group_anagrams_2(strings):
    if not strings:
        return []
    temp_dict = collections.defaultdict(list)

    for string in strings:
        temp_string = str(sorted(string))
        temp_dict[temp_string].append(string)
    return list(temp_dict.values())
    
print(group_anagrams_2(["eat","tea","tan","ate","nat","bat"]))
