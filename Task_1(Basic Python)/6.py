'''Question Link:- https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true'''

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
    
    return leap

year = int(input('Enter the year:'))
print(is_leap(year))