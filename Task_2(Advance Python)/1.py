'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''
class Solution:
    def defangIPaddr(self,address):
        address = address.split('.')
        return '[.]'.join(address)

ip = input('Enter any IP address:')
obj = Solution()
result = obj.defangIPaddr(ip)
print(result)