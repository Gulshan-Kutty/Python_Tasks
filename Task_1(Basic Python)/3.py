'''
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers
'''

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

print('Sum of {} & {} = {}'.format(a,b,a+b))
print('Difference of {} & {} = {}'.format(a,b,a-b))
print('Product of {} & {} = {}'.format(a,b,a*b))