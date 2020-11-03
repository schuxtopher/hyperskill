number = int(input())
divisor = 2

while True:
    if number == 1:
        print("This number is not prime")
        break

    if divisor == number:
        print("This number is prime")
        break

    if number % divisor == 0:
        print("This number is not prime")
        break

    divisor += 1
