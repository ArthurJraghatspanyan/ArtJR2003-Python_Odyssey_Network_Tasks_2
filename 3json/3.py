import json

data = {
  "company": "TechCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Manager"}
      ]
    },
    {
      "name": "Sales",
      "employees": [
        {"id": 3, "name": "Charlie", "role": "Sales Rep"},
        {"id": 4, "name": "Dana", "role": "Sales Lead"}
      ]
    }
  ]
}


with open("company_data.json", "w") as comp_data:
    json.dump(data, comp_data, indent = 2)

with open("company_data.json", "r") as f:
    data_for_read = f.read()

print(data_for_read)