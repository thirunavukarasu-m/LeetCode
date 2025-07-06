'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:
Input: s = "rat", t = "car"

Output: false
'''
def valid_anagram_1(s,t):
    if not s or not t:
        return False
    
    if len(s) != len(t):
        return False
    
    s = set(s)
    for i in t:
        if i not in s:
            return False
    return True
    
# This previous logic has a major Flaw.
# What if the input is s = aacc and t = ccac. This code will return true but the answer is false.ArithmeticError
# We have to keep track of the counts.

def valid_anagram(s,t):
    if not s or not t:
        return False
    
    if len(s) != len(t):
        return False
    
    "anagram"
    temp_dictionary_1 = {
        "a": 3,
        "n" : 1,
        'g': 1,
        'r': 1,
        'm':1
    }
    temp_dictionary_2 = {
        "a": 3,
        "n" : 1,
        'g': 1,
        'r': 1,
        'm':1
    }
    
    
    for i in s:
        if i not in temp_dictionary_1:
            temp_dictionary_1[i] = 1
        else:
            temp_dictionary_1[i] += 1
    
    for j in t:
        if j not in temp_dictionary_2:
            temp_dictionary_2[j] = 1
        else:
            temp_dictionary_2[j] += 1
    return temp_dictionary_1 == temp_dictionary_2
    
print(valid_anagram("bala", "alab"))
# This logic works but is very slow.