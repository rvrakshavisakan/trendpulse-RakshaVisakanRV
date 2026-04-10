import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data/trends_clean.csv")
print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Basic stats
print(f"\nAverage score   : {df['score'].mean():,.0f}")
print(f"Average comments: {df['num_comments'].mean():,.0f}")

# NumPy analysis
scores = df["score"].to_numpy()

print("\n--- NumPy Stats ---")
print(f"Mean score    : {np.mean(scores):,.0f}")
print(f"Median score  : {np.median(scores):,.0f}")
print(f"Std deviation : {np.std(scores):,.0f}")
print(f"Max score     : {np.max(scores):,}")
print(f"Min score     : {np.min(scores)}")

# Most stories category
most_common_cat = df["category"].value_counts().idxmax()
print(f"\nMost stories in: {most_common_cat} ({df['category'].value_counts().max()} stories)")

# Most commented story
most_commented = df.loc[df["num_comments"].idxmax()]
print(f"Most commented story: \"{most_commented['title']}\" — {most_commented['num_comments']} comments")

# New columns
avg_score = df["score"].mean()
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Save
df.to_csv("data/trends_analysed.csv", index=False)
print("\nSaved to data/trends_analysed.csv")