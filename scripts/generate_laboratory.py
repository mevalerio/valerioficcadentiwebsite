import subprocess
import sys

# Auto-install missing packages
required = {"bibtexparser", "python-slugify", "requests"}
installed = {pkg.key for pkg in __import__("pkg_resources").working_set}
missing = required - installed
if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

import os
import re
import bibtexparser
import requests
from slugify import slugify
from pathlib import Path

# === Static info ===
# Enriched author metadata
DATA = {
    "Marcel Ausloos": {
        "Affiliations": [
            "University of Leicester, UK",
            "Academia de Studii Economice din Bucureşti, Romania"
        ],
        "Links": [
            "https://le.ac.uk/people/marcel-ausloos",
            "https://www.ase.ro/en/"
        ],
        "ORCID": "0000-0001-9973-0019"
    },
    "Valerio Ficcadenti": {
        "Affiliations": ["London South Bank University, Business School, UK"],
        "Links": ["https://www.lsbu.ac.uk/about-us/people/valerio-ficcadenti"],
        "ORCID": "0000-0001-8786-8213"
    },
    "Gurjeet Dhesi": {
        "Affiliations": ["University of Leicester, UK"],
        "Links": ["https://le.ac.uk/people/gurjeet-dhesi"],
        "ORCID": "0000-0002-5596-3010"
    },
    "Muhammad Shakeel": {
        "Affiliations": ["University of Leicester, UK"],
        "Links": ["https://le.ac.uk/people/muhammad-shakeel"],
        "ORCID": None
    },
    "Roy Cerqueti": {
        "Affiliations": [
            "Sapienza University of Rome, Italy",
            "University of Macerata, Italy (former)"
        ],
        "Links": [
            "https://www.uniroma1.it/en/personale/roy-cerqueti",
            "https://docenti.unimc.it/roy.cerqueti"
        ],
        "ORCID": "0000-0002-1871-7371"
    },
    "Matteo Cinelli": {
        "Affiliations": ["Sapienza University of Rome, Italy"],
        "Links": ["https://cinhelli.github.io"],
        "ORCID": "0000-0003-3899-4592"
    },
    "Jessica Riccioni": {
        "Affiliations": ["Sapienza University of Rome, Italy"],
        "Links": [],
        "ORCID": "0000-0003-2718-5669"
    },
    "Parmjit Kaur": {
        "Affiliations": ["University of Leicester, UK"],
        "Links": ["https://le.ac.uk/people/parmjit-kaur"],
        "ORCID": "0000-0001-5031-9704"
    },
    "Stefano Marmani": {
        "Affiliations": ["Affiliation not found (likely Italian institution)"],
        "Links": [],
        "ORCID": None
    },
    "Ciro Hosseini Varde’i": {
        "Affiliations": ["Affiliation not found"],
        "Links": [],
        "ORCID": None
    },
    "Francesco Cesarone": {
        "Affiliations": ["University of Rome Tor Vergata, Italy"],
        "Links": ["https://www.uniroma2.it/didattica/docenti/francesco-cesarone"],
        "ORCID": "0000-0003-2326-4204"
    },
    "Raffaele Mattera": {
        "Affiliations": ["Sapienza University of Rome, Italy"],
        "Links": ["https://www.uniroma1.it/en/personale/raffaele-mattera"],
        "ORCID": "0000-0001-8770-7049"
    }
}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = PROJECT_ROOT / "publications.bib"
OUTPUT_DIR = PROJECT_ROOT / "content/laboratory"
DEFAULT_ROLE = "Research Collaborator"

with open(BIB_PATH, encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

author_set = set()
for entry in bib_database.entries:
    if "author" in entry:
        authors = re.split(r"\s+and\s+", entry["author"])
        author_set.update([a.strip() for a in authors])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def get_initials(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        return parts[0][0] + parts[-1][0]
    elif len(parts) == 1:
        return parts[0][0] * 2
    else:
        return "xx"

for author in sorted(author_set):
    slug = slugify(author)
    initials = get_initials(author).lower()
    avatar_file = f"{initials}.jpg"
    folder = os.path.join(OUTPUT_DIR, slug)
    os.makedirs(folder, exist_ok=True)

    info = DATA.get(author, {})
    role = DEFAULT_ROLE
    affiliations = info.get("Affiliations", ["Affiliation Unknown"])
    links = info.get("Links", [])
    orcid = info.get("ORCID", "")

    index_path = os.path.join(folder, "_index.md")
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"---\n")
            f.write(f'title: "{author}"\n')
            f.write(f'role: "{role}"\n')
            f.write(f'organization:\n')
            for aff in affiliations:
                f.write(f"  - \"{aff}\"\n")
            f.write(f'avatar: "{avatar_file}"\n')
            f.write(f'user_groups: ["Laboratory"]\n')
            f.write(f'identifier: "{slug}"\n')
            if links:
                f.write("links:\n")
                for url in links:
                    f.write(f"  - icon: link\n    name: Website\n    url: {url}\n")
            if orcid:
                f.write(f'orcid: "{orcid}"\n')
            f.write(f"---\n")
        print(f"Created: {index_path}")
    else:
        print(f"Skipped: {index_path}")
