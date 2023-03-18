'''
Question Link:- https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
'''
T = int(input())
for i in range(T):
    m = int(input())
    A = set(map(int, input().split()))
    n = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))