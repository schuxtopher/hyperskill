# put your python code here
sequence = input().split()
target = input()
positions = [str(index) for index in range(0, len(sequence)) if sequence[index] == target]
print(" ".join(positions) if positions else "not found")
