mean = 0
count = 0

while True:
    stream = input()

    if stream == ".":
        break

    mean += int(stream)
    count += 1

print(mean / count)
