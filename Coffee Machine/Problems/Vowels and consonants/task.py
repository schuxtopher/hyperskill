sequence = input().lower()

consonant = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"

for char in sequence:

    if char in consonant:
        print("consonant")
        continue

    if char in vowel:
        print("vowel")
        continue

    break
