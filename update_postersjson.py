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
        content = base[len("ePoster_"):]
        if ' ' in content:
            title, author = content.rsplit(' ', 1)
        else:
            title = content
            author = "Unknown"
        key = f"{title.strip().lower()}_{author.strip().lower()}"
        entries[key] = {
            "author": author.strip(),
            "title": title.strip(),
            "pdf": f"{folder}/{f}",
            "slide": None
        }

    elif base.startswith("FlashTalk_"):
        content = base[len("FlashTalk_"):]
        if ' ' in content:
            title, author = content.rsplit(' ', 1)
        else:
            title = content
            author = "Unknown"
        key = f"{title.strip().lower()}_{author.strip().lower()}"
        if key in entries:
            entries[key]["slide"] = f"{folder}/{f}"
        else:
            entries[key] = {
                "author": author.strip(),
                "title": title.strip(),
                "pdf": None,
                "slide": f"{folder}/{f}"
            }

posters = list(entries.values())

with open('posters.json', 'w') as out:
    json.dump(posters, out, indent=2)

print(f"Successfully generated posters.json generated with {len(posters)} posters.")
