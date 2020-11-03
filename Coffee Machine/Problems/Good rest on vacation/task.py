duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

total_cost = food_cost * duration + flight_cost * 2 + hotel_cost * (duration - 1)

print(total_cost)
