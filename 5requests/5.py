import requests

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url, params = "userId=1")

data = r.json()

if __name__ == "__main__":
    for i in data:
        print(i['title'])