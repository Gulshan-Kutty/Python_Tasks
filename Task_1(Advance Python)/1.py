'''
Running Sum of 1D Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
'''
class Solution:
    def runningsum(self,inp):
        sum = 0
        out = []
        for i in inp:
            sum += i
            out.append(sum)
        return out

input = [1,2,3,4,5]
s = Solution()
output = s.runningsum(input) # out value is stored in output
print(output)
# OR
# print(s.runningsum(input))