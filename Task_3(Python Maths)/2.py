'''
Question link:- https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
'''

import math
AB = int(input('Enter side 1:'))
BC = int(input('Enter side 2:'))
AC = math.sqrt(AB**2+BC**2)
print(AC)
angle = math.acos(BC/AC)
print(angle)
print(str(round(math.degrees(angle)))+ chr(176)) # chr(176) means degree symbol