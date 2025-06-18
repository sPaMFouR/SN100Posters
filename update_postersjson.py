import os
import json

folder = 'posters'
posters = []

for f in sorted(os.listdir(folder)):
    if f.endswith('.pdf'):
        base = os.path.splitext(f)[0]
        posters.append({
            "title": base.replace('_', ' ').title(),
            "pdf": f"{folder}/{base}.pdf",
            # "thumb": f"{folder}/{base}_thumb.jpg"
        })

with open('posters.json', 'w') as out:
    json.dump(posters, out, indent=2)
    
print(f"Successfully generate posters.json generated with {len(posters)} posters.")