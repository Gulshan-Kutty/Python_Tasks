'''
Question Link:- https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
'''

def operations():
    global output
    op_with_len = input().split()
    operation = op_with_len[0]
    
    updater_set = set(map(int, input().split()))
    if operation == 'intersection_update':
        a.intersection_update(updater_set)
    if operation == 'update':
        a.update(updater_set)
    if operation == 'symmetric_difference_update':
        a.symmetric_difference_update(updater_set)
    if operation == 'difference_update':
        a.difference_update(updater_set)
    output = sum(a)
    
    
n = int(input())
a = set(map(int, input().split()))
N = int(input())
for i in range(N):
    operations()
print(output)