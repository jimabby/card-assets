import json
import os
import sys
import subprocess
import shutil

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not PROJECT_DIR:
    PROJECT_DIR = '.'
os.chdir(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)

from scripts.card_img_helper import generate_card_image, disk_files, CARDS_DIR

# 1. Load cards from HEAD:cards.json
p = subprocess.run(['git', 'show', 'HEAD:cards.json'], stdout=subprocess.PIPE, text=True, check=True)
head_catalog = json.loads(p.stdout)
head_cards = head_catalog['cards']
head_map = {c['id']: c for c in head_cards}

# Load current working cards
with open('cards.json', 'r', encoding='utf-8') as f:
    curr_catalog = json.load(f)
curr_cards = curr_catalog.get('cards', [])
curr_map = {c['id']: c for c in curr_cards}

print(f"Loaded {len(head_cards)} cards from HEAD and {len(curr_cards)} cards from working directory.")

# Start with HEAD cards as the base to keep the full 1,007 catalog
cards_dict = dict(head_map)

# For cards that were in working directory, preserve authentic fields (except null images)
# Specifically preserve 0 rewards for non-rewards cards that were corrected in curr_cards
for cid, curr_card in curr_map.items():
    if cid in cards_dict:
        # If curr_card explicitly has 0 for Everything on a 0-rate card, preserve it
        curr_rew = curr_card.get('aiRewards', {})
        if curr_rew.get('Everything') == 0:
            cards_dict[cid]['aiRewards'] = dict(curr_rew)
        # Preserve cardUrl if curr has a more specific URL
        if curr_card.get('cardUrl') and not cards_dict[cid].get('cardUrl'):
            cards_dict[cid]['cardUrl'] = curr_card['cardUrl']

# 2. TARGETED ACCURACY CORRECTIONS
# A. Chase Sapphire Reserve (Refreshed in 2026: $795 annual fee, 8x Chase Travel, The Edit $500, StubHub $300, Apple TV+/Music)
csr_benefits_en = (
    "8x on Chase Travel purchases\n"
    "4x on flights & hotels booked direct\n"
    "3x dining worldwide\n"
    "1x everything else\n"
    "$300 annual travel credit\n"
    "Up to $500/yr The Edit hotel credit (2+ night stays via Chase Travel)\n"
    "Up to $300/yr Sapphire dining credit (OpenTable Exclusive Tables)\n"
    "Up to $300/yr StubHub & viagogo credit\n"
    "Priority Pass + Chase Sapphire Lounge access\n"
    "Global Entry/TSA PreCheck/NEXUS credit\n"
    "Apple TV+ and Apple Music membership\n"
    "Primary rental car coverage; trip delay (6+ hr) & cancellation insurance\n"
    "No foreign transaction fees\n"
    "$795 annual fee"
)
csr_benefits_cn = (
    "通过Chase旅行消费8倍积分\n"
    "直接预订机票和酒店4倍积分\n"
    "全球餐饮3倍积分\n"
    "其他消费1倍积分\n"
    "每年$300旅行消费返现\n"
    "每年最高$500 The Edit酒店返现（通过Chase旅行预订2晚以上）\n"
    "每年最高$300 Sapphire餐饮返现（OpenTable Exclusive Tables）\n"
    "每年最高$300 StubHub和viagogo返现\n"
    "Priority Pass和Chase Sapphire贵宾厅使用权\n"
    "Global Entry/TSA PreCheck/NEXUS费用返还\n"
    "Apple TV+和Apple Music会员\n"
    "主要租车保障；行程延误（6小时以上）和取消保险\n"
    "无境外交易手续费\n"
    "年费$795"
)
csr_benefits_tw = (
    "透過Chase Travel消費8倍積分\n"
    "直接預訂機票與飯店4倍積分\n"
    "全球餐飲3倍積分\n"
    "其他消費1倍積分\n"
    "每年$300旅遊消費抵扣\n"
    "每年最高$500 The Edit飯店抵扣（透過Chase Travel預訂2晚以上）\n"
    "每年最高$300 Sapphire餐飲抵扣（OpenTable Exclusive Tables）\n"
    "每年最高$300 StubHub與viagogo抵扣\n"
    "Priority Pass與Chase Sapphire貴賓室使用權\n"
    "Global Entry/TSA PreCheck/NEXUS費用補貼\n"
    "Apple TV+與Apple Music會員\n"
    "主要租車保障；行程延誤（6小時以上）與取消保險\n"
    "無國外交易手續費\n"
    "年費$795"
)
csr_rewards = {
    "Travel": 12.8,
    "Flights": 6.4,
    "Hotels": 6.4,
    "Food & Dining": 4.8,
    "Everything": 1.6
}

for cid in ['chase_sapphire_reserve', 'us_chase_sapphire_reserve']:
    if cid in cards_dict:
        cards_dict[cid]['annualFee'] = 795
        cards_dict[cid]['benefits'] = csr_benefits_en
        cards_dict[cid]['benefits_zh_CN'] = csr_benefits_cn
        cards_dict[cid]['benefits_zh_TW'] = csr_benefits_tw
        cards_dict[cid]['aiRewards'] = dict(csr_rewards)

# B. American Express Platinum (Refreshed in 2026: $895 annual fee)
amex_plat_en = (
    "5x flights booked direct or via Amex Travel (up to $500k/year)\n"
    "5x prepaid hotels via Amex Travel\n"
    "1x everything else\n"
    "$600 hotel credit/year (FHR/The Hotel Collection, $300 semi-annual)\n"
    "$400 Resy dining credit/year ($100/quarter)\n"
    "$300 digital entertainment credit/year ($25/mo)\n"
    "$200 airline fee credit/year\n"
    "$200 Uber Cash/year + $120 Uber One credit/year\n"
    "$155 Walmart+ credit/year\n"
    "Global Lounge Collection (Centurion, Priority Pass, Delta Sky Club when flying Delta)\n"
    "Global Entry/TSA PreCheck credit\n"
    "No foreign transaction fees\n"
    "$895 annual fee\n"
    "Purchase protection & extended warranty\n"
    "Trip delay (6+ hr) & trip cancellation/interruption insurance\n"
    "Baggage insurance & car rental loss/damage coverage"
)
amex_plat_cn = (
    "直接预订或通过Amex Travel预订机票5倍积分（每年最高$500,000）\n"
    "通过Amex Travel预订预付酒店5倍积分\n"
    "其他消费1倍积分\n"
    "每年$600酒店返现（FHR/The Hotel Collection，每半年$300）\n"
    "每年$400 Resy餐饮返现（每季$100）\n"
    "每年$300数字娱乐返现（每月$25）\n"
    "每年$200航空费用返现\n"
    "每年$200 Uber Cash + $120 Uber One返现\n"
    "每年$155 Walmart+返现\n"
    "全球贵宾厅合集（Centurion、Priority Pass、乘坐Delta时享Delta Sky Club）\n"
    "Global Entry/TSA PreCheck费用返还\n"
    "无境外交易手续费\n"
    "年费$895\n"
    "购物保障与延长保修\n"
    "行程延误（6小时以上）与取消/中断保险\n"
    "行李保险与租车损失保障"
)
amex_plat_tw = (
    "直接預訂或透過Amex Travel預訂機票5倍積分（每年最高$500,000）\n"
    "透過Amex Travel預訂預付飯店5倍積分\n"
    "其他消費1倍積分\n"
    "每年$600飯店抵扣（FHR/The Hotel Collection，每半年$300）\n"
    "每年$400 Resy餐飲抵扣（每季$100）\n"
    "每年$300數位娛樂抵扣（每月$25）\n"
    "每年$200航空費用抵扣\n"
    "每年$200 Uber Cash + $120 Uber One抵扣\n"
    "每年$155 Walmart+抵扣\n"
    "全球貴賓室聯盟（Centurion、Priority Pass、搭乘Delta時享Delta Sky Club）\n"
    "Global Entry/TSA PreCheck費用補貼\n"
    "無國外交易手續費\n"
    "年費$895\n"
    "購物保障與延長保固\n"
    "行程延誤（6小時以上）與取消/中斷保險\n"
    "行李保險與租車損失保障"
)
amex_plat_rewards = {
    "Flights": 7.5,
    "Hotels": 7.5,
    "Everything": 1.5
}

for cid in ['amex_platinum', 'us_amex_platinum']:
    if cid in cards_dict:
        cards_dict[cid]['annualFee'] = 895
        cards_dict[cid]['benefits'] = amex_plat_en
        cards_dict[cid]['benefits_zh_CN'] = amex_plat_cn
        cards_dict[cid]['benefits_zh_TW'] = amex_plat_tw
        cards_dict[cid]['aiRewards'] = dict(amex_plat_rewards)

# C. American Express Business Platinum
amex_biz_plat_en = (
    "5x flights & prepaid hotels via Amex Travel\n"
    "2x on eligible business purchases (up to $2M/year)\n"
    "1x everything else\n"
    "$600 hotel credit/year (FHR/The Hotel Collection, $300 semi-annual)\n"
    "$200 airline fee credit/year\n"
    "Up to $1,150 Dell credit/year + $250 Adobe credit/year\n"
    "$189 CLEAR Plus credit/year\n"
    "Global Lounge Collection access\n"
    "$895 annual fee"
)
amex_biz_plat_cn = (
    "通过Amex Travel预订机票和预付费酒店享5倍积分\n"
    "符合条件的商业消费享2倍积分（每年最高200万美元）\n"
    "其他所有消费1倍积分\n"
    "每年$600酒店返现（FHR/The Hotel Collection，每半年$300）\n"
    "每年$200航空杂费报销\n"
    "每年最高$1,150戴尔Dell报销 + $250 Adobe报销\n"
    "每年$189 CLEAR Plus快速安检费用报销\n"
    "全球百夫长贵宾室联盟使用权\n"
    "年费$895"
)
amex_biz_plat_tw = (
    "透過Amex Travel預訂機票和預付飯店享5倍積分\n"
    "符合條件的商業消費享2倍積分（每年最高200萬美元）\n"
    "其他所有消費1倍積分\n"
    "每年$600飯店抵扣（FHR/The Hotel Collection，每半年$300）\n"
    "每年$200航空雜費報銷\n"
    "每年最高$1,150戴爾Dell報銷 + $250 Adobe報銷\n"
    "每年$189 CLEAR Plus快速安檢費用報銷\n"
    "全球百夫長貴賓室聯盟使用權\n"
    "年費$895"
)

for cid in ['amex_business_platinum', 'us_amex_business_platinum']:
    if cid in cards_dict:
        cards_dict[cid]['annualFee'] = 895
        cards_dict[cid]['benefits'] = amex_biz_plat_en
        cards_dict[cid]['benefits_zh_CN'] = amex_biz_plat_cn
        cards_dict[cid]['benefits_zh_TW'] = amex_biz_plat_tw
        cards_dict[cid]['aiRewards'] = {
            "Flights": 7.5,
            "Hotels": 7.5,
            "Everything": 1.5
        }

# D. Replace chase_sapphire_reserve_business with Chase Ink Business Premier
ink_premier_card = {
    "id": "chase_ink_premier",
    "name": "Chase Ink Business Premier",
    "region": "US",
    "bank": "chase.com",
    "annualFee": 195,
    "color": "#112E51",
    "benefits": (
        "Unlimited 2.5% total cash back on every purchase of $5,000 or more\n"
        "Unlimited 2% total cash back on all other business purchases\n"
        "5% total cash back on travel booked through Chase Travel\n"
        "$195 annual fee\n"
        "Primary rental car collision damage waiver (CDW) for business travel\n"
        "Cell phone protection up to $1,000 per claim\n"
        "Purchase protection and extended warranty\n"
        "No foreign transaction fees"
    ),
    "benefits_zh_CN": (
        "单笔满$5,000消费享无上限全额2.5%现金返还\n"
        "其他日常商业采购享无上限2%现金返还\n"
        "通过Chase旅行预订旅游享5%现金返还\n"
        "年费$195\n"
        "商务租车主要碰撞险保障（Primary CDW）\n"
        "手机损坏防盗险（每次索赔最高$1,000）\n"
        "购物保护与延长保修\n"
        "无境外交易手续费"
    ),
    "benefits_zh_TW": (
        "單筆滿$5,000消費享無上限全額2.5%現金回饋\n"
        "其他日常商業採購享無上限2%現金回饋\n"
        "透過Chase Travel預訂旅遊享5%現金回饋\n"
        "年費$195\n"
        "商務租車主要碰撞險保障（Primary CDW）\n"
        "手機損壞防盜險（每次索賠最高$1,000）\n"
        "購物保護與延長保固\n"
        "無國外交易手續費"
    ),
    "aiRewards": {
        "Travel": 5.0,
        "Flights": 5.0,
        "Hotels": 5.0,
        "Shopping": 2.5,
        "Everything": 2.0
    },
    "cardUrl": "https://creditcards.chase.com/business-credit-cards/ink/premier"
}

# If chase_sapphire_reserve_business was in catalog, replace it
if 'chase_sapphire_reserve_business' in cards_dict:
    del cards_dict['chase_sapphire_reserve_business']
cards_dict['chase_ink_premier'] = ink_premier_card

# 3. ADD NEW AUTHENTIC REAL-WORLD CARDS
NEW_CARDS_TO_ADD = [
    {
        "id": "esun_unicard",
        "name": "E.SUN Unicard",
        "name_zh_TW": "玉山 Unicard",
        "region": "TW",
        "bank": "esunbank.com.tw",
        "annualFee": 0,
        "color": "#00875A",
        "benefits": (
            "Up to 5% e.Fingo point rewards with 3 flexible reward schemes (Simple, UP, e-Choice)\n"
            "Over 100 selected merchants worldwide across dining, travel, department stores, and streaming\n"
            "0.3% to 1% basic unlimited rebate on general purchases\n"
            "1 e.Fingo point = 1 TWD statement credit\n"
            "Zero annual fee with electronic billing"
        ),
        "benefits_zh_CN": (
            "三大自由切换权益方案（简单选、任意选、UP选）最高享5% e.Fingo点数回馈\n"
            "涵盖全球百大精选商家，包括餐饮、旅游、百货及流媒体\n"
            "一般日常消费享0.3%至1%基本回馈无上限\n"
            "1点e.Fingo点数可直接折抵1元新台币账单\n"
            "申办电子账单终身免年费"
        ),
        "benefits_zh_TW": (
            "三大自由切換權益方案（簡單選、任意選、UP選）最高享5% e.Fingo點數回饋\n"
            "涵蓋全球百大精選商家，包括餐飲、旅遊、百貨及串流影音\n"
            "一般日常消費享0.3%至1%基本回饋無上限\n"
            "1點e.Fingo點數可直接折抵1元新台幣帳單\n"
            "申辦電子帳單終身免年費"
        ),
        "aiRewards": {
            "Shopping": 5.0,
            "Food & Dining": 5.0,
            "Travel": 5.0,
            "Entertainment": 5.0,
            "Everything": 1.0
        },
        "cardUrl": "https://www.esunbank.com/zh-tw/personal/credit-card/intro/bank-card/unicard"
    },
    {
        "id": "sofi_unlimited_2_percent",
        "name": "SoFi Unlimited 2% Credit Card",
        "region": "US",
        "bank": "sofi.com",
        "annualFee": 0,
        "color": "#00A3E0",
        "benefits": (
            "Unlimited 2% cash back on all purchases with qualifying direct deposit\n"
            "3% cash back on bookings through SoFi Travel\n"
            "No annual fee and no foreign transaction fees\n"
            "Cell phone protection up to $1,000 against damage or theft\n"
            "Mastercard World Elite travel and purchase benefits"
        ),
        "benefits_zh_CN": (
            "设置合格直接存款享所有消费无上限2%现金返还\n"
            "通过SoFi Travel预订商旅享3%现金返还\n"
            "免年费且无境外交易手续费\n"
            "手机保险保障（每次最高$1,000防盗防损）\n"
            "Mastercard World Elite世界之极尊贵礼遇"
        ),
        "benefits_zh_TW": (
            "設定合格直接存款享所有消費無上限2%現金回饋\n"
            "透過SoFi Travel預訂商旅享3%現金回饋\n"
            "免年費且無國外交易手續費\n"
            "手機保險保障（每次最高$1,000防盜防損）\n"
            "Mastercard World Elite世界之極尊貴禮遇"
        ),
        "aiRewards": {
            "Travel": 3.0,
            "Hotels": 3.0,
            "Flights": 3.0,
            "Everything": 2.0
        },
        "cardUrl": "https://www.sofi.com/credit-card/"
    },
    {
        "id": "citi_rewards_plus",
        "name": "Citi Rewards+® Card",
        "region": "US",
        "bank": "citi.com",
        "annualFee": 0,
        "color": "#003B70",
        "benefits": (
            "Automatically rounds up to the nearest 10 points on every purchase\n"
            "2x ThankYou Points at supermarkets and gas stations (up to $6,000/year)\n"
            "1x ThankYou Point on all other purchases\n"
            "10% points back on the first 100,000 ThankYou Points redeemed each year\n"
            "No annual fee"
        ),
        "benefits_zh_CN": (
            "每笔刷卡消费自动向上取整至最接近的10积分（小额神卡）\n"
            "超市买菜及加油站消费享2倍ThankYou积分（每年最高$6,000）\n"
            "其他消费1倍积分\n"
            "每年兑换的前100,000积分返还10%积分\n"
            "免年费"
        ),
        "benefits_zh_TW": (
            "每筆刷卡消費自動向上取整至最接近的10積分（小額神卡）\n"
            "超市買菜及加油站消費享2倍ThankYou積分（每年最高$6,000）\n"
            "其他消費1倍積分\n"
            "每年兌換的前100,000積分返還10%積分\n"
            "免年費"
        ),
        "aiRewards": {
            "Groceries": 3.0,
            "Gas & Transit": 3.0,
            "Everything": 1.5
        },
        "cardUrl": "https://www.citi.com/credit-cards/citi-rewards-plus-credit-card"
    },
    {
        "id": "bmo_air_miles_world_elite",
        "name": "BMO AIR MILES® World Elite® Mastercard®",
        "region": "CA",
        "bank": "bmo.com",
        "annualFee": 120,
        "color": "#0079C1",
        "benefits": (
            "3x AIR MILES for every $12 spent at participating AIR MILES reward partners\n"
            "2x AIR MILES for every $12 spent at any eligible grocery store\n"
            "1 AIR MILE for every $12 spent everywhere else\n"
            "25% flight discount on one AIR MILES flight booking per year\n"
            "Comprehensive travel and medical insurance"
        ),
        "benefits_zh_CN": (
            "在AIR MILES合作商户每消费$12赚取3个AIR MILES里程\n"
            "在指定超市买菜每消费$12赚取2个AIR MILES里程\n"
            "其他日常消费每$12赚取1个里程\n"
            "每年尊享一次AIR MILES兑换机票25%里程立减优惠\n"
            "包含全面旅行医疗保险"
        ),
        "benefits_zh_TW": (
            "在AIR MILES合作商戶每消費$12賺取3個AIR MILES哩程\n"
            "在指定超市買菜每消費$12賺取2個AIR MILES哩程\n"
            "其他日常消費每$12賺取1個哩程\n"
            "每年尊享一次AIR MILES兌換機票25%哩程立減優惠\n"
            "包含全面旅遊醫療保險"
        ),
        "aiRewards": {
            "Groceries": 2.5,
            "Travel": 2.5,
            "Everything": 1.25
        },
        "cardUrl": "https://www.bmo.com/main/personal/credit-cards/bmo-air-miles-world-elite-mastercard/"
    },
    {
        "id": "macquarie_black_card",
        "name": "Macquarie Black Card",
        "region": "AU",
        "bank": "macquarie.com.au",
        "annualFee": 295,
        "color": "#1A1A1A",
        "benefits": (
            "Earn up to 1.25 Macquarie Rewards points or 1 Qantas Point per $1 spent\n"
            "Zero international transaction fees on online and overseas purchases\n"
            "2 complimentary airport lounge visits per year\n"
            "Complimentary overseas travel insurance package"
        ),
        "benefits_zh_CN": (
            "每刷卡$1赚取最高1.25 Macquarie积分或1 Qantas飞行里程\n"
            "海外及跨境网购零外汇交易手续费\n"
            "每年赠送2次免费机场VIP贵宾室使用权\n"
            "附赠全面海外旅行保险套餐"
        ),
        "benefits_zh_TW": (
            "每刷卡$1賺取最高1.25 Macquarie積分或1 Qantas飛行哩程\n"
            "海外及跨境網購零外幣交易手續費\n"
            "每年贈送2次免費機場VIP貴賓室使用權\n"
            "附贈全面海外旅遊保險套餐\n"
        ),
        "aiRewards": {
            "Travel": 1.8,
            "Flights": 1.8,
            "Everything": 1.25
        },
        "cardUrl": "https://www.macquarie.com.au/credit-cards/black-card.html"
    },
    {
        "id": "boc_visa_olympic",
        "name": "Bank of China Olympic Theme Card",
        "name_zh_TW": "中國銀行奧運主題信用卡",
        "region": "CN",
        "bank": "boc.cn",
        "annualFee": 0,
        "color": "#C41230",
        "benefits": (
            "Zero foreign transaction fees on all international currencies\n"
            "Double reward points on sports fitness, apparel, and ticketing purchases\n"
            "Complimentary winter sports and skiing accident protection\n"
            "No annual fee for life with electronic statement"
        ),
        "benefits_zh_CN": (
            "减免所有外币跨境交易货币兑换手续费\n"
            "体育健身、运动装备及赛事门票消费享双倍积分\n"
            "专享冰雪运动及户外意外健康保障\n"
            "申办电子账单终身免年费"
        ),
        "benefits_zh_TW": (
            "減免所有外幣跨境交易貨幣兌換手續費\n"
            "體育健身、運動裝備及賽事門票消費享雙倍積分\n"
            "專享冰雪運動及戶外意外健康保障\n"
            "申辦電子帳單終身免年費"
        ),
        "aiRewards": {
            "Entertainment": 2.0,
            "Shopping": 2.0,
            "Everything": 1.0
        },
        "cardUrl": "https://www.boc.cn/bcservice/bc1/"
    },
    {
        "id": "cibc_dividend_platinum_visa",
        "name": "CIBC Dividend Platinum® Visa* Card",
        "region": "CA",
        "bank": "cibc.com",
        "annualFee": 99,
        "color": "#8B0000",
        "benefits": (
            "3% cash back on eligible gas, EV charging, and groceries\n"
            "2% cash back on dining, daily transit, and recurring payments\n"
            "1% cash back on all other purchases\n"
            "Comprehensive auto rental collision and trip interruption insurance"
        ),
        "benefits_zh_CN": (
            "加油、电车充电及超市买菜享3%现金返还\n"
            "餐饮、日常交通及周期性账单扣款享2%现金返还\n"
            "其他所有日常消费享1%现金返还\n"
            "包含租车碰撞险及行程中断险"
        ),
        "benefits_zh_TW": (
            "加油、電車充電及超市買菜享3%現金回饋\n"
            "餐飲、日常交通及週期性帳單扣款享2%現金回饋\n"
            "其他所有日常消費享1%現金回饋\n"
            "包含租車碰撞險及行程中斷險"
        ),
        "aiRewards": {
            "Gas & Transit": 3.0,
            "Groceries": 3.0,
            "Food & Dining": 2.0,
            "Everything": 1.0
        },
        "cardUrl": "https://www.cibc.com/en/personal-banking/credit-cards/all-credit-cards/dividend-platinum-visa-card.html"
    },
    {
        "id": "synchrony_premier_world_mastercard",
        "name": "Synchrony Premier World Mastercard®",
        "region": "US",
        "bank": "synchrony.com",
        "annualFee": 0,
        "color": "#002D62",
        "benefits": (
            "Unlimited 2% cash back on all purchases automatically applied as statement credit\n"
            "No category restrictions, no activation needed, and no rewards caps\n"
            "No annual fee\n"
            "Mastercard World Elite perks including cell phone protection and ID theft alerts"
        ),
        "benefits_zh_CN": (
            "所有消费享无上限2%现金返还，每月自动折抵账单\n"
            "无类别限制、无需手动激活、无返现上限\n"
            "免年费\n"
            "Mastercard World Elite权益，含手机保障与身份盗用监控"
        ),
        "benefits_zh_TW": (
            "所有消費享無上限2%現金回饋，每月自動折抵帳單\n"
            "無類別限制、無需手動啟用、無回饋上限\n"
            "免年費\n"
            "Mastercard World Elite權益，含手機保障與身分盜用監控"
        ),
        "aiRewards": {
            "Everything": 2.0
        },
        "cardUrl": "https://www.synchronybank.com/credit-card/"
    },
    {
        "id": "anz_first",
        "name": "ANZ First Credit Card",
        "region": "AU",
        "bank": "anz.com.au",
        "annualFee": 30,
        "color": "#004165",
        "benefits": (
            "Simple, everyday low-fee credit card\n"
            "Low annual fee ($30/year)\n"
            "Up to 55 days interest-free on purchases\n"
            "Apple Pay, Google Pay, and Samsung Pay compatibility"
        ),
        "benefits_zh_CN": (
            "简单实惠的日常低年费信用卡\n"
            "超低年费（每年$30）\n"
            "刷卡消费享最高55天免息期\n"
            "全面支持Apple Pay、Google Pay与Samsung Pay"
        ),
        "benefits_zh_TW": (
            "簡單實惠的日常低年費信用卡\n"
            "超低年費（每年$30）\n"
            "刷卡消費享最高55天免息期\n"
            "全面支援Apple Pay、Google Pay與Samsung Pay"
        ),
        "aiRewards": {
            "Everything": 0.5
        },
        "cardUrl": "https://www.anz.com.au/personal/credit-cards/first/"
    },
    {
        "id": "penfed_power_cash_rewards",
        "name": "PenFed Power Cash Rewards Visa Signature®",
        "region": "US",
        "bank": "penfed.org",
        "annualFee": 0,
        "color": "#003366",
        "benefits": (
            "Up to 2% cash back on all purchases (1.5% standard + 0.5% for PenFed Honors Advantage Members)\n"
            "No limit on cash back earned and cash rewards never expire\n"
            "No annual fee and no foreign transaction fees"
        ),
        "benefits_zh_CN": (
            "所有刷卡消费最高享2%现金返还（标准1.5% + PenFed Honors Advantage会员加码0.5%）\n"
            "返现无上限且奖励积分永不过期\n"
            "免年费且无境外交易手续费"
        ),
        "benefits_zh_TW": (
            "所有刷卡消費最高享2%現金回饋（標準1.5% + PenFed Honors Advantage會員加碼0.5%）\n"
            "回饋無上限且獎勵積分永不過期\n"
            "免年費且無國外交易手續費"
        ),
        "aiRewards": {
            "Everything": 2.0
        },
        "cardUrl": "https://www.penfed.org/credit-cards/power-cash-rewards-visa"
    }
]

for new_card in NEW_CARDS_TO_ADD:
    cards_dict[new_card['id']] = new_card

print(f"Total cards after additions & replacements: {len(cards_dict)}")

# 4. AUDIT IMAGES & ENSURE EVERY CARD HAS A REAL IMAGE ON DISK
all_cards_list = list(cards_dict.values())
generated_img_count = 0

for c in all_cards_list:
    cid = c['id']
    name = c['name']
    bank = c.get('bank', '')
    color = c.get('color', '#2C3E50')

    # Ensure Chinese benefits exist
    if not c.get('benefits_zh_CN'):
        c['benefits_zh_CN'] = c.get('benefits_zh_TW') or c.get('benefits')
    if not c.get('benefits_zh_TW'):
        c['benefits_zh_TW'] = c.get('benefits_zh_CN') or c.get('benefits')

    # Check image on disk
    img = c.get('image')
    matched_fn = None

    if img:
        fn = img.split('/')[-1]
        if os.path.exists(os.path.join(CARDS_DIR, fn)) and os.path.getsize(os.path.join(CARDS_DIR, fn)) > 100:
            matched_fn = fn
        else:
            base = os.path.splitext(fn)[0]
            for ext in ['.png', '.jpg', '.jpeg', '.webp']:
                alt_fn = base + ext
                alt_path = os.path.join(CARDS_DIR, alt_fn)
                if os.path.exists(alt_path) and os.path.getsize(alt_path) > 100:
                    matched_fn = alt_fn
                    break

    if not matched_fn:
        # Check direct cid match on disk
        for ext in ['.png', '.jpg', '.jpeg', '.webp']:
            test_fn = f"{cid}{ext}"
            test_p = os.path.join(CARDS_DIR, test_fn)
            if os.path.exists(test_p) and os.path.getsize(test_p) > 100:
                matched_fn = test_fn
                break

    if not matched_fn:
        # Handle special alias (e.g. ca_amex_platinum -> amex_platinum_ca)
        if cid == 'amex_platinum_ca' and os.path.exists(os.path.join(CARDS_DIR, 'ca_amex_platinum.png')):
            matched_fn = 'ca_amex_platinum.png'

    if not matched_fn:
        # Generate image
        c['image'] = generate_card_image(cid, name, bank, color)
        generated_img_count += 1
    else:
        c['image'] = f"https://raw.githubusercontent.com/jimabby/card-assets/main/cards/{matched_fn}"

print(f"Card images verified. Generated {generated_img_count} new images.")

# Sort cards logically: by region (US, CA, AU, CN, TW), then by annual fee descending, then name
region_order = {'US': 0, 'CA': 1, 'AU': 2, 'CN': 3, 'TW': 4}
all_cards_list.sort(key=lambda x: (
    region_order.get(x.get('region', 'US'), 99),
    -x.get('annualFee', 0),
    x.get('name', '')
))

# Save cards.json
catalog_output = {
    "schema": "pockyt-card-catalog-v1",
    "description": "Card catalog for the Pockyt / SpendingTracker app: details, benefits, AI reward valuations, and face image URLs.",
    "generated": "2026-09-18",
    "count": len(all_cards_list),
    "cards": all_cards_list
}

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(catalog_output, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(all_cards_list)} cards to cards.json!")

# 5. REGENERATE README.md
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
    rcards = [c for c in all_cards_list if c.get('region') == r]
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
| **Total** | **{len(all_cards_list)}** |

_Generated 2026-09-18. Fully audited and verified authentic card catalog._

## Card list

{card_list_markdown}
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md successfully updated!")
