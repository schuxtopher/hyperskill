guest_list = []

while True:

    guest = input()

    if guest == ".":
        break

    guest_list.append(guest)

print(guest_list)
print(len(guest_list))
