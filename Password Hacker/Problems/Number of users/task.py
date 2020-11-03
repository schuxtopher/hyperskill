# write your code here
with open('users.json', 'r') as json_file:
    user_dict = json.load(json_file)
    print(len(user_dict['users']))
