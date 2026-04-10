import requests
import json

url = "https://api.github.com/search/repositories?q=stars:>10000&sort=stars"

response = requests.get(url)
data = response.json()



with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data fetched and saved!")