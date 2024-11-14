import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = {
    "userID": 11,
    "title": "Chlp",
    "body": "ChlpChlpChlp"
}

data1 = open('data1.json', 'w')

r1 = requests.get(url)
json.dump(r1.json(), data1, indent=2)


r2 = requests.post(url, response)
json.dump(r2.json(), data1, indent=2)