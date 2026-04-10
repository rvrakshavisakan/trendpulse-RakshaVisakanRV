import requests
import json
import os
import time
from datetime import datetime

# Headers as required
headers = {"User-Agent": "TrendPulse/1.0"}

# Keyword mapping for categorization (case-insensitive)
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title_lower = title.lower()
    for cat, keywords in CATEGORIES.items():
        if any(kw in title_lower for kw in keywords):
            return cat
    return "technology"  # default if no match

# Step 1: Create data folder
os.makedirs("data", exist_ok=True)

# Step 2: Get top story IDs
print("Fetching top stories IDs...")
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", headers=headers)
if response.status_code != 200:
    print("Failed to fetch top stories")
    exit()

story_ids = response.json()[:500]  # first 500

stories = []
collected_count = {cat: 0 for cat in CATEGORIES.keys()}

print("Fetching story details...")

for i, story_id in enumerate(story_ids):
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        resp = requests.get(url, headers=headers)
        
        if resp.status_code != 200:
            print(f"Failed to fetch story {story_id}")
            continue
            
        story = resp.json()
        
        if not story or "title" not in story:
            continue
            
        category = get_category(story["title"])
        
        # Limit to 25 per category
        if collected_count[category] >= 25:
            continue
            
        story_data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().isoformat()
        }
        
        stories.append(story_data)
        collected_count[category] += 1
        
        # Progress
        if len(stories) % 20 == 0:
            print(f"Collected {len(stories)} stories...")
            
    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")
        continue

# Save to JSON
date_str = datetime.now().strftime("%Y%m%d")


with open(data.json, "w", encoding="utf-8") as f:
    json.dump(stories, f, indent=2, ensure_ascii=False)

print(f"\nCollected {len(stories)} stories. Saved to {filename}")