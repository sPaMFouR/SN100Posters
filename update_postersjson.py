import os
import json

folder = 'posters'
entries = []

# Step 1: Gather FlashTalks
flash_talks = {}
# for f in os.listdir(folder):
for f in os.listdir(folder):
    if f.startswith("FlashTalk_") and f.endswith(".pdf"):
        base = os.path.splitext(f)[0]
        try:
            _, rest = base.split("_", 1)
            title_part, author_part = rest.rsplit("_", 1)
            key = f"{title_part.strip().lower()}_{author_part.strip().lower()}"
            flash_talks[key] = f"{folder}/{f}"
        except ValueError:
            print(f"Skipping malformed FlashTalk filename: {f}")

# Step 2: Build entries only from ePosters
for f in sorted(os.listdir(folder)):
    if not f.startswith("ePoster_") or not f.endswith(".pdf"):
        continue

    base = os.path.splitext(f)[0]
    try:
        _, rest = base.split("_", 1)
        title_part, author_part = rest.rsplit("_", 1)
    except ValueError:
        print(f"Skipping malformed ePoster filename: {f}")
        continue

    title = title_part.strip()
    author = author_part.strip()
    key = f"{title.lower()}_{author.lower()}"

    slide_path = flash_talks.get(key, None)

    entries.append({
        "author": author,
        "title": title,
        "pdf": f"{folder}/{f}",
        "slide": slide_path
    })

# Write to JSON
entries.sort(key=lambda x: x["author"].lower())
with open('posters.json', 'w') as out:
    json.dump(entries, out, indent=2)
print(f"Successfully generated posters.json generated with {len(entries)} posters.")
