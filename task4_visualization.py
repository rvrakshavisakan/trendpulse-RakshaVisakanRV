import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_data.csv")
language_count = df["language"].value_counts().head(5)
plt.figure()
language_count.plot(kind="bar")
plt.title("Top Programming Languages (Trending Repos)")
plt.xlabel("Language")
plt.ylabel("Count")
plt.show()