import json
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

from scripts.card_img_helper import generate_card_image, disk_files, CARDS_DIR

# 1. Load current catalog
with open('cards.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

cards = catalog['cards']

# Remove synthetic suffix template cards from previous run
synthetic_suffixes = [
    '_rewards_plus', '_cashback_preferred', '_travel_infinite',
    '_business_rewards', '_world_elite', '_low_rate_classic', '_student_cash'
]

synthetic_ids = set()
authentic_cards = []

for c in cards:
    cid = c['id']
    is_synth = False
    for s in synthetic_suffixes:
        if cid.endswith(s) and (cid.startswith('ca_') or cid.startswith('us_') or cid.startswith('au_') or cid.startswith('cn_') or cid.startswith('tw_')):
            is_synth = True
            synthetic_ids.add(cid)
            break
    if not is_synth:
        authentic_cards.append(c)

# Clean synthetic images from disk
for cid in synthetic_ids:
    for ext in ['.png', '.jpg', '.jpeg', '.webp']:
        p = os.path.join(CARDS_DIR, f"{cid}{ext}")
        if os.path.exists(p):
            try:
                os.remove(p)
            except Exception:
                pass

print(f"Base authentic cards remaining: {len(authentic_cards)}")
existing_ids = {c['id'] for c in authentic_cards}

# 2. Add real-world specific credit card products
NEW_REAL_CARDS = [
    # US REAL CARDS
    ("chase_united_quest", "Chase United Quest Card", "US", "chase.com", 250, "#00205B", "3x miles on United Airlines purchases\n2x miles on dining, gas, and select streaming\nUp to $125 annual United purchase credit\nTwo 5,000-mile award flight credits each year\nFirst & second checked bag free", "预订联合航空消费享3倍里程\n餐饮、加油及精选流媒体享2倍里程\n每年最高$125联合航空消费抵扣\n每年赠送两次5,000里程奖励机票抵扣\n主卡及同行人前两件托运行李免费", {"Flights": 4.2, "Travel": 4.2, "Food & Dining": 2.8, "Gas & Transit": 2.8, "Everything": 1.4}),
    ("chase_united_club_infinite", "Chase United Club Infinite Card", "US", "chase.com", 525, "#00142E", "4x miles on United Airlines purchases\n2x miles on all other travel and dining\nComplimentary United Club lounge membership\nFirst & second checked bag free\n25% inflight discount", "预订联合航空消费享4倍里程\n其他旅行及餐饮消费享2倍里程\n免费尊享联合航空United Club贵宾厅会员\n主卡及同行人前两件托运行李免费\n机上消费享75折优惠", {"Flights": 5.6, "Travel": 5.6, "Food & Dining": 2.8, "Hotels": 2.8, "Everything": 1.4}),
    ("chase_southwest_plus", "Chase Southwest Rapid Rewards Plus", "US", "chase.com", 69, "#304CB2", "2x points on Southwest purchases, local transit, and internet/phone/streaming\n1x point elsewhere\n3,000 anniversary points each year\n2 EarlyBird Check-In per year", "西南航空、本地交通及网络/电话/流媒体消费享2倍积分\n其他消费1倍积分\n每年续卡赠送3,000周年奖励积分\n每年赠送2次优先登机EarlyBird Check-In", {"Flights": 3.0, "Travel": 3.0, "Gas & Transit": 3.0, "Everything": 1.5}),
    ("chase_southwest_premier", "Chase Southwest Rapid Rewards Premier", "US", "chase.com", 99, "#112B85", "3x points on Southwest purchases\n2x points on local transit, internet, cable, and streaming\n6,000 anniversary points each year\nNo foreign transaction fees", "西南航空消费享3倍积分\n本地交通、网络、有线电视及流媒体享2倍积分\n每年续卡赠送6,000周年奖励积分\n无境外交易手续费", {"Flights": 4.5, "Travel": 4.5, "Gas & Transit": 3.0, "Everything": 1.5}),
    ("chase_southwest_performance_biz", "Chase Southwest Performance Business", "US", "chase.com", 199, "#001A70", "4x points on Southwest purchases\n2x points on social media/search advertising, transit, and telecom\n9,000 anniversary points each year\n4 Upgraded Boardings per year\nInflight Wi-Fi credits", "西南航空消费享4倍积分\n社交媒体/搜索广告、交通及通信服务享2倍积分\n每年续卡赠送9,000周年奖励积分\n每年4次免费升等登机A1-A15位置\n机上Wi-Fi费用报销", {"Flights": 6.0, "Travel": 6.0, "Shopping": 3.0, "Everything": 1.5}),
    ("chase_hyatt_business", "Chase World of Hyatt Business Credit Card", "US", "chase.com", 199, "#1A1A1A", "9x total points on Hyatt stays\n2x points in your top 2 spend categories each quarter\nDiscoverist status for up to 5 employees\n$100 annual Hyatt statement credit", "凯悦旗下酒店消费享最高9倍积分\n每季度最高消费的前2个类别享2倍积分加成\n可为最多5名员工赠送Discoverist会籍\n每年$100凯悦酒店消费抵扣", {"Hotels": 7.2, "Travel": 7.2, "Food & Dining": 3.2, "Everything": 1.6}),
    ("chase_ihg_traveler", "Chase IHG One Rewards Traveler", "US", "chase.com", 0, "#1E3A8A", "Up to 17x total points at IHG Hotels & Resorts\n3x points on gas stations, utilities, dining, and streaming\n2x points on all other purchases\nNo annual fee", "洲际IHG旗下酒店消费享最高17倍总积分\n加油站、公共事业缴费、餐饮及流媒体享3倍积分\n其他所有消费享2倍积分\n免年费", {"Hotels": 3.4, "Food & Dining": 1.5, "Gas & Transit": 1.5, "Everything": 1.0}),
    ("amex_hilton_business", "Hilton Honors Business Amex", "US", "americanexpress.com", 195, "#001E36", "12x points on Hilton hotel stays\n5x points on everyday business purchases\nComplimentary Hilton Honors Gold status\nNo foreign transaction fees", "希尔顿旗下酒店消费享12倍积分\n日常商业消费享5倍积分\n免费赠送希尔顿尊贵金卡会籍\n无境外交易手续费", {"Hotels": 6.0, "Travel": 6.0, "Shopping": 2.5, "Everything": 1.5}),
    ("amex_delta_blue", "Delta SkyMiles Blue Amex", "US", "americanexpress.com", 0, "#002244", "2x miles on Delta purchases and at restaurants worldwide\n1x mile on all other purchases\n25% inflight food & beverage savings\nNo foreign transaction fees", "达美航空消费及全球餐厅消费享2倍里程\n其他消费1倍里程\n机上餐饮享75折优惠\n无境外交易手续费", {"Flights": 2.4, "Food & Dining": 2.4, "Everything": 1.2}),
    ("capital_one_venture_x_business", "Capital One Venture X Business", "US", "capitalone.com", 395, "#0B2545", "10x miles on hotels & rental cars through Capital One Travel\n5x miles on flights through Capital One Travel\n2x miles on all other purchases\n10,000 anniversary miles each year\nCapital One & Partner Lounge access", "通过Capital One商旅预订酒店及租车享10倍里程\n预订机票享5倍里程\n其他所有商业消费享2倍里程\n每年续卡赠送10,000周年奖励里程\n无限次进入Capital One及合作贵宾室", {"Travel": 10.0, "Hotels": 10.0, "Car Rental": 10.0, "Flights": 5.0, "Everything": 2.0}),
    ("wells_fargo_choice_privileges_select", "Choice Privileges Select Mastercard", "US", "wellsfargo.com", 95, "#003366", "10x points at participating Choice Hotels\n5x points on gas, groceries, home improvement, and phone plans\n30,000 bonus points each anniversary year\nComplimentary Choice Privileges Platinum status", "Choice合作酒店消费享10倍积分\n加油、超市买菜、家装及手机套餐享5倍积分\n每年续卡赠送30,000周年奖励积分\n免费赠送Choice Privileges白金卡会籍", {"Hotels": 6.0, "Groceries": 3.0, "Gas & Transit": 3.0, "Shopping": 3.0, "Everything": 1.2}),
    ("barclays_wyndham_earner_business", "Wyndham Rewards Earner Business Card", "US", "barclaysus.com", 95, "#00539B", "8x points on Wyndham hotel stays and gas stations\n5x points on marketing, utility, and telecom services\nComplimentary Wyndham Diamond status\n15,000 anniversary points per year", "温德姆旗下酒店及加油站消费享8倍积分\n营销广告、公共事业及通信服务享5倍积分\n免费赠送温德姆最高钻石会员会籍\n每年续卡赠送15,000周年奖励积分", {"Hotels": 7.2, "Gas & Transit": 7.2, "Shopping": 4.5, "Everything": 0.9}),
    ("barclays_hawaiian_biz", "Hawaiian Airlines Business Mastercard", "US", "barclaysus.com", 99, "#4A0E4E", "3x miles on Hawaiian Airlines purchases\n2x miles on gas, dining, office supply, and cell phone services\nUp to 40,000 anniversary bonus miles based on annual spend", "夏威夷航空消费享3倍里程\n加油、餐饮、办公用品及手机费扣款享2倍里程\n依据年度刷卡额度最高赠送40,000周年里程", {"Flights": 3.0, "Food & Dining": 2.0, "Gas & Transit": 2.0, "Everything": 1.0}),
    ("synchrony_walgreens_mastercard", "Walgreens Mastercard", "US", "synchrony.com", 0, "#E31837", "10% cash back in myWalgreens cash rewards on Walgreens brand products\n5% cash back on other Walgreens purchases\n3% cash back on grocery and health & wellness purchases", "在Walgreens购买自有品牌商品享10%现金奖励\n购买其他商品享5%现金奖励\n超市买菜及健康养生消费享3%现金返还", {"Groceries": 3.0, "Shopping": 5.0, "Everything": 1.0}),
    ("synchrony_bp_me_rewards", "BP me Rewards Visa", "US", "synchrony.com", 0, "#009933", "15c off per gallon on BP & Amoco fuel purchases\n3% cash back on dining and grocery store purchases\n1% cash back on all other purchases", "在BP及Amoco加油站加油每加仑立减15分\n餐饮及超市买菜享3%现金返还\n其他消费1%", {"Gas & Transit": 5.0, "Food & Dining": 3.0, "Groceries": 3.0, "Everything": 1.0}),
    ("navy_federal_nrewards", "Navy Federal nRewards Secured", "US", "navyfederal.org", 0, "#003366", "1 point per $1 spent on all purchases\nDesigned to help active duty military and veterans build credit history\nAutomatic review for graduation to unsecured card starting at 6 months", "所有刷卡消费每$1赚1积分\n专为现役军人及退役军人建立与修复个人信用设计\n开卡6个月起自动评估毕业转为无担保信用卡", {"Everything": 1.0}),
    ("usaa_eagle_navigator", "USAA Eagle Navigator Visa Signature", "US", "usaa.com", 95, "#0B2341", "3x points on travel purchases (flights, hotels, vacation rentals)\n2x points on all other eligible purchases\n10,000 anniversary bonus points after qualifying annual travel spend", "旅行消费（机票、酒店、度假租赁）享3倍积分\n其他所有符合条件的消费享2倍积分\n年度旅行刷卡达标赠送10,000周年奖励积分", {"Travel": 3.0, "Flights": 3.0, "Hotels": 3.0, "Everything": 2.0}),
    ("pnc_points_visa", "PNC Points Visa Credit Card", "US", "pnc.com", 0, "#F47920", "4x points on all purchases\nBonus points of 25% to 75% with qualifying PNC Virtual Wallet checking accounts\nNo annual fee", "所有刷卡消费享4倍积分\n搭配PNC Virtual Wallet支票账户最高享75%额外积分加成\n免年费", {"Everything": 1.5}),
    ("fifth_third_preferred_cash", "Fifth Third Preferred Cash Back", "US", "53.com", 0, "#003B70", "2% cash back on all purchases with Fifth Third Preferred Banking\nNo category restrictions and no rewards caps\nNo annual fee", "绑定Fifth Third Preferred理财账户刷卡享全品类2%现金返还\n无类别限制及返现上限\n免年费", {"Everything": 2.0}),
    ("truist_enjoy_travel", "Truist Enjoy Travel Credit Card", "US", "truist.com", 0, "#482683", "2x miles on airfare, car rentals, and hotels\n1x mile on all other purchases\n$85 air travel credit every 4 years for TSA PreCheck/Global Entry", "机票、租车及酒店预订享2倍里程\n其他消费1倍里程\n每4年报销最高$85 TSA PreCheck/Global Entry申请费", {"Travel": 2.0, "Flights": 2.0, "Hotels": 2.0, "Car Rental": 2.0, "Everything": 1.0}),
    ("citizens_bank_clear_value", "Citizens Bank Clear Value Mastercard", "US", "citizensbank.com", 0, "#008559", "Consistently low ongoing interest rate on purchases and balance transfers\nNo annual fee\nWorld Mastercard travel benefits", "刷卡消费及余额转账保持超低年利率\n免年费\nWorld Mastercard尊贵旅行权益", {"Everything": 0.5}),
    ("keybank_rewards", "KeyBank Key Rewards Credit Card", "US", "key.com", 0, "#D32F2F", "2x points on all purchases when maintaining qualifying KeyBank relationship\n1x point standard\nNo annual fee", "符合KeyBank综合理财条件享所有消费2倍积分\n标准消费1倍积分\n免年费", {"Everything": 1.5}),
    ("td_clear_visa", "TD Clear Visa Credit Card", "US", "td.com", 0, "#008A00", "No interest charges credit card with a simple flat monthly subscription fee ($10 or $20)\nNo late fees & no foreign transaction fees", "零利息信用卡，仅按月收取固定服务费（$10或$20）\n无滞纳金且无境外交易手续费", {"Everything": 0.5}),
    ("td_flexpay", "TD FlexPay Credit Card", "US", "td.com", 0, "#008A00", "Increased flexibility with one free late fee waiver per 12 months\n0% intro APR on balance transfers for 18 months\nNo annual fee", "极高还款灵活性，每12个月免费免除一次滞纳金\n余额转账享前18个月0%优惠年利率\n免年费", {"Everything": 0.5}),
    ("bmo_alto_mastercard", "BMO Alto Mastercard", "US", "bmo.com", 0, "#0079C1", "Unlimited 1% cash back on all purchases\n0% intro APR on balance transfers for 12 months\nNo annual fee", "所有刷卡消费享1%无上限现金返还\n余额转账享前12个月0%优惠年利率\n免年费", {"Everything": 1.0}),
    ("fnbo_evergreen", "FNBO Evergreen Credit Card", "US", "fnbo.com", 0, "#006633", "2% cash back on every purchase with no caps or category limits\n10,000 bonus points after spending $1,000 in first 6 months\nNo annual fee", "无类别及返现上限享2%现金返还\n开卡前6个月刷卡满$1,000赠送10,000奖励积分\n免年费", {"Everything": 2.0}),
    ("bread_financial_cashback", "Bread Financial Cashback Amex", "US", "breadfinancial.com", 0, "#003087", "Unlimited 2% cash back on all purchases\nExclusive American Express merchant offers\nNo annual fee & no foreign fees", "所有刷卡消费享无上限2%现金返还\n尊享美国运通AE专属商家优惠特惠\n免年费且无外币手续费", {"Everything": 2.0}),
    ("alaska_airlines_biz_visa", "Alaska Airlines Business Visa", "US", "alaskair.com", 95, "#004B87", "3x miles on Alaska Airlines purchases\n2x miles on gas, shipping, and transit\nFamous Alaska Companion Fare every year\nFirst checked bag free", "预订阿拉斯加航空消费享3倍里程\n加油、快递发货及交通消费享2倍里程\n每年续卡赠送著名同行机票优惠券\n首件托运行李免费", {"Flights": 3.0, "Travel": 3.0, "Gas & Transit": 2.0, "Everything": 1.0}),
    ("us_bank_business_triple_cash", "U.S. Bank Business Triple Cash Rewards", "US", "usbank.com", 0, "#0C2340", "3% cash back on gas/EV charging, office supply, cell phone, and dining\n1% on all other purchases\n$100 annual software credit for recurring subscriptions\nNo annual fee", "加油/充电、办公用品、手机费及餐饮享3%现金返还\n其他消费1%\n每年$100软件订阅服务报销\n免年费", {"Food & Dining": 3.0, "Gas & Transit": 3.0, "Shopping": 3.0, "Everything": 1.0}),

    # CA REAL CARDS
    ("scotiabank_passport_visa_infinite", "Scotiabank Passport Visa Infinite", "CA", "scotiabank.com", 150, "#EC1C24", "Zero foreign transaction fees on all international spending\n3x Scene+ points on groceries\n2x points on dining, entertainment, and daily transit\n6 complimentary DragonPass airport lounge passes per year", "所有国际外币消费零外汇手续费\n在Sobeys、Safeway及FreshCo超市买菜享3倍Scene+积分\n餐饮、娱乐及日常交通享2倍积分\n每年赠送6次DragonPass龙腾出行VIP机场贵宾厅", {"Groceries": 3.0, "Food & Dining": 2.0, "Entertainment": 2.0, "Gas & Transit": 2.0, "Everything": 1.0}),
    ("rbc_ion_plus_visa", "RBC ION+ Visa", "CA", "rbc.com", 48, "#005DAA", "3x Avion Rewards points on grocery, dining, food delivery, rideshare, streaming, and gaming\n1x point elsewhere\nSave 3c/L on gas at Petro-Canada", "超市买菜、餐饮、外卖、网约车、流媒体及游戏消费享3倍Avion积分\n其他消费1分\nPetro-Canada加油每升节省3分", {"Food & Dining": 3.0, "Groceries": 3.0, "Gas & Transit": 3.0, "Entertainment": 3.0, "Everything": 1.0}),
    ("rbc_westjet_world_elite", "RBC WestJet World Elite Mastercard", "CA", "rbc.com", 119, "#005DAA", "2% back in WestJet dollars on WestJet flight purchases\n1.5% back in WestJet dollars on all other purchases\nAnnual World Companion Voucher starting at $119\nFree first checked bag for up to 9 travelers", "预订西捷航空WestJet机票享2% WestJet Dollars返现\n其他所有消费享1.5%返现\n每年赠送极具价值的同行机票优惠券（$119起）\n主卡及同行最多8人首件托运行李免费", {"Flights": 2.0, "Travel": 2.0, "Everything": 1.5}),
    ("cibc_aeroplan_visa_infinite", "CIBC Aeroplan Visa Infinite", "CA", "cibc.com", 139, "#C41230", "1.5 Aeroplan points/$1 on Air Canada, gas, and groceries\n1 point/$1 on all other purchases\nFree first checked bag for cardholder and companions", "加拿大航空、加油及超市买菜每$1赚1.5 Aeroplan里程\n其他消费1分\n主卡及同行人首件托运行李免费", {"Flights": 2.25, "Groceries": 2.25, "Gas & Transit": 2.25, "Everything": 1.5}),
    ("td_aeroplan_visa_infinite", "TD Aeroplan Visa Infinite", "CA", "td.com", 139, "#008A00", "1.5 Aeroplan points/$1 on gas, grocery, and direct Air Canada purchases\n1 point/$1 elsewhere\nFree first checked bag on Air Canada", "加油、超市买菜及加航直营预订每$1赚1.5 Aeroplan里程\n其他消费1分\n加拿大航空首件托运行李免费", {"Flights": 2.25, "Groceries": 2.25, "Gas & Transit": 2.25, "Everything": 1.5}),
    ("koho_extra_mastercard", "KOHO Extra Mastercard", "CA", "koho.ca", 108, "#00D2C8", "2% cash back on groceries, dining, and transportation\n0.5% cash back on all other purchases\nEarn high interest on card balance\nNo foreign transaction fees", "买菜、餐饮及交通消费享2%现金返还\n其他消费0.5%\n卡内资金赚取高额利息\n零外汇手续费", {"Food & Dining": 2.0, "Groceries": 2.0, "Gas & Transit": 2.0, "Everything": 0.5}),
    ("wealthsimple_cash_card", "Wealthsimple Cash Prepaid Mastercard", "CA", "wealthsimple.com", 0, "#000000", "1% cash back or crypto/stock rewards on all purchases\nZero foreign transaction fees\nHigh savings interest rate on card balance\nNo annual fee", "所有消费享1%现金返还或加密货币/股票奖励\n零外币交易手续费\n卡内资金享受高额存款利息\n免年费", {"Everything": 1.0}),
    ("walmart_rewards_mastercard_ca", "Walmart Rewards Mastercard Canada", "CA", "walmart.ca", 0, "#0071CE", "1.25% back in Walmart Rewards on Walmart.ca and in-store\n1% back on all other purchases\nNo annual fee", "在Walmart加拿大官网及门店消费享1.25% Walmart Rewards返现\n其他消费1%\n免年费", {"Groceries": 1.25, "Shopping": 1.25, "Everything": 1.0}),
    ("atb_world_elite_mastercard", "ATB World Elite Mastercard", "CA", "atb.com", 120, "#008559", "2% cash back on all purchases or 3% back when redeemed into ATB investment account\nComplimentary travel medical insurance", "所有刷卡消费享2%现金返还（兑换存入ATB投资账户升至3%）\n包含旅行医疗保险", {"Everything": 2.0}),

    # AU REAL CARDS
    ("qantas_premier_everyday", "Qantas Premier Everyday", "AU", "qantas.com", 49, "#E0001A", "0.75 Qantas Point per $1 spent up to $3,000/mo (0.4 pts/$1 thereafter)\n1 bonus Qantas Point per $1 on eligible Qantas spend\nLow annual fee", "每月前$3,000消费每$1赚0.75 Qantas积分\n预订Qantas机票每$1额外赚1分\n超低年费", {"Flights": 2.0, "Travel": 2.0, "Everything": 0.75}),
    ("woolworths_qantas_platinum", "Woolworths Qantas Platinum", "AU", "woolworths.com.au", 99, "#007A33", "1 Qantas Point per $1 spent on Woolworths purchases\n0.5 Qantas Points/$1 elsewhere\n10% off one Woolworths shop every month", "在Woolworths超市消费每$1赚1 Qantas积分\n其他消费0.5分\n每月享受一次Woolworths买菜9折", {"Groceries": 4.0, "Everything": 0.5}),
    ("hsbc_premier_world_elite", "HSBC Premier World Elite Mastercard", "AU", "hsbc.com.au", 0, "#DB0011", "2 HSBC Premier Rewards points per $1 spent on all eligible purchases\nComplimentary unlimited LoungeKey airport lounge access\nZero annual fee for HSBC Premier banking clients", "所有符合条件的刷卡消费每$1赚2 HSBC Premier积分\n无限次免费使用LoungeKey全球机场VIP贵宾厅\n汇丰Premier卓越理财客户免收年费", {"Travel": 2.0, "Flights": 2.0, "Hotels": 2.0, "Food & Dining": 1.6, "Everything": 1.6}),
    ("bankwest_more_platinum", "Bankwest More Platinum Mastercard", "AU", "bankwest.com.au", 160, "#FF6600", "1.5 More Rewards Points per $1 spent on eligible purchases\nPoints redeemable for cashback, gift cards, and electronic products\nComplimentary international travel insurance", "符合条件的刷卡消费每$1赚取1.5 More奖励积分\n积分可自由兑换帐单现金回馈、礼品卡及电子产品\n附赠全面国际旅游保险", {"Shopping": 0.8, "Everything": 0.8}),
    ("virgin_money_high_flyer", "Virgin Money High Flyer Credit Card", "AU", "virginmoney.com.au", 289, "#C8102E", "1 Velocity Point per $1 spent up to $8,000 per month (0.5 pts/$1 thereafter)\n2 complimentary Virgin Australia lounge passes each year\n$129 Virgin Australia gift voucher each year upon renewal", "每月前$8,000消費每$1賺取1 Velocity哩程積分（超出部分0.5積分/$1）\n每年贈送2張澳洲維珍航空Virgin Australia機場VIP貴賓室門票\n每年續卡獲贈$129維珍航空機票優惠券", {"Flights": 2.5, "Travel": 2.5, "Everything": 1.2}),
    ("suncorp_clear_options_platinum", "Suncorp Clear Options Platinum", "AU", "suncorp.com.au", 129, "#005F60", "1.25 Suncorp Rewards points per $1 spent on eligible purchases\nPoints redeemable for cashback, gift cards, or airline frequent flyer points\nComplimentary international travel insurance", "符合條件的刷卡消費每$1賺取1.25 Suncorp積分\n積分可自由兌換現金回饋、禮品卡或合作航空公司哩程\n包含全面國際旅遊保險", {"Everything": 0.8}),
    ("citibank_premier_au", "Citi Premier Credit Card AU", "AU", "citibank.com.au", 300, "#005696", "2 Citi Rewards Points per $1 spent on overseas transactions\n1 Citi Rewards Point per $1 spent domestically\n2 complimentary Priority Pass airport lounge visits per year\nFree bottle of wine at Citi Dining Program restaurants", "海外刷卡消費每$1賺取2 Citi Rewards積分\n澳大利亞國內消費每$1賺取1積分\n每年贈送2次Priority Pass VIP機場貴賓室\n在Citi Dining合作餐廳用餐贈送免費美酒一瓶", {"Travel": 2.0, "Flights": 2.0, "Hotels": 2.0, "Everything": 1.0}),
    ("great_southern_bank_everyday", "Great Southern Bank Everyday Mastercard", "AU", "greatsouthernbank.com.au", 0, "#003366", "Low rate credit card with zero annual fee\nZero foreign currency conversion fee option\nInstant lock and unlock features via mobile app", "零年费低利率信用卡\n可选零外汇转换费方案\n支持手机App即时锁卡与解锁", {"Everything": 0.5}),

    # CN REAL CARDS
    ("icbc_constellation_card", "ICBC Constellation Credit Card", "CN", "icbc.com.cn", 0, "#121212", "Customized 12 constellation card face designs with black core technology\nZero annual fee for lifetime\nDouble points on mobile payment transactions (WeChat & Alipay)", "专属12星座个性化黑芯工艺卡面设计\n终身免年费\n微信支付、支付宝绑定刷卡享双倍积分", {"Shopping": 1.0, "Everything": 1.0}),
    ("ccb_long_joy_white", "CCB Long Card Joy Platinum Card", "CN", "ccb.com", 580, "#FF8C00", "5x points on video streaming, gaming, and online ordering\nComplimentary JD Plus annual membership upon qualifying card spend\n3 complimentary high-speed railway VIP lounge visits per year", "影音串流、游戏及外卖点餐刷卡享5倍积分\n刷卡达标免费赠送京东JD Plus年卡会员\n每年3次免费全国高铁VIP贵宾室礼遇", {"Entertainment": 2.5, "Food & Dining": 2.5, "Shopping": 2.5, "Everything": 0.5}),
    ("spdb_bilibili_card", "SPDB Bilibili Co-branded Credit Card", "CN", "spdb.com.cn", 0, "#00A1D6", "Complimentary Bilibili VIP annual membership upon meeting card spend quota\nDouble points on ACG comic, gaming, and online video purchases\nNo annual fee for lifetime with electronic statement", "刷卡达标免费赠送Bilibili哔哩哔哩大会员年卡\n二次元动漫、游戏及视频消费享双倍积分加成\n申办电子账单终身免年费", {"Entertainment": 2.5, "Everything": 1.0}),
    ("ceb_tiktok_card", "CEB Douyin Co-branded Credit Card", "CN", "cebbank.com", 0, "#161823", "Complimentary Douyin E-commerce shopping cash vouchers upon card activation\n3x points on mobile payments (WeChat, Alipay, Douyin Pay)\nFirst year annual fee waived", "开卡达标即送抖音电商购物立减券礼包\n微信支付、支付宝及抖音支付消费享3倍积分\n首年免年费", {"Shopping": 2.5, "Entertainment": 2.5, "Everything": 1.0}),
    ("citic_ihg_premier", "CITIC IHG One Rewards Platinum Card", "CN", "citicbank.com", 480, "#1E3A8A", "Favorable 8:1 exchange rate directly credited into IHG One Rewards points\nComplimentary IHG One Rewards Gold Elite status\n85% off room rates on IHG weekend stays in Greater China", "刷卡以8:1优异汇率直接自动兑换IHG洲际优悦会积分\n免费赠送IHG洲际优悦会金卡精英会员会籍\n预订大中华区IHG旗下饭店周末住宿享85折特惠", {"Hotels": 4.0, "Travel": 4.0, "Everything": 1.2}),
    ("guangfa_meituan_card", "CGB Meituan Co-branded Credit Card", "CN", "cgbchina.com.cn", 0, "#FFC000", "5% cash back / Zero-threshold Meituan cash vouchers on food delivery and group buying\n1% cash back on general daily spend credited as Meituan payment credit\nNo annual fee for lifetime", "美团外卖点餐、到店团购消费享5%无门槛美团现金抵用券回馈\n日常刷卡一般消费享1%美团支付立减金\n申办电子账单终身免年费", {"Food & Dining": 5.0, "Groceries": 5.0, "Everything": 1.0}),

    # TW REAL CARDS
    ("cathay_cube_card", "Cathay United CUBE Card", "TW", "cathaybk.com.tw", 0, "#00875A", "3% tree points (uncapped) with 4 customizable daily reward themes\nSwitch themes once per day freely via Cathay United Mobile Banking App\n1 Tree Point = 1 TWD statement credit deduction", "四大指定權益方案（玩數位、樂饗購、趣旅行、集精選）享最高3%小樹點回饋無上限\n每日可透過國泰世華CUBE App免費切換一次方案\n1點小樹點可無門檻折抵1元帳單刷卡金", {"Shopping": 3.0, "Food & Dining": 3.0, "Travel": 3.0, "Everything": 0.3}),
    ("hsbc_live_plus_tw", "HSBC Live+ Cash Back Card", "TW", "hsbc.com.tw", 0, "#DB0011", "3.88% cash back on dining, shopping, and entertainment across 8 Asian markets\n1% uncapped cash back on general domestic & overseas spending\n0.88% extra cash back when setting up HSBC auto debit payment", "亞洲8大國家地區指定餐飲、購物及娛樂消費享最高3.88%現金回饋\n國內及海外一般消費享1%現金回饋無上限\n綁定匯豐帳戶自動扣繳享額外0.88%加碼回饋", {"Food & Dining": 3.88, "Entertainment": 3.88, "Shopping": 3.88, "Everything": 1.0}),
    ("ctbc_foodpanda_card", "CTBC foodpanda Co-branded Card", "TW", "ctbcbank.com", 0, "#FF2B85", "Up to 8% foodpanda Coins reward on foodpanda delivery and Pandamart orders\n1% foodpanda Coins reward on general domestic & overseas spending\nFree foodpanda delivery vouchers awarded monthly", "foodpanda外送及生鮮雜貨熊貓超市消費享最高8%胖胖幣回饋\n國內及海外一般消費享1%胖胖幣回饋無上限\n每月加碼贈送foodpanda免運費優惠券", {"Food & Dining": 8.0, "Groceries": 8.0, "Everything": 1.0}),
    ("taishin_flygo_card", "Taishin FlyGo Card", "TW", "taishinbank.com.tw", 0, "#D32F2F", "Up to 5% cash back / Taishin Point on travel, airline tickets, High-Speed Rail, and foreign transactions\n1% uncapped domestic general spending reward", "指定航空、旅行社、高鐵及海外刷卡消費享最高5%回饋\n國內一般消費享1%無上限回饋\n贈送最高3,000萬元高額旅遊平安險保障", {"Travel": 5.0, "Flights": 5.0, "Hotels": 5.0, "Gas & Transit": 5.0, "Everything": 1.0}),
    ("sinopac_daway_line", "SinoPac DAWAY LINE Pay Card", "TW", "sinopac.com", 0, "#1C1C1C", "Up to 3% LINE POINTS reward when spending with LINE Pay mobile wallet\n3% LINE POINTS reward on overseas physical & online shopping\n1% basic LINE POINTS reward on general domestic spend", "綁定LINE Pay行動支付消費享最高3% LINE POINTS回饋\n海外實體及網購刷卡消費享3% LINE POINTS回饋\n國內一般消費享1% LINE POINTS基本回饋無上限", {"Shopping": 3.0, "Food & Dining": 3.0, "Everything": 1.0}),
    ("nextbank_dajiang_card", "Next Bank Da Jiang Card", "TW", "nextbank.com.tw", 0, "#00A859", "Up to 3.5% N Point reward on overseas spending and gourmet dining\n1.5% basic N Point reward on domestic spending\n1 N Point = 1 TWD statement credit", "海外刷卡及指定全台精選美食餐廳享最高3.5% N點回饋\n國內一般消費享1.5% N點基本回饋無上限\n1點N點可直接無門檻折抵1元帳單刷卡金", {"Food & Dining": 3.5, "Travel": 3.5, "Everything": 1.5}),
    ("first_ileo_card", "First Bank iLEO Card", "TW", "firstbank.com.tw", 0, "#009688", "Up to 3% cash back when bound to mobile payments (Taiwan Pay, Line Pay, Apple Pay)\n2% cash back on overseas physical spending\n0.5% uncapped cash back on domestic general spend", "綁定指定行動支付（台灣Pay、LINE Pay、Apple Pay等）享最高3%現金回饋\n海外實體刷卡消費享2%現金回饋\n國內一般消費享0.5%現金回饋無上限", {"Shopping": 3.0, "Everything": 0.5}),
    ("yuanta_diamond_card", "Yuanta Diamond Card", "TW", "yuantabank.com.tw", 0, "#003366", "2.2% cash back uncapped on all overseas transactions\n1.2% cash back uncapped on domestic general spending\nNo spending thresholds or category restrictions", "海外刷卡消費享2.2%現金回饋無上限\n國內一般消費享1.2%現金回饋無上限\n無消費門檻及級距限制，直接自動折抵帳單", {"Travel": 2.2, "Everything": 1.2}),
    ("hncb_sny_card", "Hua Nan SnY Credit Card", "TW", "hncb.com.tw", 0, "#E60012", "5% cash back on online shopping (Shopee, Momo, PChome, Yahoo)\n10% cash back on streaming platforms (Netflix, Spotify, YouTube Premium)\n0.5% uncapped domestic & overseas basic reward", "指定網購通路（包含蝦皮、momo、PChome等）享最高5%現金回饋\n指定串流影音（Netflix、Spotify、YouTube Premium等）享最高10%現金回饋\n國內及海外一般消費享0.5%基本回饋無上限", {"Entertainment": 10.0, "Shopping": 5.0, "Everything": 0.5}),
    ("shanghai_minions_card", "SCSB Minions Card", "TW", "scsb.com.tw", 0, "#FFF000", "5% cash back on domestic online shopping & cinema tickets\n2% cash back on overseas spending\n1% uncapped domestic general spending reward", "國內網購及全台各大影城看電影享最高5%現金回饋\n海外刷卡消費享2%現金回饋\n國內一般消費享1%無上限回饋", {"Entertainment": 5.0, "Shopping": 5.0, "Everything": 1.0})
]

added_count = 0
for item in NEW_REAL_CARDS:
    cid, name, region, bank, fee, color, b_en, b_cn, rewards = item
    if cid not in existing_ids:
        authentic_cards.append({
            "id": cid,
            "name": name,
            "region": region,
            "bank": bank,
            "annualFee": fee,
            "color": color,
            "benefits": b_en,
            "benefits_zh_CN": b_cn,
            "benefits_zh_TW": b_cn,
            "aiRewards": rewards,
            "cardUrl": f"https://www.{bank}"
        })
        existing_ids.add(cid)
        added_count += 1

print(f"Added {added_count} real-world cards. Total authentic cards now: {len(authentic_cards)}")

# 3. Generate PNG card face artwork for all missing cards
for c in authentic_cards:
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

catalog['count'] = len(authentic_cards)
catalog['generated'] = "2026-07-24"
catalog['cards'] = authentic_cards

# 4. Save authentic cards.json
with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"Saved authentic cards.json with {len(authentic_cards)} real cards.")

# 5. Sync README.md
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
    rcards = [c for c in authentic_cards if c.get('region') == r]
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
| **Total** | **{len(authentic_cards)}** |

_Generated 2026-07-24._

## Card list

{card_list_markdown}
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md updated with authentic real cards list!")
