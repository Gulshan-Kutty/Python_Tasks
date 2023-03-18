'''
Question Link:- https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    commands = input().split()
    
    if commands[0] == 'remove':
        s.remove(int(commands[1]))
    elif commands[0] == 'discard':
        s.discard(int(commands[1]))
    elif commands[0] == 'pop':
        s.pop()
print(sum(s))

#OR

# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
# for i in range(N):
#     commands = input().split()
#     if len(commands) > 1:
#         e = int(commands[1])
#     if commands[0] == 'remove':
#         s.remove(e)
#     elif commands[0] == 'discard':
#         s.discard(e)
#     elif commands[0] == 'pop':
#         s.pop()
# print(sum(s))