import json
import csv
import glob

# get latest JSON file
file = sorted(glob.glob("data/trends_*.json"))[-1]

with open(file, "r") as f:
    data = json.load(f)

cleaned = []

for item in data:
    # remove missing values
    if not item["title"] or not item["author"]:
        continue

    cleaned.append(item)

# save CSV
csv_file = file.replace(".json", ".csv")

with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned[0].keys())
    writer.writeheader()
    writer.writerows(cleaned)

print(f"Cleaned data saved to {csv_file}")