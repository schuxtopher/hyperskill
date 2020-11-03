# put your python code here
first_number = float(input())
second_number = float(input())
operand = input()

solution = "invalid operation"
error = "Division by 0!"

if operand == "+":
    solution = first_number + second_number
elif operand == "-":
    solution = first_number - second_number
elif operand == "*":
    solution = first_number * second_number
elif operand == "pow":
    solution = first_number ** second_number
elif operand == "/":
    if second_number != 0:
        solution = first_number / second_number
    else:
        solution = error
elif operand == "div":
    if second_number != 0:
        solution = first_number // second_number
    else:
        solution = error
elif operand == "mod":
    if second_number != 0:
        solution = first_number % second_number
    else:
        solution = error

print(solution)
