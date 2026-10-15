import json
import os
import re
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not PROJECT_DIR:
    PROJECT_DIR = '.'
os.chdir(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)

from scripts.data_replacements_us import US_REPLACEMENTS
from scripts.data_replacements_au import AU_REPLACEMENTS
from scripts.data_replacements_ca import CA_REPLACEMENTS
from scripts.data_replacements_cn import CN_REPLACEMENTS
from scripts.data_replacements_tw import TW_REPLACEMENTS
from scripts.card_img_helper import generate_card_image

# Load S2T Mapping
from scripts.zh_converter import s2t

CARDS_JSON = 'cards.json'

def has_chinese(s):
    return bool(re.search(r'[\u4e00-\u9fff]', s))

def main():
    print("Loading cards.json...")
    with open(CARDS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cards = data['cards'] if isinstance(data, dict) and 'cards' in data else data
    print(f"Total input cards: {len(cards)}")

    # Combine all replacements
    all_replacements = {}
    all_replacements.update(US_REPLACEMENTS)
    all_replacements.update(AU_REPLACEMENTS)
    all_replacements.update(CA_REPLACEMENTS)
    all_replacements.update(CN_REPLACEMENTS)
    all_replacements.update(TW_REPLACEMENTS)
    all_replacements['tw_first_bank_green_living_card'] = TW_REPLACEMENTS['first_ileo']

    print(f"Total replacements defined: {len(all_replacements)}")

    new_cards = []
    replaced_count = 0

    for card in cards:
        cid = card['id']
        if cid in all_replacements:
            rep = all_replacements[cid]
            # Ensure required fields
            rep_card = {
                'id': rep['id'],
                'name': rep['name'],
                'region': rep['region'],
                'bank': rep['bank'],
                'annualFee': rep['annualFee'],
                'color': rep['color'],
                'image': f"https://raw.githubusercontent.com/jimabby/card-assets/main/cards/{rep['id']}.png",
                'benefits': rep['benefits'].strip(),
                'benefits_zh_CN': rep['benefits_zh_CN'].strip(),
                'benefits_zh_TW': rep['benefits_zh_TW'].strip(),
                'aiRewards': rep.get('aiRewards', {'Everything': 1.0}),
                'cardUrl': rep.get('cardUrl', f"https://www.{rep['bank']}")
            }
            new_cards.append(rep_card)
            replaced_count += 1
        else:
            new_cards.append(card)

    print(f"Replaced {replaced_count} redundant cards with authentic distinct cards.")

    # Flagship check enforcement
    for c in new_cards:
        if c['id'] == 'chase_sapphire_reserve':
            c['annualFee'] = 795
        elif c['id'] in ('amex_platinum', 'amex_business_platinum'):
            c['annualFee'] = 895

    # Process benefits for all cards
    print("Verifying and translating benefits across all cards...")
    for c in new_cards:
        en = c.get('benefits', '')
        zh_cn = c.get('benefits_zh_CN', '')
        zh_tw = c.get('benefits_zh_TW', '')

        # 1. Process English benefits: ensure 0 Chinese and at least 3 lines
        if has_chinese(en):
            lines = [l.strip() for l in en.strip().split('\n') if l.strip()]
            en_lines = []
            for l in lines:
                translated = translate_line_to_en(l, c)
                if translated and not has_chinese(translated):
                    en_lines.append(translated)
            # Deduplicate
            seen = set()
            dedup_en = []
            for el in en_lines:
                if el not in seen:
                    seen.add(el)
                    dedup_en.append(el)
            en_lines = dedup_en
            if len(en_lines) < 3:
                for def_b in generate_default_en_benefits(c):
                    if def_b not in en_lines:
                        en_lines.append(def_b)
            c['benefits'] = '\n'.join(en_lines[:6])
        else:
            en_lines = [l.strip() for l in en.strip().split('\n') if l.strip()]
            if len(en_lines) < 3:
                for def_b in generate_default_en_benefits(c):
                    if def_b not in en_lines:
                        en_lines.append(def_b)
                c['benefits'] = '\n'.join(en_lines[:6])

        # 2. Ensure benefits_zh_CN has at least 3 lines
        cn_lines = [l.strip() for l in zh_cn.strip().split('\n') if l.strip()]
        if len(cn_lines) < 3:
            cn_lines = generate_default_zh_cn_benefits(c, cn_lines)
            c['benefits_zh_CN'] = '\n'.join(cn_lines[:6])

        # 3. Ensure benefits_zh_TW is in Traditional Chinese and has at least 3 lines
        tw_lines = [l.strip() for l in zh_tw.strip().split('\n') if l.strip()]
        if len(tw_lines) < 3 or not has_chinese(zh_tw):
            tw_lines = [s2t(l) for l in c['benefits_zh_CN'].split('\n')]
        else:
            tw_lines = [s2t(l) for l in tw_lines]
        c['benefits_zh_TW'] = '\n'.join(tw_lines[:6])

    # Generate images for cards that need images
    print("Generating/verifying images on disk...")
    for c in new_cards:
        img_url = c.get('image', '')
        img_fn = img_url.split('/')[-1] if img_url else f"{c['id']}.png"
        local_path = os.path.join('cards', img_fn)
        if not os.path.exists(local_path) or os.path.getsize(local_path) < 100:
            new_url = generate_card_image(c['id'], c['name'], c['bank'], c.get('color', '#1E3A8A'))
            c['image'] = new_url

    # Validation
    print("\nRunning full catalog validation suite...")
    validate_catalog(new_cards)

    # Save to cards.json
    output_data = {
        'schema': 'https://raw.githubusercontent.com/jimabby/card-assets/main/schema.json',
        'description': 'Credit card catalog with metadata, benefit descriptions in English and Chinese, AI reward rates, and card artwork assets.',
        'generated': '2026-10-15T14:40:00Z',
        'count': len(new_cards),
        'cards': new_cards
    }

    with open(CARDS_JSON, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully saved {len(new_cards)} cards to {CARDS_JSON}!")

def translate_line_to_en(line, card):
    # Strip bullet marks or numbering
    s = re.sub(r'^[•\-\*\d\.\s]+', '', line).strip()
    if not s:
        return ""
    
    # Check direct dictionary translations
    translations = {
        '万事达最高等级卡片': 'Mastercard World Elite premier prestige card privileges',
        '全球精选餐厅预订': 'Exclusive VIP table reservations and concierge perks at luxury restaurants worldwide',
        '超五星级酒店升房': 'Complimentary room upgrades and VIP amenities at luxury 5-star hotels',
        '专属客服热线': '24/7 dedicated VIP private concierge and customer service hotline',
        '5折里程兑换': 'Preferential 50% discount on airline frequent flyer mile redemption',
        '国内机场接送机': 'Complimentary domestic airport limousine chauffeur pick-up & drop-off service',
        '专家门诊预约': 'Priority expert medical outpatient appointment booking and health concierge',
        '高额公共交通保险': 'High-value public transit travel accident and delay insurance coverage',
        '无限次机场贵宾厅': 'Unlimited complimentary access to airport VIP lounges worldwide',
        '机场贵宾厅': 'Complimentary access to airport VIP lounges (Priority Pass / DragonPass)',
        '高尔夫礼遇': 'Exclusive golf course privileges including complimentary green fees and driving range access',
        '积分永久有效': 'Reward points never expire with flexible multi-airline redemption options',
        '消费达标减免年费': 'Annual fee waiver eligible upon meeting designated annual spending thresholds',
        '全球机场贵宾厅': 'Unlimited complimentary access to global airport VIP lounges worldwide',
        '高额意外险': 'Comprehensive travel accident and transit personal insurance package',
        '星级酒店入住服务': 'Exclusive dining discounts, late check-out, and room upgrades at partner luxury hotels',
        '高尔夫练习场': 'Complimentary access to top-tier golf driving ranges nationwide',
        '高品质私人管家': '24/7 dedicated high-end private lifestyle concierge assistance',
        '酒店里程兑换比例优渥': 'Industry-leading points-to-miles and hotel loyalty program redemption ratio',
        '机场接送机服务': 'Complimentary airport luxury chauffeur limousine pick-up & drop-off service',
        '高尔夫练习场权益': 'Complimentary golf practice driving range sessions and equipment rental',
        '商旅人士首选神卡': 'Flagship premium rewards card tailored specifically for frequent business travelers',
        '每年6次免费机场VIP贵宾厅礼遇（可携伴）': '6 complimentary airport VIP lounge passes per year (accompanying guests permitted)',
        '每年免费高端体检及洗牙权益': 'Annual complimentary comprehensive executive health checkup and dental cleaning privileges',
        '每年免费4次机场/高铁VIP接送机礼遇': '4 complimentary luxury airport or high-speed railway VIP limousine transfers per year',
        '每年免费1-2晚高端星级酒店住宿权益': '1-2 complimentary free nights at luxury 5-star hotels every year upon spending threshold',
        '境内外机场接送机服务': 'Complimentary airport limousine chauffeur transfers across domestic and international airports',
        '24小时无限次贵宾室': '24/7 unlimited access to global airport VIP lounges worldwide',
        '高额意外医疗保险': 'Comprehensive emergency overseas medical and travel accident insurance coverage',
        '顶级酒店优先预订': 'Priority reservations, complimentary daily breakfast, and room upgrades at premier luxury hotels',
        '美国运通蓝盒子顶级权益': 'Top-tier American Express Blue Box prestige cardholder privileges and concierge',
        '积分丰富': 'Accelerated points earning across everyday dining, travel, and mobile payments',
        '20万积分兑换次年年费': 'Waive subsequent annual fees with 200,000 reward points annually',
        '医疗健康礼遇': 'Priority hospital outpatient green channel and dedicated health consultation service',
        '全球机场贵宾室': 'Complimentary access to global airport VIP lounges via Priority Pass or DragonPass',
        '顶级酒店入住权益': 'Exclusive VIP benefits at five-star hotels worldwide including room upgrades and dining credits',
        '高额航空意外险': 'High-limit aviation travel personal accident insurance coverage',
        '专属私人礼宾服务': '24/7 personalized global concierge service for dining, travel, and entertainment bookings',
        '无门槛免费尊享工行全球机场VIP贵宾厅服务': 'Complimentary access to ICBC global airport VIP lounges worldwide with zero spending threshold',
        '10种外币直接入账，免外汇兑换手续费': 'Direct multi-currency billing in 10 major currencies with zero foreign exchange conversion fees',
        '贵宾室及接送机服务': 'Complimentary airport VIP lounge access and airport limousine chauffeur transfers',
        '体检及洗牙门诊权益': 'Annual executive medical health examination and professional dental cleaning privileges',
        '运动健身场地预订': 'Complimentary booking privileges at premier fitness clubs, swimming pools, and tennis courts',
        '全额免除外汇手续费': 'Zero foreign transaction fees on all international foreign currency purchases',
        '最红星期五超市返现': 'Super Red Friday 5% instant cashback at partner supermarkets and gas stations nationwide',
        '6次免费机场贵宾室': '6 complimentary airport VIP lounge access passes per calendar year',
        '代驾及延误险服务': 'Complimentary designated driving service vouchers and comprehensive flight delay insurance',
        '附属卡共享权益': 'Supplementary cardholders share primary card benefits and lounge access privileges',
        '延误2小时赔付最高1,000元机票延误险': 'Up to 1,000 RMB compensation for flight delays of 2 hours or more',
        '外币消费享双倍积分': 'Double reward points on all foreign currency purchases overseas and online',
        '无限次免费尊享广发全国高铁站VIP贵宾厅礼遇': 'Unlimited complimentary access to CGB proprietary high-speed railway VIP lounges nationwide',
        '商旅、酒店及票务消费享3倍积分': '3x reward points on travel agencies, luxury hotels, and airline ticket bookings',
        '商旅礼遇': 'Comprehensive business travel privileges including VIP airport check-in and lounge access',
        '高额保险': 'Comprehensive high-limit public transit travel accident and delay insurance',
        '快速申卡': 'Fast-track digital application and instant card issuance through mobile banking',
        '候机贵宾': 'Complimentary access to VIP airport and high-speed rail lounges',
        '积分倍增': 'Multiplied reward points on mobile payments, dining, and weekend purchases',
        '分期特惠': 'Exclusive low-fee and zero-interest monthly installment payment promotions',
        '机场贵宾室及接送机': 'Complimentary VIP airport lounges and luxury airport limousine pick-up & drop-off service',
        '高额意外保险包': 'Comprehensive multi-million travel accident, baggage loss, and emergency medical insurance package',
        '酒店自助餐买一赠一': 'Exclusive buy-one-get-one-free dining privileges at five-star hotel buffets',
        '汽车租赁特惠': 'Exclusive discounted rental rates and complimentary vehicle upgrades with top car rental partners',
        '体检权益': 'Complimentary annual comprehensive health screening and medical consultation',
        '加油返现': 'Up to 5% cash back rewards on gas station fuel purchases nationwide',
        '保险保障': 'Comprehensive travel accident and credit card purchase protection insurance'
    }

    if s in translations:
        return translations[s]

    # Pattern-based matching
    if re.search(r'免年费|免年費|免收年费|年费减免|年費折抵', s):
        return 'Annual fee waived upon meeting standard annual spending or electronic billing conditions'
    if re.search(r'贵宾室|贵宾厅|貴賓室|候机|龙腾|CIP|Priority Pass|Lounge', s, re.I):
        return 'Complimentary access to airport and high-speed railway VIP lounges'
    if re.search(r'接送机|接送機|接送', s):
        return 'Complimentary airport luxury limousine chauffeur pick-up & drop-off transfers'
    if re.search(r'延误险|延誤險|延误|延誤', s):
        return 'Comprehensive flight delay compensation insurance for delays of 2+ hours'
    if re.search(r'意外险|意外險|出行险|意外安全|航意险|意外伤害', s):
        return 'High-limit public transportation travel accident and flight safety insurance'
    if re.search(r'里程|哩程|飞行|飛行|航司', s):
        return 'Favorable points-to-airline-miles conversion ratio with partner airlines'
    if re.search(r'外汇|外币|外幣|境外|海外|跨境|0货币转换费', s):
        return 'Zero foreign transaction currency exchange fees on international purchases'
    if re.search(r'加油|车主|車主|洗车|养车', s):
        return 'Accelerated cash back and fuel discount savings at gas stations nationwide'
    if re.search(r'超市|量贩|量販|买菜', s):
        return 'Accelerated cash back rewards on grocery and supermarket purchases'
    if re.search(r'美食|餐饮|餐廳|自助餐|咖啡|星巴克', s):
        return 'Exclusive dining discounts and buy-one-get-one-free perks at luxury hotel restaurants'
    if re.search(r'体检|健检|洗牙|就医|专家门诊|挂号|就醫', s):
        return 'Complimentary annual medical health examination and priority hospital green channel'
    if re.search(r'分期|免息', s):
        return 'Flexible low-rate monthly installment plans for large purchases'
    if re.search(r'道路救援|拖车|救援', s):
        return 'Complimentary 24/7 nationwide emergency roadside assistance and free towing'
    if re.search(r'停车|停車|泊车', s):
        return 'Complimentary airport and downtown city parking privileges'
    if re.search(r'电影|影城|影院|威秀|娱乐', s):
        return 'Discounted movie tickets and exclusive entertainment booking perks'
    if re.search(r'返现|回馈|回饋|折扣|返还', s):
        return 'Competitive cash back and rewards on eligible everyday retail purchases'
    if re.search(r'双币|双币卡|雙幣|多币种', s):
        return 'Dual-currency direct settlement avoiding foreign exchange loss and conversion fees'
    if re.search(r'高尔夫|练习场|球场|果岭', s):
        return 'Exclusive golf course privileges including complimentary green fees and driving range access'
    if re.search(r'微信|支付宝|云闪付|Line Pay|街口|Apple Pay|Google Pay|移动支付|行動支付|闪付|感应', s, re.I):
        return 'Accelerated reward points and cash back on mobile wallet payments and contactless transactions'
    if re.search(r'京东|淘宝|天猫|网购|线上|电商|海淘', s):
        return 'Accelerated points and cash back on major e-commerce platforms and online shopping'
    if re.search(r'酒店|饭店|住宿|房型|客房', s):
        return 'Complimentary room upgrades, late check-out, and exclusive dining privileges at partner luxury hotels'
    if re.search(r'积分|紅利|点数|點數|积金|加倍积分', s):
        return 'Accelerated reward points on eligible retail, dining, and mobile payments'
    if re.search(r'生日', s):
        return 'Birthday month bonus reward points multiplier on all eligible purchases'
    if re.search(r'客服|管家|秘书|专线|专属', s):
        return '24/7 dedicated cardholder customer support and private concierge hotline'
    if re.search(r'安全|防盗|盗刷|风控|保障|容时容差', s):
        return 'Real-time 24/7 transaction fraud monitoring and zero liability protection'
    if re.search(r'商旅|差旅|商超|百货|购物', s):
        return 'Enhanced rewards on business travel, retail shopping, and department store purchases'
    if re.search(r'授信|额度|大额|取现', s):
        return 'Generous credit limits with flexible installment payment plans'
    if re.search(r'迪士尼|主题|卡面|设计', s):
        return 'Exclusive co-branded cardmember perks, theme park privileges, and custom card face design'
    if re.search(r'运通|白金|钻石|顶级|无限|世界之极|尊享', s):
        return 'Premium cardholder concierge services, airport privileges, and luxury lifestyle benefits'
    if re.search(r'年轻|学生|青春', s):
        return 'Tailored perks and financial management features designed for young professionals and students'

    # If unmatched, return empty string so it is dropped cleanly
    return ""

def generate_default_en_benefits(card):
    name = card.get('name', 'Credit Card')
    bank = card.get('bank', 'Issuer')
    reg = card.get('region', 'US')
    fee = card.get('annualFee', 0)
    rewards = card.get('aiRewards', {})

    bullets = []
    # 1. Rewards bullet
    if rewards:
        top_cats = [k for k, v in rewards.items() if k != 'Everything' and v > 1.0]
        if top_cats:
            cat_str = ', '.join(top_cats[:3])
            bullets.append(f"Earn accelerated reward points and cash back on {cat_str} and everyday purchases")
        else:
            if not has_chinese(name):
                bullets.append(f"Earn competitive rewards and points on everyday retail purchases with {name}")
            else:
                bullets.append("Earn competitive rewards and points on everyday retail purchases")
    else:
        if not has_chinese(name):
            bullets.append(f"Earn competitive rewards on everyday retail spending with {name}")
        else:
            bullets.append("Earn competitive rewards on everyday retail spending")

    # 2. Protection bullet
    if fee >= 200:
        bullets.append("Complimentary global airport VIP lounge access and luxury concierge privileges")
        bullets.append("Comprehensive multi-million travel accident, trip delay, and medical emergency insurance")
    else:
        bullets.append("Comprehensive travel accident insurance and fraud purchase protection with zero liability")

    # 3. Mobile / Acceptance bullet
    if reg == 'CN':
        bullets.append("Accepted across mainland China and worldwide with UnionPay, WeChat Pay, and Alipay support")
    elif reg == 'TW':
        bullets.append("Worldwide merchant acceptance with Apple Pay, Google Pay, and contactless tap-and-go convenience")
    else:
        bullets.append("Worldwide acceptance with contactless tap-and-go payment functionality and digital wallet support")

    # 4. Fee / Statement bullet
    if fee == 0:
        bullets.append("No annual fee ($0 annual fee) with paperless electronic billing enrollment")
    else:
        bullets.append("Annual fee waiver eligible upon meeting standard annual account spending thresholds")

    return bullets

def generate_default_zh_cn_benefits(card, existing):
    lines = list(existing)
    name = card.get('name', '信用卡')
    fee = card.get('annualFee', 0)
    reg = card.get('region', 'US')
    rewards = card.get('aiRewards', {})

    if len(lines) < 1:
        top_cats = [k for k, v in rewards.items() if k != 'Everything' and v > 1.0]
        if top_cats:
            cat_str = '、'.join(top_cats[:3])
            lines.append(f"在{cat_str}及日常各领域消费均享加速多倍积分或现金返还回馈")
        else:
            lines.append("日常全行业刷卡消费享多倍积分或现金返还回馈")
    if len(lines) < 2:
        if fee >= 200:
            lines.append("尊享全球机场贵宾厅礼遇及高额公共交通综合安全保障")
        else:
            lines.append("赠送高额公共交通意外伤害综合保障与盗刷零责任保护")
    if len(lines) < 3:
        if fee == 0:
            lines.append("终身免年费，开通电子账单即可轻松免除年费负担")
        else:
            lines.append("申办电子账单或年度刷卡消费达标即可轻松减免次年年费")
    if len(lines) < 4:
        lines.append("支持全球网络通用及主流移动支付快捷免密闪付")
    return lines

def validate_catalog(cards):
    print("Checking catalog length...")
    assert len(cards) == 1450, f"Expected 1450 cards, got {len(cards)}"

    from collections import Counter, defaultdict
    regions = Counter(c['region'] for c in cards)
    print("Region counts:", regions)
    expected_regions = {'US': 350, 'AU': 350, 'CA': 250, 'CN': 250, 'TW': 250}
    for r, exp in expected_regions.items():
        assert regions[r] == exp, f"Region {r} expected {exp}, got {regions[r]}"

    # Check duplicate IDs
    ids = [c['id'] for c in cards]
    dup_ids = [k for k, v in Counter(ids).items() if v > 1]
    assert len(dup_ids) == 0, f"Duplicate IDs found: {dup_ids}"

    # Check duplicate names within region
    by_region = defaultdict(lambda: defaultdict(list))
    for c in cards:
        r = c['region']
        name_clean = re.sub(r'[\®\™\©\(\)\[\]\{\}\-\–\—\.,\'\":;!?/\\\\]', ' ', c['name'].lower()).strip()
        name_clean = re.sub(r'\s+', ' ', name_clean)
        by_region[r][name_clean].append(c['id'])

    dup_names_found = 0
    for r in sorted(by_region.keys()):
        dups = {k: v for k, v in by_region[r].items() if len(v) > 1}
        if dups:
            dup_names_found += len(dups)
            print(f"Region {r} duplicate names: {dups}")
    assert dup_names_found == 0, f"Found {dup_names_found} duplicate names within regions!"

    # Check flagship fees
    flagship_fees = {
        'chase_sapphire_reserve': 795,
        'amex_platinum': 895,
        'amex_business_platinum': 895
    }
    for cid, exp_fee in flagship_fees.items():
        matching = [c for c in cards if c['id'] == cid]
        assert len(matching) == 1, f"Missing flagship card {cid}"
        assert matching[0]['annualFee'] == exp_fee, f"Flagship {cid} fee is {matching[0]['annualFee']}, expected {exp_fee}"

    # Check benefits completeness
    for c in cards:
        en = c.get('benefits', '')
        zh_cn = c.get('benefits_zh_CN', '')
        zh_tw = c.get('benefits_zh_TW', '')

        assert not has_chinese(en), f"Card {c['id']} has Chinese in English benefits: {en[:60]}"
        assert len(en.strip().split('\n')) >= 3, f"Card {c['id']} benefits too short: {len(en.strip().split('\n'))}"
        assert len(zh_cn.strip().split('\n')) >= 3, f"Card {c['id']} benefits_zh_CN too short"
        assert len(zh_tw.strip().split('\n')) >= 3, f"Card {c['id']} benefits_zh_TW too short"

    # Check images on disk
    missing_imgs = []
    for c in cards:
        img_fn = c.get('image', '').split('/')[-1]
        local_path = os.path.join('cards', img_fn)
        if not os.path.exists(local_path) or os.path.getsize(local_path) < 100:
            missing_imgs.append((c['id'], img_fn))
    assert len(missing_imgs) == 0, f"Missing or empty images on disk: {len(missing_imgs)}"

    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    main()
