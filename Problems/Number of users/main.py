import json


with open("users.json", "r") as json_file:
    users_dict = json.load(json_file)
num_users = len(list(users_dict['users']))
print(num_users)


