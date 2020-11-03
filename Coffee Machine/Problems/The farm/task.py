chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

money = int(input())

if money >= sheep_price:
    number_of_animals = money // sheep_price
    animal = "sheep"
    print(str(number_of_animals), animal)

elif money >= cow_price:
    number_of_animals = money // cow_price
    animal = "cow" if number_of_animals == 1 else "cows"
    print(str(number_of_animals), animal)

elif money >= pig_price:
    number_of_animals = money // pig_price
    animal = "pig" if number_of_animals == 1 else "pigs"
    print(str(number_of_animals), animal)

elif money >= goat_price:
    number_of_animals = money // goat_price
    animal = "goat" if number_of_animals == 1 else "goats"
    print(str(number_of_animals), animal)

elif money >= chicken_price:
    number_of_animals = money // chicken_price
    animal = "chicken" if number_of_animals == 1 else "chickens"
    print(str(number_of_animals), animal)

else:
    print("None")
