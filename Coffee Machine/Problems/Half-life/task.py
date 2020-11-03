atoms = int(input())
resulting_quantity = int(input())
days = 0

while atoms > resulting_quantity:
    atoms /= 2
    days += 12

print(days)
