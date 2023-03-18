'''
Question Link:- https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
'''

m = input()
Eng = input().split()
s1 = set(Eng)
n = input()
Fre = input().split()
s2 = set(Fre)
sym_diff = s1.symmetric_difference(s2)
print(len(sym_diff))