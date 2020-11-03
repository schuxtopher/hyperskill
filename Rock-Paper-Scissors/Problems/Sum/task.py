file = open('sums.txt', 'r')
lines = file.readlines()
file.close()

for numbers in lines:
    print(sum(map(int, numbers.split())))
