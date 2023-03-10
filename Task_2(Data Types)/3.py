'''
Question Link:- https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
'''
list = []
second_lowest_names = []
scores = set()

for i in range(int(input("Enter number of students:"))):
    name = input("Enter Name : ")
    score = float(input("Enter Score : "))
    list.append([name, score])
    scores.add(score)

second_lowest = sorted(scores)[1]

for name, score in list:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name)