string = input()
string = string.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

print(string.lower())
