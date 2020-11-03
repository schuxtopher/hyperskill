sequence = input().split()
print(''.join([sequence[0].lower()] + [word.capitalize() for word in sequence[1:]]))
