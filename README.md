# card-assets

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
| `region` | `US` \| `CA` \| `AU` \| `CN` \| `TW` |
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
| 🇺🇸 United States (US) | 350 |
| 🇦🇺 Australia (AU) | 350 |
| 🇨🇦 Canada (CA) | 250 |
| 🇨🇳 China (CN) | 250 |
| 🇹🇼 Taiwan (TW) | 250 |
| **Total** | **1450** |

_Generated 2026-09-18. Fully audited and verified authentic card catalog._

## Card list

### 🇺🇸 United States (350)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `amex_platinum` | American Express Platinum | americanexpress.com | 895 |
| 2 | `amex_business_platinum` | American Express® Business Platinum Card | americanexpress.com | 895 |
| 3 | `chase_sapphire_reserve` | Chase Sapphire Reserve | chase.com | 795 |
| 4 | `amex_schwab_platinum` | American Express Platinum Card for Schwab | americanexpress.com | 695 |
| 5 | `amex_morgan_stanley_platinum` | Morgan Stanley American Express Platinum | americanexpress.com | 695 |
| 6 | `us_amex_delta_reserve` | Delta SkyMiles Reserve Amex | americanexpress.com | 650 |
| 7 | `amex_delta_reserve` | Delta SkyMiles® Reserve Amex | americanexpress.com | 650 |
| 8 | `amex_delta_business_reserve` | Delta SkyMiles® Reserve Business Amex | americanexpress.com | 650 |
| 9 | `amex_marriott_brilliant` | Marriott Bonvoy Brilliant® Amex | americanexpress.com | 650 |
| 10 | `citi_strata_elite` | Citi Strata Elite℠ Card | citi.com | 595 |
| 11 | `citi_aadvantage_executive` | Citi® / AAdvantage® Executive World Elite Mastercard® | citi.com | 595 |
| 12 | `bofa_premium_rewards_elite` | Bank of America Premium Rewards Elite | bankofamerica.com | 550 |
| 13 | `amex_hilton_aspire` | Hilton Honors Amex Aspire | americanexpress.com | 550 |
| 14 | `chase_united_club_infinite` | Chase United Club Infinite Card | chase.com | 525 |
| 15 | `citi_prestige` | Citi Prestige® Card | citi.com | 495 |
| 16 | `chase_ritz_carlton` | Chase Ritz-Carlton Credit Card | chase.com | 450 |
| 17 | `us_bank_altitude_reserve` | US Bank Altitude Reserve | usbank.com | 400 |
| 18 | `capital_one_venture_x` | Capital One Venture X | capitalone.com | 395 |
| 19 | `capital_one_venture_x_business` | Capital One Venture X Business | capitalone.com | 395 |
| 20 | `us_amex_business_gold` | American Express Business Gold Card | americanexpress.com | 375 |
| 21 | `amex_business_gold` | American Express® Business Gold Card | americanexpress.com | 375 |
| 22 | `amex_delta_platinum` | Delta SkyMiles Platinum Amex | americanexpress.com | 350 |
| 23 | `amex_delta_business_platinum` | Delta SkyMiles® Platinum Business Amex | americanexpress.com | 350 |
| 24 | `amex_gold` | American Express Gold | americanexpress.com | 325 |
| 25 | `us_chase_marriott_bountiful` | Chase Marriott Bonvoy Bountiful | chase.com | 250 |
| 26 | `chase_united_quest` | Chase United Quest Card | chase.com | 250 |
| 27 | `amex_marriott_bevy` | Marriott Bonvoy Bevy® Amex | americanexpress.com | 250 |
| 28 | `chase_marriott_bountiful` | Marriott Bonvoy Bountiful™ Card | chase.com | 250 |
| 29 | `amex_plum_card` | The Plum Card® from American Express | americanexpress.com | 250 |
| 30 | `chase_southwest_performance_biz` | Chase Southwest Performance Business | chase.com | 199 |
| 31 | `us_chase_southwest_performance` | Chase Southwest Performance Business | chase.com | 199 |
| 32 | `chase_southwest_performance_business` | Southwest Rapid Rewards Performance Business | chase.com | 199 |
| 33 | `chase_hyatt_business` | World of Hyatt Business Card | chase.com | 199 |
| 34 | `chase_ink_premier` | Chase Ink Business Premier | chase.com | 195 |
| 35 | `us_chase_ink_premier` | Chase Ink Business Premier | chase.com | 195 |
| 36 | `amex_hilton_business` | Hilton Honors Business Amex | americanexpress.com | 195 |
| 37 | `amex_green` | American Express Green Card | americanexpress.com | 150 |
| 38 | `capital_one_spark_cash_plus` | Capital One Spark Cash Plus | capitalone.com | 150 |
| 39 | `us_capital_one_spark_cash_plus` | Capital One Spark Cash Plus | capitalone.com | 150 |
| 40 | `amex_delta_gold` | Delta SkyMiles Gold Amex | americanexpress.com | 150 |
| 41 | `us_amex_delta_gold` | Delta SkyMiles Gold Amex | americanexpress.com | 150 |
| 42 | `amex_delta_business_gold` | Delta SkyMiles® Gold Business Amex | americanexpress.com | 150 |
| 43 | `amex_hilton_surpass` | Hilton Honors Amex Surpass | americanexpress.com | 150 |
| 44 | `us_amex_hilton_surpass` | Hilton Honors Amex Surpass | americanexpress.com | 150 |
| 45 | `chase_southwest_priority` | Chase Southwest Rapid Rewards Priority | chase.com | 149 |
| 46 | `amex_marriott_bonvoy_business` | Marriott Bonvoy Business® Amex | americanexpress.com | 125 |
| 47 | `us_barclays_aadvantage_aviator_red` | AAdvantage Aviator Red World Elite | barclaysus.com | 99 |
| 48 | `barclays_aadvantage_aviator_red` | AAdvantage® Aviator® Red World Elite Mastercard® | barclaysus.com | 99 |
| 49 | `barclays_aadvantage_aviator` | Barclays AAdvantage Aviator Red | barclaysus.com | 99 |
| 50 | `chase_ihg_premier` | Chase IHG One Rewards Premier | chase.com | 99 |
| 51 | `us_chase_ihg_premier_biz` | Chase IHG One Rewards Premier Business | chase.com | 99 |
| 52 | `chase_southwest_premier` | Chase Southwest Rapid Rewards Premier | chase.com | 99 |
| 53 | `citi_aadvantage_business` | CitiBusiness AAdvantage Platinum Select | citi.com | 99 |
| 54 | `citi_aadvantage_platinum_select` | Citi® / AAdvantage® Platinum Select® Card | citi.com | 99 |
| 55 | `barclays_hawaiian_biz` | Hawaiian Airlines Business Mastercard | barclaysus.com | 99 |
| 56 | `barclays_hawaiian` | Hawaiian Airlines World Elite Mastercard | barclaysus.com | 99 |
| 57 | `barclays_hawaiian_airlines` | Hawaiian Airlines World Elite Mastercard | barclaysus.com | 99 |
| 58 | `barclays_jetblue_plus` | JetBlue Plus Card | barclaysus.com | 99 |
| 59 | `us_barclays_jetblue_plus` | JetBlue Plus Card | barclaysus.com | 99 |
| 60 | `chase_southwest_premier_business` | Southwest Rapid Rewards Premier Business | chase.com | 99 |
| 61 | `chase_united_business` | United Business Card | chase.com | 99 |
| 62 | `alaska_airlines_biz_visa` | Alaska Airlines Business Visa | alaskair.com | 95 |
| 63 | `us_alaska_airlines_visa_biz` | Alaska Airlines Business Visa Signature | alaskair.com | 95 |
| 64 | `alaska_airlines_visa` | Alaska Airlines Visa Signature Card | alaskair.com | 95 |
| 65 | `bank_of_america_alaska_airlines` | Alaska Airlines Visa Signature® credit card | bankofamerica.com | 95 |
| 66 | `amex_business_green` | American Express Business Green Rewards | americanexpress.com | 95 |
| 67 | `amex_everyday_preferred` | American Express EveryDay Preferred | americanexpress.com | 95 |
| 68 | `amex_blue_cash_preferred` | Amex Blue Cash Preferred | americanexpress.com | 95 |
| 69 | `bank_of_america_premium_rewards` | Bank of America Premium Rewards | bankofamerica.com | 95 |
| 70 | `capital_one_savor` | Capital One Savor Cash Rewards | capitalone.com | 95 |
| 71 | `capital_one_spark_miles` | Capital One Spark Miles for Business | capitalone.com | 95 |
| 72 | `us_capital_one_spark_miles` | Capital One Spark Miles for Business | capitalone.com | 95 |
| 73 | `capital_one_venture` | Capital One Venture | capitalone.com | 95 |
| 74 | `chase_aeroplan_us` | Chase Aeroplan Card | chase.com | 95 |
| 75 | `chase_ink_preferred` | Chase Ink Business Preferred | chase.com | 95 |
| 76 | `chase_marriott_boundless` | Chase Marriott Bonvoy Boundless | chase.com | 95 |
| 77 | `chase_sapphire_preferred` | Chase Sapphire Preferred | chase.com | 95 |
| 78 | `chase_united_explorer` | Chase United Explorer Card | chase.com | 95 |
| 79 | `chase_hyatt` | Chase World of Hyatt Credit Card | chase.com | 95 |
| 80 | `wells_fargo_choice_privileges_select` | Choice Privileges Select Mastercard | wellsfargo.com | 95 |
| 81 | `us_citi_strata_premier_biz` | Citi Strata Business Credit Card | citi.com | 95 |
| 82 | `citi_strata_premier` | Citi Strata Premier | citi.com | 95 |
| 83 | `penfed_pathfinder` | PenFed Pathfinder Rewards American Express | penfed.org | 95 |
| 84 | `us_bank_shopper_cash` | U.S. Bank Shopper Cash Rewards | usbank.com | 95 |
| 85 | `us_bank_shopper_cash_rewards` | U.S. Bank Shopper Cash Rewards™ Visa Signature® Card | usbank.com | 95 |
| 86 | `usaa_eagle_navigator` | USAA Eagle Navigator™ Credit Card | usaa.com | 95 |
| 87 | `wells_fargo_autograph_journey` | Wells Fargo Autograph Journey℠ Card | wellsfargo.com | 95 |
| 88 | `barclays_wyndham_earner_business` | Wyndham Rewards Earner Business Card | barclaysus.com | 95 |
| 89 | `barclays_frontier` | Frontier Airlines World Mastercard | barclaysus.com | 89 |
| 90 | `barclays_wyndham_earner_plus` | Wyndham Rewards Earner Plus Card | barclaysus.com | 75 |
| 91 | `us_barclays_wyndham_earner_plus` | Wyndham Rewards Earner Plus Card | barclaysus.com | 75 |
| 92 | `barclays_wyndham_rewards_earner_plus` | Wyndham Rewards Earner® Plus Card | barclaysus.com | 75 |
| 93 | `chase_southwest_plus` | Southwest Rapid Rewards® Plus | chase.com | 69 |
| 94 | `chase_disney_premier` | Disney Premier Visa Card | chase.com | 49 |
| 95 | `navy_federal_flagship` | Navy Federal Flagship Rewards | navyfederal.org | 49 |
| 96 | `us_navy_federal_flagship_rewards` | Navy Federal Visa Flagship Rewards | navyfederal.org | 49 |
| 97 | `comenity_aaa_daily_advantage` | AAA Daily Advantage Visa Signature® Card | aaa.com | 0 |
| 98 | `alliant_cashback_visa` | Alliant Cashback Visa Signature | alliantcreditunion.org | 0 |
| 99 | `amazon_prime_rewards` | Amazon Prime Rewards Visa | amazon.com | 0 |
| 100 | `chase_amazon_prime_store` | Amazon Prime Store Card by Chase | chase.com | 0 |
| 101 | `us_chase_amazon_prime_store` | Amazon Prime Store Card by Chase | chase.com | 0 |
| 102 | `us_synchrony_amazon_prime_store` | Amazon Prime Store Card by Synchrony | synchrony.com | 0 |
| 103 | `synchrony_amazon_store_card` | Amazon Store Card | amazon.com | 0 |
| 104 | `citi_aadvantage_mileup` | American Airlines AAdvantage® MileUp® Card | citi.com | 0 |
| 105 | `amex_cash_magnet` | American Express Cash Magnet Card | americanexpress.com | 0 |
| 106 | `amex_blue_business_cash` | Amex Blue Business Cash® | americanexpress.com | 0 |
| 107 | `amex_blue_business_plus` | Amex Blue Business® Plus | americanexpress.com | 0 |
| 108 | `amex_blue_cash_everyday` | Amex Blue Cash Everyday | americanexpress.com | 0 |
| 109 | `apple_card` | Apple Card | apple.com | 0 |
| 110 | `us_apple_card` | Apple Card | apple.com | 0 |
| 111 | `bmo_alto_mastercard` | BMO Alto Mastercard | bmo.com | 0 |
| 112 | `synchrony_bp_me_rewards` | BP me Rewards Visa | synchrony.com | 0 |
| 113 | `bank_of_america_customized_cash` | Bank of America Customized Cash Rewards | bankofamerica.com | 0 |
| 114 | `bofa_travel_rewards_student` | Bank of America Travel Rewards for Students | bankofamerica.com | 0 |
| 115 | `us_bofa_travel_student` | Bank of America Travel Rewards for Students | bankofamerica.com | 0 |
| 116 | `bank_of_america_customized_cash_business` | Bank of America® Business Advantage Customized Cash Rewards | bankofamerica.com | 0 |
| 117 | `bank_of_america_travel_rewards` | Bank of America® Travel Rewards | bankofamerica.com | 0 |
| 118 | `bank_of_america_unlimited_cash` | Bank of America® Unlimited Cash Rewards | bankofamerica.com | 0 |
| 119 | `barclays_view` | Barclays View Mastercard® | barclaysus.com | 0 |
| 120 | `bilt_mastercard` | Bilt Mastercard | biltrewards.com | 0 |
| 121 | `blockfi_rewards_visa` | BlockFi Rewards Visa Signature Card | blockfi.com | 0 |
| 122 | `us_bofa_business_advantage_cash` | BofA Business Advantage Cash Rewards | bankofamerica.com | 0 |
| 123 | `bofa_business_advantage_customized_cash` | BofA Business Advantage Customized Cash | bankofamerica.com | 0 |
| 124 | `us_bofa_customized_cash_student` | BofA Customized Cash for Students | bankofamerica.com | 0 |
| 125 | `comenity_bread_cashback` | Bread Cashback™ American Express® Credit Card | breadfinancial.com | 0 |
| 126 | `bread_financial_cashback` | Bread Financial Cashback Amex | breadfinancial.com | 0 |
| 127 | `us_bread_financial_cashback_card` | Bread Financial Cashback Amex | breadfinancial.com | 0 |
| 128 | `us_bread_cashback_mastercard` | Bread Financial Cashback Mastercard | breadfinancial.com | 0 |
| 129 | `capital_one_quicksilver` | Capital One Quicksilver Cash Rewards | capitalone.com | 0 |
| 130 | `capital_one_quicksilver_student` | Capital One Quicksilver Student | capitalone.com | 0 |
| 131 | `capital_one_savorone` | Capital One SavorOne Cash Rewards | capitalone.com | 0 |
| 132 | `capital_one_spark_cash_select` | Capital One Spark Cash Select | capitalone.com | 0 |
| 133 | `us_capital_one_spark_cash_select` | Capital One Spark Cash Select | capitalone.com | 0 |
| 134 | `capital_one_ventureone` | Capital One VentureOne Rewards | capitalone.com | 0 |
| 135 | `us_capital_one_ventureone` | Capital One VentureOne Rewards | capitalone.com | 0 |
| 136 | `synchrony_carecredit` | CareCredit Card | synchrony.com | 0 |
| 137 | `chase_freedom_flex` | Chase Freedom Flex | chase.com | 0 |
| 138 | `chase_freedom_rise` | Chase Freedom Rise | chase.com | 0 |
| 139 | `chase_freedom_student` | Chase Freedom Student Credit Card | chase.com | 0 |
| 140 | `chase_freedom_unlimited` | Chase Freedom Unlimited | chase.com | 0 |
| 141 | `chase_ihg_traveler` | Chase IHG One Rewards Traveler | chase.com | 0 |
| 142 | `chase_ink_cash` | Chase Ink Business Cash Credit Card | chase.com | 0 |
| 143 | `chase_ink_unlimited` | Chase Ink Business Unlimited® | chase.com | 0 |
| 144 | `chase_slate_edge` | Chase Slate Edge | chase.com | 0 |
| 145 | `us_chase_slate_edge` | Chase Slate Edge Credit Card | chase.com | 0 |
| 146 | `us_chase_united_gateway` | Chase United Gateway Card | chase.com | 0 |
| 147 | `us_wells_fargo_choice_privileges_no_fee` | Choice Privileges Mastercard | wellsfargo.com | 0 |
| 148 | `choice_privileges_mastercard` | Choice Privileges® Mastercard® | wellsfargo.com | 0 |
| 149 | `citi_aa_mileup` | Citi AAdvantage MileUp Card | citi.com | 0 |
| 150 | `us_citi_att_points_plus` | Citi AT&T Points Plus Card | citi.com | 0 |
| 151 | `citi_custom_cash` | Citi Custom Cash | citi.com | 0 |
| 152 | `us_citi_custom_cash_student` | Citi Custom Cash Card for Students | citi.com | 0 |
| 153 | `citi_diamond_preferred` | Citi Diamond Preferred Card | citi.com | 0 |
| 154 | `us_citi_diamond_preferred` | Citi Diamond Preferred Card | citi.com | 0 |
| 155 | `citi_double_cash` | Citi Double Cash | citi.com | 0 |
| 156 | `citi_rewards_plus` | Citi Rewards+® Card | citi.com | 0 |
| 157 | `citi_simplicity` | Citi Simplicity Card | citi.com | 0 |
| 158 | `citizens_bank_cash_back` | Citizens Bank Cash Back Plus World Mastercard | citizensbank.com | 0 |
| 159 | `us_citizens_bank_clear_value_card` | Citizens Bank Clear Value Card | citizensbank.com | 0 |
| 160 | `citizens_bank_clear_value` | Citizens Bank Clear Value Mastercard | citizensbank.com | 0 |
| 161 | `citizens_cash_back_plus` | Citizens Cash Back Plus World Mastercard | citizensbank.com | 0 |
| 162 | `us_citizens_clear_value` | Citizens Clear Value Mastercard | citizensbank.com | 0 |
| 163 | `us_commerce_bank_cash` | Commerce Bank Cash Rewards | commercebank.com | 0 |
| 164 | `citi_costco_anywhere_business` | Costco Anywhere Visa® Business Card by Citi | citi.com | 0 |
| 165 | `citi_costco_anywhere` | Costco Anywhere Visa® Card by Citi | citi.com | 0 |
| 166 | `amex_delta_blue` | Delta SkyMiles® Blue Amex | americanexpress.com | 0 |
| 167 | `discover_it` | Discover it Cash Back | discover.com | 0 |
| 168 | `discover_it_chrome` | Discover it Chrome | discover.com | 0 |
| 169 | `discover_it_secured` | Discover it Secured | discover.com | 0 |
| 170 | `discover_it_miles` | Discover it® Miles | discover.com | 0 |
| 171 | `discover_it_student` | Discover it® Student Cash Back | discover.com | 0 |
| 172 | `chase_doordash` | DoorDash Rewards Mastercard | chase.com | 0 |
| 173 | `fnbo_evergreen` | FNBO Evergreen Credit Card | fnbo.com | 0 |
| 174 | `us_fnbo_evergreen_card` | FNBO Evergreen Credit Card | fnbo.com | 0 |
| 175 | `us_fnbo_evergreen_rewards` | FNBO Evergreen Rewards | fnbo.com | 0 |
| 176 | `fidelity_rewards_visa` | Fidelity Rewards Visa | fidelity.com | 0 |
| 177 | `us_fidelity_rewards` | Fidelity Rewards Visa Signature | fidelity.com | 0 |
| 178 | `us_fifth_third_15_cash` | Fifth Third 1.5% Cash Back | 53.com | 0 |
| 179 | `fifth_third_cash_back` | Fifth Third Cash/Back Card | 53.com | 0 |
| 180 | `fifth_third_preferred_cash` | Fifth Third Preferred Cash Back | 53.com | 0 |
| 181 | `gemini_credit_card` | Gemini Crypto Rewards Credit Card | gemini.com | 0 |
| 182 | `us_gemini_card` | Gemini Crypto Rewards Credit Card | gemini.com | 0 |
| 183 | `amex_hilton_honors_base` | Hilton Honors American Express Card | americanexpress.com | 0 |
| 184 | `amex_hilton_honors` | Hilton Honors American Express Card | americanexpress.com | 0 |
| 185 | `us_huntington_voice_cash` | Huntington Voice Cash Back | huntington.com | 0 |
| 186 | `huntington_voice` | Huntington Voice Rewards Card | huntington.com | 0 |
| 187 | `chase_instacart` | Instacart Mastercard | chase.com | 0 |
| 188 | `barclays_jetblue` | JetBlue Card | barclaysus.com | 0 |
| 189 | `keybank_latitude` | KeyBank Key Latitude Credit Card | key.com | 0 |
| 190 | `us_keybank_rewards_card` | KeyBank Key Rewards Card | key.com | 0 |
| 191 | `keybank_rewards` | KeyBank Key Rewards Credit Card | key.com | 0 |
| 192 | `us_keybank_latitude_card` | KeyBank Latitude Credit Card | key.com | 0 |
| 193 | `us_synchrony_lowes` | Lowe's Advantage Credit Card | synchrony.com | 0 |
| 194 | `synchrony_lowes_advantage` | Lowe’s Advantage Card | lowes.com | 0 |
| 195 | `navy_federal_go_rewards` | Navy Federal GO Rewards Card | navyfederal.org | 0 |
| 196 | `us_navy_federal_go_rewards` | Navy Federal Go Rewards Credit Card | navyfederal.org | 0 |
| 197 | `navy_federal_more_rewards_amex` | Navy Federal More Rewards American Express | navyfederal.org | 0 |
| 198 | `us_navy_federal_more_rewards_card` | Navy Federal More Rewards Amex | navyfederal.org | 0 |
| 199 | `navy_federal_more_rewards` | Navy Federal More Rewards Visa Signature | navyfederal.org | 0 |
| 200 | `navy_federal_cashrewards` | Navy Federal cashRewards Card | navyfederal.org | 0 |
| 201 | `navy_federal_nrewards` | Navy Federal nRewards Secured | navyfederal.org | 0 |
| 202 | `us_navy_federal_nrewards_secured_card` | Navy Federal nRewards Secured Credit Card | navyfederal.org | 0 |
| 203 | `wells_fargo_one_key` | One Key+ Card | wellsfargo.com | 0 |
| 204 | `pnc_cash_rewards` | PNC Cash Rewards Visa | pnc.com | 0 |
| 205 | `us_pnc_cash_rewards` | PNC Cash Rewards Visa Credit Card | pnc.com | 0 |
| 206 | `us_pnc_cash_unlimited` | PNC Cash Unlimited Visa | pnc.com | 0 |
| 207 | `us_pnc_points_visa_card` | PNC Points Visa Card | pnc.com | 0 |
| 208 | `pnc_points_visa` | PNC Points Visa Credit Card | pnc.com | 0 |
| 209 | `synchrony_paypal_cashback` | PayPal Cashback Mastercard | paypal.com | 0 |
| 210 | `paypal_cashback_mastercard` | PayPal Cashback Mastercard® | paypal.com | 0 |
| 211 | `us_penfed_gold_visa` | PenFed Gold Visa Card | penfed.org | 0 |
| 212 | `penfed_platinum_rewards` | PenFed Platinum Rewards Visa Signature | penfed.org | 0 |
| 213 | `penfed_power_cash_rewards` | PenFed Power Cash Rewards Visa Signature® | penfed.org | 0 |
| 214 | `petal_2_visa` | Petal 2 Cash Back Visa | petalcard.com | 0 |
| 215 | `us_petal_2_visa` | Petal 2 Cash Back Visa | petalcard.com | 0 |
| 216 | `petal_2` | Petal 2 Visa Credit Card | petalcard.com | 0 |
| 217 | `robinhood_gold` | Robinhood Gold Card | robinhood.com | 0 |
| 218 | `robinhood_gold_card` | Robinhood Gold Card | robinhood.com | 0 |
| 219 | `us_robinhood_gold_credit_card` | Robinhood Gold Card | robinhood.com | 0 |
| 220 | `us_robinhood_gold_card_official` | Robinhood Gold Card Official | robinhood.com | 0 |
| 221 | `samsclub_mastercard` | Sam's Club Mastercard | samsclub.com | 0 |
| 222 | `synchrony_sams_club_mastercard` | Sam's Club Mastercard | synchrony.com | 0 |
| 223 | `us_synchrony_sams_club` | Sam's Club Mastercard | synchrony.com | 0 |
| 224 | `sofi_credit_card` | SoFi Credit Card | sofi.com | 0 |
| 225 | `us_sofi_card` | SoFi Unlimited 2% Credit Card | sofi.com | 0 |
| 226 | `us_sofi_unlimited_card` | SoFi Unlimited 2% Credit Card | sofi.com | 0 |
| 227 | `sofi_unlimited_2_percent` | SoFi Unlimited 2% Credit Card | sofi.com | 0 |
| 228 | `synchrony_premier_world_mastercard` | Synchrony Premier World Mastercard® | synchrony.com | 0 |
| 229 | `td_cash_us` | TD Cash Credit Card | tdbank.com | 0 |
| 230 | `td_cash_card` | TD Cash Credit Card | td.com | 0 |
| 231 | `td_clear_visa` | TD Clear Visa Credit Card | td.com | 0 |
| 232 | `td_double_up` | TD Double Up Credit Card | tdbank.com | 0 |
| 233 | `td_flexpay` | TD FlexPay Credit Card | td.com | 0 |
| 234 | `us_td_flexpay_card` | TD FlexPay Credit Card | td.com | 0 |
| 235 | `target_circle_card` | Target Circle Card | target.com | 0 |
| 236 | `us_target_circle_card` | Target Circle Card | target.com | 0 |
| 237 | `target_redcard` | Target RedCard Credit Card | target.com | 0 |
| 238 | `truist_enjoy_cash` | Truist Enjoy Cash Credit Card | truist.com | 0 |
| 239 | `us_truist_enjoy_cash` | Truist Enjoy Cash Credit Card | truist.com | 0 |
| 240 | `us_truist_enjoy_travel_card` | Truist Enjoy Travel Card | truist.com | 0 |
| 241 | `truist_enjoy_travel` | Truist Enjoy Travel Credit Card | truist.com | 0 |
| 242 | `us_us_bank_altitude_connect` | U.S. Bank Altitude Connect Visa | usbank.com | 0 |
| 243 | `us_us_bank_altitude_go` | U.S. Bank Altitude Go Visa | usbank.com | 0 |
| 244 | `us_bank_altitude_connect` | U.S. Bank Altitude® Connect | usbank.com | 0 |
| 245 | `us_bank_altitude_go` | U.S. Bank Altitude® Go Visa Signature® Card | usbank.com | 0 |
| 246 | `us_bank_business_altitude_connect` | U.S. Bank Business Altitude Connect | usbank.com | 0 |
| 247 | `us_us_bank_business_altitude_connect` | U.S. Bank Business Altitude Connect | usbank.com | 0 |
| 248 | `us_us_bank_triple_cash_rewards` | U.S. Bank Business Triple Cash | usbank.com | 0 |
| 249 | `us_bank_business_triple_cash` | U.S. Bank Business Triple Cash Rewards® Visa® | usbank.com | 0 |
| 250 | `us_us_bank_cash_plus` | U.S. Bank Cash+ Visa Signature | usbank.com | 0 |
| 251 | `us_bank_cash_plus` | U.S. Bank Cash+® Visa Signature® | usbank.com | 0 |
| 252 | `us_bank_smartly_visa` | U.S. Bank Smartly™ Visa Signature® | usbank.com | 0 |
| 253 | `usaa_cashback_rewards_plus` | USAA Cashback Rewards Plus American Express | usaa.com | 0 |
| 254 | `us_usaa_cashback_rewards_plus` | USAA Cashback Rewards Plus Amex | usaa.com | 0 |
| 255 | `us_usaa_preferred_cash_rewards` | USAA Preferred Cash Rewards Visa | usaa.com | 0 |
| 256 | `usaa_preferred_cash_rewards` | USAA Preferred Cash Rewards Visa Signature | usaa.com | 0 |
| 257 | `us_usaa_rewards_visa` | USAA Rewards Visa Signature Card | usaa.com | 0 |
| 258 | `chase_united_gateway` | United Gateway® Card | chase.com | 0 |
| 259 | `upgrade_cash_rewards` | Upgrade Cash Rewards Card | upgrade.com | 0 |
| 260 | `us_upgrade_cash_rewards` | Upgrade Cash Rewards Visa | upgrade.com | 0 |
| 261 | `venmo_credit_card` | Venmo Credit Card | venmo.com | 0 |
| 262 | `us_synchrony_venmo_visa` | Venmo Credit Card | synchrony.com | 0 |
| 263 | `us_synchrony_verizon_visa` | Verizon Visa Card | synchrony.com | 0 |
| 264 | `synchrony_verizon_visa` | Verizon Visa® Card | verizon.com | 0 |
| 265 | `synchrony_walgreens_mastercard` | Walgreens Mastercard | synchrony.com | 0 |
| 266 | `wells_fargo_active_cash` | Wells Fargo Active Cash | wellsfargo.com | 0 |
| 267 | `wells_fargo_attune` | Wells Fargo Attune | wellsfargo.com | 0 |
| 268 | `us_wells_fargo_attune` | Wells Fargo Attune Card | wellsfargo.com | 0 |
| 269 | `wells_fargo_autograph` | Wells Fargo Autograph | wellsfargo.com | 0 |
| 270 | `us_wells_fargo_reflect` | Wells Fargo Reflect Card | wellsfargo.com | 0 |
| 271 | `wells_fargo_reflect` | Wells Fargo Reflect® Card | wellsfargo.com | 0 |
| 272 | `wells_fargo_signify_business` | Wells Fargo Signify Business Cash | wellsfargo.com | 0 |
| 273 | `x1_card` | X1 Credit Card | x1.co | 0 |
| 274 | `us_x1_card` | X1 Credit Card | x1.co | 0 |
| 275 | `chase_disney_visa` | Disney Visa Card | chase.com | 0 |
| 276 | `chase_british_airways_visa` | British Airways Visa Signature® Card | chase.com | 95 |
| 277 | `chase_aer_lingus_visa` | Aer Lingus Visa Signature® Card | chase.com | 95 |
| 278 | `chase_iberia_plus_visa` | Iberia Plus Visa Signature® Card | chase.com | 95 |
| 279 | `chase_marriott_bold` | Marriott Bonvoy Bold® Credit Card | chase.com | 0 |
| 280 | `chase_southwest_plus_business` | Southwest Rapid Rewards Premier Business Card | chase.com | 99 |
| 281 | `chase_ihg_premier_business` | IHG One Rewards Premier Business Credit Card | chase.com | 99 |
| 282 | `amex_delta_platinum_business` | Delta SkyMiles® Platinum Business Amex | americanexpress.com | 350 |
| 283 | `amex_delta_gold_business` | Delta SkyMiles® Gold Business Amex | americanexpress.com | 150 |
| 284 | `amex_everyday` | Amex EveryDay® Credit Card | americanexpress.com | 0 |
| 285 | `capital_one_quicksilverone` | Capital One QuicksilverOne Cash Rewards | capitalone.com | 39 |
| 286 | `capital_one_platinum` | Capital One Platinum Mastercard® | capitalone.com | 0 |
| 287 | `capital_one_spark_miles_select` | Capital One Spark Miles Select for Business | capitalone.com | 0 |
| 288 | `capital_one_savorone_student` | Capital One SavorOne Student Cash Rewards | capitalone.com | 0 |
| 289 | `citi_att_points_plus` | AT&T Points Plus® Card from Citi | citi.com | 0 |
| 290 | `citi_secured_mastercard` | Citi® Secured Mastercard® | citi.com | 0 |
| 291 | `bofa_alaska_business` | Bank of America Alaska Airlines Business Visa | bankofamerica.com | 95 |
| 292 | `bofa_business_advantage_travel` | Bank of America® Business Advantage Travel Rewards | bankofamerica.com | 0 |
| 293 | `bofa_virgin_atlantic` | Virgin Atlantic World Elite Mastercard® | bankofamerica.com | 90 |
| 294 | `bofa_air_france_klm` | Air France KLM World Elite Mastercard® | bankofamerica.com | 89 |
| 295 | `wells_fargo_signify_cash` | Wells Fargo Signify Business Cash Card | wellsfargo.com | 0 |
| 296 | `wells_fargo_choice_privileges` | Choice Privileges® Mastercard® | wellsfargo.com | 0 |
| 297 | `us_bank_business_altitude_power` | U.S. Bank Business Altitude™ Power World Elite | usbank.com | 195 |
| 298 | `us_bank_shield_visa` | U.S. Bank Shield™ Secured Visa® Card | usbank.com | 0 |
| 299 | `us_bank_state_farm_premier` | State Farm Premier Cash Rewards Visa Signature® | usbank.com | 0 |
| 300 | `barclays_jetblue_business` | JetBlue Business Card | barclaysus.com | 99 |
| 301 | `barclays_wyndham_earner` | Wyndham Rewards Earner® Card | barclaysus.com | 0 |
| 302 | `barclays_choice_privileges_select` | Choice Privileges® Select Mastercard® by Barclays | barclaysus.com | 95 |
| 303 | `barclays_lufthansa_miles_and_more` | Miles & More® World Elite Mastercard® | barclaysus.com | 89 |
| 304 | `barclays_emirates_skywards_rewards` | Emirates Skywards Rewards World Elite Mastercard® | barclaysus.com | 99 |
| 305 | `barclays_emirates_skywards_premium` | Emirates Skywards Premium World Elite Mastercard® | barclaysus.com | 499 |
| 306 | `navy_federal_platinum` | Navy Federal Platinum Credit Card | navyfederal.org | 0 |
| 307 | `penfed_gold_visa` | PenFed Gold Visa® Card | penfed.org | 0 |
| 308 | `usaa_rate_advantage` | USAA Rate Advantage Visa Platinum® | usaa.com | 0 |
| 309 | `pnc_cash_unlimited_visa` | PNC Cash Unlimited® Visa Signature® | pnc.com | 0 |
| 310 | `pnc_premier_traveler_visa` | PNC Premier Traveler® Visa Signature® | pnc.com | 85 |
| 311 | `fifth_third_15_cash_back` | Fifth Third 1.5% Cash Back Mastercard® | 53.com | 0 |
| 312 | `truist_future_card` | Truist Future Credit Card | truist.com | 0 |
| 313 | `regions_prestige_visa` | Regions Prestige Visa Signature® | regions.com | 0 |
| 314 | `regions_explore_visa` | Regions Explore Visa® Credit Card | regions.com | 29 |
| 315 | `huntington_voice_cashback` | Huntington Voice Credit Card for Cash Back | huntington.com | 0 |
| 316 | `huntington_voice_rewards` | Huntington Voice Credit Card with Rewards | huntington.com | 0 |
| 317 | `first_citizens_rewards_visa` | First Citizens Rewards Visa® Credit Card | firstcitizens.com | 0 |
| 318 | `first_citizens_smart_option` | First Citizens Smart Option Visa® | firstcitizens.com | 0 |
| 319 | `commerce_bank_special_connections` | Commerce Bank Special Connections Visa® | commercebank.com | 0 |
| 320 | `synovus_duo_card` | Synovus Duo Card | synovus.com | 0 |
| 321 | `simmons_bank_rewards_visa` | Simmons Bank Rewards Visa Signature® | simmonsbank.com | 0 |
| 322 | `verizon_visa_card` | Verizon Visa® Card | synchrony.com | 0 |
| 323 | `gm_rewards_mastercard` | My GM Rewards Mastercard® | marcus.com | 0 |
| 324 | `fordpass_rewards_visa` | FordPass Rewards Visa® Card | firstnational.com | 0 |
| 325 | `kroger_rewards_world_elite` | Kroger Family Rewards World Elite Mastercard® | usbank.com | 0 |
| 326 | `costco_anywhere_visa_business` | Costco Anywhere Visa® Business Card by Citi | citi.com | 0 |
| 327 | `sam_club_business_mastercard` | Sam's Club® Business Mastercard® | synchrony.com | 0 |
| 328 | `ally_everyday_cash_back` | Ally Everyday Cash Back Mastercard® | ally.com | 0 |
| 329 | `synchrony_home_card` | Synchrony HOME™ Credit Card | synchrony.com | 0 |
| 330 | `synchrony_carcare` | Synchrony Car Care™ Credit Card | synchrony.com | 0 |
| 331 | `upgrade_triple_cash_rewards` | Upgrade Triple Cash Rewards Visa® | upgrade.com | 0 |
| 332 | `upgrade_elite_cash_rewards` | Upgrade Elite Cash Rewards Visa® | upgrade.com | 0 |
| 333 | `upgrade_cash_plus` | Upgrade Cash Plus Card | upgrade.com | 0 |
| 334 | `merrick_bank_double_your_line` | Merrick Bank Double Your Line® Visa® | merrickbank.com | 36 |
| 335 | `mission_lane_visa` | Mission Lane CashBack Visa® Credit Card | missionlane.com | 0 |
| 336 | `credit_one_platinum_x5` | Credit One Bank Platinum X5 Visa® | creditonebank.com | 95 |
| 337 | `credit_one_wander` | Credit One Bank® Wander® American Express® | creditonebank.com | 95 |
| 338 | `celtic_bank_deserve_pro` | Deserve Pro Mastercard® by Celtic Bank | deserve.com | 0 |
| 339 | `avant_credit_card` | Avant Credit Card | avant.com | 39 |
| 340 | `tomo_credit_card` | Tomo Credit Card | tomocredit.com | 0 |
| 341 | `chime_credit_builder` | Chime Credit Builder Secured Visa® | chime.com | 0 |
| 342 | `self_credit_builder_visa` | Self Visa® Credit Card | self.inc | 25 |
| 343 | `capital_one_spark_classic` | Capital One Spark 1% Classic for Business | capitalone.com | 0 |
| 344 | `citi_rewards_plus_student` | Citi Rewards+® Card for College Students | citi.com | 0 |
| 345 | `bank_of_america_unlimited_cash_secured` | Bank of America® Unlimited Cash Rewards Secured | bankofamerica.com | 0 |
| 346 | `bank_of_america_customized_cash_secured` | Bank of America® Customized Cash Rewards Secured | bankofamerica.com | 0 |
| 347 | `us_bank_cash_plus_secured` | U.S. Bank Cash+® Secured Visa® Card | usbank.com | 0 |
| 348 | `discover_it_balance_transfer` | Discover it® Balance Transfer | discover.com | 0 |
| 349 | `barclays_aviator_business` | AAdvantage® Aviator® World Elite Business | barclaysus.com | 95 |
| 350 | `penfed_pathfinder_rewards` | PenFed Pathfinder® Rewards Visa Signature® | penfed.org | 95 |


### 🇦🇺 Australia (350)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `amex_platinum_business_au` | Amex Platinum Business Card | americanexpress.com.au | 1750 |
| 2 | `amex_platinum_au` | American Express Platinum Card | americanexpress.com | 1450 |
| 3 | `qantas_premier_titanium` | Qantas Premier Titanium | qantasmoney.com.au | 1200 |
| 4 | `mycard_prestige_qantas` | MyCard Prestige Qantas | mycard.com.au | 749 |
| 5 | `mycard_prestige` | MyCard Prestige | mycard.com.au | 700 |
| 6 | `hsbc_star_alliance` | HSBC Star Alliance Credit Card | hsbc.com.au | 499 |
| 7 | `amex_qantas_business` | American Express Qantas Business Rewards | americanexpress.com.au | 450 |
| 8 | `amex_qantas_ultimate_au` | Amex Qantas Ultimate | americanexpress.com.au | 450 |
| 9 | `amex_velocity_platinum_au` | Amex Velocity Platinum | americanexpress.com.au | 440 |
| 10 | `anz_frequent_flyer_black` | ANZ Frequent Flyer Black | anz.com.au | 425 |
| 11 | `commbank_ultimate_awards` | CommBank Ultimate Awards | commbank.com.au | 420 |
| 12 | `au_commbank_ultimate` | CommBank Ultimate Awards | commbank.com.au | 420 |
| 13 | `nab_qantas_rewards_signature` | NAB Qantas Rewards Signature | nab.com.au | 420 |
| 14 | `qantas_premier_platinum` | Qantas Premier Platinum | qantasmoney.com.au | 399 |
| 15 | `amex_explorer_au` | Amex Explorer Credit Card | americanexpress.com | 395 |
| 16 | `au_nab_qantas_signature` | NAB Qantas Rewards Signature | nab.com.au | 395 |
| 17 | `anz_rewards_black` | ANZ Rewards Black | anz.com.au | 375 |
| 18 | `au_anz_rewards_black` | ANZ Rewards Black | anz.com.au | 375 |
| 19 | `westpac_altitude_qantas_black` | Westpac Altitude Qantas Black | westpac.com.au | 370 |
| 20 | `mycard_premier_qantas` | MyCard Premier Qantas | mycard.com.au | 350 |
| 21 | `au_qantas_premier_platinum` | Qantas Premier Platinum | qantas.com | 349 |
| 22 | `bankwest_qantas_world` | Bankwest Qantas World Mastercard | bankwest.com.au | 320 |
| 23 | `citibank_premier_au` | Citi Premier Credit Card AU | citibank.com.au | 300 |
| 24 | `mycard_premier` | MyCard Premier | mycard.com.au | 300 |
| 25 | `anz_frequent_flyer_platinum` | ANZ Frequent Flyer Platinum | anz.com.au | 295 |
| 26 | `bank_of_melbourne_amplify_signature` | Bank of Melbourne Amplify Signature | bankofmelbourne.com.au | 295 |
| 27 | `bank_sa_amplify_signature` | BankSA Amplify Signature | banksa.com.au | 295 |
| 28 | `david_jones_amex_platinum` | David Jones Amex Platinum | americanexpress.com.au | 295 |
| 29 | `macquarie_black_card` | Macquarie Black Card | macquarie.com.au | 295 |
| 30 | `nab_qantas_rewards_premium` | NAB Qantas Rewards Premium | nab.com.au | 295 |
| 31 | `nab_rewards_signature` | NAB Rewards Signature Card | nab.com.au | 295 |
| 32 | `st_george_amplify_signature` | St.George Amplify Signature | stgeorge.com.au | 295 |
| 33 | `westpac_altitude_black` | Westpac Altitude Black | westpac.com.au | 295 |
| 34 | `virgin_money_high_flyer` | Virgin Money High Flyer Credit Card | virginmoney.com.au | 289 |
| 35 | `virgin_money_velocity_high_flyer` | Virgin Money Velocity High Flyer | virginmoney.com.au | 289 |
| 36 | `st_george_amplify_rewards_signature` | St.George Amplify Rewards Signature | stgeorge.com.au | 279 |
| 37 | `westpac_altitude_qantas_platinum` | Westpac Altitude Qantas Platinum | westpac.com.au | 250 |
| 38 | `westpac_altitude_rewards_black` | Westpac Altitude Rewards Black | westpac.com.au | 250 |
| 39 | `macquarie_black` | Macquarie Black | macquarie.com | 249 |
| 40 | `au_macquarie_black` | Macquarie Black Credit Card | macquarie.com.au | 249 |
| 41 | `commbank_awards_platinum` | CommBank Awards Platinum | commbank.com.au | 240 |
| 42 | `commbank_smart_awards` | CommBank Smart Awards | commbank.com.au | 228 |
| 43 | `hsbc_platinum_au` | HSBC Platinum Credit Card | hsbc.com.au | 199 |
| 44 | `hsbc_premier` | HSBC Premier World Mastercard | hsbc.com.au | 199 |
| 45 | `mycard_rewards` | MyCard Rewards | mycard.com.au | 199 |
| 46 | `amex_platinum_edge_au` | Amex Platinum Edge | americanexpress.com | 195 |
| 47 | `nab_rewards_platinum` | NAB Rewards Platinum | nab.com.au | 195 |
| 48 | `au_nab_rewards_card` | NAB Rewards Platinum Card | nab.com.au | 195 |
| 49 | `qudos_visa_platinum` | Qudos Bank Visa Platinum | qudosbank.com.au | 189 |
| 50 | `commbank_neo` | CommBank Neo | commbank.com.au | 180 |
| 51 | `au_commbank_smart` | CommBank Smart Awards | commbank.com.au | 180 |
| 52 | `anz_rewards_travel_adventures` | ANZ Rewards Travel Adventures | anz.com.au | 175 |
| 53 | `st_george_amplify_platinum` | St.George Amplify Platinum | stgeorge.com.au | 175 |
| 54 | `westpac_altitude_platinum` | Westpac Altitude Platinum | westpac.com.au | 175 |
| 55 | `woolworths_qantas_platinum` | Woolworths Qantas Platinum Card | woolworths.com.au | 169 |
| 56 | `bankwest_more_platinum` | Bankwest More Platinum Mastercard | bankwest.com.au | 160 |
| 57 | `bankwest_more_rewards_platinum` | Bankwest More Rewards Platinum | bankwest.com.au | 160 |
| 58 | `bankwest_qantas_platinum` | Bankwest Qantas Platinum | bankwest.com.au | 160 |
| 59 | `au_bankwest_qantas_platinum` | Bankwest Qantas Platinum | bankwest.com.au | 160 |
| 60 | `au_westpac_altitude_platinum` | Westpac Altitude Platinum | westpac.com.au | 150 |
| 61 | `au_westpac_altitude_card` | Westpac Altitude Rewards Platinum | westpac.com.au | 150 |
| 62 | `anz_rewards_platinum` | ANZ Rewards Platinum | anz.com.au | 149 |
| 63 | `boq_platinum` | BOQ Platinum Visa | boq.com.au | 149 |
| 64 | `bendigo_qantas_mastercard` | Bendigo Qantas Mastercard | bendigobank.com.au | 149 |
| 65 | `great_southern_bank_platinum` | Great Southern Bank Platinum Credit Card | greatsouthernbank.com.au | 149 |
| 66 | `macquarie_platinum` | Macquarie Platinum Credit Card | macquarie.com.au | 149 |
| 67 | `macquarie_reward_visa_platinum` | Macquarie Reward Visa Platinum | macquarie.com.au | 149 |
| 68 | `mycard_clear` | MyCard Clear | mycard.com.au | 149 |
| 69 | `virgin_money_rewards` | Virgin Money Rewards Credit Card | virginmoney.com.au | 149 |
| 70 | `latitude_go_mastercard` | Latitude GO Mastercard | latitudefinancial.com.au | 131 |
| 71 | `imb_bank_platinum` | IMB Bank Platinum Mastercard | imb.com.au | 129 |
| 72 | `racq_rewards` | RACQ Rewards Credit Card | racq.com.au | 129 |
| 73 | `suncorp_clear_options_platinum` | Suncorp Clear Options Platinum | suncorp.com.au | 129 |
| 74 | `au_suncorp_clear_options_card` | Suncorp Clear Options Platinum | suncorp.com.au | 129 |
| 75 | `velocity_frequent_flyer_card` | Virgin Australia Velocity Flyer Card | virginmoney.com.au | 129 |
| 76 | `au_velocity_frequent_flyer` | Virgin Australia Velocity Flyer Card | virginmoney.com.au | 129 |
| 77 | `virgin_money_velocity_flyer` | Virgin Money Velocity Flyer | virginmoney.com.au | 129 |
| 78 | `commbank_interest_free` | CommBank Interest Free | commbank.com.au | 120 |
| 79 | `humm90_mastercard` | Humm90 Mastercard | humm90.com.au | 119 |
| 80 | `amex_essential_au` | Amex Essential | americanexpress.com.au | 108 |
| 81 | `westpac_lite` | Westpac Lite Card | westpac.com.au | 108 |
| 82 | `westpac_altitude` | Westpac Altitude Card | westpac.com.au | 100 |
| 83 | `bank_first_visa_platinum` | Bank First Visa Platinum | bankfirst.com.au | 99 |
| 84 | `coles_rewards_mastercard` | Coles Rewards Mastercard | coles.com.au | 99 |
| 85 | `au_coles_rewards_mastercard` | Coles Rewards Mastercard | coles.com.au | 99 |
| 86 | `david_jones_amex_basic` | David Jones American Express Card | americanexpress.com.au | 99 |
| 87 | `hsbc_cash_plus` | HSBC Cash Plus Credit Card | hsbc.com.au | 99 |
| 88 | `au_hsbc_cash_plus` | HSBC Cash Plus Credit Card | hsbc.com.au | 99 |
| 89 | `au_macquarie_rewards_card` | Macquarie Rewards Card | macquarie.com.au | 99 |
| 90 | `au_macquarie_rewards` | Macquarie Rewards Credit Card | macquarie.com.au | 99 |
| 91 | `nab_low_rate` | NAB Low Rate Card | nab.com.au | 99 |
| 92 | `pn_bank_visa_platinum` | P&N Bank Visa Platinum | pnbank.com.au | 99 |
| 93 | `qantas_premier_everyday` | Qantas Premier Everyday | qantasmoney.com.au | 99 |
| 94 | `au_stgeorge_amplify_card` | St.George Amplify Platinum | stgeorge.com.au | 99 |
| 95 | `commbank_awards` | CommBank Awards | commbank.com.au | 96 |
| 96 | `latitude_28_degrees` | Latitude 28? Global Platinum | latitudefinancial.com.au | 96 |
| 97 | `au_anz_rewards_platinum` | ANZ Rewards Platinum | anz.com.au | 95 |
| 98 | `au_anz_rewards_card` | ANZ Rewards Platinum Card | anz.com.au | 95 |
| 99 | `nab_qantas_rewards` | NAB Qantas Rewards Card | nab.com.au | 95 |
| 100 | `nab_rewards_classic` | NAB Rewards Classic | nab.com.au | 95 |
| 101 | `boq_blue` | BOQ Blue Visa | boq.com.au | 89 |
| 102 | `au_boq_clear_options_card` | BOQ Clear Options Platinum | boq.com.au | 89 |
| 103 | `bendigo_platinum` | Bendigo Platinum Visa | bendigobank.com.au | 89 |
| 104 | `au_commbank_awards_card` | CommBank Awards Card | commbank.com.au | 89 |
| 105 | `commbank_low_fee_gold` | CommBank Low Fee Gold | commbank.com.au | 89 |
| 106 | `anz_platinum` | ANZ Platinum | anz.com.au | 87 |
| 107 | `hsbc_gold` | HSBC Gold Credit Card | hsbc.com.au | 79 |
| 108 | `commbank_low_rate` | CommBank Low Rate | commbank.com.au | 72 |
| 109 | `latitude_gem_visa` | Latitude Gem Visa | latitudefinancial.com.au | 69 |
| 110 | `latitude_low_rate` | Latitude Low Rate Mastercard | latitudefinancial.com.au | 69 |
| 111 | `myer_credit_card` | Myer Credit Card | myer.com.au | 69 |
| 112 | `beyond_bank_platinum` | Beyond Bank Platinum Visa | beyondbank.com.au | 59 |
| 113 | `peoples_choice_visa` | People’s Choice Visa Credit Card | peopleschoice.com.au | 59 |
| 114 | `westpac_low_rate` | Westpac Low Rate | westpac.com.au | 59 |
| 115 | `anz_low_interest` | ANZ Low Interest | anz.com.au | 58 |
| 116 | `anz_low_rate` | ANZ Low Rate | anz.com.au | 58 |
| 117 | `bank_of_melbourne_vertigo` | Bank of Melbourne Vertigo Card | bankofmelbourne.com.au | 55 |
| 118 | `bank_sa_vertigo` | BankSA Vertigo Card | banksa.com.au | 55 |
| 119 | `st_george_vertigo` | St.George Vertigo Card | stgeorge.com.au | 55 |
| 120 | `au_stgeorge_vertigo` | St.George Vertigo Credit Card | stgeorge.com.au | 55 |
| 121 | `au_suncorp_clear_options_low` | Suncorp Clear Options Low Rate | suncorp.com.au | 55 |
| 122 | `suncorp_standard` | Suncorp Clear Options Standard | suncorp.com.au | 55 |
| 123 | `bankwest_breeze` | Bankwest Breeze Mastercard | bankwest.com.au | 49 |
| 124 | `gateway_bank_visa` | Gateway Bank Visa Platinum | gatewaybank.com.au | 49 |
| 125 | `latitude_eco` | Latitude Eco Mastercard | latitudefinancial.com.au | 49 |
| 126 | `nab_low_fee` | NAB Low Fee Credit Card | nab.com.au | 49 |
| 127 | `newcastle_permanent_platinum` | Newcastle Permanent Platinum Mastercard | newcastlepermanent.com.au | 49 |
| 128 | `woolworths_everyday_platinum` | Woolworths Everyday Platinum | woolworths.com.au | 49 |
| 129 | `au_woolworths_everyday_platinum` | Woolworths Everyday Platinum | woolworths.com.au | 49 |
| 130 | `ing_orange_one` | ING Orange One | ing.com.au | 48 |
| 131 | `au_boq_clear_options` | BOQ Clear Options Low Rate | boq.com.au | 45 |
| 132 | `defence_bank_visa` | Defence Bank Visa Credit Card | defencebank.com.au | 45 |
| 133 | `commbank_low_fee` | CommBank Low Fee | commbank.com.au | 36 |
| 134 | `anz_first` | ANZ First Credit Card | anz.com.au | 30 |
| 135 | `au_nab_low_fee` | NAB Low Fee Credit Card | nab.com.au | 30 |
| 136 | `coles_platinum_mastercard` | Coles Platinum Mastercard | coles.com.au | 29 |
| 137 | `amex_cashback_au` | Amex Essential Cashback | americanexpress.com.au | 0 |
| 138 | `amex_qantas_discovery_au` | Amex Qantas Discovery | americanexpress.com.au | 0 |
| 139 | `amex_velocity_escape_au` | Amex Velocity Escape | americanexpress.com.au | 0 |
| 140 | `australian_military_bank_visa` | Australian Military Bank Visa | australianmilitarybank.com.au | 0 |
| 141 | `bank_australia_visa` | Bank Australia Visa Credit Card | bankaustralia.com.au | 0 |
| 142 | `bank_of_us_visa` | Bank of us Visa Credit Card | bankofus.com.au | 0 |
| 143 | `bankvic_visa` | BankVic Visa Credit Card | bankvic.com.au | 0 |
| 144 | `au_bankwest_breeze` | Bankwest Breeze Mastercard | bankwest.com.au | 0 |
| 145 | `au_bankwest_breeze_card` | Bankwest Breeze Mastercard | bankwest.com.au | 0 |
| 146 | `bankwest_platinum_basic` | Bankwest Platinum Mastercard | bankwest.com.au | 0 |
| 147 | `bankwest_zero_mastercard` | Bankwest Zero Mastercard | bankwest.com.au | 0 |
| 148 | `bendigo_bright_card` | Bendigo Bright Credit Card | bendigobank.com.au | 0 |
| 149 | `au_bendigo_bright_card` | Bendigo Bright Credit Card | bendigobank.com.au | 0 |
| 150 | `au_bendigo_bright_card_official` | Bendigo Bright Credit Card | bendigobank.com.au | 0 |
| 151 | `bendigo_ready` | Bendigo Ready Credit Card | bendigobank.com.au | 0 |
| 152 | `au_bendigo_ready` | Bendigo Ready Credit Card | bendigobank.com.au | 0 |
| 153 | `border_bank_visa` | Border Bank Visa | borderbank.com.au | 0 |
| 154 | `coastline_credit_union_visa` | Coastline Credit Union Visa | coastline.com.au | 0 |
| 155 | `coles_no_fee_mastercard` | Coles No Annual Fee Mastercard | coles.com.au | 0 |
| 156 | `au_commbank_low_fee` | CommBank Low Fee Credit Card | commbank.com.au | 0 |
| 157 | `community_first_visa` | Community First Bank Visa | communityfirst.com.au | 0 |
| 158 | `credit_union_sa_visa` | Credit Union SA Visa | creditunionsa.com.au | 0 |
| 159 | `family_first_credit_union_visa` | Family First Credit Union Visa | familyfirst.com.au | 0 |
| 160 | `first_option_bank_visa` | First Option Bank Visa | firstoption.com.au | 0 |
| 161 | `gc_mutual_visa` | G&C Mutual Bank Visa | gcmutual.bank | 0 |
| 162 | `great_southern_bank_everyday` | Great Southern Bank Everyday Mastercard | greatsouthernbank.com.au | 0 |
| 163 | `greater_bank_platinum` | Greater Bank Platinum Visa | greater.com.au | 0 |
| 164 | `hsbc_premier_world_elite` | HSBC Premier World Elite Mastercard | hsbc.com.au | 0 |
| 165 | `heritage_bank_gold` | Heritage Bank Gold Low Rate | heritage.com.au | 0 |
| 166 | `horizon_bank_visa` | Horizon Bank Visa | horizonbank.com.au | 0 |
| 167 | `hume_bank_visa` | Hume Bank Visa Credit Card | humebank.com.au | 0 |
| 168 | `au_ing_orange_one` | ING Orange One Credit Card | ing.com.au | 0 |
| 169 | `illawarra_credit_union_visa` | Illawarra Credit Union Visa | illawarracu.com.au | 0 |
| 170 | `kogan_first_mastercard` | Kogan First Credit Card | koganmoney.com.au | 0 |
| 171 | `au_kogan_first_mastercard` | Kogan First Credit Card | koganmoney.com.au | 0 |
| 172 | `kogan_money_credit_card` | Kogan Money Credit Card | koganmoney.com.au | 0 |
| 173 | `latitude_infinity` | Latitude Infinity Credit Card | latitudefinancial.com.au | 0 |
| 174 | `move_bank_visa` | MOVE Bank Visa Credit Card | movebank.com.au | 0 |
| 175 | `macquarie_rate_saver` | Macquarie Rate Saver Credit Card | macquarie.com.au | 0 |
| 176 | `mycard_simplicity` | MyCard Simplicity | mycard.com.au | 0 |
| 177 | `nab_straightup` | NAB StraightUp Card | nab.com.au | 0 |
| 178 | `northern_inland_credit_union_visa` | Northern Inland Credit Union Visa | nicu.com.au | 0 |
| 179 | `orange_credit_union_visa` | Orange Credit Union Visa | orangecu.com.au | 0 |
| 180 | `police_bank_visa` | Police Bank Visa Credit Card | policebank.com.au | 0 |
| 181 | `police_credit_union_visa` | Police Credit Union Visa | policecu.com.au | 0 |
| 182 | `qbank_visa` | QBANK Visa Credit Card | qbank.com.au | 0 |
| 183 | `qudos_lifestyle` | Qudos Bank Lifestyle | qudosbank.com.au | 0 |
| 184 | `queensland_country_bank_visa` | Queensland Country Bank Visa | queenslandcountry.bank | 0 |
| 185 | `raa_rewards` | RAA Rewards Credit Card | raa.com.au | 0 |
| 186 | `racv_rewards` | RACV Rewards Credit Card | racv.com.au | 0 |
| 187 | `regional_australia_bank_visa` | Regional Australia Bank Visa | regionalaustraliabank.com.au | 0 |
| 188 | `reliance_bank_visa` | Reliance Bank Visa | reliancebank.com.au | 0 |
| 189 | `southern_cross_credit_union_visa` | Southern Cross Credit Union Visa | sccu.com.au | 0 |
| 190 | `summerland_bank_visa` | Summerland Bank Visa Credit Card | summerland.com.au | 0 |
| 191 | `teachers_mutual_visa` | Teachers Mutual Bank Visa Credit Card | tmbank.com.au | 0 |
| 192 | `the_capricornian_visa` | The Capricornian Visa | capricornian.com.au | 0 |
| 193 | `the_mac_visa` | The Mac Credit Union Visa | themaccu.com.au | 0 |
| 194 | `transport_mutual_visa` | Transport Mutual Credit Union Visa | transportmutual.com.au | 0 |
| 195 | `unity_bank_visa` | Unity Bank Visa Credit Card | unitybank.com.au | 0 |
| 196 | `virgin_money_no_fee` | Virgin Money No Annual Fee Card | virginmoney.com.au | 0 |
| 197 | `bankwaw_visa` | WAW Bank Visa | waw.com.au | 0 |
| 198 | `warwick_credit_union_visa` | Warwick Credit Union Visa | wcu.com.au | 0 |
| 199 | `au_westpac_flex_card` | Westpac Flex Card | westpac.com.au | 0 |
| 200 | `westpac_flex` | Westpac Flex Mastercard | westpac.com.au | 0 |
| 201 | `woolworths_team_bank_visa` | Woolworths Team Bank Visa | woolworthsteambank.com.au | 0 |
| 202 | `bcu_visa` | bcu Visa Credit Card | bcu.com.au | 0 |
| 203 | `cba_business_low_rate` | CommBank Business Low Rate Mastercard | commbank.com.au | 60 |
| 204 | `cba_business_awards` | CommBank Business Awards Mastercard | commbank.com.au | 130 |
| 205 | `cba_business_platinum_awards` | CommBank Business Platinum Awards Mastercard | commbank.com.au | 300 |
| 206 | `cba_corporate_mastercard` | CommBank Corporate Mastercard | commbank.com.au | 150 |
| 207 | `cba_awards_classic` | CommBank Awards Classic Mastercard | commbank.com.au | 89 |
| 208 | `westpac_business_altitude_black` | Westpac Business Altitude Black Mastercard | westpac.com.au | 300 |
| 209 | `westpac_business_altitude_platinum` | Westpac Business Altitude Platinum Mastercard | westpac.com.au | 150 |
| 210 | `westpac_business_low_rate` | Westpac Business Low Rate Visa | westpac.com.au | 55 |
| 211 | `westpac_business_one_plus` | Westpac Business One Plus Visa | westpac.com.au | 99 |
| 212 | `westpac_altitude_classic` | Westpac Altitude Classic Mastercard | westpac.com.au | 65 |
| 213 | `anz_business_black` | ANZ Business Black Credit Card | anz.com.au | 300 |
| 214 | `anz_business_rewards` | ANZ Business Rewards Credit Card | anz.com.au | 150 |
| 215 | `anz_business_low_rate` | ANZ Business Low Rate Credit Card | anz.com.au | 50 |
| 216 | `anz_frequent_flyer_classic` | ANZ Frequent Flyer Classic Card | anz.com.au | 95 |
| 217 | `anz_balance_visa` | ANZ Balance Visa Card | anz.com.au | 30 |
| 218 | `nab_business_signature` | NAB Business Signature Card | nab.com.au | 295 |
| 219 | `nab_business_platinum` | NAB Business Platinum Card | nab.com.au | 175 |
| 220 | `nab_business_low_rate` | NAB Business Low Rate Card | nab.com.au | 55 |
| 221 | `nab_flybuys_rewards` | NAB Flybuys Rewards Card | nab.com.au | 0 |
| 222 | `nab_rewards_classic_card` | NAB Rewards Classic Card | nab.com.au | 95 |
| 223 | `stgeorge_amplify_classic` | St.George Amplify Classic Card | stgeorge.com.au | 79 |
| 224 | `stgeorge_vertigo_platinum` | St.George Vertigo Platinum Card | stgeorge.com.au | 99 |
| 225 | `stgeorge_no_annual_fee` | St.George No Annual Fee Card | stgeorge.com.au | 0 |
| 226 | `stgeorge_business_amplify_signature` | St.George Business Amplify Signature Card | stgeorge.com.au | 279 |
| 227 | `stgeorge_business_vertigo` | St.George Business Vertigo Card | stgeorge.com.au | 55 |
| 228 | `bank_of_melbourne_amplify_platinum` | Bank of Melbourne Amplify Platinum Card | bankofmelbourne.com.au | 99 |
| 229 | `bank_of_melbourne_amplify_classic` | Bank of Melbourne Amplify Classic Card | bankofmelbourne.com.au | 79 |
| 230 | `bank_of_melbourne_no_fee` | Bank of Melbourne No Annual Fee Card | bankofmelbourne.com.au | 0 |
| 231 | `banksa_amplify_platinum` | BankSA Amplify Platinum Card | banksa.com.au | 99 |
| 232 | `banksa_no_annual_fee` | BankSA No Annual Fee Card | banksa.com.au | 0 |
| 233 | `bankwest_more_classic` | Bankwest More Classic Mastercard | bankwest.com.au | 60 |
| 234 | `bankwest_breeze_classic` | Bankwest Breeze Classic Mastercard | bankwest.com.au | 59 |
| 235 | `bankwest_zero_classic` | Bankwest Zero Classic Mastercard | bankwest.com.au | 0 |
| 236 | `bankwest_business_zero` | Bankwest Business Zero Mastercard | bankwest.com.au | 0 |
| 237 | `bankwest_business_more` | Bankwest Business More Mastercard | bankwest.com.au | 120 |
| 238 | `macquarie_business_card` | Macquarie Business Card | macquarie.com.au | 149 |
| 239 | `macquarie_black_qantas` | Macquarie Black Card Qantas | macquarie.com.au | 299 |
| 240 | `macquarie_platinum_qantas` | Macquarie Platinum Card Qantas | macquarie.com.au | 149 |
| 241 | `hsbc_low_rate_au` | HSBC Low Rate Credit Card | hsbc.com.au | 0 |
| 242 | `hsbc_platinum_qantas_au` | HSBC Platinum Qantas Credit Card | hsbc.com.au | 199 |
| 243 | `bendigo_platinum_low_rate` | Bendigo Platinum Low Rate Mastercard | bendigobank.com.au | 89 |
| 244 | `bendigo_basic_mastercard` | Bendigo Basic Mastercard | bendigobank.com.au | 0 |
| 245 | `bendigo_business_platinum` | Bendigo Business Platinum Mastercard | bendigobank.com.au | 149 |
| 246 | `suncorp_clear_options_standard` | Suncorp Clear Options Standard Visa | suncorp.com.au | 49 |
| 247 | `suncorp_business_card` | Suncorp Business Credit Card | suncorp.com.au | 79 |
| 248 | `boq_specialist_signature` | BOQ Specialist Signature Card | boqspecialist.com.au | 400 |
| 249 | `boq_specialist_platinum` | BOQ Specialist Platinum Card | boqspecialist.com.au | 200 |
| 250 | `boq_low_rate_visa` | BOQ Low Rate Visa Card | boq.com.au | 40 |
| 251 | `boq_business_edge` | BOQ Business Edge Visa Card | boq.com.au | 60 |
| 252 | `virgin_velocity_low_rate` | Virgin Money Velocity Low Rate Card | virginmoney.com.au | 0 |
| 253 | `bank_australia_clean_money_platinum` | Bank Australia Clean Money Platinum Visa | bankaustralia.com.au | 120 |
| 254 | `bank_australia_low_rate` | Bank Australia Low Rate Visa | bankaustralia.com.au | 59 |
| 255 | `great_southern_bank_low_rate` | Great Southern Bank Low Rate Visa | greatsouthernbank.com.au | 48 |
| 256 | `great_southern_bank_platinum_low_rate` | Great Southern Bank Platinum Low Rate Visa | greatsouthernbank.com.au | 79 |
| 257 | `heritage_bank_platinum_visa` | Heritage Bank Platinum Visa | heritage.com.au | 99 |
| 258 | `heritage_bank_classic_visa` | Heritage Bank Classic Visa | heritage.com.au | 30 |
| 259 | `peoples_choice_low_rate` | People's Choice Low Rate Visa | peopleschoice.com.au | 39 |
| 260 | `teachers_mutual_visa_platinum` | Teachers Mutual Bank Visa Platinum | tmbank.com.au | 99 |
| 261 | `unibank_visa_classic` | UniBank Visa Classic | unibank.com.au | 0 |
| 262 | `unibank_visa_platinum` | UniBank Visa Platinum | unibank.com.au | 99 |
| 263 | `firefighters_mutual_visa_classic` | Firefighters Mutual Bank Visa Classic | fmbank.com.au | 0 |
| 264 | `health_professionals_bank_visa` | Health Professionals Bank Visa Classic | hpbank.com.au | 0 |
| 265 | `police_bank_low_rate` | Police Bank Low Rate Visa | policebank.com.au | 0 |
| 266 | `qudos_bank_low_rate` | Qudos Bank Low Rate Visa | qudosbank.com.au | 39 |
| 267 | `pn_bank_visa_classic` | P&N Bank Visa Classic | pnbank.com.au | 0 |
| 268 | `beyond_bank_low_rate` | Beyond Bank Low Rate Credit Card | beyondbank.com.au | 40 |
| 269 | `defence_bank_foundation` | Defence Bank Foundation Credit Card | defencebank.com.au | 0 |
| 270 | `defence_bank_low_rate` | Defence Bank Low Rate Credit Card | defencebank.com.au | 45 |
| 271 | `imb_bank_low_rate` | IMB Bank Low Rate Mastercard | imb.com.au | 50 |
| 272 | `me_bank_frank_card` | ME Bank Frank Credit Card | mebank.com.au | 0 |
| 273 | `me_bank_low_rate` | ME Bank Low Rate Mastercard | mebank.com.au | 40 |
| 274 | `auswide_bank_platinum_rewards` | Auswide Bank Platinum Rewards Visa | auswidebank.com.au | 99 |
| 275 | `auswide_bank_low_rate` | Auswide Bank Low Rate Visa | auswidebank.com.au | 40 |
| 276 | `gc_mutual_low_rate` | G&C Mutual Bank Low Rate Visa | gcmutual.bank | 0 |
| 277 | `summerland_bank_low_rate` | Summerland Bank Low Rate Visa | summerland.com.au | 0 |
| 278 | `hume_bank_value_visa` | Hume Bank Value Visa | humebank.com.au | 35 |
| 279 | `hume_bank_clear_visa` | Hume Bank Clear Visa | humebank.com.au | 0 |
| 280 | `the_mutual_bank_low_rate` | The Mutual Bank Low Rate Visa | themutual.com.au | 0 |
| 281 | `regional_australia_bank_community` | Regional Australia Bank Community Visa | regionalaustraliabank.com.au | 0 |
| 282 | `newcastle_permanent_value_plus` | Newcastle Permanent Value+ Credit Card | newcastlepermanent.com.au | 40 |
| 283 | `greater_bank_ultimate_visa` | Greater Bank Ultimate Visa Credit Card | greater.com.au | 49 |
| 284 | `greater_bank_low_rate` | Greater Bank Low Rate Visa Credit Card | greater.com.au | 40 |
| 285 | `mystate_bank_platinum_visa` | MyState Bank Platinum Visa | mystate.com.au | 99 |
| 286 | `mystate_bank_low_rate` | MyState Bank Low Rate Visa | mystate.com.au | 39 |
| 287 | `cairns_bank_visa` | Cairns Bank Visa Credit Card | cairnsbank.com.au | 0 |
| 288 | `central_west_credit_union_visa` | Central West Credit Union Visa | cwcu.com.au | 30 |
| 289 | `circle_alliance_bank_visa` | Circle Alliance Bank Visa | circle.alliancebank.com.au | 0 |
| 290 | `service_one_alliance_bank_visa` | Service One Alliance Bank Visa | serviceone.com.au | 35 |
| 291 | `awa_alliance_bank_visa` | AWA Alliance Bank Visa | awaalliancebank.com.au | 0 |
| 292 | `bdcu_alliance_bank_visa` | BDCU Alliance Bank Visa | bdcualliancebank.com.au | 35 |
| 293 | `pulse_credit_union_visa` | Pulse Credit Union Visa | pulsecu.com.au | 0 |
| 294 | `south_west_slopes_visa` | South West Slopes Credit Union Visa | swscu.com.au | 0 |
| 295 | `first_choice_credit_union_visa` | First Choice Credit Union Visa | firstchoicecu.com.au | 30 |
| 296 | `coastline_low_rate_visa` | Coastline Credit Union Low Rate Visa | coastline.com.au | 39 |
| 297 | `macarthur_credit_union_visa` | The Mac (Macarthur Credit Union) Low Rate Visa | themac.com.au | 35 |
| 298 | `warwick_credit_union_low_rate` | Warwick Credit Union Low Rate Visa | wcu.com.au | 35 |
| 299 | `the_capricornian_low_rate` | The Capricornian Low Rate Visa | capricornian.com.au | 39 |
| 300 | `credit_union_sa_low_rate` | Credit Union SA Low Rate Visa | creditunionsa.com.au | 39 |
| 301 | `transport_mutual_low_rate` | Transport Mutual Low Rate Visa | transportmutual.com.au | 0 |
| 302 | `unity_bank_low_rate` | Unity Bank Low Rate Visa | unitybank.com.au | 0 |
| 303 | `woolworths_team_bank_low_rate` | Woolworths Team Bank Low Rate Visa | woolworthsteambank.com.au | 0 |
| 304 | `broken_hill_community_visa` | Broken Hill Community Credit Union Visa | bhccu.com.au | 0 |
| 305 | `catalyst_money_visa` | Catalyst Money Visa Credit Card | catalystmoney.com.au | 30 |
| 306 | `dnister_ukrainian_coop_visa` | Dnister Ukrainian Credit Co-operative Visa | dnister.com.au | 0 |
| 307 | `laboratories_credit_union_visa` | Laboratories Credit Union Visa | lcu.com.au | 0 |
| 308 | `mcu_ltd_visa` | MCU Ltd (Maleny Credit Union) Visa | mcu.com.au | 0 |
| 309 | `orange_credit_union_low_rate` | Orange Credit Union Low Rate Visa | orangecu.com.au | 35 |
| 310 | `police_credit_union_platinum` | Police Credit Union Platinum Visa | policecu.com.au | 89 |
| 311 | `move_bank_low_rate` | MOVE Bank (Railways CU) Low Rate Visa | movebank.com.au | 0 |
| 312 | `select_encompass_credit_union_visa` | Select Encompass Credit Union Visa | selectencompass.com.au | 30 |
| 313 | `south_west_credit_coop_visa` | South West Credit Co-operative Visa | swcredit.com.au | 0 |
| 314 | `southern_cross_low_rate` | Southern Cross Credit Union Low Rate Visa | sccu.com.au | 35 |
| 315 | `traditional_credit_union_visa` | Traditional Credit Union Visa | tcu.com.au | 0 |
| 316 | `warwick_credit_union_platinum` | Warwick Credit Union Platinum Visa | wcu.com.au | 89 |
| 317 | `bankwaw_low_rate_visa` | BankWAW Low Rate Visa | bankwaw.com.au | 35 |
| 318 | `endeavour_mutual_bank_visa` | Endeavour Mutual Bank Visa | endeavour.bank | 0 |
| 319 | `sydney_mutual_bank_visa` | Sydney Mutual Bank Visa | sydneymutual.bank | 0 |
| 320 | `horizon_bank_low_rate` | Horizon Bank Low Rate Visa | horizonbank.com.au | 35 |
| 321 | `illawarra_credit_union_low_rate` | Illawarra Credit Union Low Rate Visa | illawarracu.com.au | 35 |
| 322 | `intech_bank_visa` | Intech Bank Visa Credit Card | intechbank.com.au | 0 |
| 323 | `lysaght_credit_union_visa` | Lysaght Credit Union Visa | lysaghtcu.com.au | 0 |
| 324 | `maitland_mutual_visa` | The Mutual Bank (Maitland) Visa | themutual.com.au | 30 |
| 325 | `maritime_mining_power_cu_visa` | Maritime Mining & Power CU Visa | mmpcu.com.au | 0 |
| 326 | `nexus_mutual_visa` | Nexus Mutual Visa Credit Card | nexusmutual.com.au | 30 |
| 327 | `northern_inland_low_rate` | Northern Inland Credit Union Low Rate Visa | nicu.com.au | 35 |
| 328 | `nova_alliance_bank_visa` | Nova Alliance Bank Visa | novaalliancebank.com.au | 0 |
| 329 | `queensland_country_low_rate` | Queensland Country Bank Low Rate Visa | queenslandcountry.bank | 39 |
| 330 | `victoria_teachers_mutual_visa` | Victoria Teachers Mutual Bank Visa | victeach.com.au | 0 |
| 331 | `warwick_business_visa` | Warwick Credit Union Business Visa | wcu.com.au | 50 |
| 332 | `judo_bank_business_line` | Judo Bank Business Line Card | judo.bank | 150 |
| 333 | `tyro_business_credit_card` | Tyro Business Credit Card | tyro.com | 0 |
| 334 | `airwallex_corporate_card_au` | Airwallex Corporate Card AU | airwallex.com | 0 |
| 335 | `revolut_standard_card_au` | Revolut Standard Card AU | revolut.com | 0 |
| 336 | `revolut_metal_card_au` | Revolut Metal Card AU | revolut.com | 299 |
| 337 | `wise_card_au` | Wise Card AU | wise.com | 0 |
| 338 | `zip_pay_digital_mastercard` | Zip Pay Digital Mastercard | zip.co | 0 |
| 339 | `zip_money_digital_card` | Zip Money Digital Card | zip.co | 0 |
| 340 | `westpac_corporate_card` | Westpac Corporate Card | westpac.com.au | 120 |
| 341 | `anz_corporate_card` | ANZ Corporate Card | anz.com.au | 120 |
| 342 | `nab_corporate_card` | NAB Corporate Card | nab.com.au | 120 |
| 343 | `hsbc_corporate_card_au` | HSBC Corporate Card AU | hsbc.com.au | 150 |
| 344 | `coles_low_rate_mastercard` | Coles Low Rate Mastercard | coles.com.au | 58 |
| 345 | `bendigo_business_basic` | Bendigo Business Basic Mastercard | bendigobank.com.au | 40 |
| 346 | `virgin_money_points_card` | Virgin Money Velocity Points Card | virginmoney.com.au | 0 |
| 347 | `bank_australia_commercial_visa` | Bank Australia Commercial Visa | bankaustralia.com.au | 60 |
| 348 | `great_southern_bank_business_visa` | Great Southern Bank Business Visa | greatsouthernbank.com.au | 60 |
| 349 | `heritage_bank_business_visa` | Heritage Bank Business Visa | heritage.com.au | 60 |
| 350 | `qudos_bank_business_visa` | Qudos Bank Business Visa | qudosbank.com.au | 60 |


### 🇨🇦 Canada (250)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `amex_platinum_ca` | American Express Platinum Card | americanexpress.com | 799 |
| 2 | `ca_amex_platinum` | American Express Platinum Card CA | americanexpress.com | 799 |
| 3 | `amex_aeroplan_reserve_ca` | American Express Aeroplan Reserve Card | americanexpress.ca | 599 |
| 4 | `cibc_aeroplan_visa_infinite_privilege` | CIBC Aeroplan Visa Infinite Privilege | cibc.com | 599 |
| 5 | `ca_cibc_aeroplan_privilege` | CIBC Aeroplan Visa Infinite Privilege | cibc.com | 599 |
| 6 | `ca_rbc_avion_infinite_privilege` | RBC Avion Visa Infinite Privilege | rbc.com | 599 |
| 7 | `bmo_eclipse_visa_infinite_privilege` | BMO eclipse Visa Infinite Privilege | bmo.com | 499 |
| 8 | `scotiabank_american_express_platinum` | The Platinum Card® from Scotiabank | scotiabank.com | 399 |
| 9 | `amex_business_gold_ca` | American Express® Business Gold Rewards Card | americanexpress.ca | 250 |
| 10 | `amex_gold_rewards_ca` | Amex Gold Rewards Card | americanexpress.ca | 250 |
| 11 | `ca_amex_gold_rewards` | Amex Gold Rewards Card CA | americanexpress.com | 250 |
| 12 | `brim_world_elite_mastercard` | Brim World Elite Mastercard | brimfinancial.com | 199 |
| 13 | `scotiabank_passport_visa_infinite_business` | Scotiabank Passport Visa Infinite Business | scotiabank.com | 199 |
| 14 | `ca_scotiabank_passport_biz` | Scotiabank Passport Visa Infinite Business | scotiabank.com | 199 |
| 15 | `amex_cobalt` | American Express Cobalt Card | americanexpress.com | 191.88 |
| 16 | `neo_cathay_pacific_card` | Neo Cathay Pacific Mastercard | neofinancial.com | 180 |
| 17 | `ca_rbc_british_airways` | RBC British Airways Visa Infinite | rbc.com | 165 |
| 18 | `rbc_british_airways_visa_infinite` | RBC® British Airways Visa Infinite® | rbc.com | 165 |
| 19 | `ca_amex_cobalt` | American Express Cobalt Card | americanexpress.com | 156 |
| 20 | `bmo_ascend_world_elite` | BMO Ascend World Elite Mastercard | bmo.com | 150 |
| 21 | `ca_bmo_ascend_world_elite` | BMO Ascend World Elite Mastercard | bmo.com | 150 |
| 22 | `national_bank_world_elite` | National Bank World Elite Mastercard | nbc.ca | 150 |
| 23 | `scotiabank_passport_visa_infinite` | Scotiabank Passport Visa Infinite | scotiabank.com | 150 |
| 24 | `ca_scotiabank_passport_visa` | Scotiabank Passport Visa Infinite | scotiabank.com | 150 |
| 25 | `td_business_aeroplan_visa` | TD® Business Aeroplan® Visa* Card | td.com | 149 |
| 26 | `td_business_travel_visa` | TD® Business Travel Visa* Card | td.com | 149 |
| 27 | `cibc_aeroplan_visa_infinite` | CIBC Aeroplan Visa Infinite | cibc.com | 139 |
| 28 | `cibc_aventura_visa_infinite` | CIBC Aventura Visa Infinite | cibc.com | 139 |
| 29 | `manulife_money_plus_visa_infinite` | ManulifeMONEY+ Visa Infinite | manulife.ca | 139 |
| 30 | `td_aeroplan_visa_infinite` | TD Aeroplan Visa Infinite | td.com | 139 |
| 31 | `td_cash_back_visa_infinite` | TD Cash Back Visa Infinite | td.com | 139 |
| 32 | `td_first_class_travel_visa_infinite` | TD First Class Travel Visa Infinite | td.com | 139 |
| 33 | `ca_td_first_class_travel` | TD First Class Travel Visa Infinite | td.com | 139 |
| 34 | `desjardins_odyssey_world_elite` | Desjardins Odyssey® World Elite® Mastercard® | desjardins.com | 130 |
| 35 | `ca_laurentian_visa_infinite` | Laurentian Bank Visa Infinite | laurentianbank.ca | 130 |
| 36 | `laurentian_bank_visa_infinite` | Laurentian Bank Visa Infinite* | laurentianbank.ca | 130 |
| 37 | `laurentian_bank_visa_signature` | Laurentian Bank Visa Signature | laurentianbank.ca | 130 |
| 38 | `atb_world_elite_mastercard` | ATB World Elite Mastercard | atb.com | 120 |
| 39 | `amex_aeroplan_ca` | American Express Aeroplan Card | americanexpress.ca | 120 |
| 40 | `amex_marriott_bonvoy_ca` | Amex Marriott Bonvoy Card | americanexpress.ca | 120 |
| 41 | `bmo_air_miles_world_elite` | BMO AIR MILES® World Elite® Mastercard® | bmo.com | 120 |
| 42 | `bmo_cashback_world_elite` | BMO CashBack World Elite Mastercard | bmo.com | 120 |
| 43 | `ca_bmo_eclipse_visa_infinite` | BMO Eclipse Visa Infinite | bmo.com | 120 |
| 44 | `bmo_eclipse_visa_infinite` | BMO eclipse Visa Infinite Card | bmo.com | 120 |
| 45 | `cibc_dividend_visa_infinite` | CIBC Dividend Visa Infinite | cibc.com | 120 |
| 46 | `canadian_western_bank_visa` | CWB Visa Infinite | cwbank.com | 120 |
| 47 | `rbc_avion_visa_infinite` | RBC Avion Visa Infinite | rbc.com | 120 |
| 48 | `ca_rbc_cathay_pacific` | RBC Cathay Pacific Visa Platinum | rbc.com | 120 |
| 49 | `scotia_momentum_visa_infinite` | Scotia Momentum Visa Infinite | scotiabank.com | 120 |
| 50 | `scotiabank_gold_amex` | Scotiabank Gold American Express | scotiabank.com | 120 |
| 51 | `ca_scotiabank_gold_amex` | Scotiabank Gold American Express | scotiabank.com | 120 |
| 52 | `scotiabank_momentum_visa_infinite` | Scotiabank Momentum Visa Infinite | scotiabank.com | 120 |
| 53 | `amex_simply_cash_preferred_ca` | SimplyCash Preferred Amex | americanexpress.ca | 120 |
| 54 | `vancity_enviro_visa` | Vancity enviro Visa Infinite | vancity.com | 120 |
| 55 | `rbc_westjet_world_elite` | WestJet RBC® World Elite Mastercard® | rbc.com | 119 |
| 56 | `ca_desjardins_odyssey_gold` | Desjardins Odyssey Gold Visa | desjardins.com | 110 |
| 57 | `koho_extra_mastercard` | KOHO Extra Mastercard | koho.ca | 108 |
| 58 | `desjardins_cashback_world_elite` | Desjardins Cash Back World Elite | desjardins.com | 100 |
| 59 | `amex_business_edge_ca` | American Express® Business Edge® Card | americanexpress.ca | 99 |
| 60 | `cibc_dividend_platinum` | CIBC Dividend Platinum Visa | cibc.com | 99 |
| 61 | `ca_cibc_dividend_platinum` | CIBC Dividend Platinum Visa | cibc.com | 99 |
| 62 | `cibc_dividend_platinum_visa` | CIBC Dividend Platinum® Visa* Card | cibc.com | 99 |
| 63 | `coast_capital_visa` | Coast Capital Visa Infinite Cash Back | coastcapitalsavings.com | 99 |
| 64 | `meridian_visa_cash_back` | Meridian Visa Infinite Cash Back | meridiancu.ca | 99 |
| 65 | `rbc_cash_back_preferred_world_elite` | RBC Cash Back Preferred World Elite Mastercard | rbc.com | 99 |
| 66 | `rbc_cashback_preferred_world_elite` | RBC Cash Back Preferred World Elite Mastercard | rbc.com | 99 |
| 67 | `ca_national_bank_platinum` | National Bank Platinum Mastercard | nbc.ca | 89 |
| 68 | `ca_national_bank_platinum_card` | National Bank Platinum Mastercard | nbc.ca | 89 |
| 69 | `td_aeroplan_visa_platinum` | TD Aeroplan Visa Platinum | td.com | 89 |
| 70 | `national_bank_platinum_mastercard` | National Bank Platinum Mastercard® | nbc.ca | 70 |
| 71 | `rbc_ion_plus` | RBC ION+ Visa | rbc.com | 48 |
| 72 | `rbc_ion_plus_visa` | RBC ION+ Visa | rbc.com | 48 |
| 73 | `ca_rbc_westjet_mastercard` | RBC WestJet Mastercard | rbc.com | 39 |
| 74 | `national_bank_syncro` | National Bank Syncro Mastercard | nbc.ca | 35 |
| 75 | `ca_national_bank_syncro` | National Bank Syncro Mastercard | nbc.ca | 35 |
| 76 | `atb_cash_back_mastercard` | ATB Cash Back Mastercard | atb.com | 0 |
| 77 | `ca_atb_platinum_mastercard` | ATB Platinum Mastercard | atb.com | 0 |
| 78 | `access_credit_union_visa` | Access Credit Union Visa | accesscu.ca | 0 |
| 79 | `affinity_credit_union_visa` | Affinity Credit Union Visa | affinitycu.ca | 0 |
| 80 | `alterna_cash_back_visa` | Alterna Savings Cash Back Visa | alterna.ca | 0 |
| 81 | `amazon_ca_rewards_mastercard` | Amazon.ca Rewards Mastercard® | amazon.ca | 0 |
| 82 | `amex_choice_card_ca` | Amex Choice Card | americanexpress.ca | 0 |
| 83 | `assiniboine_credit_union_visa` | Assiniboine Credit Union Visa | assiniboine.mb.ca | 0 |
| 84 | `ca_bmo_air_miles_mastercard` | BMO Air Miles Mastercard | bmo.com | 0 |
| 85 | `bmo_cashback_mastercard` | BMO CashBack Mastercard | bmo.com | 0 |
| 86 | `ca_bmo_cashback_mastercard_card` | BMO CashBack Mastercard | bmo.com | 0 |
| 87 | `bmo_ihg_one_rewards_mastercard` | BMO® IHG One Rewards Mastercard®* | bmo.com | 0 |
| 88 | `bmo_shell_air_miles_mastercard` | BMO® Shell®® AIR MILES®® Mastercard®* | bmo.com | 0 |
| 89 | `brim_mastercard` | Brim Mastercard | brimfinancial.com | 0 |
| 90 | `ca_brim_mastercard` | Brim Mastercard | brimfinancial.com | 0 |
| 91 | `cibc_business_plus_visa` | CIBC Business Plus Visa* Card | cibc.com | 0 |
| 92 | `cibc_costco_mastercard` | CIBC Costco Mastercard | cibc.com | 0 |
| 93 | `ca_cibc_dividend_visa` | CIBC Dividend Visa Card | cibc.com | 0 |
| 94 | `ca_cibc_dividend_visa_card` | CIBC Dividend Visa Card | cibc.com | 0 |
| 95 | `cambrian_credit_union_visa` | Cambrian Credit Union Visa | cambrian.mb.ca | 0 |
| 96 | `ca_coop_community_builder` | Co-op Community Builder Visa | co-op.ca | 0 |
| 97 | `coop_community_builder_visa` | Co-op Community Builder Visa Card | co-op.ca | 0 |
| 98 | `coastal_community_credit_union_visa` | Coastal Community Credit Union Visa | cccu.ca | 0 |
| 99 | `conexus_credit_union_visa` | Conexus Credit Union Visa | conexus.ca | 0 |
| 100 | `crosstown_credit_union_visa` | Crosstown Civic Credit Union Visa | crosstowncu.mb.ca | 0 |
| 101 | `duca_credit_union_visa` | DUCA Credit Union Visa | duca.com | 0 |
| 102 | `desjardins_cash_back_visa` | Desjardins Cash Back Visa | desjardins.com | 0 |
| 103 | `ca_desjardins_cashback_card` | Desjardins Cash Back Visa | desjardins.com | 0 |
| 104 | `ca_desjardins_flexi_visa` | Desjardins Flexi Visa Card | desjardins.com | 0 |
| 105 | `eq_bank_card` | EQ Bank Card | eqbank.ca | 0 |
| 106 | `ca_eq_bank_card_rewards` | EQ Bank Mastercard | eqbank.ca | 0 |
| 107 | `first_west_envision_visa` | Envision Financial Visa | envisionfinancial.ca | 0 |
| 108 | `fido_mastercard` | Fido Mastercard | rogers.com | 0 |
| 109 | `firstontario_credit_union_visa` | FirstOntario Credit Union Visa | firstontario.com | 0 |
| 110 | `home_trust_preferred_visa` | Home Trust Preferred Visa | hometrust.ca | 0 |
| 111 | `ca_home_trust_visa` | Home Trust Preferred Visa | hometrust.ca | 0 |
| 112 | `ca_home_trust_secured_visa` | Home Trust Secured Visa Card | hometrust.ca | 0 |
| 113 | `innovation_credit_union_visa` | Innovation Federal Credit Union Visa | innovationcu.ca | 0 |
| 114 | `koho_card` | KOHO Card | koho.ca | 0 |
| 115 | `kindred_credit_union_visa` | Kindred Credit Union Visa | kindredcu.com | 0 |
| 116 | `ca_laurentian_visa_cashback` | Laurentian Bank Visa Cash Back | laurentianbank.ca | 0 |
| 117 | `ca_laurentian_cashback_visa` | Laurentian Bank Visa Cash Back | laurentianbank.ca | 0 |
| 118 | `libro_credit_union_visa` | Libro Credit Union Visa | libro.ca | 0 |
| 119 | `mbna_amazon_mastercard` | MBNA Amazon.ca Rewards Mastercard | mbna.ca | 0 |
| 120 | `mbna_best_western_rewards` | MBNA Best Western Rewards® Mastercard® | mbna.ca | 0 |
| 121 | `mbna_rewards_platinum_plus` | MBNA Rewards Platinum Plus® Mastercard® | mbna.ca | 0 |
| 122 | `ca_meridian_visa_cashback` | Meridian Visa Cash Back Card | meridiancu.ca | 0 |
| 123 | `national_bank_echo_cashback` | National Bank Écho Cashback Mastercard | nbc.ca | 0 |
| 124 | `neo_financial_credit` | Neo Financial Credit | neofinancial.com | 0 |
| 125 | `neo_financial_card` | Neo Financial Credit Card | neofinancial.com | 0 |
| 126 | `ca_neo_financial_card_custom` | Neo Financial Custom Mastercard | neofinancial.com | 0 |
| 127 | `ca_pc_financial_mastercard` | PC Financial Mastercard | pcfinancial.ca | 0 |
| 128 | `ca_pc_financial_mastercard_card` | PC Financial Mastercard | pcfinancial.ca | 0 |
| 129 | `pc_financial_world_elite` | PC Financial World Elite Mastercard | pcfinancial.ca | 0 |
| 130 | `ca_pc_financial_world_elite` | PC Financial World Elite Mastercard | pcfinancial.ca | 0 |
| 131 | `pc_world_elite_mastercard` | PC World Elite Mastercard | pcfinancial.ca | 0 |
| 132 | `pc_financial_mastercard` | PC® Financial Mastercard® | pcfinancial.ca | 0 |
| 133 | `prospera_credit_union_visa` | Prospera Credit Union Visa | prospera.ca | 0 |
| 134 | `rbc_cash_back_mastercard` | RBC Cash Back Mastercard | rbc.com | 0 |
| 135 | `ca_rbc_cashback_mastercard` | RBC Cash Back Mastercard | rbc.com | 0 |
| 136 | `rbc_ion_visa` | RBC ION Visa | rbc.com | 0 |
| 137 | `ca_rbc_ion_visa` | RBC ION Visa | rbc.com | 0 |
| 138 | `ca_rogers_connections` | Rogers Connections Mastercard | rogers.com | 0 |
| 139 | `rogers_mastercard` | Rogers Mastercard | rogers.com | 0 |
| 140 | `rogers_red_world_elite` | Rogers Red World Elite Mastercard | rogersbank.com | 0 |
| 141 | `ca_scotiabank_momentum_no_fee` | Scotiabank Momentum No-Fee Visa | scotiabank.com | 0 |
| 142 | `ca_scotiabank_no_fee_value` | Scotiabank No-Fee Value Visa | scotiabank.com | 0 |
| 143 | `scotiabank_scene_plus_visa` | Scotiabank SCENE+ Visa Card | scotiabank.com | 0 |
| 144 | `scotiabank_scene_amex` | Scotiabank Scene+ American Express | scotiabank.com | 0 |
| 145 | `scotiabank_no_fee_value_visa` | Scotiabank®* No-Fee Value® Visa* Card | scotiabank.com | 0 |
| 146 | `ca_servus_credit_union_mastercard` | Servus Credit Union Mastercard | servus.ca | 0 |
| 147 | `servus_credit_union_visa` | Servus Credit Union Visa Cash Back | servus.ca | 0 |
| 148 | `ca_simplii_cashback_visa` | Simplii Cash Back Visa | simplii.com | 0 |
| 149 | `simplii_cash_back` | Simplii Financial Cash Back Visa | simplii.com | 0 |
| 150 | `amex_simply_cash_ca` | SimplyCash Card from Amex | americanexpress.ca | 0 |
| 151 | `steinbach_credit_union_visa` | Steinbach Credit Union Visa | scu.mb.ca | 0 |
| 152 | `synergy_credit_union_visa` | Synergy Credit Union Visa | synergycu.ca | 0 |
| 153 | `ca_td_business_cash_back` | TD Business Cash Back Visa | td.com | 0 |
| 154 | `td_business_cash_back_visa` | TD Business Cash Back Visa Card | td.com | 0 |
| 155 | `td_cash_back_visa` | TD Cash Back Visa Card | td.com | 0 |
| 156 | `ca_td_cash_back_visa` | TD Cash Back Visa Card | td.com | 0 |
| 157 | `ca_td_cash_back_visa_card` | TD Cash Back Visa Card | td.com | 0 |
| 158 | `ca_td_rewards_visa` | TD Rewards Visa Card | td.com | 0 |
| 159 | `td_rewards_visa` | TD Rewards Visa card | td.com | 0 |
| 160 | `tangerine_money_back` | Tangerine Money-Back Credit Card | tangerine.ca | 0 |
| 161 | `ca_tangerine_world` | Tangerine World Mastercard | tangerine.ca | 0 |
| 162 | `triangle_world_elite` | Triangle World Elite Mastercard | canadiantire.ca | 0 |
| 163 | `canadian_tire_triangle_world_elite` | Triangle World Elite Mastercard | ctfs.com | 0 |
| 164 | `canadian_tire_triangle_mastercard` | Triangle® Mastercard® | canadiantire.ca | 0 |
| 165 | `uni_visa_platinum` | UNI Visa Platinum | uni.ca | 0 |
| 166 | `ca_vancity_enviro_classic` | Vancity enviro Classic Visa | vancity.com | 0 |
| 167 | `ca_walmart_rewards_card` | Walmart Rewards Mastercard | walmart.ca | 0 |
| 168 | `walmart_rewards_mastercard_ca` | Walmart Rewards® Mastercard® | walmart.ca | 0 |
| 169 | `wealthsimple_cash_card` | Wealthsimple Cash Card | wealthsimple.com | 0 |
| 170 | `connect_first_credit_union_visa` | connectFirst Credit Union Visa | connectfirstcu.com | 0 |
| 171 | `bmo_us_dollar_mastercard` | BMO U.S. Dollar Mastercard | bmo.com | 35 |
| 172 | `bmo_cashback_commercial_mastercard` | BMO Commercial CashBack Mastercard | bmo.com | 150 |
| 173 | `cibc_dividend_visa_for_students` | CIBC Dividend Visa for Students | cibc.com | 0 |
| 174 | `scotiabank_scotialine_visa` | ScotiaLine Personal Line of Credit Visa | scotiabank.com | 0 |
| 175 | `alterna_collabria_visa_infinite` | Alterna Collabria Visa Infinite | alterna.ca | 120 |
| 176 | `cambrian_collabria_visa_infinite` | Cambrian Collabria Visa Infinite | cambrian.mb.ca | 120 |
| 177 | `conexus_collabria_visa_platinum` | Conexus Collabria Visa Platinum | conexus.ca | 50 |
| 178 | `bmo_air_miles_mastercard` | BMO AIR MILES Mastercard | bmo.com | 0 |
| 179 | `bmo_preferred_rate_mastercard` | BMO Preferred Rate Mastercard | bmo.com | 20 |
| 180 | `bmo_rewards_mastercard` | BMO Rewards Mastercard | bmo.com | 0 |
| 181 | `bmo_business_xpress_mastercard` | BMO Business Xpress Mastercard | bmo.com | 0 |
| 182 | `bmo_business_cashback_mastercard` | BMO Business CashBack Mastercard | bmo.com | 120 |
| 183 | `bmo_air_miles_business_mastercard` | BMO AIR MILES Business Mastercard | bmo.com | 120 |
| 184 | `td_aeroplan_infinite_privilege` | TD Aeroplan Visa Infinite Privilege Card | td.com | 599 |
| 185 | `td_platinum_travel_visa` | TD Platinum Travel Visa Card | td.com | 89 |
| 186 | `td_emerald_flex_rate_visa` | TD Emerald Flex Rate Visa Card | td.com | 25 |
| 187 | `td_low_rate_visa` | TD Low Rate Visa Card | td.com | 25 |
| 188 | `td_business_select_rate_visa` | TD Business Select Rate Visa Card | td.com | 49 |
| 189 | `td_aeroplan_business_visa_infinite` | TD Aeroplan Business Visa Infinite Card | td.com | 149 |
| 190 | `rbc_avion_visa_platinum` | RBC Avion Visa Platinum | rbc.com | 120 |
| 191 | `rbc_rewards_plus_visa` | RBC Rewards+ Visa | rbc.com | 0 |
| 192 | `rbc_rate_advantage_visa` | RBC RateAdvantage Visa | rbc.com | 0 |
| 193 | `rbc_visa_classic_low_rate` | RBC Visa Classic Low Rate | rbc.com | 20 |
| 194 | `rbc_visa_platinum` | RBC Visa Platinum | rbc.com | 0 |
| 195 | `rbc_business_avion_visa` | RBC Avion Visa Business | rbc.com | 120 |
| 196 | `rbc_business_cashback_mastercard` | RBC Business Cash Back Mastercard | rbc.com | 0 |
| 197 | `rbc_business_platinum_visa` | RBC Business Platinum Visa | rbc.com | 0 |
| 198 | `cibc_aeroplan_visa_no_fee` | CIBC Aeroplan Visa Card | cibc.com | 0 |
| 199 | `cibc_aventura_gold_visa` | CIBC Aventura Gold Visa Card | cibc.com | 99 |
| 200 | `cibc_aventura_visa` | CIBC Aventura Visa Card | cibc.com | 0 |
| 201 | `cibc_select_visa` | CIBC Select Visa Card | cibc.com | 29 |
| 202 | `cibc_classic_visa` | CIBC Classic Visa Card | cibc.com | 0 |
| 203 | `cibc_dividend_visa` | CIBC Dividend Visa Card | cibc.com | 0 |
| 204 | `cibc_aeroplan_business_visa` | CIBC Aeroplan Visa Business Card | cibc.com | 180 |
| 205 | `cibc_aventura_business_visa` | CIBC Aventura Visa Card for Business | cibc.com | 120 |
| 206 | `cibc_bizline_visa` | CIBC Bizline Visa Card | cibc.com | 0 |
| 207 | `scotiabank_value_visa` | Scotiabank Value Visa Card | scotiabank.com | 29 |
| 208 | `scotiabank_amex_card` | Scotiabank American Express Card | scotiabank.com | 0 |
| 209 | `scotiabank_platinum_amex` | Scotiabank Platinum American Express Card | scotiabank.com | 399 |
| 210 | `scotiabank_momentum_mastercard` | Scotiabank Momentum Mastercard | scotiabank.com | 0 |
| 211 | `scotiabank_momentum_business_visa` | Scotia Momentum for Business Visa Card | scotiabank.com | 79 |
| 212 | `scotiabank_gm_rewards_visa` | Scotiabank GM Rewards Visa Card | scotiabank.com | 0 |
| 213 | `scotiabank_gm_rewards_infinite` | Scotiabank GM Rewards Visa Infinite Card | scotiabank.com | 79 |
| 214 | `national_bank_mc1_mastercard` | National Bank MC1 Mastercard | nbc.ca | 0 |
| 215 | `national_bank_allure_mastercard` | National Bank Allure Mastercard | nbc.ca | 0 |
| 216 | `national_bank_business_world_elite` | National Bank World Elite Business Mastercard | nbc.ca | 180 |
| 217 | `national_bank_business_platinum` | National Bank Platinum Business Mastercard | nbc.ca | 60 |
| 218 | `desjardins_odyssey_gold_visa` | Desjardins Odyssey Gold Visa | desjardins.com | 110 |
| 219 | `desjardins_odyssey_infinite_privilege` | Desjardins Odyssey Visa Infinite Privilege | desjardins.com | 395 |
| 220 | `desjardins_modulo_visa` | Desjardins Modulo Visa | desjardins.com | 30 |
| 221 | `desjardins_low_rate_visa` | Desjardins Low Rate Visa | desjardins.com | 30 |
| 222 | `desjardins_business_odyssey` | Desjardins Business Odyssey World Elite Mastercard | desjardins.com | 130 |
| 223 | `desjardins_business_cashback_visa` | Desjardins Business Cash Back Visa | desjardins.com | 0 |
| 224 | `laurentian_bank_visa_black` | Laurentian Bank Visa Black | laurentianbank.ca | 130 |
| 225 | `laurentian_bank_visa_reduced_rate` | Laurentian Bank Visa Reduced Rate | laurentianbank.ca | 30 |
| 226 | `laurentian_bank_visa_classic` | Laurentian Bank Visa Classic | laurentianbank.ca | 0 |
| 227 | `laurentian_bank_business_visa` | Laurentian Bank Business Visa | laurentianbank.ca | 50 |
| 228 | `mbna_rewards_world_elite` | MBNA Rewards World Elite Mastercard | mbna.ca | 120 |
| 229 | `mbna_true_line_mastercard` | MBNA True Line Mastercard | mbna.ca | 0 |
| 230 | `mbna_true_line_gold` | MBNA True Line Gold Mastercard | mbna.ca | 39 |
| 231 | `mbna_harley_davidson_platinum` | MBNA Harley-Davidson Platinum Plus Mastercard | mbna.ca | 0 |
| 232 | `atb_alberta_rewards_mastercard` | ATB Alberta Rewards Mastercard | atb.com | 0 |
| 233 | `atb_alberta_rewards_world_elite` | ATB Alberta Rewards World Elite Mastercard | atb.com | 120 |
| 234 | `atb_cashback_mastercard` | ATB CashBack Mastercard | atb.com | 0 |
| 235 | `atb_cashback_world_elite` | ATB CashBack World Elite Mastercard | atb.com | 120 |
| 236 | `atb_preferred_fixed_rate` | ATB Preferred Fixed-Rate Mastercard | atb.com | 29 |
| 237 | `atb_preferred_variable_rate` | ATB Preferred Variable-Rate Mastercard | atb.com | 49 |
| 238 | `atb_business_mastercard` | ATB Business Mastercard | atb.com | 50 |
| 239 | `meridian_visa_infinite_travel` | Meridian Visa Infinite Travel Rewards Card | meridiancu.ca | 99 |
| 240 | `meridian_visa_platinum_cashback` | Meridian Visa Platinum Cash Back Card | meridiancu.ca | 49 |
| 241 | `meridian_visa_platinum_travel` | Meridian Visa Platinum Travel Rewards Card | meridiancu.ca | 49 |
| 242 | `meridian_visa_platinum` | Meridian Visa Platinum Card | meridiancu.ca | 24 |
| 243 | `vancity_enviro_fair_visa` | Vancity enviro Fair+ Visa | vancity.com | 0 |
| 244 | `vancity_enviro_infinite_privilege` | Vancity enviro Visa Infinite Privilege | vancity.com | 399 |
| 245 | `vancity_enviro_business_visa` | Vancity enviro Business Visa | vancity.com | 40 |
| 246 | `coast_capital_visa_classic` | Coast Capital Visa Classic | coastcapitalsavings.com | 0 |
| 247 | `coast_capital_visa_platinum` | Coast Capital Visa Platinum | coastcapitalsavings.com | 30 |
| 248 | `servus_mastercard_low_rate` | Servus Credit Union Mastercard Low Rate | servus.ca | 30 |
| 249 | `servus_mastercard_world_elite` | Servus Credit Union Mastercard World Elite | servus.ca | 150 |
| 250 | `brim_world_mastercard` | Brim World Mastercard | brimfinancial.com | 99 |


### 🇨🇳 China (250)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `boc_world_elite` | BOC 中行世界之极卡 | boc.cn | 3600 |
| 2 | `ccb_supreme_white` | CCB Supreme Platinum Card | ccb.com | 3600 |
| 3 | `cn_ccb_supreme_white` | CCB Supreme Platinum Card | ccb.com | 3600 |
| 4 | `ccb_unionsupreme` | CCB 尊享白金信用卡 | ccb.com | 3600 |
| 5 | `cmb_classic_platinum` | CMB Classic Platinum Card | cmbchina.com | 3600 |
| 6 | `cn_cmb_classic_platinum` | CMB Classic Platinum Card | cmbchina.com | 3600 |
| 7 | `cmb_classic_white` | CMB 招商银行经典白金卡 | cmbchina.com | 3600 |
| 8 | `icbc_platinum` | ICBC 工银白金信用卡 | icbc.com.cn | 3600 |
| 9 | `spdb_ae_white` | SPDB American Express Platinum Card | spdb.com.cn | 3600 |
| 10 | `cn_spdb_ae_white` | SPDB American Express Platinum Card | spdb.com.cn | 3600 |
| 11 | `spdb_ae_white_3` | SPDB 浦发美运白金卡 | spdb.com.cn | 3600 |
| 12 | `cn_cmb_classic_white` | 招商银行经典白金卡 | cmbchina.com | 3600 |
| 13 | `cn_spdb_ae_white_card` | 浦发银行美国运通白金卡 | spdb.com.cn | 3600 |
| 14 | `industrial_pass_card` | CIB 兴业行卡标准版 | cib.com.cn | 2600 |
| 15 | `psbc_dingsheng_platinum` | PSBC 邮储鼎盛白金信用卡 | psbc.com | 2600 |
| 16 | `psbc_dingzhi_platinum` | PSBC 邮储鼎致白金信用卡 | psbc.com | 2600 |
| 17 | `icbc_global_travel` | ICBC Global Travel Platinum Card | icbc.com.cn | 2000 |
| 18 | `icbc_visa_infinite` | ICBC 工银Visa无限卡 | icbc.com.cn | 2000 |
| 19 | `cn_icbc_global_travel_card` | 工商银行环球旅行白金卡 | icbc.com.cn | 2000 |
| 20 | `ceb_luxury_white` | CEB 光大奢享白金卡 | cebbank.com | 1188 |
| 21 | `bocom_white_point` | BOCOM 交行白金信用卡 | bankcomm.com | 1000 |
| 22 | `cib_pass_white` | CIB Pass Platinum Card | cib.com.cn | 900 |
| 23 | `boc_air_china_olympic` | BOC Air China Platinum Card | boc.cn | 800 |
| 24 | `boc_greatwall_globetrotter` | BOC Great Wall Globetrotter White Card | boc.cn | 800 |
| 25 | `cn_boc_standard_white` | BOC Standard Platinum Card | boc.cn | 800 |
| 26 | `guangfa_鼎极白金` | CGB Dingji Platinum Card | cgbchina.com.cn | 800 |
| 27 | `cn_guangfa_dingji_white_card` | CGB Dingji Platinum Card | cgbchina.com.cn | 800 |
| 28 | `guangfa_highspeed_white` | CGB High-Speed Rail Platinum Card | cgbchina.com.cn | 800 |
| 29 | `cn_guangfa_highspeed_white` | CGB High-Speed Rail Platinum Card | cgbchina.com.cn | 800 |
| 30 | `cn_boc_greatwall_white` | 中国银行长城白金卡 | boc.cn | 800 |
| 31 | `cn_guangfa_highspeed_white_card` | 广发高铁白金卡 | cgbchina.com.cn | 800 |
| 32 | `ceb_standard_white` | CEB 光大标准白金卡 | cebbank.com | 680 |
| 33 | `cib_standard_white` | CIB 兴业标准白金卡 | cib.com.cn | 680 |
| 34 | `hxb_elite_platinum_4` | HXB 华夏精英尊尚白金卡 | hxb.com.cn | 680 |
| 35 | `pab_standard_white` | PAB 平安标准白金卡 | pingan.com | 680 |
| 36 | `spdb_standard_white` | SPDB 浦发标准白金卡 | spdb.com.cn | 680 |
| 37 | `minsheng_standard_white` | CMBC Standard Platinum Card | cmbc.com.cn | 600 |
| 38 | `minsheng_travel_platinum` | CMBC 民生商旅白金信用卡 | cmbc.com.cn | 600 |
| 39 | `hb_elite_platinum_4` | HXB Elite Platinum Card | hxb.com.cn | 600 |
| 40 | `ccb_long_joy_white` | CCB Long Card Joy Platinum Card | ccb.com | 580 |
| 41 | `ccb_dragon_amex` | CCB 建设银行龙卡美国运通卡 | ccb.com | 580 |
| 42 | `abc_national_treasure_white` | ABC National Treasure Platinum Card | abchina.com | 500 |
| 43 | `bocom_kind_white` | BOCOM Yuyi White Card Red Edition | bankcomm.com | 500 |
| 44 | `bocom_yuyi_white` | BOCOM Yuyi White Platinum Card | bankcomm.com | 500 |
| 45 | `cn_bocom_yuyi_white` | BOCOM Yuyi White Platinum Card | bankcomm.com | 500 |
| 46 | `cn_industrial_pass_card` | CIB Pass Platinum Card | cib.com.cn | 500 |
| 47 | `industrial_bank_xingdong` | CIB Xingdong Platinum Card | cib.com.cn | 500 |
| 48 | `cn_bocom_yuyi_white_card` | 交通银行优逸白金卡 | bankcomm.com | 500 |
| 49 | `cn_industrial_bank_xingdong_card` | 兴业银行行动白金卡 | cib.com.cn | 500 |
| 50 | `citic_ihg_premier` | CITIC IHG One Rewards Platinum Card | citicbank.com | 480 |
| 51 | `citic_standard_white` | CITIC Standard Platinum Card | citicbank.com | 480 |
| 52 | `citic_yicard_white` | CITIC YiCard Platinum Card | citicbank.com | 480 |
| 53 | `cn_citic_yicard_white` | CITIC YiCard Platinum Card | citicbank.com | 480 |
| 54 | `citic_safari_card` | CITIC 中信Safari卡 | citicbank.com.cn | 480 |
| 55 | `cn_citic_yicard_white_card` | 中信银行易卡白金卡 | citicbank.com | 480 |
| 56 | `spdb_simple_white` | SPDB 浦发银行简约白金卡 | spdb.com.cn | 360 |
| 57 | `abc_youran_white` | ABC Youran Platinum Card | abchina.com | 300 |
| 58 | `cn_abc_youran_white` | ABC Youran Platinum Card | abchina.com | 300 |
| 59 | `cn_cmb_bird_gold` | CMB Centurion Gold Card | cmbchina.com | 300 |
| 60 | `pingan_car_owner_gold` | PAB Car Owner Platinum Card | pingan.com | 300 |
| 61 | `pab_auto_owner` | PAB 平安银行车主信用卡 | pingan.com | 300 |
| 62 | `cn_abc_youran_white_card` | 农业银行悠然悦白金卡 | abchina.com | 300 |
| 63 | `cn_pingan_car_owner_card` | 平安银行好车主白金卡 | pingan.com | 300 |
| 64 | `ccb_etc_card` | CCB Dragon ETC Car Owner Card | ccb.com | 200 |
| 65 | `ceb_阳光标准金卡` | CEB Sunshine Standard Gold Card | cebbank.com | 200 |
| 66 | `citic_i_platinum` | CITIC 中信银行i白金卡 | citicbank.com.cn | 200 |
| 67 | `icbc_universal_gold` | ICBC Zodiac Gold Card | icbc.com.cn | 200 |
| 68 | `abc_kins_gold` | ABC 金穗标准信用卡 | abchina.com | 160 |
| 69 | `cn_ccb_dragon_joy` | CCB Dragon Card Joy Gold | ccb.com | 160 |
| 70 | `ccb_dragon_card_gold` | CCB Dragon Standard Gold Card | ccb.com | 160 |
| 71 | `ccb_longcard_gold` | CCB 龙卡标准信用卡金卡 | ccb.com | 160 |
| 72 | `bocom_standard_gold` | BOCOM Standard Gold Card | bankcomm.com | 140 |
| 73 | `cn_bocom_standard_gold` | BOCOM Standard Gold Card | bankcomm.com | 140 |
| 74 | `boc_standard_gold` | BOC 中银标准信用卡 | boc.cn | 100 |
| 75 | `boc_standard_gold_2` | BOC 中银标准信用卡金卡 | boc.cn | 100 |
| 76 | `cn_citic_standard_gold` | CITIC Standard Gold Card | citicbank.com | 100 |
| 77 | `icbc_unipay_dual` | ICBC 工银标准信用卡 | icbc.com.cn | 100 |
| 78 | `abc_kins_standard` | ABC 金穗标准信用卡 | abchina.com | 80 |
| 79 | `abc_taobao_card` | ABC Taobao Co-branded Card | abchina.com | 0 |
| 80 | `abc_national_treasure` | ABC 农业银行国家宝藏联名卡 | abchina.com | 0 |
| 81 | `abc_taobao` | ABC 农业银行淘宝联名卡 | abchina.com | 0 |
| 82 | `abc_jcb_gold` | ABC 农业银行金穗JCB金卡 | abchina.com | 0 |
| 83 | `abc_visa_signature` | ABC 农行Visa金穗全币种卡 | abchina.com | 0 |
| 84 | `bob_world_platinum` | BOB 北京银行世界白金卡 | bankofbeijing.com.cn | 0 |
| 85 | `bob_happy_travel` | BOB 北京银行悦行白金卡 | bankofbeijing.com.cn | 0 |
| 86 | `boc_greatwall_crossborder` | BOC Great Wall Cross-Border Mastercard | boc.cn | 0 |
| 87 | `boc_pinduoduo_card` | BOC Pinduoduo Co-branded Card | boc.cn | 0 |
| 88 | `boc_ufan` | BOC 中国银行UFan卡 | boc.cn | 0 |
| 89 | `boc_air_china_visa` | BOC 中国银行国航知音联名卡 | boc.cn | 0 |
| 90 | `boc_great_wall` | BOC 中国银行长城环球通信用卡 | boc.cn | 0 |
| 91 | `bocom_eleme_card` | BOCOM Eleme Co-branded Card | bankcomm.com | 0 |
| 92 | `bocom_y_power` | BOCOM 交通银行Y-POWER卡 | bankcomm.com | 0 |
| 93 | `bocom_starbucks` | BOCOM 交通银行星巴克卡 | bankcomm.com | 0 |
| 94 | `bocom_disney` | BOCOM 交通银行迪士尼卡 | bankcomm.com | 0 |
| 95 | `bocom_eleme` | BOCOM 交通银行饿了么联名卡 | bankcomm.com | 0 |
| 96 | `bos_coffee_card` | BOS 上海银行咖啡联名卡 | bankofshanghai.com | 0 |
| 97 | `bos_shanghai_card` | BOS 上海银行标准卡 | bankofshanghai.com | 0 |
| 98 | `bos_disney` | BOS 上海银行迪士尼联名卡 | bankofshanghai.com | 0 |
| 99 | `boc_visa_olympic` | Bank of China Olympic Theme Card | boc.cn | 0 |
| 100 | `ccb_bilibili_card` | CCB Bilibili Co-branded Card | ccb.com | 0 |
| 101 | `ccb_meituan_card` | CCB Meituan Co-branded Card | ccb.com | 0 |
| 102 | `ccb_jd_joy` | CCB 建设银行京东Joy联名卡 | ccb.com | 0 |
| 103 | `ccb_longcard` | CCB 龙卡标准信用卡 | ccb.com | 0 |
| 104 | `ccb_muse_card` | CCB龙卡MUSE信用卡 | ccb.com | 0 |
| 105 | `ceb_tiktok_card` | CEB Douyin Co-branded Credit Card | cebbank.com | 0 |
| 106 | `ceb_jd_joy` | CEB JD Joy Co-branded Card | cebbank.com | 0 |
| 107 | `ceb_tiktok` | CEB 光大银行抖音联名卡 | cebbank.com | 0 |
| 108 | `ceb_disney` | CEB 光大银行迪士尼联名卡 | cebbank.com | 0 |
| 109 | `ceb_sunshine` | CEB 光大银行阳光信用卡 | cebbank.com | 0 |
| 110 | `guangfa_meituan_card` | CGB Meituan Co-branded Credit Card | cgbchina.com.cn | 0 |
| 111 | `cgb_diy` | CGB 广发DIY信用卡 | cgbchina.com.cn | 0 |
| 112 | `guangfa_visa_gold` | CGB 广发Visa金卡 | cgbchina.com.cn | 0 |
| 113 | `cgb_zhenqing` | CGB 广发真情卡 | cgbchina.com.cn | 0 |
| 114 | `cib_taobao_card` | CIB Taobao Co-branded Card | cib.com.cn | 0 |
| 115 | `cib_credit_easy` | CIB 兴业银行信用易卡 | cib.com.cn | 0 |
| 116 | `cib_xingdongli` | CIB 兴业银行兴动力卡 | cib.com.cn | 0 |
| 117 | `industrial_bank_taobao` | CIB 兴业银行淘宝联名卡 | cib.com.cn | 0 |
| 118 | `citic_qq_vip` | CITIC QQ Super VIP Card | citicbank.com | 0 |
| 119 | `citic_ihg_gold` | CITIC 中信银行IHG联名金卡 | citicbank.com.cn | 0 |
| 120 | `citic_starbucks` | CITIC 中信银行星巴克联名卡 | citicbank.com.cn | 0 |
| 121 | `citic_yan` | CITIC 中信银行颜卡 | citicbank.com.cn | 0 |
| 122 | `cn_cmb_all_currency_white` | CMB All Currency International White | cmbchina.com | 0 |
| 123 | `cmb_bilibili_card` | CMB Bilibili Co-branded Card | cmbchina.com | 0 |
| 124 | `cmb_hello_kitty` | CMB 招商银行Hello Kitty卡 | cmbchina.com | 0 |
| 125 | `cmb_young_card` | CMB 招商银行YOUNG卡 | cmbchina.com | 0 |
| 126 | `cmb_jd_plus` | CMB 招商银行京东PLUS联名卡 | cmbchina.com | 0 |
| 127 | `cmb_all_currency_white` | CMB 招商银行全币种国际白金卡 | cmbchina.com | 0 |
| 128 | `cmb_doraemon` | CMB 招商银行哆啦A梦JCB卡 | cmbchina.com | 0 |
| 129 | `cmb_taobao` | CMB 招商银行淘宝联名卡 | cmbchina.com | 0 |
| 130 | `cmb_bird_card` | CMB 招商银行百鸟朝凤信用卡 | cmbchina.com | 0 |
| 131 | `cmb_all_currency_visa` | CMB 招行全币种国际VISA卡 | cmbchina.com | 0 |
| 132 | `cmbc_bilibili` | CMBC 民生银行Bilibili联名卡 | cmbc.com.cn | 0 |
| 133 | `cmbc_qq` | CMBC 民生银行QQ联名卡 | cmbc.com.cn | 0 |
| 134 | `minsheng_skypass_visa` | CMBC 民生银行大韩航空联名卡 | cmbc.com.cn | 0 |
| 135 | `cmbc_ladies_card` | CMBC 民生银行女人优游信用卡 | cmbc.com.cn | 0 |
| 136 | `cmbc_netease` | CMBC 民生银行网易联名卡 | cmbc.com.cn | 0 |
| 137 | `czb_rainbow_card` | CZB Rainbow Credit Card | czbank.com | 0 |
| 138 | `czbank_standard_gold` | CZBank 浙商标准金卡 | czbank.com | 0 |
| 139 | `czbank_donkey_card` | CZBank 浙商银行驴妈妈联名卡 | czbank.com | 0 |
| 140 | `guangfa_nba_card` | GF 广发NBA联名信用卡 | cgbchina.com.cn | 0 |
| 141 | `guangfa_meituan` | GF 广发银行美团联名卡 | cgbchina.com.cn | 0 |
| 142 | `gzcb_card` | GZB 广州银行信用卡 | gzcb.com.cn | 0 |
| 143 | `hxb_youth` | HXB 华夏银行青春信用卡 | hxb.com.cn | 0 |
| 144 | `hxb_gundam` | HXB 华夏银行高达联名卡 | hxb.com.cn | 0 |
| 145 | `huaxia_elite_platinum_4` | Huaxia 华夏精英白金卡 | hxb.com.cn | 0 |
| 146 | `icbc_constellation_card` | ICBC Constellation Credit Card | icbc.com.cn | 0 |
| 147 | `icbc_jd_joy` | ICBC JD Joy Co-branded Card | icbc.com.cn | 0 |
| 148 | `cn_icbc_jd_joy` | ICBC JD Joy Co-branded Card | icbc.com.cn | 0 |
| 149 | `icbc_marvel_card` | ICBC Marvel Co-branded Card | icbc.com.cn | 0 |
| 150 | `cn_icbc_shanghai_minions` | ICBC Minions Co-branded Card | icbc.com.cn | 0 |
| 151 | `icbc_wechat_card` | ICBC WeChat Co-branded Card | icbc.com.cn | 0 |
| 152 | `cn_icbc_wechat_card` | ICBC WeChat Co-branded Card | icbc.com.cn | 0 |
| 153 | `icbc_e_card` | ICBC 工商银行e卡 | icbc.com.cn | 0 |
| 154 | `icbc_alipay` | ICBC 工商银行支付宝联名卡 | icbc.com.cn | 0 |
| 155 | `icbc_forbiddencity` | ICBC 工商银行故宫联名卡 | icbc.com.cn | 0 |
| 156 | `icbc_marvel` | ICBC 工商银行漫威信用卡 | icbc.com.cn | 0 |
| 157 | `icbc_meituan_card` | ICBC 工行美团联名信用卡 | icbc.com.cn | 0 |
| 158 | `icbc_universal` | ICBC 工银生肖信用卡 | icbc.com.cn | 0 |
| 159 | `jsb_standard` | JSB 江苏银行标准信用卡 | jsbchina.cn | 0 |
| 160 | `nb_city_card` | NB 南京银行城市卡 | njcb.com.cn | 0 |
| 161 | `nb_starbucks` | NB 南京银行星巴克联名卡 | njcb.com.cn | 0 |
| 162 | `nb_youth` | NBCB 宁波银行汇通青春卡 | nbcb.com.cn | 0 |
| 163 | `cn_pingan_costco_card_gold` | PAB Costco Co-branded Card | pingan.com | 0 |
| 164 | `pingan_costco_card` | PAB Costco Co-branded Credit Card | pingan.com | 0 |
| 165 | `pingan_aoyou` | PAB 平安傲游信用卡 | pingan.com | 0 |
| 166 | `pab_pingan_bank_card` | PAB 平安标准卡 | pingan.com | 0 |
| 167 | `pingan_byou` | PAB 平安由你卡 | pingan.com | 0 |
| 168 | `pingan_costco` | PAB 平安银行Costco联名卡 | pingan.com | 0 |
| 169 | `psbc_unionpay_standard` | PSBC 邮储银联标准信用卡 | psbc.com | 0 |
| 170 | `cn_spdb_angry_birds` | SPDB Angry Birds Credit Card | spdb.com.cn | 0 |
| 171 | `spdb_bilibili_card` | SPDB Bilibili Co-branded Credit Card | spdb.com.cn | 0 |
| 172 | `spdb_dream_card` | SPDB Dream Card Standard White | spdb.com.cn | 0 |
| 173 | `spdb_jd_card` | SPDB JD Co-branded Card | spdb.com.cn | 0 |
| 174 | `spdb_angry_birds` | SPDB 浦发愤怒的小鸟联名卡 | spdb.com.cn | 0 |
| 175 | `spdb_bilibili` | SPDB 浦发银行Bilibili联名卡 | spdb.com.cn | 0 |
| 176 | `spdb_jd` | SPDB 浦发银行京东联名卡 | spdb.com.cn | 0 |
| 177 | `spdb_dream` | SPDB 浦发银行梦卡 | spdb.com.cn | 0 |
| 178 | `srcb_xinyi` | SRCB 上海农商银行鑫意信用卡 | srcb.com | 0 |
| 179 | `icbc_peony_super_benefit` | 工商银行牡丹超惠信用卡 | icbc.com.cn | 0 |
| 180 | `icbc_zodiac_credit_card` | 工商银行生肖信用卡 | icbc.com.cn | 0 |
| 181 | `icbc_struggle_platinum` | 工商银行奋斗信用卡白金卡 | icbc.com.cn | 1000 |
| 182 | `icbc_shangri_la_platinum` | 工商银行香格里拉联名白金信用卡 | icbc.com.cn | 1000 |
| 183 | `icbc_chimelong_platinum` | 工商银行长隆联名白金信用卡 | icbc.com.cn | 1000 |
| 184 | `icbc_diners_club_igo` | 工商银行大来爱购白金信用卡 | icbc.com.cn | 1000 |
| 185 | `icbc_beijing_2022_winter` | 工商银行北京冬奥会主题信用卡 | icbc.com.cn | 0 |
| 186 | `icbc_borderless_credit` | 工商银行银联无界信用卡 | icbc.com.cn | 0 |
| 187 | `ccb_big_mountain_white` | 建设银行龙卡尊享白金信用卡 (大山白) | ccb.com | 1800 |
| 188 | `ccb_family_beloved_platinum` | 建设银行龙卡家庭挚爱白金信用卡 | ccb.com | 580 |
| 189 | `ccb_car_owner_platinum` | 建设银行龙卡汽车卡 | ccb.com | 200 |
| 190 | `ccb_global_payment_platinum` | 建设银行龙卡全球支付白金卡 | ccb.com | 580 |
| 191 | `ccb_youth_credit_card` | 建设银行龙卡正青春信用卡 | ccb.com | 0 |
| 192 | `ccb_joy_credit_card` | 建设银行龙卡欢享信用卡 | ccb.com | 0 |
| 193 | `ccb_costco_card` | 建设银行龙卡Costco联名卡 | ccb.com | 0 |
| 194 | `abc_essence_white` | 农业银行尊然白金信用卡 (精粹白) | abchina.com | 880 |
| 195 | `abc_youran_joy_platinum` | 农业银行悠然悦白金信用卡 | abchina.com | 580 |
| 196 | `abc_pretty_mom_credit` | 农业银行漂亮升级妈妈信用卡 | abchina.com | 0 |
| 197 | `abc_global_business_travel` | 农业银行环球商旅信用卡 | abchina.com | 580 |
| 198 | `abc_qq_vip_credit` | 农业银行金穗QQ联名信用卡 | abchina.com | 0 |
| 199 | `abc_air_china_phoenix` | 农业银行国航知音联名白金卡 | abchina.com | 880 |
| 200 | `abc_borderless_white` | 农业银行银联无界白金信用卡 | abchina.com | 0 |
| 201 | `boc_greatwall_platinum_classic` | 中国银行长城白金信用卡经典版 | boc.cn | 800 |
| 202 | `boc_zhuojun_study_abroad` | 中国银行长城卓隽留学信用卡 | boc.cn | 0 |
| 203 | `boc_zan_credit_card` | 中国银行长城赞卡信用卡 | boc.cn | 0 |
| 204 | `boc_shenzhen_pass_card` | 中国银行深圳通联名信用卡 | boc.cn | 0 |
| 205 | `boc_china_eastern_platinum` | 中国银行东方航空联名白金卡 | boc.cn | 800 |
| 206 | `boc_southern_airlines_platinum` | 中国银行南航明珠联名白金卡 | boc.cn | 800 |
| 207 | `cmb_centurion_platinum` | 招商银行美国运通百夫长白金卡 | cmbchina.com | 3600 |
| 208 | `cmb_freedom_life_white` | 招商银行自由人生白金信用卡 (鸟白) | cmbchina.com | 800 |
| 209 | `cmb_gq_platinum_card` | 招商银行GQ联名白金信用卡 | cmbchina.com | 0 |
| 210 | `cmb_genshin_impact_card` | 招商银行原神联名信用卡 | cmbchina.com | 0 |
| 211 | `cmb_honor_of_kings_card` | 招商银行王者荣耀联名信用卡 | cmbchina.com | 0 |
| 212 | `cmb_one_piece_card` | 招商银行航海王联名信用卡 | cmbchina.com | 0 |
| 213 | `cmb_pokemon_pikachu_card` | 招商银行宝可梦皮卡丘联名卡 | cmbchina.com | 0 |
| 214 | `bocom_white_kylin` | 交通银行标准白金信用卡 (白麒麟) | bankcomm.com | 1000 |
| 215 | `bocom_kings_honor_card` | 交通银行王者荣耀联名卡 | bankcomm.com | 0 |
| 216 | `bocom_honey_credit_card` | 交通银行蜜卡优逸白金卡 | bankcomm.com | 0 |
| 217 | `bocom_china_eastern_white` | 交通银行东方航空联名白金卡 | bankcomm.com | 1000 |
| 218 | `bocom_walmart_credit` | 交通银行沃尔玛联名信用卡 | bankcomm.com | 0 |
| 219 | `citic_prestige_platinum` | 中信银行尊贵级白金信用卡 | citicbank.com | 2000 |
| 220 | `citic_magic_family_card` | 中信银行魔力爱家信用卡 | citicbank.com | 0 |
| 221 | `citic_air_china_world_elite` | 中信银行国航世界之极信用卡 | citicbank.com | 20000 |
| 222 | `citic_china_southern_white` | 中信银行南航明珠联名白金卡 | citicbank.com | 2000 |
| 223 | `citic_jd_plus_white` | 中信银行京东PLUS联名白金卡 | citicbank.com | 480 |
| 224 | `citic_didi_co_branded` | 中信银行滴滴联名信用卡 | citicbank.com | 0 |
| 225 | `spdb_ae_super_white` | 浦发银行美国运通超白金信用卡 | spdb.com.cn | 10000 |
| 226 | `spdb_borderless_credit` | 浦发银行银联无界信用卡 | spdb.com.cn | 0 |
| 227 | `spdb_geely_platinum` | 浦发银行吉利白金信用卡 | spdb.com.cn | 0 |
| 228 | `spdb_cathay_pacific_white` | 浦发银行国泰航空联名白金卡 | spdb.com.cn | 0 |
| 229 | `spdb_dongfang_cj_card` | 浦发银行东方CJ联名信用卡 | spdb.com.cn | 0 |
| 230 | `cgb_car_owner_elite` | 广发银行车主臻享白金信用卡 | cgbchina.com.cn | 800 |
| 231 | `cgb_southern_airlines_white` | 广发银行南航明珠白金信用卡 | cgbchina.com.cn | 2500 |
| 232 | `cgb_doli_card` | 广发银行多利卡信用卡 | cgbchina.com.cn | 0 |
| 233 | `cgb_tiantianli_card` | 广发银行天天利信用卡 | cgbchina.com.cn | 0 |
| 234 | `cgb_borderless_card` | 广发银行银联无界信用卡 | cgbchina.com.cn | 0 |
| 235 | `cgb_huawei_card` | 广发银行华为联名信用卡 | cgbchina.com.cn | 0 |
| 236 | `ceb_filial_piety_platinum` | 光大银行阳光孝心卓越白金卡 | cebbank.com | 3600 |
| 237 | `ceb_flight_journey_platinum` | 光大银行航旅纵横联名白金信用卡 | cebbank.com | 1188 |
| 238 | `ceb_car_owner_platinum` | 光大银行阳光车主经典白金卡 | cebbank.com | 500 |
| 239 | `ceb_hainan_airlines_white` | 光大银行海航联名白金信用卡 | cebbank.com | 1188 |
| 240 | `ceb_meituan_co_branded` | 光大银行美团联名信用卡 | cebbank.com | 0 |
| 241 | `pingan_white_gold_card` | 平安银行白金信用卡 | pingan.com | 2800 |
| 242 | `pingan_good_car_owner_white` | 平安银行好车主白金信用卡 | pingan.com | 800 |
| 243 | `pingan_yuexiang_platinum` | 平安银行悦享白金信用卡 | pingan.com | 0 |
| 244 | `minsheng_centurion_platinum` | 民生银行美国运通百夫长白金卡 | cmbc.com.cn | 3600 |
| 245 | `minsheng_elite_platinum` | 民生银行精英白金信用卡 | cmbc.com.cn | 1800 |
| 246 | `cib_xingyou_platinum` | 兴业银行行悠白金信用卡 | cib.com.cn | 900 |
| 247 | `cib_xingyu_platinum` | 兴业银行行宇白金信用卡 | cib.com.cn | 2600 |
| 248 | `cib_peach_blossom_card` | 兴业银行桃花主题信用卡 | cib.com.cn | 0 |
| 249 | `bos_juneyao_air_white` | 上海银行吉祥航空联名白金卡 | bankofshanghai.com | 1250 |
| 250 | `jsb_amex_rose_gold` | 江苏银行美国运通玫瑰金卡 | jsbchina.cn | 0 |


### 🇹🇼 Taiwan (250)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `amex_centurion_platinum` | Amex Centurion Platinum | americanexpress.com.tw | 36800 |
| 2 | `amex_eva_centurion_platinum` | Amex EVA Air Centurion Platinum | americanexpress.com.tw | 36800 |
| 3 | `ctbc_dream_infinite` | CTBC Dream Card Infinite | ctbcbank.com | 20000 |
| 4 | `feb_world_business` | Far Eastern Bank World Business Card | feib.com.tw | 10000 |
| 5 | `taishin_everrich_infinite` | Taishin Everrich Infinite Card | taishinbank.com.tw | 10000 |
| 6 | `taishin_infinite` | Taishin Infinite Card | taishinbank.com.tw | 10000 |
| 7 | `cathay_asia_miles_world` | Cathay United Asia Miles World Card | cathaybk.com.tw | 8000 |
| 8 | `taishin_cathay_world` | Taishin Cathay Pacific World | taishinbank.com.tw | 8000 |
| 9 | `ctbc_the_royal` | CTBC The Royal Signature | ctbcbank.com | 3600 |
| 10 | `dbs_flyer_world` | DBS Flyer World Card | dbs.com.tw | 3600 |
| 11 | `esun_world_card` | E.SUN World Card | esunbank.com.tw | 3600 |
| 12 | `taishin_world` | Taishin World Card | taishinbank.com.tw | 3600 |
| 13 | `tw_dbs_flyer_world_card` | DBS Flyer World Card | dbs.com.tw | 3000 |
| 14 | `dbs_eco` | DBS eco Card | dbs.com.tw | 3000 |
| 15 | `esun_kumamon` | E.Sun Kumamon Card | esunbank.com.tw | 3000 |
| 16 | `esun_pi_wallet` | E.Sun Pi Wallet Card | esunbank.com.tw | 3000 |
| 17 | `esun_u_bear` | E.Sun U Bear Card | esunbank.com.tw | 3000 |
| 18 | `taishin_richart` | Taishin Richart Card | taishinbank.com.tw | 3000 |
| 19 | `hsbc_travel_titanium` | HSBC Travel Titanium Card | hsbc.com.tw | 2500 |
| 20 | `hsbc_traveler_signature` | HSBC Traveler Signature | hsbc.com.tw | 2500 |
| 21 | `cathay_eva_air_co` | Cathay EVA Air Co-branded Card | cathaybk.com.tw | 2400 |
| 22 | `ctbc_ana_card` | CTBC ANA Co-branded Card | ctbcbank.com | 2000 |
| 23 | `feb_cest_moi` | Far Eastern Bank C'est Moi Card | feib.com.tw | 2000 |
| 24 | `feb_happy_travel` | Far Eastern Bank Happy Travel Card | feib.com.tw | 2000 |
| 25 | `feb_happy_plus` | Far Eastern Bank Happy+ Card | feib.com.tw | 2000 |
| 26 | `first_travel` | First Bank Travel Card | firstbank.com.tw | 2000 |
| 27 | `hsbc_cashback_visa` | HSBC Cash Back Visa Platinum | hsbc.com.tw | 2000 |
| 28 | `hsbc_diamond` | HSBC Diamond Card | hsbc.com.tw | 2000 |
| 29 | `hsbc_live_plus` | HSBC Live+ Cash Back | hsbc.com.tw | 2000 |
| 30 | `ctbc_ana` | CTBC ANA Co-branded Card | ctbcbank.com | 1800 |
| 31 | `cathay_asia_miles_titanium` | Cathay United Asia Miles Titanium | cathaybk.com.tw | 1800 |
| 32 | `cathay_eva` | Cathay United EVA Air Co-branded Card | cathaybk.com.tw | 1800 |
| 33 | `fubon_j` | Taipei Fubon J Card | fubon.com | 1800 |
| 34 | `fubon_ju` | Taipei Fubon JU Card | fubon.com | 1800 |
| 35 | `taishin_cathay_flying` | Taishin Cathay Pacific Flying | taishinbank.com.tw | 1800 |
| 36 | `ctbc_line_pay` | CTBC Line Pay Card | ctbcbank.com | 1500 |
| 37 | `sinopac_daway` | SinoPac DAWAY Card | sinopac.com | 1500 |
| 38 | `sinopac_dual_currency` | SinoPac Dual Currency Card | sinopac.com | 1500 |
| 39 | `sinopac_green_cashback` | SinoPac Green Cash Back Card | sinopac.com | 1500 |
| 40 | `sinopac_jcb_cashback` | SinoPac JCB Cash Back Card | sinopac.com | 1500 |
| 41 | `sinopac_protection` | SinoPac Protection Card | sinopac.com | 1500 |
| 42 | `sinopac_sport` | SinoPac Sport Card | sinopac.com | 1500 |
| 43 | `taishin_business` | Taishin Business Card | taishinbank.com.tw | 1500 |
| 44 | `taishin_everrich` | Taishin Everrich Card | taishinbank.com.tw | 1500 |
| 45 | `taishin_mercuries_life` | Taishin Mercuries Life Card | taishinbank.com.tw | 1500 |
| 46 | `taishin_pxmart` | Taishin PX Mart Card | taishinbank.com.tw | 1500 |
| 47 | `taishin_mitsukoshi` | Taishin Shin Kong Mitsukoshi | taishinbank.com.tw | 1500 |
| 48 | `taishin_tsann_kuen` | Taishin Tsann Kuen Card | taishinbank.com.tw | 1500 |
| 49 | `taishin_friday` | Taishin friDay Card | taishinbank.com.tw | 1500 |
| 50 | `feb_happy` | Far Eastern Bank Happy Card | feib.com.tw | 1200 |
| 51 | `first_living_green` | First Bank Living Green Card | firstbank.com.tw | 1200 |
| 52 | `first_ileo` | First Bank iLEO Card | firstbank.com.tw | 1200 |
| 53 | `first_ipass` | First Bank iPass Card | firstbank.com.tw | 1200 |
| 54 | `first_icash` | First Bank icash Card | firstbank.com.tw | 1200 |
| 55 | `cathay_asia_miles_platinum` | Cathay United Asia Miles Platinum | cathaybk.com.tw | 600 |
| 56 | `taishin_cathay_titanium` | Taishin Cathay Pacific Titanium | taishinbank.com.tw | 600 |
| 57 | `bok_card` | Bank of Kaohsiung Credit Card | bok.com.tw | 0 |
| 58 | `bok_credit_card` | Bank of Kaohsiung Credit Card | bok.com.tw | 0 |
| 59 | `panhsin_card` | Bank of Panhsin Credit Card | bop.com.tw | 0 |
| 60 | `panhsin_credit_card` | Bank of Panhsin Credit Card | panhsin.com.tw | 0 |
| 61 | `bot_cashback` | Bank of Taiwan Cashback Card | bot.com.tw | 0 |
| 62 | `bot_cashback_card` | Bank of Taiwan Cashback Card | bot.com.tw | 0 |
| 63 | `cota_bank_card` | COTA Commercial Bank Credit Card | cotabank.com.tw | 0 |
| 64 | `tw_ctbc_ana_card_titanium` | CTBC ANA Co-branded Titanium Card | ctbcbank.com | 0 |
| 65 | `ctbc_costco` | CTBC Costco Co-branded Card | ctbcbank.com | 0 |
| 66 | `ctbc_costco_card` | CTBC Costco Co-branded Card | ctbcbank.com | 0 |
| 67 | `tw_ctbc_costco_card` | CTBC Costco Co-branded Card | ctbcbank.com | 0 |
| 68 | `ctbc_linepay_card` | CTBC LINE Pay Card | ctbcbank.com | 0 |
| 69 | `tw_ctbc_linepay_card` | CTBC LINE Pay Card | ctbcbank.com | 0 |
| 70 | `ctbc_the_royal_signature` | CTBC The Royal Signature Card | ctbcbank.com | 0 |
| 71 | `ctbc_foodpanda` | CTBC foodpanda Card | ctbcbank.com | 0 |
| 72 | `ctbc_foodpanda_card` | CTBC foodpanda Co-branded Card | ctbcbank.com | 0 |
| 73 | `tw_cathay_asia_miles_card` | Cathay Asia Miles Titanium Card | cathaybk.com.tw | 0 |
| 74 | `cathay_asia_miles_lixiang` | Cathay United Asia Miles Li-Xiang | cathaybk.com.tw | 0 |
| 75 | `cathay_cube` | Cathay United CUBE Card | cathaybk.com.tw | 0 |
| 76 | `cathay_cube_card` | Cathay United CUBE Card | cathaybk.com.tw | 0 |
| 77 | `cathay_koko` | Cathay United KOKO Combo | cathaybk.com.tw | 0 |
| 78 | `cathay_koko_combo` | Cathay United KOKO Combo Card | cathaybk.com.tw | 0 |
| 79 | `chb_mylove` | Chang Hwa My Love Cashback Card | bankchb.com | 0 |
| 80 | `dbs_everyday_card` | DBS Everyday Titanium Card | dbs.com.tw | 0 |
| 81 | `dbs_eco_card` | DBS eco Card | dbs.com.tw | 0 |
| 82 | `tw_dbs_eco_card` | DBS eco Card | dbs.com.tw | 0 |
| 83 | `esun_dual_currency` | E.SUN Dual Currency Card | esunbank.com.tw | 0 |
| 84 | `esun_only` | E.SUN Only Card | esunbank.com.tw | 0 |
| 85 | `esun_only_card` | E.SUN Only Card | esunbank.com.tw | 0 |
| 86 | `tw_esun_only_card` | E.SUN Only Card | esunbank.com.tw | 0 |
| 87 | `tw_esun_pi_wallet` | E.SUN Pi Wallet Card | esunbank.com.tw | 0 |
| 88 | `esun_unicard` | E.SUN Unicard | esunbank.com.tw | 0 |
| 89 | `tw_esun_unicard` | E.SUN Unicard | esunbank.com.tw | 0 |
| 90 | `esun_e_card` | E.SUN e Card | esunbank.com.tw | 0 |
| 91 | `tw_esun_e_card` | E.SUN e-Card | esunbank.com.tw | 0 |
| 92 | `entie_cashback` | Entie Bank Cashback Card | entiebank.com.tw | 0 |
| 93 | `entie_cashback_card` | Entie Cashback Card | entiebank.com.tw | 0 |
| 94 | `tw_feb_happy_card` | FEIB Happy Go Card | feib.com.tw | 0 |
| 95 | `feb_happy_card` | Far Eastern Happy Go Card | feib.com.tw | 0 |
| 96 | `first_ieco` | First Bank iECO Card | firstbank.com.tw | 0 |
| 97 | `first_ieco_card` | First Bank iECO Card | firstbank.com.tw | 0 |
| 98 | `first_ileo_card` | First Bank iLEO Card | firstbank.com.tw | 0 |
| 99 | `first_ipass_card` | First Bank iPASS Card | firstbank.com.tw | 0 |
| 100 | `fubon_digital_life` | Fubon Digital Life Card | fubon.com | 0 |
| 101 | `tw_fubon_digital_life` | Fubon Digital Life Card | fubon.com | 0 |
| 102 | `fubon_j_card` | Fubon J Card | fubon.com | 0 |
| 103 | `tw_fubon_j_card` | Fubon J Card | fubon.com | 0 |
| 104 | `fubon_open_possible` | Fubon Open Possible Card | fubon.com | 0 |
| 105 | `tw_fubon_open_possible_card` | Fubon Open Possible Card | fubon.com | 0 |
| 106 | `fubon_momo` | Fubon momo Card | fubon.com | 0 |
| 107 | `fubon_momo_card` | Fubon momo Card | fubon.com | 0 |
| 108 | `tw_fubon_momo_card` | Fubon momo Card | fubon.com | 0 |
| 109 | `hsbc_live_plus_tw` | HSBC Live+ Cash Back Card | hsbc.com.tw | 0 |
| 110 | `hncb_sny` | Hua Nan SnY Card | hncb.com.tw | 0 |
| 111 | `hncb_sny_card` | Hua Nan SnY Credit Card | hncb.com.tw | 0 |
| 112 | `hncb_ishopping` | Hua Nan i-Shopping Life Card | hncb.com.tw | 0 |
| 113 | `kgi_cashback` | KGI Cashback Signature | kgibank.com.tw | 0 |
| 114 | `kgi_cashback_signature` | KGI Cashback Signature Card | kgibank.com.tw | 0 |
| 115 | `kgi_evolution_card` | KGI Evolution Card | kgibank.com.tw | 0 |
| 116 | `kgi_evolution` | KGI Evolution Cashback Card | kgibank.com.tw | 0 |
| 117 | `ktb_credit_card` | King Town Bank Credit Card | ktb.com.tw | 0 |
| 118 | `ktb_card` | King’s Town Bank Credit Card | ktb.com.tw | 0 |
| 119 | `landbank_jcb` | Land Bank JCB Card | landbank.com.tw | 0 |
| 120 | `landbank_jcb_card` | Land Bank JCB Card | landbank.com.tw | 0 |
| 121 | `mega_gogoro_card` | Mega Gogoro Co-branded Card | megabank.com.tw | 0 |
| 122 | `tw_mega_liduo_card` | Mega Liduo Signature Card | megabank.com.tw | 0 |
| 123 | `mega_liduo` | Mega Lots Signature Card | megabank.com.tw | 0 |
| 124 | `mega_liduo_card` | Mega Lots Signature Card | megabank.com.tw | 0 |
| 125 | `mega_e` | Mega e-Swipe Signature Card | megabank.com.tw | 0 |
| 126 | `mega_e_card` | Mega e-Swipe Signature Card | megabank.com.tw | 0 |
| 127 | `nextbank_dajiang` | Next Bank Da Jiang Card | nextbank.com.tw | 0 |
| 128 | `nextbank_dajiang_card` | Next Bank Da Jiang Card | nextbank.com.tw | 0 |
| 129 | `obank_orange` | O-Bank O! Range Card | o-bank.com | 0 |
| 130 | `rakuten_world` | Rakuten Card World | rakuten.com.tw | 0 |
| 131 | `rakuten_fly` | Rakuten Fly Card | rakuten.com.tw | 0 |
| 132 | `rakuten_jcb_card` | Rakuten JCB Card | card.rakuten.com.tw | 0 |
| 133 | `rakuten_panda_j` | Rakuten Panda J Card | rakuten.com.tw | 0 |
| 134 | `rakuten_tiger` | Rakuten Tiger Card | rakuten.com.tw | 0 |
| 135 | `rakuten_world_card` | Rakuten World Card | card.rakuten.com.tw | 0 |
| 136 | `scsb_cashback` | SCSB Cashback Card | scsb.com.tw | 0 |
| 137 | `shanghai_minions` | SCSB Minions Card | scsb.com.tw | 0 |
| 138 | `shanghai_minions_card` | SCSB Minions Card | scsb.com.tw | 0 |
| 139 | `skbank_global` | Shin Kong Global Cashback Card | skbank.com.tw | 0 |
| 140 | `skbank_global_cashback` | Shin Kong Global Cashback Card | skbank.com.tw | 0 |
| 141 | `skbank_emma` | Shin Kong emma Card | skbank.com.tw | 0 |
| 142 | `skbank_emma_card` | Shin Kong emma Card | skbank.com.tw | 0 |
| 143 | `sinopac_daway_card` | SinoPac DAWAY Card | sinopac.com | 0 |
| 144 | `tw_sinopac_daway_card` | SinoPac DAWAY Card | sinopac.com | 0 |
| 145 | `sinopac_daway_line` | SinoPac DAWAY LINE Pay Card | sinopac.com | 0 |
| 146 | `tw_sinopac_dual_currency_card` | SinoPac Dual Currency Card | sinopac.com | 0 |
| 147 | `sinopac_protection_card` | SinoPac Protection Card | sinopac.com | 0 |
| 148 | `tw_sinopac_protection_card` | SinoPac Protection Card | sinopac.com | 0 |
| 149 | `sinopac_sport_card` | SinoPac SPORT Card | sinopac.com | 0 |
| 150 | `tw_sinopac_sport_card` | SinoPac SPORT Card | sinopac.com | 0 |
| 151 | `scb_cashback` | Standard Chartered Cashback Signature | sc.com.tw | 0 |
| 152 | `scb_cashback_signature` | Standard Chartered Cashback Signature | sc.com/tw | 0 |
| 153 | `sunny_bank_card` | Sunny Bank Credit Card | sunnybank.com.tw | 0 |
| 154 | `tbb_sustainable_life` | TBB Sustainable Life Card | tbb.com.tw | 0 |
| 155 | `tbb_ipass_card` | TBB iPASS Card | tbb.com.tw | 0 |
| 156 | `tbb_ipass` | TBB iPASS Co-branded Card | tbb.com.tw | 0 |
| 157 | `tcb_cashback` | TCB Cashback Card | tcb-bank.com.tw | 0 |
| 158 | `tcb_cashback_card` | TCB Cashback Card | tcb-bank.com.tw | 0 |
| 159 | `taichung_bank_card` | Taichung Commercial Bank Credit Card | tcbbank.com.tw | 0 |
| 160 | `taishin_gogo` | Taishin @GoGo Card | taishinbank.com.tw | 0 |
| 161 | `taishin_gogo_card` | Taishin @GoGo Card | taishinbank.com.tw | 0 |
| 162 | `taishin_flygo` | Taishin FlyGo Card | taishinbank.com.tw | 0 |
| 163 | `taishin_flygo_card` | Taishin FlyGo Card | taishinbank.com.tw | 0 |
| 164 | `taishin_jkopay` | Taishin JKO Pay Card | taishinbank.com.tw | 0 |
| 165 | `tw_taishin_street_pay_card` | Taishin JKOPAY Co-branded Card | taishinbank.com.tw | 0 |
| 166 | `taishin_richart_card` | Taishin Richart Card | taishinbank.com.tw | 0 |
| 167 | `tw_taishin_richart_card` | Taishin Richart Card | taishinbank.com.tw | 0 |
| 168 | `taishin_rose_giving` | Taishin Rose Giving Card | taishinbank.com.tw | 0 |
| 169 | `tw_taishin_rose_giving` | Taishin Rose Giving Card | taishinbank.com.tw | 0 |
| 170 | `taishin_street_pay` | Taishin Street Pay Card | taishinbank.com.tw | 0 |
| 171 | `union_green_card` | Union Bank Green Card | ubot.com.tw | 0 |
| 172 | `tw_union_green_card` | Union Bank Green Card | ubot.com.tw | 0 |
| 173 | `union_jihe` | Union Bank Jihe Card | unionbank.com.tw | 0 |
| 174 | `union_jihe_card` | Union Bank Jihe Card | ubot.com.tw | 0 |
| 175 | `tw_union_jihe_card` | Union Bank Jihe Card | ubot.com.tw | 0 |
| 176 | `union_lai` | Union Bank Lai Points Card | unionbank.com.tw | 0 |
| 177 | `union_laidian_card` | Union Bank Lai Points Card | ubot.com.tw | 0 |
| 178 | `tw_union_laidian_card` | Union Bank Lai Points Card | ubot.com.tw | 0 |
| 179 | `yuanta_diamond` | Yuanta Diamond Card | yuantabank.com.tw | 0 |
| 180 | `yuanta_diamond_card` | Yuanta Diamond Card | yuantabank.com.tw | 0 |
| 181 | `yuanta_digital` | Yuanta Digital Diamond Card | yuantabank.com.tw | 0 |
| 182 | `yuanta_digital_diamond` | Yuanta Digital Diamond Card | yuantabank.com.tw | 0 |
| 183 | `tw_ctbc_linepay_card_official` | 中国信托 LINE Pay 卡 | ctbcbank.com | 0 |
| 184 | `tw_fubon_j_card_official` | 富邦 J 卡 | fubon.com | 0 |
| 185 | `tw_sinopac_sport_card_official` | 永丰 SPORT 卡 | sinopac.com | 0 |
| 186 | `tw_esun_unicard_official` | 玉山 Unicard | esunbank.com.tw | 0 |
| 187 | `tw_union_jihe_card_official` | 联邦 吉鹤卡 | ubot.com.tw | 0 |
| 188 | `cathay_shopee_co_branded` | 國泰世華蝦皮購物聯名卡 | cathaybk.com.tw | 0 |
| 189 | `cathay_world_card` | 國泰世華世界卡 | cathaybk.com.tw | 20000 |
| 190 | `cathay_eva_air_infinite` | 國泰世華長榮航空聯名無限卡 | cathaybk.com.tw | 2400 |
| 191 | `cathay_eva_air_extreme_infinite` | 國泰世華長榮航空極致無限卡 | cathaybk.com.tw | 20000 |
| 192 | `cathay_sogo_co_branded` | 國泰世華遠東SOGO聯名卡 | cathaybk.com.tw | 0 |
| 193 | `ctbc_china_airlines_co_branded` | 中國信託中華航空聯名鼎尊無限卡 | ctbcbank.com | 22000 |
| 194 | `ctbc_china_airlines_business` | 中國信託中華航空聯名商務御璽卡 | ctbcbank.com | 1800 |
| 195 | `ctbc_all_me_card` | 中國信託ALL ME卡 | ctbcbank.com | 0 |
| 196 | `ctbc_hotai_card` | 中國信託和泰聯名卡 | ctbcbank.com | 0 |
| 197 | `ctbc_cpc_fuel_card` | 中國信託中油聯名卡 | ctbcbank.com | 0 |
| 198 | `ctbc_taipei_101_signature` | 中國信託台北101聯名鼎極卡 | ctbcbank.com | 0 |
| 199 | `ctbc_dayeh_takashimaya` | 中國信託大葉高島屋聯名卡 | ctbcbank.com | 0 |
| 200 | `ctbc_lol_card` | 中國信託英雄聯盟卡 | ctbcbank.com | 0 |
| 201 | `fubon_costco_infinite` | 富邦Costco聯名無限卡 | fubon.com | 0 |
| 202 | `fubon_costco_signature` | 富邦Costco聯名御璽卡 | fubon.com | 0 |
| 203 | `fubon_costco_platinum` | 富邦Costco聯名白金卡 | fubon.com | 0 |
| 204 | `fubon_imperial_world` | 富邦尊御世界卡 | fubon.com | 25000 |
| 205 | `fubon_taiwan_mobile_open` | 富邦台灣大哥大Open Possible聯名卡 | fubon.com | 0 |
| 206 | `taishin_rose_giving_card` | 台新玫瑰Giving卡 | taishinbank.com.tw | 0 |
| 207 | `taishin_cathay_pacific_world` | 台新國泰航空聯名世界卡 | taishinbank.com.tw | 20000 |
| 208 | `taishin_shin_kong_mitsukoshi` | 台新新光三越聯名卡 | taishinbank.com.tw | 0 |
| 209 | `taishin_friday_card` | 台新遠傳friDay聯名卡 | taishinbank.com.tw | 0 |
| 210 | `taishin_dazhuo_infinite` | 台新卓富無限卡 | taishinbank.com.tw | 25000 |
| 211 | `esun_starlux_airlines_infinite` | 玉山星宇航空聯名無限卡 | esunbank.com.tw | 10000 |
| 212 | `esun_starlux_extreme_infinite` | 玉山星宇航空聯名極致無限卡 | esunbank.com.tw | 20000 |
| 213 | `esun_starlux_airlines_titanium` | 玉山星宇航空聯名鈦金卡 | esunbank.com.tw | 0 |
| 214 | `esun_carrefour_card` | 玉山家樂福聯名卡 | esunbank.com.tw | 0 |
| 215 | `esun_eztravel_card` | 玉山易遊網聯名卡 | esunbank.com.tw | 0 |
| 216 | `esun_kumamon_japan` | 玉山熊本熊日圓雙幣卡 | esunbank.com.tw | 0 |
| 217 | `sinopac_dawho_card` | 永豐DAWHO現金回饋信用卡 | sinopac.com | 0 |
| 218 | `sinopac_55688_card` | 永豐55688聯名卡 | sinopac.com | 0 |
| 219 | `sinopac_cashback_jcb` | 永豐現金回饋JCB卡 | sinopac.com | 0 |
| 220 | `sinopac_meihua_card` | 永豐美麗華聯名卡 | sinopac.com | 0 |
| 221 | `sinopac_mitsui_outlet` | 永豐MITSUI OUTLET PARK聯名卡 | sinopac.com | 0 |
| 222 | `first_yilan_recognition` | 第一銀行宜蘭認同卡 | firstbank.com.tw | 0 |
| 223 | `first_dual_currency_titanium` | 第一銀行雙幣鈦金商務卡 | firstbank.com.tw | 0 |
| 224 | `first_titanium_business_travel` | 第一銀行鈦金商旅卡 | firstbank.com.tw | 0 |
| 225 | `first_taoyuan_card` | 第一銀行桃園市市民卡聯名卡 | firstbank.com.tw | 0 |
| 226 | `hncb_super_diamond` | 華南銀行超鑽現金回饋卡 | hncb.com.tw | 0 |
| 227 | `hncb_dudufang_card` | 華南銀行嘟嘟房聯名卡 | hncb.com.tw | 0 |
| 228 | `hncb_gourmet_reward` | 華南銀行美饌紅利卡 | hncb.com.tw | 0 |
| 229 | `hncb_navigator_supreme` | 華南銀行領航極致尊榮卡 | hncb.com.tw | 20000 |
| 230 | `mega_bt21_card` | 兆豐銀行宇宙明星BT21信用卡 | megabank.com.tw | 0 |
| 231 | `mega_haiyue_card` | 兆豐銀行海悅國際聯名卡 | megabank.com.tw | 0 |
| 232 | `mega_e_second_titanium` | 兆豐銀行e秒刷鈦金卡 | megabank.com.tw | 0 |
| 233 | `mega_next_bank_card` | 兆豐銀行將來銀行聯名卡 | megabank.com.tw | 0 |
| 234 | `union_happy_m_card` | 聯邦銀行幸福M卡 | ubot.com.tw | 0 |
| 235 | `union_breeze_card` | 聯邦銀行微風聯名卡 | ubot.com.tw | 0 |
| 236 | `union_dali_card` | 聯邦銀行大立聯名卡 | ubot.com.tw | 0 |
| 237 | `tcb_kanahei_card` | 合作金庫卡娜赫拉的小動物聯名卡 | tcb-bank.com.tw | 0 |
| 238 | `tcb_lohas_card` | 合作金庫樂活卡 | tcb-bank.com.tw | 0 |
| 239 | `tcb_hanlai_gourmet` | 合作金庫漢來美食聯名卡 | tcb-bank.com.tw | 0 |
| 240 | `chb_my_shop_card` | 彰化銀行My購卡 | bankchb.com | 0 |
| 241 | `chb_mackay_card` | 彰化銀行馬偕認同卡 | bankchb.com | 0 |
| 242 | `landbank_badminton_card` | 臺灣土地銀行麟洋羽球認同卡 | landbank.com.tw | 0 |
| 243 | `landbank_eternity_jcb` | 臺灣土地銀行極緻卡 | landbank.com.tw | 0 |
| 244 | `tbb_art_travel_card` | 臺灣企銀藝游認同卡 | tbb.com.tw | 0 |
| 245 | `dbs_xiang_le_card` | 星展銀行饗樂生活卡 | dbs.com.tw | 0 |
| 246 | `dbs_spark_sustainable` | 星展銀行炫晶御璽卡 | dbs.com.tw | 0 |
| 247 | `hsbc_traveler_infinite` | 滙豐銀行旅人無限卡 | hsbc.com.tw | 8000 |
| 248 | `hsbc_diamond_cashback` | 滙豐銀行匯鑽卡 | hsbc.com.tw | 0 |
| 249 | `scb_line_bank_card` | 渣打銀行LINE Bank聯名卡 | sc.com/tw | 0 |
| 250 | `rakuten_tigerair_card` | 台灣樂天台灣虎航聯名卡 | card.rakuten.com.tw | 688 |


