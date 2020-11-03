income = int(input())

if income < 15528:
    percent = 0

elif income < 42708:
    percent = 15

elif income < 85415:
    percent = 22

elif income < 132407:
    percent = 26

else:
    percent = 28

calculated_tax = income * percent / 100

print(f"The tax for {income} is {percent}%. That is {calculated_tax:.2f} dollars!")
