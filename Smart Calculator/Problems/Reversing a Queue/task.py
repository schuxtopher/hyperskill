from collections import deque

reversed_queue = deque()

while queue:
    reversed_queue.append(queue.pop())
