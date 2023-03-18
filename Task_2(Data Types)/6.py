'''
Question Link:- https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
'''

n = int(input('Enter no of input to enter : '))
t = map(int, input('Enter Input : ').split())
t = tuple(t)
print(hash(t))