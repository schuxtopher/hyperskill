from collections import deque

number_of_operations = int(input())
queue = deque()

for _ in range(number_of_operations):
    operation = input().split()

    if operation[0] == 'ENQUEUE':
        queue.appendleft(operation[1])
    elif operation[0] == 'DEQUEUE':
        queue.pop()

while queue:
    print(queue.pop())
