order = input().lower()

pizza_menu = "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy"
salad_menu = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup_menu = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"

if order == "pizza":
    print(pizza_menu)
elif order == "salad":
    print(salad_menu)
elif order == "soup":
    print(soup_menu)
else:
    print("Sorry, we don't have it in the menu")
