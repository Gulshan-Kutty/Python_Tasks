'''
Question Link:- https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
'''

N = int(input())
lst = list()
for i in range(N):
    inp = input().split() # it takes all inputs as strings
        
    if inp[0] == 'insert':
        lst.insert(int(inp[1]), int(inp[2]))
    if inp[0] == 'print':
        print(lst)
    if inp[0] == 'remove':
        lst.remove(int(inp[1]))
    if inp[0] == 'append':
        lst.append(int(inp[1]))
    if inp[0] == 'sort':
        lst.sort()
    if inp[0] == 'pop':
        lst.pop()
    if inp[0] == 'reverse':
        lst.reverse()


#OR

# N = int(input())
# lst = list()
# for i in range(N):
#     inp = input().split() # it takes all inputs as strings
    
#     if len(inp) == 2:
#         x = int(inp[1])
#     if len(inp) == 3:
#         x = int(inp[1])
#         y = int(inp[2])
#     if inp[0] == 'insert':
#         lst.insert(x, y)
#     if inp[0] == 'print':
#         print(lst)
#     if inp[0] == 'remove':
#         lst.remove(x)
#     if inp[0] == 'append':
#         lst.append(x)
#     if inp[0] == 'sort':
#         lst.sort()
#     if inp[0] == 'pop':
#         lst.pop()
#     if inp[0] == 'reverse':
#         lst.reverse()
    