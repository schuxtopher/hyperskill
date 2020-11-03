from collections import deque

unread_books = deque()
read_books = deque()

for _ in range(int(input())):
    cmd = input().split(' ', 1)

    if cmd[0] == 'BUY':
        unread_books.append(cmd[1])
    elif cmd[0] == 'READ':
        read_books.append(unread_books.pop())

print('\n'.join(read_books))
