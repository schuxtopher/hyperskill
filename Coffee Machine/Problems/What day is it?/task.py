offset = int(input())

if offset > 13:
    day_of_the_week = "Wednesday"
elif offset < -10:
    day_of_the_week = "Monday"
else:
    day_of_the_week = "Tuesday"

print(day_of_the_week)
