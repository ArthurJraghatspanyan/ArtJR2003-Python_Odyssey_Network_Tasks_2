import requests

url = "https://jsonplaceholder.typicode.com/invalid-url"

r = requests.get(url)

if r.status_code == 404:
    raise FileNotFoundError("Error 404: Not Found!")
print(f"Status code isL {r.status_code}")