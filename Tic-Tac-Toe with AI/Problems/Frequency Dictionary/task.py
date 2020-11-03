# put your python code here
sequence = input().lower().split()
dictionary = {key: sequence.count(key) for key in sequence}

for key, item in dictionary.items():
    print(key, item)
