from collections import deque

num_of_records = int(input())
students = deque()
passed_students = deque()

for _ in range(num_of_records):
    log = input().split()

    if log[0] == 'READY':
        students.appendleft(log[1])
    elif log[0] == 'PASSED':
        passed_students.appendleft(students.pop())
    elif log[0] == 'EXTRA':
        students.appendleft(students.pop())

while passed_students:
    print(passed_students.pop())
