total_h = int(input())

triangle = [((2 * h - 1) * '#').center(2 * total_h - 1) for h in range(1, total_h + 1)]

print('\n'.join(triangle))
