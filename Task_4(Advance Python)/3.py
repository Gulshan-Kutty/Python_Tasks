'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer
'''
class Solution:
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        
        firstbit = xor & (xor-1) ^ xor
        num1 = 0
        for n in nums:
            if n & firstbit:
                num1 ^= n
        return [num1,num1^xor]
    
n = [1,2,1,3,2,5]
obj = Solution()
print(obj.singleNumber(n))