phone_number = input()
names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for digit in phone_number:
    print(names[int(digit)])
