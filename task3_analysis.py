import pandas as pd
import glob
import os

# === Load the latest JSON file ===
files = glob.glob("data/trends_*.json") + glob.glob("data/data.json")

if not files:
    print("No data file found in 'data/' folder!")
    print("Make sure you ran the collection script first.")
else:
    latest_file = sorted(files)[-1]   # Get the most recent one
    print(f"Loading file: {latest_file}\n")
    
    # Read JSON file
    df = pd.read_json(latest_file)
    
    # Basic Analysis
    print("Total stories collected:", len(df))
    print("="*50)
    
    print("\nStories per category:")
    print(df["category"].value_counts())
    
    print("\nAverage score per category:")
    print(df.groupby("category")["score"].mean().round(2))
    
    print("\nTop 5 highest scored stories:")
    top5 = df.sort_values(by="score", ascending=False).head(5)
    print(top5[["title", "category", "score", "num_comments"]])
    
    # Optional: Save analysis as CSV for later use
    df.to_csv("data/latest_analysis.csv", index=False)
    print(f"\nAnalysis also saved as: data/latest_analysis.csv")