numbers = [int(x) for x in input().split()]
mean = 0

for element in numbers:
    mean += element

print(mean / len(numbers))
