import os
import re
import bibtexparser
from slugify import slugify
from pathlib import Path

# === Settings ===
BIB_PATH = "publications.bib"
OUTPUT_DIR = "content/laboratory"
DEFAULT_ROLE = "Research Collaborator"
DEFAULT_ORG = "Affiliation Unknown"

# === Load .bib file ===
with open(BIB_PATH, encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# === Extract unique author names ===
author_set = set()

for entry in bib_database.entries:
    if "author" in entry:
        raw_authors = entry["author"]
        authors = re.split(" and ", raw_authors)
        author_set.update([a.strip() for a in authors])

print(f"Found {len(author_set)} unique authors.")

# === Generate folders ===
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def get_initials(name):
    # Split into words, take first letter of first and last parts
    parts = name.strip().split()
    if len(parts) >= 2:
        return parts[0][0] + parts[-1][0]
    elif len(parts) == 1:
        return parts[0][0] * 2  # e.g., "Plato" → "pp"
    else:
        return "xx"

for author in sorted(author_set):
    slug = slugify(author)
    initials = get_initials(author).lower()
    avatar_file = f"{initials}.jpg"

    folder = os.path.join(OUTPUT_DIR, slug)
    os.makedirs(folder, exist_ok=True)

    index_path = os.path.join(folder, "_index.md")
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"""---
title: "{author}"
role: "{DEFAULT_ROLE}"
organization: "{DEFAULT_ORG}"
avatar: "{avatar_file}"
user_groups: ["Laboratory"]
identifier: "{slug}"
---
""")
        print(f"Created: {index_path}")
    else:
        print(f"Skipped (already exists): {index_path}")
