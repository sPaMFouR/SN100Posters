import os
import json

folder = 'posters'
posters = []

for f in sorted(os.listdir(folder)):
    if f.endswith('.pdf'):
        base = os.path.splitext(f)[0]
        if ' - ' in base:
            author, title = base.split(' - ', 1)
        else:
            author = "Unknown"
            title = base
        posters.append({
            "author": author.strip(),
            "title": title.strip(),
            "pdf": f"{folder}/{f}"
        })

with open('posters.json', 'w') as out:
    json.dump(posters, out, indent=2)

print(f"Successfully generated posters.json generated with {len(posters)} posters.")