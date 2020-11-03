from collections import deque

brackets = deque()
term = input()

try:
    for i in term:
        if i == '(':
            brackets.append(i)
        elif i == ')':
            brackets.pop()
    assert not brackets
except (IndexError, AssertionError):
    print('ERROR')
else:
    print('OK')
