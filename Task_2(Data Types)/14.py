'''
Question Link:- https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
'''

n = int(input())
s1 = set(map(int,input().split()))
b = int(input())
s2 = set(map(int,input().split()))
res = s1.intersection(s2)
print(len(res))