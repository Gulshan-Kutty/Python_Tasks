'''
Question Link:- https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''

n = int(input('Enter how many value pairs you want to enter: '))
student_list = {}
for _ in range(n):
    name, *marks = input('Enter name and marks : ').split()
    marks = list(map(float, marks))
    student_list[name] = marks


query_name = input('Enter name for whom you want average: ')
st_marks = student_list[query_name]
s = sum(st_marks)
result = s/len(st_marks)
print('Average marks of {} is {}'.format(query_name,result))