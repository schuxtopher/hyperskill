smallest_number = input()

if smallest_number != ".":
    smallest_number = float(smallest_number)

    while True:
        new_input = input()

        if new_input == ".":
            break

        new_input = float(new_input)

        if new_input < smallest_number:
            smallest_number = new_input

    print(smallest_number)
