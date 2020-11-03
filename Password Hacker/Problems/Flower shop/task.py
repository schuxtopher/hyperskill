import itertools

for n in range(3):
    for bouquet in itertools.combinations(flower_names, n + 1):
        print(bouquet)
