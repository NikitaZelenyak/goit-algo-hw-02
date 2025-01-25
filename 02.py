from collections import deque

d = deque()
print(d)  

def is_it_palindrome(string):
    for char in string:
        d.append(char)
    while len(d) > 1:
        if d.popleft() != d.pop():
            print(f'{string} is not a palindrome')
            return False
    print(f'{string} is palindrome')
    
is_it_palindrome('radar') 
is_it_palindrome('hello')