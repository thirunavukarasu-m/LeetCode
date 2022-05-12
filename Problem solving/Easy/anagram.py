# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Input: s = "anagram", t = "nagaram"
# Output: true




def isAnagram(s,t):
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        return False
#         if len(s) != len(t):
#             return False
        
#         s_d = {}
#         t_d = {}
        
#         for i in range(len(s)):
#             s_d[s[i]] = 1 + s_d.get(s[i],0)
#             t_d[t[i]] = 1 + t_d.get(t[i],0)
        
       
#         return s_d == t_d
