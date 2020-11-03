a = int(input())
b = int(input())
average = 0
counter = 0

for number in range(a, b + 1):
    if number % 3 == 0:
        average += number
        counter += 1

print(average / counter)
