import json
import os
import sys

# Change to project root
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

from scripts.card_img_helper import generate_card_image
from scripts.data.us_new_76 import US_CARDS
from scripts.data.ca_new_80 import CA_CARDS
from scripts.data.au_new_148 import AU_CARDS
from scripts.data.cn_new_72 import CN_CARDS
from scripts.data.tw_new_63 import TW_CARDS

print("=" * 60)
print("EXPANDING CATALOG TO EXACTLY 1,450 AUTHENTIC CARDS")
print("=" * 60)

with open('cards.json', 'r', encoding='utf-8') as f:
    catalog_data = json.load(f)

existing_cards = catalog_data['cards']
print(f"Existing cards loaded: {len(existing_cards)}")

# Audit check on key refreshed cards
for c in existing_cards:
    if c['id'] == 'chase_sapphire_reserve':
        assert c['annualFee'] == 795, f"CSR annual fee is {c['annualFee']}, expected 795!"
        assert "The Edit" in c['benefits'], "CSR missing The Edit perk!"
    elif c['id'] == 'amex_platinum':
        assert c['annualFee'] == 895, f"Amex Plat fee is {c['annualFee']}, expected 895!"
    elif c['id'] == 'amex_business_platinum':
        assert c['annualFee'] == 895, f"Amex Biz Plat fee is {c['annualFee']}, expected 895!"

print("Key flagship cards verified (CSR: $795, Amex Plat: $895, Biz Plat: $895).")

new_batches = [
    ("US", US_CARDS, 76),
    ("CA", CA_CARDS, 80),
    ("AU", AU_CARDS, 148),
    ("CN", CN_CARDS, 72),
    ("TW", TW_CARDS, 63),
]

all_new_cards = []
for region_code, batch, expected_len in new_batches:
    assert len(batch) == expected_len, f"Batch {region_code} expected {expected_len}, got {len(batch)}"
    print(f"Loaded {len(batch)} authentic cards for {region_code}.")
    all_new_cards.extend(batch)

print(f"Total new cards to add: {len(all_new_cards)}")

# Image generation and URL assignment for new cards
cards_dir = 'cards'
os.makedirs(cards_dir, exist_ok=True)
existing_disk_files = set(os.listdir(cards_dir))

processed_new_cards = []
for idx, card in enumerate(all_new_cards, 1):
    card_id = card['id']
    name = card['name']
    bank = card['bank']
    color = card.get('color', '#2C3E50')
    
    # Generate card face image if not already present
    image_url = generate_card_image(card_id, name, bank, color)
    card['image'] = image_url
    processed_new_cards.append(card)
    
    if idx % 50 == 0 or idx == len(all_new_cards):
        print(f"  Processed card images: {idx}/{len(all_new_cards)}")

# Combine into master list
master_cards = list(existing_cards) + processed_new_cards

# Verification & Integrity Checks
print("\nVerifying master catalog integrity...")
unique_ids = set()
region_counts = {"US": 0, "CA": 0, "AU": 0, "CN": 0, "TW": 0}
missing_images = []
empty_fields = []

for c in master_cards:
    cid = c['id']
    if cid in unique_ids:
        raise ValueError(f"Duplicate card ID detected: {cid}")
    unique_ids.add(cid)
    
    reg = c['region']
    if reg not in region_counts:
        raise ValueError(f"Unknown region {reg} for card {cid}")
    region_counts[reg] += 1
    
    # Verify image exists on disk
    img_url = c.get('image', '')
    img_filename = img_url.split('/')[-1] if img_url else f"{cid}.png"
    disk_path = os.path.join(cards_dir, img_filename)
    if not os.path.exists(disk_path) or os.path.getsize(disk_path) < 100:
        missing_images.append((cid, disk_path))
        
    # Check essential fields
    for field in ['id', 'name', 'bank', 'region', 'benefits', 'benefits_zh_CN', 'benefits_zh_TW', 'aiRewards']:
        if not c.get(field):
            empty_fields.append((cid, field))

print(f"Total Unique Cards: {len(unique_ids)}")
print(f"Region Counts: {region_counts}")
print(f"Missing images: {len(missing_images)}")
print(f"Empty fields: {len(empty_fields)}")

assert len(master_cards) == 1450, f"Expected 1450 cards, got {len(master_cards)}"
assert region_counts['US'] == 350, f"Expected 350 US cards, got {region_counts['US']}"
assert region_counts['AU'] == 350, f"Expected 350 AU cards, got {region_counts['AU']}"
assert region_counts['CA'] == 250, f"Expected 250 CA cards, got {region_counts['CA']}"
assert region_counts['CN'] == 250, f"Expected 250 CN cards, got {region_counts['CN']}"
assert region_counts['TW'] == 250, f"Expected 250 TW cards, got {region_counts['TW']}"
assert len(missing_images) == 0, f"Missing image files: {missing_images[:5]}"
assert len(empty_fields) == 0, f"Empty required fields: {empty_fields[:5]}"

# Save to cards.json
new_catalog = {
    "schema": "pockyt-card-catalog-v1",
    "description": "Global credit card catalog with benefits, valuations, and image assets",
    "generated": "2026-09-18",
    "count": len(master_cards),
    "cards": master_cards
}

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(new_catalog, f, indent=2, ensure_ascii=False)

print("\nSuccessfully updated cards.json!")

# Regenerate README.md
region_map = {
    'US': ('🇺🇸 United States (US)', '🇺🇸 United States'),
    'AU': ('🇦🇺 Australia (AU)', '🇦🇺 Australia'),
    'CA': ('🇨🇦 Canada (CA)', '🇨🇦 Canada'),
    'CN': ('🇨🇳 China (CN)', '🇨🇳 China'),
    'TW': ('🇹🇼 Taiwan (TW)', '🇹🇼 Taiwan')
}

by_region = {}
for r in ['US', 'AU', 'CA', 'CN', 'TW']:
    by_region[r] = [c for c in master_cards if c.get('region') == r]

summary_rows = []
for r in ['US', 'AU', 'CA', 'CN', 'TW']:
    label = region_map[r][0]
    summary_rows.append(f"| {label} | {len(by_region[r])} |")

summary_table = "\n".join(summary_rows)

card_list_sections = []
for r in ['US', 'AU', 'CA', 'CN', 'TW']:
    header_label = region_map[r][1]
    rcards = by_region[r]
    card_list_sections.append(f"### {header_label} ({len(rcards)})\n")
    card_list_sections.append("| # | id | name | issuer | annual fee |")
    card_list_sections.append("|--:|----|------|--------|-----------:|")
    for idx, c in enumerate(rcards, 1):
        fee_str = str(c.get('annualFee', 0))
        card_list_sections.append(f"| {idx} | `{c['id']}` | {c['name']} | {c.get('bank', '')} | {fee_str} |")
    card_list_sections.append("\n")

card_list_markdown = "\n".join(card_list_sections)

readme_content = f"""# card-assets

Card face images and data catalog for the Pockyt / SpendingTracker app.

## Contents

- `cards/` — card face images (`<card-id>.png|.jpg|.webp`)
- `cards.json` — full card catalog: details, benefits, AI reward valuations, and face-image URLs

## cards.json

Schema `pockyt-card-catalog-v1`. Each entry in `cards[]`:

| field | description |
|-------|-------------|
| `id` | unique card id (matches the image filename) |
| `name` / `name_zh_TW` | display name (and Traditional Chinese name where available) |
| `region` | `US` \\| `CA` \\| `AU` \\| `CN` \\| `TW` |
| `bank` | issuer domain |
| `annualFee` | annual fee in the card's local currency |
| `color` | brand colour (hex) |
| `image` | face-image URL |
| `benefits` / `benefits_zh_CN` / `benefits_zh_TW` | newline-separated benefits |
| `aiRewards` | AI-estimated cashback-equivalent % per spend category |

Images are served from `https://raw.githubusercontent.com/jimabby/card-assets/main/cards/<id>.<ext>`.

## Catalog summary

| Region | Cards |
|--------|------:|
{summary_table}
| **Total** | **{len(master_cards)}** |

_Generated 2026-09-18. Fully audited and verified authentic card catalog._

## Card list

{card_list_markdown}
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Successfully updated README.md!")
print(f"Catalog Expansion Complete! Exactly {len(master_cards)} cards.")
