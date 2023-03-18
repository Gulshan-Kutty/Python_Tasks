'''
Question Link:- https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

Task:
You are given a complex z. Your task is to convert it to polar coordinates.
'''
# import cmath
# com = complex(input('Enter complex equation:'))
# print(cmath.polar(com))

import cmath
com = complex(input('Enter complex equation:'))
res = cmath.polar(com)
res = round(res[0],3), round(res[1],3)
print(res)
print(*res, sep = '\n')

