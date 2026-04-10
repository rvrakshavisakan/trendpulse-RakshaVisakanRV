import pandas as pd
import os
from datetime import datetime

# Load JSON
print("Loading JSON file...")
json_files = [f for f in os.listdir("data") if f.startswith("trends_") and f.endswith(".json")]
latest_file = max(json_files)  # get latest
df = pd.read_json(f"data/{latest_file}")

print(f"Loaded {len(df)} stories from {latest_file}")

# Cleaning
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip whitespace
df["title"] = df["title"].str.strip()

# Save as CSV
os.makedirs("data", exist_ok=True)
df.to_csv("data/trends_clean.csv", index=False)

print(f"\nSaved {len(df)} rows to data/trends_clean.csv")

# Summary
print("\nStories per category:")
print(df["category"].value_counts().sort_index())