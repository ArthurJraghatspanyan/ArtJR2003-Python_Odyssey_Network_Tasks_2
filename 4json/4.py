import json

with open("user_data.json") as user_data:
    data = json.load(user_data)


ls = []
for item in data:
    if item['age'] > 30 and item['role'] == 'manager':
        ls.append(item)

with open("filtered_users.json", 'w') as filtered_data:
    json.dump(ls, filtered_data, indent=2)