import pandas as pd
import json

with open("data.json") as f:
    data = json.load(f)

repos = data['items']

cleaned_data = []

for repo in repos:
    cleaned_data.append({
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "language": repo["language"],
        "url": repo["html_url"]
    })

df = pd.DataFrame(cleaned_data)

# Handle missing values
df["language"].fillna("Unknown", inplace=True)

df.to_csv("clean_data.csv", index=False)

print("Data cleaned and saved!")