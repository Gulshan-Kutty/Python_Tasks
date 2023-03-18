'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12
'''
class Solution:
    def maxProduct(self,nums):
        max_1 = max(nums)
        max_2 = sorted(nums)
        max_2 = max_2[-2]
        return (max_1 - 1)*(max_2 - 1)
lst = [3,4,5,2,6]
obj = Solution()
result = obj.maxProduct(lst)
print(result)