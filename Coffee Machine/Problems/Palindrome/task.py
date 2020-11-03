word = input()

for letter in range(len(word) // 2):

    if word[letter] != word[len(word) - (letter + 1)]:
        print("Not palindrome")
        break

else:
    print("Palindrome")
