'''
Question Link:- https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
'''

M = int(input())
a = set(map(int,input().split()))
N = int(input())
b = set(map(int,input().split()))
result = a.symmetric_difference(b)
sol = sorted(result)
for i in sol:
    print(i)