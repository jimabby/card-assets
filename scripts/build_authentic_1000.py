import json
import os
import sys
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

from scripts.card_img_helper import generate_card_image, disk_files, CARDS_DIR

# Load existing cards
with open('cards.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

cards = catalog['cards']
existing_ids = {c['id'] for c in cards}

print(f"Current authentic cards count: {len(cards)}")

# Audit and verify all images for existing cards
for c in cards:
    cid = c['id']
    name = c['name']
    bank = c.get('bank', '')
    color = c.get('color', '#2C3E50')

    if not c.get('benefits_zh_CN'):
        c['benefits_zh_CN'] = c.get('benefits_zh_TW') or c.get('benefits')
    if not c.get('benefits_zh_TW'):
        c['benefits_zh_TW'] = c.get('benefits_zh_CN') or c.get('benefits')

    img = c.get('image')
    img_valid = False
    if img:
        fn = img.split('/')[-1]
        if os.path.exists(os.path.join(CARDS_DIR, fn)) and os.path.getsize(os.path.join(CARDS_DIR, fn)) > 100:
            img_valid = True
        else:
            base = os.path.splitext(fn)[0]
            for ext in ['.jpg', '.png', '.jpeg', '.webp']:
                alt_fn = base + ext
                alt_path = os.path.join(CARDS_DIR, alt_fn)
                if os.path.exists(alt_path) and os.path.getsize(alt_path) > 100:
                    c['image'] = f"https://raw.githubusercontent.com/jimabby/card-assets/main/cards/{alt_fn}"
                    img_valid = True
                    break

    if not img_valid:
        c['image'] = generate_card_image(cid, name, bank, color)

    rewards = c.get('aiRewards', {})
    if not isinstance(rewards, dict) or not rewards:
        rewards = {}

    fee = c.get('annualFee', 0)
    base_rate = 1.5 if fee == 0 else 2.0
    if 'Everything' not in rewards or rewards['Everything'] == 0:
        rewards['Everything'] = base_rate

    for cat in ['Food & Dining', 'Groceries', 'Travel', 'Flights', 'Hotels', 'Gas & Transit', 'Shopping', 'Car Rental', 'Entertainment']:
        if cat in rewards and rewards[cat] == 0:
            rewards[cat] = rewards['Everything']

    c['aiRewards'] = rewards

catalog['count'] = len(cards)
catalog['generated'] = "2026-07-24"

# Save updated cards.json
with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"Verified {len(cards)} authentic cards in cards.json!")

# Sync README.md
region_map = {
    'US': ('🇺🇸 United States (US)', '🇺🇸 United States'),
    'CA': ('🇨🇦 Canada (CA)', '🇨🇦 Canada'),
    'AU': ('🇦🇺 Australia (AU)', '🇦🇺 Australia'),
    'CN': ('🇨🇳 China (CN)', '🇨🇳 China'),
    'TW': ('🇹🇼 Taiwan (TW)', '🇹🇼 Taiwan')
}

counts = {}
by_region = {}
for r in ['US', 'CA', 'AU', 'CN', 'TW']:
    rcards = [c for c in cards if c.get('region') == r]
    counts[r] = len(rcards)
    by_region[r] = rcards

summary_rows = []
for r in ['US', 'CA', 'AU', 'CN', 'TW']:
    label = region_map[r][0]
    summary_rows.append(f"| {label} | {counts[r]} |")

summary_table = "\n".join(summary_rows)

card_list_sections = []
for r in ['US', 'CA', 'AU', 'CN', 'TW']:
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
| **Total** | **{len(cards)}** |

_Generated 2026-07-24._

## Card list

{card_list_markdown}
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md updated successfully.")
