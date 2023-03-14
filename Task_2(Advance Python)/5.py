'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

class Solution:
    def subtractProductAndSum(self, n):
        prod, sum = 1,0
        for i in str(n):
            prod *= int(i)
            sum += int(i)
        return (prod-sum)
    
num = int(input('Enter any number:'))
obj = Solution()
result = obj.subtractProductAndSum(num)
print(result)