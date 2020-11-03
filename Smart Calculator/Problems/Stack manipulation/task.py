stack = []
for n in range(int(input())):
    string = input().split()
    if string[0] == 'PUSH':
        stack.append(string[1])
    if string[0] == 'POP':
        stack.pop()

print('\n'.join(reversed(stack)))
