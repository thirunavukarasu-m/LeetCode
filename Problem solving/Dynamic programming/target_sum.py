# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3






def findTargetSumWays(nums,target):
    dp = {}
    
    def backtrack(i,total):
    
        if i == len(nums):
            return 1 if total == target else 0
        if (i,total) in dp:
            return dp[(i,total)]
        dp[(i,total)] = (backtrack(i+1,total+nums[i])) + (backtrack(i+1,total-nums[i]))
        
        return dp[(i,total)]
    
    return backtrack(0,0)
        
        
nums = [1,1,1,1,1]

print(findTargetSumWays(nums,3))