import pandas as pd

df = pd.read_csv("clean_data.csv")

# Top 5 repositories
top_repos = df.sort_values(by="stars", ascending=False).head(5)
print("\nTop 5 Repositories:\n", top_repos)

# Most common languages
language_count = df["language"].value_counts()
print("\nLanguages Distribution:\n", language_count)