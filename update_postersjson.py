import os
import json

folder = 'posters'
entries = {}

# for f in sorted(os.listdir(folder)):
#     if f.endswith('.pdf'):
#         base = os.path.splitext(f)[0]
#         if ' - ' in base:
#             author, title = base.split(' - ', 1)
#         else:
#             author = "Unknown"
#             title = base
#         posters.append({
#             "author": author.strip(),
#             "title": title.strip(),
#             "pdf": f"{folder}/{f}"
#         })

for f in sorted(os.listdir(folder)):
    if not f.endswith('.pdf'):
        continue

    base = os.path.splitext(f)[0]

    if base.startswith("ePoster_"):
        parts = base[len("ePoster_"):].rsplit('_', 1)
        if len(parts) == 2:
            title, author = parts
        else:
            title = parts[0]
            author = "Unknown"
        key = f"{title.strip().lower()}_{author.strip().lower()}"
        entries[key] = {
            "author": author.strip(),
            "title": title.strip(),
            "pdf": f"{folder}/{f}",
            "slide": None  # to be updated if FlashTalk exists
        }

    elif base.startswith("FlashTalk_"):
        parts = base[len("FlashTalk_"):].rsplit('_', 1)
        if len(parts) == 2:
            title, author = parts
        else:
            title = parts[0]
            author = "Unknown"
        key = f"{title.strip().lower()}_{author.strip().lower()}"
        if key in entries:
            entries[key]["slide"] = f"{folder}/{f}"
        else:
            # Create new entry with slide only, pdf is None
            entries[key] = {
                "author": author.strip(),
                "title": title.strip(),
                "pdf": None,
                "slide": f"{folder}/{f}"
            }

# Convert to list
posters = list(entries.values())

with open('posters.json', 'w') as out:
    json.dump(posters, out, indent=2)

print(f"Successfully generated posters.json generated with {len(posters)} posters.")
