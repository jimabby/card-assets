import json
import os
import sys
import subprocess
import html

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not PROJECT_DIR:
    PROJECT_DIR = '.'
os.chdir(PROJECT_DIR)

CARDS_JSON = 'cards.json'
CARDS_DIR = 'cards'

# Ensure cards directory exists
os.makedirs(CARDS_DIR, exist_ok=True)

disk_files = set(os.listdir(CARDS_DIR))

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def generate_svg(name, bank, hex_color):
    hex_color = (hex_color or '2C3E50').lstrip('#')
    if len(hex_color) != 6:
        hex_color = '2C3E50'
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    top_color = f'rgb({min(255, int(r * 1.1))}, {min(255, int(g * 1.1))}, {min(255, int(b * 1.1))})'
    bot_color = f'rgb({max(0, int(r * 0.7))}, {max(0, int(g * 0.7))}, {max(0, int(b * 0.7))})'
    
    clean_bank = bank.replace('.com', '').replace('.ca', '').replace('.au', '').replace('.cn', '').replace('.tw', '').replace('.org', '').upper()
    display_name = name if len(name) <= 35 else name[:32] + '...'
    
    clean_bank_esc = html.escape(clean_bank)
    display_name_esc = html.escape(display_name)
    
    svg = f'''<svg width="600" height="380" viewBox="0 0 600 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{top_color}" />
      <stop offset="100%" stop-color="{bot_color}" />
    </linearGradient>
    <clipPath id="roundedCorners">
      <rect width="600" height="380" rx="24" ry="24" />
    </clipPath>
  </defs>
  
  <g clip-path="url(#roundedCorners)">
    <rect width="600" height="380" fill="url(#cardGrad)" />
    <ellipse cx="480" cy="70" rx="300" ry="200" fill="white" fill-opacity="0.09" />
    <ellipse cx="80" cy="340" rx="200" ry="190" fill="white" fill-opacity="0.05" />
    
    <rect x="48" y="135" width="64" height="46" rx="8" ry="8" fill="#D4AF37" stroke="#AA871E" stroke-width="2" />
    <line x1="48" y1="158" x2="112" y2="158" stroke="#A07814" stroke-width="1.5" />
    <line x1="80" y1="135" x2="80" y2="181" stroke="#A07814" stroke-width="1.5" />
    
    <text x="48" y="52" fill="white" fill-opacity="0.9" font-family="Helvetica, -apple-system, sans-serif" font-size="19" font-weight="600" letter-spacing="1">{clean_bank_esc}</text>
    <text x="520" y="52" fill="white" fill-opacity="0.7" font-family="Helvetica, -apple-system, sans-serif" font-size="19" font-weight="bold">))))</text>
    
    <text x="48" y="335" fill="white" font-family="Helvetica, -apple-system, sans-serif" font-size="22" font-weight="bold">{display_name_esc}</text>
  </g>
</svg>'''
    return svg

def generate_card_image(card_id, name, bank, hex_color):
    # Check if a matching image already exists on disk
    for ext in ['.png', '.jpg', '.jpeg', '.webp']:
        fn = f"{card_id}{ext}"
        if fn in disk_files and os.path.getsize(os.path.join(CARDS_DIR, fn)) > 100:
            return f"https://raw.githubusercontent.com/jimabby/card-assets/main/cards/{fn}"
            
    # Otherwise generate a high quality PNG image
    filename = f"{card_id}.png"
    output_path = os.path.join(CARDS_DIR, filename)
    
    if HAS_PIL:
        width, height = 600, 380
        hex_color = (hex_color or '2C3E50').lstrip('#')
        if len(hex_color) != 6:
            hex_color = '2C3E50'
            
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        radius = 24
        for y in range(height):
            ratio = y / height
            nr = int(max(0, min(255, r * (1.1 - ratio * 0.4))))
            ng = int(max(0, min(255, g * (1.1 - ratio * 0.4))))
            nb = int(max(0, min(255, b * (1.1 - ratio * 0.4))))
            draw.line([(0, y), (width, y)], fill=(nr, ng, nb, 255))
            
        mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([0, 0, width, height], radius=radius, fill=255)
        img.putalpha(mask)
        
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        ov_draw = ImageDraw.Draw(overlay)
        ov_draw.ellipse([width * 0.3, -100, width * 1.3, height * 0.9], fill=(255, 255, 255, 22))
        ov_draw.ellipse([-100, height * 0.4, width * 0.6, height * 1.4], fill=(255, 255, 255, 12))
        img.alpha_composite(overlay)
        
        draw = ImageDraw.Draw(img)
        
        chip_x, chip_y, chip_w, chip_h = 48, 135, 64, 46
        draw.rounded_rectangle([chip_x, chip_y, chip_x + chip_w, chip_y + chip_h], radius=8, fill=(212, 175, 55, 255), outline=(170, 135, 30, 255), width=2)
        draw.line([(chip_x, chip_y + 23), (chip_x + chip_w, chip_y + 23)], fill=(160, 120, 20, 255), width=1)
        draw.line([(chip_x + 32, chip_y), (chip_x + 32, chip_y + chip_h)], fill=(160, 120, 20, 255), width=1)

        clean_bank = bank.replace('.com', '').replace('.ca', '').replace('.au', '').replace('.cn', '').replace('.tw', '').replace('.org', '').upper()
        
        try:
            font_large = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
            font_bank = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 19)
        except Exception:
            font_large = font_bank = ImageFont.load_default()
            
        draw.text((48, 32), clean_bank, fill=(255, 255, 255, 230), font=font_bank)
        draw.text((width - 85, 32), '))))', fill=(255, 255, 255, 180), font=font_bank)
        
        display_name = name if len(name) <= 35 else name[:32] + '...'
        draw.text((48, height - 68), display_name, fill=(255, 255, 255, 255), font=font_large)
        
        img.save(output_path, 'PNG')
    else:
        svg = generate_svg(name, bank, hex_color)
        tmp_svg = os.path.join(CARDS_DIR, f"{card_id}_tmp.svg")
        with open(tmp_svg, 'w', encoding='utf-8') as f:
            f.write(svg)
        subprocess.run(['sips', '-s', 'format', 'png', tmp_svg, '--out', output_path], stdout=subprocess.DEVNULL, check=True)
        if os.path.exists(tmp_svg):
            os.remove(tmp_svg)

    disk_files.add(filename)
    return f"https://raw.githubusercontent.com/jimabby/card-assets/main/cards/{filename}"

if __name__ == '__main__':
    print(f"Image helper defined. HAS_PIL={HAS_PIL}")

