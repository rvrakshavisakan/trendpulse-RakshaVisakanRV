import pandas as pd
import matplotlib.pyplot as plt
import os

# Setup
df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)

plt.style.use("default")

# Chart 1: Top 10 Stories by Score
plt.figure(figsize=(12, 6))
top10 = df.nlargest(10, "score")
top10["short_title"] = top10["title"].str[:50] + "..."

plt.barh(top10["short_title"], top10["score"], color="skyblue")
plt.title("Top 10 Stories by Score")
plt.xlabel("Score (Upvotes)")
plt.ylabel("Story Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# Chart 2: Stories per Category
plt.figure(figsize=(10, 6))
cat_counts = df["category"].value_counts()
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
cat_counts.plot(kind="bar", color=colors)
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# Chart 3: Score vs Comments
plt.figure(figsize=(10, 6))
colors = df["is_popular"].map({True: "red", False: "blue"})
plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
plt.title("Score vs Number of Comments")
plt.xlabel("Score (Upvotes)")
plt.ylabel("Number of Comments")
plt.legend(["Popular (score > avg)", "Not Popular"], loc="upper left")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# Bonus Dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Top stories
axes[0,0].barh(top10["short_title"], top10["score"], color="skyblue")
axes[0,0].set_title("Top 10 Stories")
axes[0,0].invert_yaxis()

# Categories
cat_counts.plot(kind="bar", ax=axes[0,1], color=colors)
axes[0,1].set_title("Stories per Category")
axes[0,1].tick_params(axis='x', rotation=45)

# Scatter
axes[1,0].scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
axes[1,0].set_title("Score vs Comments")
axes[1,0].set_xlabel("Score")
axes[1,0].set_ylabel("Comments")

# Empty for layout
axes[1,1].axis('off')

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved successfully in outputs/ folder!")
print("✓ chart1_top_stories.png")
print("✓ chart2_categories.png")
print("✓ chart3_scatter.png")
print("✓ dashboard.png (bonus)")