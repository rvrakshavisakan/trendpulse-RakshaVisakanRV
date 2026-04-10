import pandas as pd
import matplotlib.pyplot as plt
import glob

# === Find the latest JSON file ===
files = glob.glob("data/data.json") + glob.glob("data/trends_*.json")

if not files:
    print("❌ No data file found!")
    print("Please run your collection script first (task_data_collection.py)")
else:
    latest_file = sorted(files)[-1]
    print(f"✅ Loading: {latest_file}\n")
    
    # Load the JSON file
    df = pd.read_json(latest_file)
    
    print(f"Total stories: {len(df)}\n")
    
    # Plot 1: Stories per Category
    plt.figure(figsize=(8, 5))
    df["category"].value_counts().plot(kind="bar", color='skyblue')
    plt.title("Number of Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot 2: Average Score per Category
    plt.figure(figsize=(8, 5))
    df.groupby("category")["score"].mean().plot(kind="bar", color='coral')
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Optional: Top 10 stories by score
    print("\nTop 10 Highest Scored Stories:")
    print(df.sort_values(by="score", ascending=False)[["title", "category", "score"]].head(10))