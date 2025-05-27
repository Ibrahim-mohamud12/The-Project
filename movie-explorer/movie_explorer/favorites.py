import json
from pathlib import Path

FAV_FILE = Path("favorites.json")

def load_favorites():
    if FAV_FILE.exists():
        with open(FAV_FILE) as f:
            return json.load(f)
    return []

def save_favorite(movie):
    favs = load_favorites()
    if movie not in favs:
        favs.append(movie)
        with open(FAV_FILE, 'w') as f:
            json.dump(favs, f, indent=2)
