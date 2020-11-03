for number in range(1, 11):
    with open(f'file{number}.txt', 'w') as file:
        print(f'{number}', file=file, flush=True)
