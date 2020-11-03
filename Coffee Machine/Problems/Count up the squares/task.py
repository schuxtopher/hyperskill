squares = 0
input_sum = 0

while True:
    new_number = int(input())
    input_sum += new_number
    squares += new_number ** 2

    if input_sum == 0:
        break

print(squares)
