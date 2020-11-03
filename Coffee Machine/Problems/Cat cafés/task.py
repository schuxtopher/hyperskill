best_cafe = ["", 0]

while True:

    new_cafe = input()

    if new_cafe == "MEOW":
        break

    new_cafe = new_cafe.split(" ")
    new_cafe[1] = int(new_cafe[1])

    if new_cafe[1] > best_cafe[1]:
        best_cafe = new_cafe

print(best_cafe[0])
