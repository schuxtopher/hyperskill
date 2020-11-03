number_of_units = int(input())

if number_of_units >= 1000:
    category = "legion"

elif number_of_units >= 500:
    category = "swarm"

elif number_of_units >= 50:
    category = "horde"

elif number_of_units >= 10:
    category = "pack"

elif number_of_units >= 1:
    category = "few"

else:
    category = "no army"


print(category)
