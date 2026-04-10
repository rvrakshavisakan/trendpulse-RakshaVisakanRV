import requests
import json
import os
import time
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}

keywords = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm","programming"],
    "worldnews": ["war","government","country","president","election","climate","attack","global","india","china"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship","cricket"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome","quantum"],
    "entertainment": ["movie","film","music","netflix","book","show","award","streaming","actor"]
}

def categorize(title):
    title = title.lower()
    for category, words in keywords.items():
        if any(word in title for word in words):
            return category
    return None

# === Main Collection ===
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", 
                       headers=headers, timeout=20)
top_ids = response.json()[:100]   # Reduced to 100 for stability

counts = {cat: 0 for cat in keywords}
data = []

for story_id in top_ids:
    try:
        res = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", 
                          headers=headers, timeout=8)
        
        if res.status_code == 200:
            story = res.json()
            title = story.get("title", "")
            category = categorize(title)

            if category and counts[category] < 25:
                data.append({
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score"),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                counts[category] += 1

        time.sleep(0.6)   # Increased delay to prevent hanging

        if all(v >= 25 for v in counts.values()):
            break

    except:
        time.sleep(1)
        continue

# Save to data.json (fixed name, overwrites every time)
os.makedirs("data", exist_ok=True)

with open("data/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Done! Collected {len(data)} stories")
print("📁 Saved to: data/data.json")