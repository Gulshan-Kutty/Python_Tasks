'''
Question Link:- https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
'''

def print_full_name(first, last):
    st = "Hello {} {}! You just delved into python."
    return (st.format(first,last))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))