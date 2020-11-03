animals = open('animals.txt', 'r')
animals_new = open('animals_new.txt', 'w')

animals_new.write(animals.read().replace('\n', ' '))

animals.close()
animals_new.close()
