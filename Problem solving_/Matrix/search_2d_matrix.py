'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

https://leetcode.com/problems/search-a-2d-matrix/description/
'''


# This works, but time limit exceeds.
class Solution:
    def searchMatrix(self, matrix, target):
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        mid = top + ((bottom - top) // 2)
        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            if matrix[mid][left] <= target <= matrix[mid][right]:
                while left < right:
                    m = left + (right - left) // 2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        left = m + 1
                    else:
                        right = m - 1
            else:
                if target > matrix[mid][right]:
                    top = mid + 1
                elif target < matrix[mid][left]:
                    bottom = mid - 1

        return False



def searchMatrix(matrix, target):
    m,n = len(matrix), len(matrix[0])
    left, right = 0, (m * n) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        i,j = mid // n, mid % n
        if matrix[i][j] == target:
            return True
        elif target > matrix[i][j]:
           left = mid + 1
        else:
            right = mid - 1
    
    return False
     
    
    