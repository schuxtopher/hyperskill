from collections import deque
n = int(input())
issues = deque()

for _ in range(n):
    log = input().split()

    if log[0] == 'ISSUE':
        issues.appendleft(log[1])
    elif log[0] == 'SOLVED':
        issues.pop()

while issues:
    print(issues.pop())
