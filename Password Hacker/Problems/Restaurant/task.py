import itertools


food_combinations = itertools.product(main_courses, desserts, drinks)
price_combinations = itertools.product(price_main_courses, price_desserts, price_drinks)

for menu, price in zip(food_combinations, price_combinations):
    total = sum(price)
    if total < 31:
        print(' '. join(menu), total)
