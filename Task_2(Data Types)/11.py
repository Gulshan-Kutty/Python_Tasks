'''
Question Link:- https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

'''
n = int(input())
s = set()

for i in range(n):
    val = input()
    s.add(val)

print(len(s))