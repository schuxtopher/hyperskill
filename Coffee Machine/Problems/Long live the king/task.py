column = int(input())
row = int(input())

# out of bounds
oob_left = column == 1
oob_right = column == 8
oob_up = row == 8
oob_down = row == 1

is_corner = (oob_left or oob_right) and (oob_down or oob_up)
is_edge = (oob_left or oob_right or oob_up or oob_down) and not is_corner

if is_corner:
    moves = 3
elif is_edge:
    moves = 5
else:
    moves = 8

print(moves)
