scores = input().split()

lives = 3
score = 0

for answer in scores:

    if lives == 0:
        print("Game over")
        break

    if answer == "I":
        lives -= 1
        continue

    if answer == "C":
        score += 1
        continue

else:
    print("You won")

print(score)
