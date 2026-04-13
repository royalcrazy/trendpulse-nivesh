import requests
import json
import time
import os
from datetime import datetime

# Configuration aur Keywords 
HEADERS = {"User-Agent": "TrendPulse/1.0"}
KEYWORDS = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def collect_trending_data():
    all_stories = []
    category_counts = {cat: 0 for cat in KEYWORDS}
    total_needed = 125

    print("Fetching top story IDs...")
    try:
        # collect the 500 storie details from browser
        top_ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_ids_url, headers=HEADERS)
        story_ids = response.json()[:500] 
    except Exception as e:
        print(f"Error fetching top stories: {e}")
        return

    print("Starting data collection (this may take a few minutes)...")
    
    # check the story detail for loop 
    for story_id in story_ids:
        if len(all_stories) >= total_needed:
            break

        try:
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story = requests.get(item_url, headers=HEADERS).json()

            if not story or 'title' not in story:
                continue

            title_lower = story['title'].lower()
            
            # Check matching category
            for category, words in KEYWORDS.items():
                if category_counts[category] < 25:
                    if any(word in title_lower for word in words):
                        
                        story_data = {
                            "post_id": story.get("id"),
                            "title": story.get("title"),
                            "category": category,
                            "score": story.get("score", 0),
                            "num_comments": story.get("descendants", 0),
                            "author": story.get("by"),
                            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        all_stories.append(story_data)
                        category_counts[category] += 1
                        print(f"Match found [{category}]: {story['title'][:50]}...")                  

                        # trigger the sleep timer
                        time.sleep(0.1)
                        break 
        
        except Exception as e:
            print(f"Failed to fetch story {story_id}: {e}")
            continue

    # save into json file 
    if not os.path.exists('data'):
        os.makedirs('data')

    today_date = datetime.now().strftime("%Y%m%d")
    filename = f"data/trends_{today_date}.json"

    with open(filename, 'w') as f:
        json.dump(all_stories, f, indent=4)
        
    print(f"\nCollected {len(all_stories)} stories. Saved to {filename}")

if __name__ == "__main__":
    collect_trending_data()
