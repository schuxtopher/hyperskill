def tallest_people(**people):
    tall_people = [f"{person} : {height}" for person, height in people.items()
                   if height == max(people.values())]
    print('\n'.join(sorted(tall_people)))
