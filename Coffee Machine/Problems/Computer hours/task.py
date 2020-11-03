# Make sure your output matches the assignment *exactly*
time_spend = int(input())

if time_spend < 2:
    print("That seems reasonable")
elif time_spend < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")
