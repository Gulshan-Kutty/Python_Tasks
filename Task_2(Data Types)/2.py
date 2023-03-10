'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.

Example:

Sample Input
5
2 3 6 6 5

Sample Output
5
'''
n = int(input('Enter the number of participants:'))
arr = map(int, input('Enter the scores:').split())
sort_arr = sorted(arr, reverse=True) # you can also use list_obj.sort() but it changes the original list and retuns None if saved in a variable.
for i in range(len(sort_arr)):
    if sort_arr[i] == sort_arr[0]:
        continue
    else:
        print(sort_arr[i])
        break



# n = int(input('Enter the number of participants:'))
# arr = map(int, input('Enter the scores:').split())
# sort_arr = sorted(arr) # you can also use list_obj.sort() but it changes the original list and retuns None if saved in a variable.
# print(sort_arr[-2]) # it won't work if maximum score is repated more than once