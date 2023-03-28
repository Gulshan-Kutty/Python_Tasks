'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

'''
from itertools import combinations

class Solution:
    def subsets(self, nums):
        return [lst for lsts in [list(combinations(nums,i)) for i in range(len(nums)+1)] for lst in lsts]

lst = [1,2,3]    
obj = Solution()
print(obj.subsets(lst))