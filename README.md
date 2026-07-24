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
| 🇺🇸 United States (US) | 177 |
| 🇨🇦 Canada (CA) | 113 |
| 🇦🇺 Australia (AU) | 165 |
| 🇨🇳 China (CN) | 147 |
| 🇹🇼 Taiwan (TW) | 156 |
| **Total** | **758** |

_Generated 2026-07-24._

## Card list

### 🇺🇸 United States (177)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `chase_sapphire_preferred` | Chase Sapphire Preferred | chase.com | 95 |
| 2 | `chase_sapphire_reserve` | Chase Sapphire Reserve | chase.com | 795 |
| 3 | `chase_freedom_unlimited` | Chase Freedom Unlimited | chase.com | 0 |
| 4 | `chase_freedom_flex` | Chase Freedom Flex | chase.com | 0 |
| 5 | `chase_ink_preferred` | Chase Ink Business Preferred | chase.com | 95 |
| 6 | `chase_hyatt` | Chase World of Hyatt Credit Card | chase.com | 95 |
| 7 | `chase_marriott_boundless` | Chase Marriott Bonvoy Boundless | chase.com | 95 |
| 8 | `amex_gold` | American Express Gold | americanexpress.com | 325 |
| 9 | `amex_platinum` | American Express Platinum | americanexpress.com | 895 |
| 10 | `amex_blue_cash_preferred` | Amex Blue Cash Preferred | americanexpress.com | 95 |
| 11 | `amex_blue_cash_everyday` | Amex Blue Cash Everyday | americanexpress.com | 0 |
| 12 | `amex_delta_gold` | Delta SkyMiles Gold Amex | americanexpress.com | 150 |
| 13 | `amex_delta_platinum` | Delta SkyMiles Platinum Amex | americanexpress.com | 350 |
| 14 | `amex_hilton_surpass` | Hilton Honors Amex Surpass | americanexpress.com | 150 |
| 15 | `capital_one_venture_x` | Capital One Venture X | capitalone.com | 395 |
| 16 | `capital_one_venture` | Capital One Venture | capitalone.com | 95 |
| 17 | `capital_one_savor` | Capital One Savor Cash Rewards | capitalone.com | 95 |
| 18 | `citi_double_cash` | Citi Double Cash | citi.com | 0 |
| 19 | `citi_strata_premier` | Citi Strata Premier | citi.com | 95 |
| 20 | `citi_custom_cash` | Citi Custom Cash | citi.com | 0 |
| 21 | `discover_it` | Discover it Cash Back | discover.com | 0 |
| 22 | `wells_fargo_active_cash` | Wells Fargo Active Cash | wellsfargo.com | 0 |
| 23 | `wells_fargo_autograph` | Wells Fargo Autograph | wellsfargo.com | 0 |
| 24 | `bank_of_america_premium_rewards` | Bank of America Premium Rewards | bankofamerica.com | 95 |
| 25 | `apple_card` | Apple Card | apple.com | 0 |
| 26 | `bilt_mastercard` | Bilt Mastercard | biltrewards.com | 0 |
| 27 | `us_bank_altitude_reserve` | US Bank Altitude Reserve | usbank.com | 400 |
| 28 | `navy_federal_flagship` | Navy Federal Flagship Rewards | navyfederal.org | 49 |
| 29 | `fidelity_rewards_visa` | Fidelity Rewards Visa | fidelity.com | 0 |
| 30 | `amazon_prime_rewards` | Amazon Prime Rewards Visa | amazon.com | 0 |
| 31 | `chase_united_explorer` | Chase United Explorer Card | chase.com | 95 |
| 32 | `chase_southwest_priority` | Chase Southwest Rapid Rewards Priority | chase.com | 149 |
| 33 | `capital_one_quicksilver` | Capital One Quicksilver Cash Rewards | capitalone.com | 0 |
| 34 | `bank_of_america_customized_cash` | Bank of America Customized Cash Rewards | bankofamerica.com | 0 |
| 35 | `chase_ink_cash` | Chase Ink Business Cash Credit Card | chase.com | 0 |
| 36 | `amex_green` | American Express Green Card | americanexpress.com | 150 |
| 37 | `capital_one_savorone` | Capital One SavorOne Cash Rewards | capitalone.com | 0 |
| 38 | `chase_freedom_rise` | Chase Freedom Rise | chase.com | 0 |
| 39 | `wells_fargo_attune` | Wells Fargo Attune | wellsfargo.com | 0 |
| 40 | `amex_hilton_aspire` | Hilton Honors Amex Aspire | americanexpress.com | 550 |
| 41 | `chase_ihg_premier` | Chase IHG One Rewards Premier | chase.com | 99 |
| 42 | `chase_ritz_carlton` | Chase Ritz-Carlton Credit Card | chase.com | 450 |
| 43 | `capital_one_ventureone` | Capital One VentureOne Rewards | capitalone.com | 0 |
| 44 | `us_bank_cash_plus` | U.S. Bank Cash+® Visa Signature® | usbank.com | 0 |
| 45 | `us_bank_altitude_connect` | U.S. Bank Altitude® Connect | usbank.com | 0 |
| 46 | `bank_of_america_travel_rewards` | Bank of America® Travel Rewards | bankofamerica.com | 0 |
| 47 | `bank_of_america_unlimited_cash` | Bank of America® Unlimited Cash Rewards | bankofamerica.com | 0 |
| 48 | `choice_privileges_mastercard` | Choice Privileges® Mastercard® | wellsfargo.com | 0 |
| 49 | `discover_it_miles` | Discover it® Miles | discover.com | 0 |
| 50 | `discover_it_student` | Discover it® Student Cash Back | discover.com | 0 |
| 51 | `citi_rewards_plus` | Citi Rewards+® Card | citi.com | 0 |
| 52 | `amex_blue_business_cash` | Amex Blue Business Cash® | americanexpress.com | 0 |
| 53 | `amex_blue_business_plus` | Amex Blue Business® Plus | americanexpress.com | 0 |
| 54 | `chase_ink_unlimited` | Chase Ink Business Unlimited® | chase.com | 0 |
| 55 | `chase_ink_premier` | Chase Ink Business Premier® | chase.com | 195 |
| 56 | `amex_marriott_bevy` | Marriott Bonvoy Bevy® Amex | americanexpress.com | 250 |
| 57 | `amex_marriott_brilliant` | Marriott Bonvoy Brilliant® Amex | americanexpress.com | 650 |
| 58 | `amex_delta_blue` | Delta SkyMiles® Blue Amex | americanexpress.com | 0 |
| 59 | `chase_united_gateway` | United Gateway® Card | chase.com | 0 |
| 60 | `chase_united_quest` | Chase United Quest Card | chase.com | 250 |
| 61 | `chase_united_club_infinite` | Chase United Club Infinite Card | chase.com | 525 |
| 62 | `chase_southwest_performance_business` | Southwest Rapid Rewards Performance Business | chase.com | 199 |
| 63 | `chase_southwest_premier_business` | Southwest Rapid Rewards Premier Business | chase.com | 99 |
| 64 | `chase_marriott_bountiful` | Marriott Bonvoy Bountiful™ Card | chase.com | 250 |
| 65 | `amex_hilton_honors_base` | Hilton Honors American Express Card | americanexpress.com | 0 |
| 66 | `amex_marriott_bonvoy_business` | Marriott Bonvoy Business® Amex | americanexpress.com | 125 |
| 67 | `amex_delta_reserve` | Delta SkyMiles® Reserve Amex | americanexpress.com | 650 |
| 68 | `amex_delta_business_gold` | Delta SkyMiles® Gold Business Amex | americanexpress.com | 150 |
| 69 | `amex_delta_business_platinum` | Delta SkyMiles® Platinum Business Amex | americanexpress.com | 350 |
| 70 | `amex_delta_business_reserve` | Delta SkyMiles® Reserve Business Amex | americanexpress.com | 650 |
| 71 | `amex_business_gold` | American Express® Business Gold Card | americanexpress.com | 375 |
| 72 | `amex_business_platinum` | American Express® Business Platinum Card | americanexpress.com | 895 |
| 73 | `amex_plum_card` | The Plum Card® from American Express | americanexpress.com | 250 |
| 74 | `citi_prestige` | Citi Prestige® Card | citi.com | 495 |
| 75 | `citi_aadvantage_platinum_select` | Citi® / AAdvantage® Platinum Select® Card | citi.com | 99 |
| 76 | `citi_aadvantage_executive` | Citi® / AAdvantage® Executive World Elite Mastercard® | citi.com | 595 |
| 77 | `citi_aadvantage_mileup` | American Airlines AAdvantage® MileUp® Card | citi.com | 0 |
| 78 | `citi_costco_anywhere` | Costco Anywhere Visa® Card by Citi | citi.com | 0 |
| 79 | `citi_costco_anywhere_business` | Costco Anywhere Visa® Business Card by Citi | citi.com | 0 |
| 80 | `capital_one_spark_cash_plus` | Capital One Spark Cash Plus | capitalone.com | 150 |
| 81 | `capital_one_spark_miles` | Capital One Spark Miles for Business | capitalone.com | 95 |
| 82 | `wells_fargo_reflect` | Wells Fargo Reflect® Card | wellsfargo.com | 0 |
| 83 | `wells_fargo_autograph_journey` | Wells Fargo Autograph Journey℠ Card | wellsfargo.com | 95 |
| 84 | `bank_of_america_alaska_airlines` | Alaska Airlines Visa Signature® credit card | bankofamerica.com | 95 |
| 85 | `bank_of_america_customized_cash_business` | Bank of America® Business Advantage Customized Cash Rewards | bankofamerica.com | 0 |
| 86 | `us_bank_altitude_go` | U.S. Bank Altitude® Go Visa Signature® Card | usbank.com | 0 |
| 87 | `us_bank_shopper_cash_rewards` | U.S. Bank Shopper Cash Rewards™ Visa Signature® Card | usbank.com | 95 |
| 88 | `us_bank_business_triple_cash` | U.S. Bank Business Triple Cash Rewards® Visa® | usbank.com | 0 |
| 89 | `barclays_view` | Barclays View Mastercard® | barclaysus.com | 0 |
| 90 | `barclays_jetblue_plus` | JetBlue Plus Card | barclaysus.com | 99 |
| 91 | `barclays_aadvantage_aviator_red` | AAdvantage® Aviator® Red World Elite Mastercard® | barclaysus.com | 99 |
| 92 | `barclays_wyndham_rewards_earner_plus` | Wyndham Rewards Earner® Plus Card | barclaysus.com | 75 |
| 93 | `synchrony_amazon_store_card` | Amazon Store Card | amazon.com | 0 |
| 94 | `synchrony_lowes_advantage` | Lowe’s Advantage Card | lowes.com | 0 |
| 95 | `synchrony_verizon_visa` | Verizon Visa® Card | verizon.com | 0 |
| 96 | `comenity_aaa_daily_advantage` | AAA Daily Advantage Visa Signature® Card | aaa.com | 0 |
| 97 | `comenity_bread_cashback` | Bread Cashback™ American Express® Credit Card | breadfinancial.com | 0 |
| 98 | `sofi_credit_card` | SoFi Credit Card | sofi.com | 0 |
| 99 | `venmo_credit_card` | Venmo Credit Card | venmo.com | 0 |
| 100 | `chase_southwest_plus` | Southwest Rapid Rewards® Plus | chase.com | 69 |
| 101 | `robinhood_gold` | Robinhood Gold Card | robinhood.com | 0 |
| 102 | `us_bank_smartly_visa` | U.S. Bank Smartly™ Visa Signature® | usbank.com | 0 |
| 103 | `citi_strata_elite` | Citi Strata Elite℠ Card | citi.com | 595 |
| 104 | `chase_sapphire_reserve_business` | Chase Sapphire Reserve for Business | chase.com | 795 |
| 105 | `penfed_power_cash_rewards` | PenFed Power Cash Rewards Visa Signature® | penfed.org | 0 |
| 106 | `usaa_eagle_navigator` | USAA Eagle Navigator™ Credit Card | usaa.com | 95 |
| 107 | `paypal_cashback_mastercard` | PayPal Cashback Mastercard® | paypal.com | 0 |
| 108 | `target_redcard` | Target RedCard Credit Card | target.com | 0 |
| 109 | `navy_federal_cashrewards` | Navy Federal cashRewards Card | navyfederal.org | 0 |
| 110 | `usaa_cashback_rewards_plus` | USAA Cashback Rewards Plus American Express | usaa.com | 0 |
| 111 | `samsclub_mastercard` | Sam's Club Mastercard | samsclub.com | 0 |
| 112 | `pnc_cash_rewards` | PNC Cash Rewards Visa | pnc.com | 0 |
| 113 | `td_double_up` | TD Double Up Credit Card | tdbank.com | 0 |
| 114 | `alliant_cashback_visa` | Alliant Cashback Visa Signature | alliantcreditunion.org | 0 |
| 115 | `citizens_cash_back_plus` | Citizens Cash Back Plus World Mastercard | citizensbank.com | 0 |
| 116 | `chase_aeroplan_us` | Chase Aeroplan Card | chase.com | 95 |
| 117 | `chase_united_business` | United Business Card | chase.com | 99 |
| 118 | `chase_hyatt_business` | World of Hyatt Business Card | chase.com | 199 |
| 119 | `chase_disney_premier` | Disney Premier Visa Card | chase.com | 49 |
| 120 | `chase_instacart` | Instacart Mastercard | chase.com | 0 |
| 121 | `chase_doordash` | DoorDash Rewards Mastercard | chase.com | 0 |
| 122 | `amex_schwab_platinum` | American Express Platinum Card for Schwab | americanexpress.com | 695 |
| 123 | `amex_morgan_stanley_platinum` | Morgan Stanley American Express Platinum | americanexpress.com | 695 |
| 124 | `capital_one_spark_cash_select` | Capital One Spark Cash Select | capitalone.com | 0 |
| 125 | `capital_one_quicksilver_student` | Capital One Quicksilver Student | capitalone.com | 0 |
| 126 | `barclays_jetblue` | JetBlue Card | barclaysus.com | 0 |
| 127 | `barclays_hawaiian` | Hawaiian Airlines World Elite Mastercard | barclaysus.com | 99 |
| 128 | `barclays_frontier` | Frontier Airlines World Mastercard | barclaysus.com | 89 |
| 129 | `citi_aadvantage_business` | CitiBusiness AAdvantage Platinum Select | citi.com | 99 |
| 130 | `synchrony_carecredit` | CareCredit Card | synchrony.com | 0 |
| 131 | `amex_everyday_preferred` | American Express EveryDay Preferred | americanexpress.com | 95 |
| 132 | `amex_cash_magnet` | American Express Cash Magnet Card | americanexpress.com | 0 |
| 133 | `amex_business_green` | American Express Business Green Rewards | americanexpress.com | 95 |
| 134 | `discover_it_chrome` | Discover it Chrome | discover.com | 0 |
| 135 | `discover_it_secured` | Discover it Secured | discover.com | 0 |
| 136 | `citi_simplicity` | Citi Simplicity Card | citi.com | 0 |
| 137 | `citi_diamond_preferred` | Citi Diamond Preferred Card | citi.com | 0 |
| 138 | `wells_fargo_one_key` | One Key+ Card | wellsfargo.com | 0 |
| 139 | `capital_one_venture_x_business` | Capital One Venture X Business | capitalone.com | 395 |
| 140 | `upgrade_cash_rewards` | Upgrade Cash Rewards Card | upgrade.com | 0 |
| 141 | `petal_2` | Petal 2 Visa Credit Card | petalcard.com | 0 |
| 142 | `navy_federal_more_rewards_amex` | Navy Federal More Rewards American Express | navyfederal.org | 0 |
| 143 | `navy_federal_go_rewards` | Navy Federal GO Rewards Card | navyfederal.org | 0 |
| 144 | `penfed_pathfinder` | PenFed Pathfinder Rewards American Express | penfed.org | 95 |
| 145 | `penfed_platinum_rewards` | PenFed Platinum Rewards Visa Signature | penfed.org | 0 |
| 146 | `usaa_preferred_cash_rewards` | USAA Preferred Cash Rewards Visa Signature | usaa.com | 0 |
| 147 | `truist_enjoy_cash` | Truist Enjoy Cash Credit Card | truist.com | 0 |
| 148 | `fifth_third_cash_back` | Fifth Third Cash/Back Card | 53.com | 0 |
| 149 | `huntington_voice` | Huntington Voice Rewards Card | huntington.com | 0 |
| 150 | `td_cash_us` | TD Cash Credit Card | tdbank.com | 0 |
| 151 | `robinhood_gold_card` | Robinhood Gold Card | robinhood.com | 0 |
| 152 | `us_bank_shopper_cash` | U.S. Bank Shopper Cash Rewards | usbank.com | 95 |
| 153 | `barclays_aadvantage_aviator` | Barclays AAdvantage Aviator Red | barclaysus.com | 99 |
| 154 | `navy_federal_more_rewards` | Navy Federal More Rewards Visa Signature | navyfederal.org | 0 |
| 155 | `chase_slate_edge` | Chase Slate Edge | chase.com | 0 |
| 156 | `citi_aa_mileup` | Citi AAdvantage MileUp Card | citi.com | 0 |
| 157 | `bofa_premium_rewards_elite` | Bank of America Premium Rewards Elite | bankofamerica.com | 550 |
| 158 | `wells_fargo_signify_business` | Wells Fargo Signify Business Cash | wellsfargo.com | 0 |
| 159 | `barclays_wyndham_earner_plus` | Wyndham Rewards Earner Plus Card | barclaysus.com | 75 |
| 160 | `us_bank_business_altitude_connect` | U.S. Bank Business Altitude Connect | usbank.com | 0 |
| 161 | `synchrony_paypal_cashback` | PayPal Cashback Mastercard | paypal.com | 0 |
| 162 | `bofa_business_advantage_customized_cash` | BofA Business Advantage Customized Cash | bankofamerica.com | 0 |
| 163 | `blockfi_rewards_visa` | BlockFi Rewards Visa Signature Card | blockfi.com | 0 |
| 164 | `chase_amazon_prime_store` | Amazon Prime Store Card by Chase | chase.com | 0 |
| 165 | `chase_freedom_student` | Chase Freedom Student Credit Card | chase.com | 0 |
| 166 | `amex_hilton_honors` | Hilton Honors American Express Card | americanexpress.com | 0 |
| 167 | `bofa_travel_rewards_student` | Bank of America Travel Rewards for Students | bankofamerica.com | 0 |
| 168 | `barclays_hawaiian_airlines` | Hawaiian Airlines World Elite Mastercard | barclaysus.com | 99 |
| 169 | `synchrony_sams_club_mastercard` | Sam's Club Mastercard | synchrony.com | 0 |
| 170 | `target_circle_card` | Target Circle Card | target.com | 0 |
| 171 | `gemini_credit_card` | Gemini Crypto Rewards Credit Card | gemini.com | 0 |
| 172 | `x1_card` | X1 Credit Card | x1.co | 0 |
| 173 | `petal_2_visa` | Petal 2 Cash Back Visa | petalcard.com | 0 |
| 174 | `citizens_bank_cash_back` | Citizens Bank Cash Back Plus World Mastercard | citizensbank.com | 0 |
| 175 | `keybank_latitude` | KeyBank Key Latitude Credit Card | key.com | 0 |
| 176 | `td_cash_card` | TD Cash Credit Card | td.com | 0 |
| 177 | `alaska_airlines_visa` | Alaska Airlines Visa Signature Card | alaskair.com | 95 |


### 🇨🇦 Canada (113)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `rbc_avion_visa_infinite` | RBC Avion Visa Infinite | rbc.com | 120 |
| 2 | `rbc_ion_plus` | RBC ION+ Visa | rbc.com | 48 |
| 3 | `td_aeroplan_visa_infinite` | TD Aeroplan Visa Infinite | td.com | 139 |
| 4 | `td_cash_back_visa_infinite` | TD Cash Back Visa Infinite | td.com | 139 |
| 5 | `scotiabank_gold_amex` | Scotiabank Gold American Express | scotiabank.com | 120 |
| 6 | `scotiabank_passport_visa_infinite` | Scotiabank Passport Visa Infinite | scotiabank.com | 150 |
| 7 | `cibc_dividend_visa_infinite` | CIBC Dividend Visa Infinite | cibc.com | 120 |
| 8 | `cibc_aeroplan_visa_infinite` | CIBC Aeroplan Visa Infinite | cibc.com | 139 |
| 9 | `bmo_cashback_world_elite` | BMO CashBack World Elite Mastercard | bmo.com | 120 |
| 10 | `bmo_ascend_world_elite` | BMO Ascend World Elite Mastercard | bmo.com | 150 |
| 11 | `amex_cobalt` | American Express Cobalt Card | americanexpress.com | 191.88 |
| 12 | `tangerine_money_back` | Tangerine Money-Back Credit Card | tangerine.ca | 0 |
| 13 | `rogers_red_world_elite` | Rogers Red World Elite Mastercard | rogersbank.com | 0 |
| 14 | `simplii_cash_back` | Simplii Financial Cash Back Visa | simplii.com | 0 |
| 15 | `amex_platinum_ca` | American Express Platinum Card | americanexpress.com | 799 |
| 16 | `amex_simply_cash_ca` | SimplyCash Card from Amex | americanexpress.ca | 0 |
| 17 | `amex_simply_cash_preferred_ca` | SimplyCash Preferred Amex | americanexpress.ca | 120 |
| 18 | `amex_gold_rewards_ca` | Amex Gold Rewards Card | americanexpress.ca | 250 |
| 19 | `amex_choice_card_ca` | Amex Choice Card | americanexpress.ca | 0 |
| 20 | `amex_marriott_bonvoy_ca` | Amex Marriott Bonvoy Card | americanexpress.ca | 120 |
| 21 | `bmo_air_miles_world_elite` | BMO AIR MILES World Elite Mastercard | bmo.com | 120 |
| 22 | `bmo_eclipse_visa_infinite` | BMO eclipse Visa Infinite Card | bmo.com | 120 |
| 23 | `bmo_eclipse_visa_infinite_privilege` | BMO eclipse Visa Infinite Privilege | bmo.com | 499 |
| 24 | `cibc_aventura_visa_infinite` | CIBC Aventura Visa Infinite | cibc.com | 139 |
| 25 | `cibc_costco_mastercard` | CIBC Costco Mastercard | cibc.com | 0 |
| 26 | `td_first_class_travel_visa_infinite` | TD First Class Travel Visa Infinite | td.com | 139 |
| 27 | `td_rewards_visa` | TD Rewards Visa card | td.com | 0 |
| 28 | `scotia_momentum_visa_infinite` | Scotia Momentum Visa Infinite | scotiabank.com | 120 |
| 29 | `scotiabank_scene_plus_visa` | Scotiabank SCENE+ Visa Card | scotiabank.com | 0 |
| 30 | `rbc_ion_visa` | RBC ION Visa | rbc.com | 0 |
| 31 | `rbc_cash_back_mastercard` | RBC Cash Back Mastercard | rbc.com | 0 |
| 32 | `national_bank_world_elite` | National Bank World Elite Mastercard | nbc.ca | 150 |
| 33 | `pc_world_elite_mastercard` | PC World Elite Mastercard | pcfinancial.ca | 0 |
| 34 | `triangle_world_elite` | Triangle World Elite Mastercard | canadiantire.ca | 0 |
| 35 | `rogers_mastercard` | Rogers Mastercard | rogers.com | 0 |
| 36 | `fido_mastercard` | Fido Mastercard | rogers.com | 0 |
| 37 | `wealthsimple_cash_card` | Wealthsimple Cash Card | wealthsimple.com | 0 |
| 38 | `neo_financial_credit` | Neo Financial Credit | neofinancial.com | 0 |
| 39 | `eq_bank_card` | EQ Bank Card | eqbank.ca | 0 |
| 40 | `brim_mastercard` | Brim Mastercard | brimfinancial.com | 0 |
| 41 | `rbc_westjet_world_elite` | WestJet RBC® World Elite Mastercard® | rbc.com | 119 |
| 42 | `rbc_british_airways_visa_infinite` | RBC® British Airways Visa Infinite® | rbc.com | 165 |
| 43 | `td_business_travel_visa` | TD® Business Travel Visa* Card | td.com | 149 |
| 44 | `td_business_aeroplan_visa` | TD® Business Aeroplan® Visa* Card | td.com | 149 |
| 45 | `bmo_shell_air_miles_mastercard` | BMO® Shell®® AIR MILES®® Mastercard®* | bmo.com | 0 |
| 46 | `bmo_ihg_one_rewards_mastercard` | BMO® IHG One Rewards Mastercard®* | bmo.com | 0 |
| 47 | `cibc_business_plus_visa` | CIBC Business Plus Visa* Card | cibc.com | 0 |
| 48 | `scotiabank_american_express_platinum` | The Platinum Card® from Scotiabank | scotiabank.com | 399 |
| 49 | `scotiabank_no_fee_value_visa` | Scotiabank®* No-Fee Value® Visa* Card | scotiabank.com | 0 |
| 50 | `national_bank_platinum_mastercard` | National Bank Platinum Mastercard® | nbc.ca | 70 |
| 51 | `desjardins_odyssey_world_elite` | Desjardins Odyssey® World Elite® Mastercard® | desjardins.com | 130 |
| 52 | `laurentian_bank_visa_infinite` | Laurentian Bank Visa Infinite* | laurentianbank.ca | 130 |
| 53 | `canadian_tire_triangle_mastercard` | Triangle® Mastercard® | canadiantire.ca | 0 |
| 54 | `pc_financial_mastercard` | PC® Financial Mastercard® | pcfinancial.ca | 0 |
| 55 | `walmart_rewards_mastercard_ca` | Walmart Rewards® Mastercard® | walmart.ca | 0 |
| 56 | `amazon_ca_rewards_mastercard` | Amazon.ca Rewards Mastercard® | amazon.ca | 0 |
| 57 | `mbna_rewards_platinum_plus` | MBNA Rewards Platinum Plus® Mastercard® | mbna.ca | 0 |
| 58 | `mbna_best_western_rewards` | MBNA Best Western Rewards® Mastercard® | mbna.ca | 0 |
| 59 | `amex_business_edge_ca` | American Express® Business Edge® Card | americanexpress.ca | 99 |
| 60 | `amex_business_gold_ca` | American Express® Business Gold Rewards Card | americanexpress.ca | 250 |
| 61 | `amex_aeroplan_reserve_ca` | American Express Aeroplan Reserve Card | americanexpress.ca | 599 |
| 62 | `amex_aeroplan_ca` | American Express Aeroplan Card | americanexpress.ca | 120 |
| 63 | `manulife_money_plus_visa_infinite` | ManulifeMONEY+ Visa Infinite | manulife.ca | 139 |
| 64 | `home_trust_preferred_visa` | Home Trust Preferred Visa | hometrust.ca | 0 |
| 65 | `koho_card` | KOHO Card | koho.ca | 0 |
| 66 | `meridian_visa_cash_back` | Meridian Visa Infinite Cash Back | meridiancu.ca | 99 |
| 67 | `vancity_enviro_visa` | Vancity enviro Visa Infinite | vancity.com | 120 |
| 68 | `coast_capital_visa` | Coast Capital Visa Infinite Cash Back | coastcapitalsavings.com | 99 |
| 69 | `servus_credit_union_visa` | Servus Credit Union Visa Cash Back | servus.ca | 0 |
| 70 | `atb_cash_back_mastercard` | ATB Cash Back Mastercard | atb.com | 0 |
| 71 | `desjardins_cash_back_visa` | Desjardins Cash Back Visa | desjardins.com | 0 |
| 72 | `laurentian_bank_visa_signature` | Laurentian Bank Visa Signature | laurentianbank.ca | 130 |
| 73 | `canadian_western_bank_visa` | CWB Visa Infinite | cwbank.com | 120 |
| 74 | `alterna_cash_back_visa` | Alterna Savings Cash Back Visa | alterna.ca | 0 |
| 75 | `uni_visa_platinum` | UNI Visa Platinum | uni.ca | 0 |
| 76 | `duca_credit_union_visa` | DUCA Credit Union Visa | duca.com | 0 |
| 77 | `national_bank_echo_cashback` | National Bank Écho Cashback Mastercard | nbc.ca | 0 |
| 78 | `national_bank_syncro` | National Bank Syncro Mastercard | nbc.ca | 35 |
| 79 | `bmo_cashback_mastercard` | BMO CashBack Mastercard | bmo.com | 0 |
| 80 | `cibc_dividend_platinum` | CIBC Dividend Platinum Visa | cibc.com | 99 |
| 81 | `rbc_cash_back_preferred_world_elite` | RBC Cash Back Preferred World Elite Mastercard | rbc.com | 99 |
| 82 | `td_aeroplan_visa_platinum` | TD Aeroplan Visa Platinum | td.com | 89 |
| 83 | `td_cash_back_visa` | TD Cash Back Visa Card | td.com | 0 |
| 84 | `scotiabank_scene_amex` | Scotiabank Scene+ American Express | scotiabank.com | 0 |
| 85 | `first_west_envision_visa` | Envision Financial Visa | envisionfinancial.ca | 0 |
| 86 | `conexus_credit_union_visa` | Conexus Credit Union Visa | conexus.ca | 0 |
| 87 | `affinity_credit_union_visa` | Affinity Credit Union Visa | affinitycu.ca | 0 |
| 88 | `cambrian_credit_union_visa` | Cambrian Credit Union Visa | cambrian.mb.ca | 0 |
| 89 | `assiniboine_credit_union_visa` | Assiniboine Credit Union Visa | assiniboine.mb.ca | 0 |
| 90 | `innovation_credit_union_visa` | Innovation Federal Credit Union Visa | innovationcu.ca | 0 |
| 91 | `prospera_credit_union_visa` | Prospera Credit Union Visa | prospera.ca | 0 |
| 92 | `libro_credit_union_visa` | Libro Credit Union Visa | libro.ca | 0 |
| 93 | `firstontario_credit_union_visa` | FirstOntario Credit Union Visa | firstontario.com | 0 |
| 94 | `connect_first_credit_union_visa` | connectFirst Credit Union Visa | connectfirstcu.com | 0 |
| 95 | `steinbach_credit_union_visa` | Steinbach Credit Union Visa | scu.mb.ca | 0 |
| 96 | `access_credit_union_visa` | Access Credit Union Visa | accesscu.ca | 0 |
| 97 | `kindred_credit_union_visa` | Kindred Credit Union Visa | kindredcu.com | 0 |
| 98 | `synergy_credit_union_visa` | Synergy Credit Union Visa | synergycu.ca | 0 |
| 99 | `coastal_community_credit_union_visa` | Coastal Community Credit Union Visa | cccu.ca | 0 |
| 100 | `crosstown_credit_union_visa` | Crosstown Civic Credit Union Visa | crosstowncu.mb.ca | 0 |
| 101 | `scotiabank_momentum_visa_infinite` | Scotiabank Momentum Visa Infinite | scotiabank.com | 120 |
| 102 | `mbna_amazon_mastercard` | MBNA Amazon.ca Rewards Mastercard | mbna.ca | 0 |
| 103 | `neo_financial_card` | Neo Financial Credit Card | neofinancial.com | 0 |
| 104 | `brim_world_elite_mastercard` | Brim World Elite Mastercard | brimfinancial.com | 199 |
| 105 | `desjardins_cashback_world_elite` | Desjardins Cash Back World Elite | desjardins.com | 100 |
| 106 | `canadian_tire_triangle_world_elite` | Triangle World Elite Mastercard | ctfs.com | 0 |
| 107 | `rbc_cashback_preferred_world_elite` | RBC Cash Back Preferred World Elite Mastercard | rbc.com | 99 |
| 108 | `td_business_cash_back_visa` | TD Business Cash Back Visa Card | td.com | 0 |
| 109 | `scotiabank_passport_visa_infinite_business` | Scotiabank Passport Visa Infinite Business | scotiabank.com | 199 |
| 110 | `cibc_aeroplan_visa_infinite_privilege` | CIBC Aeroplan Visa Infinite Privilege | cibc.com | 599 |
| 111 | `pc_financial_world_elite` | PC Financial World Elite Mastercard | pcfinancial.ca | 0 |
| 112 | `coop_community_builder_visa` | Co-op Community Builder Visa Card | co-op.ca | 0 |
| 113 | `neo_cathay_pacific_card` | Neo Cathay Pacific Mastercard | neofinancial.com | 180 |


### 🇦🇺 Australia (165)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `anz_frequent_flyer_black` | ANZ Frequent Flyer Black | anz.com.au | 425 |
| 2 | `anz_rewards_black` | ANZ Rewards Black | anz.com.au | 375 |
| 3 | `anz_low_rate` | ANZ Low Rate | anz.com.au | 58 |
| 4 | `commbank_smart_awards` | CommBank Smart Awards | commbank.com.au | 228 |
| 5 | `commbank_ultimate_awards` | CommBank Ultimate Awards | commbank.com.au | 420 |
| 6 | `nab_qantas_rewards_signature` | NAB Qantas Rewards Signature | nab.com.au | 420 |
| 7 | `nab_rewards_platinum` | NAB Rewards Platinum | nab.com.au | 195 |
| 8 | `westpac_altitude_black` | Westpac Altitude Black | westpac.com.au | 295 |
| 9 | `westpac_altitude_platinum` | Westpac Altitude Platinum | westpac.com.au | 175 |
| 10 | `amex_platinum_edge_au` | Amex Platinum Edge | americanexpress.com | 195 |
| 11 | `amex_explorer_au` | Amex Explorer Credit Card | americanexpress.com | 395 |
| 12 | `ing_orange_one` | ING Orange One | ing.com.au | 48 |
| 13 | `macquarie_black` | Macquarie Black | macquarie.com | 249 |
| 14 | `bankwest_zero_mastercard` | Bankwest Zero Mastercard | bankwest.com.au | 0 |
| 15 | `st_george_amplify_signature` | St.George Amplify Signature | stgeorge.com.au | 295 |
| 16 | `virgin_money_rewards` | Virgin Money Rewards Credit Card | virginmoney.com.au | 149 |
| 17 | `latitude_28_degrees` | Latitude 28? Global Platinum | latitudefinancial.com.au | 96 |
| 18 | `hsbc_platinum_au` | HSBC Platinum Credit Card | hsbc.com.au | 199 |
| 19 | `commbank_low_fee_gold` | CommBank Low Fee Gold | commbank.com.au | 89 |
| 20 | `westpac_lite` | Westpac Lite Card | westpac.com.au | 108 |
| 21 | `nab_straightup` | NAB StraightUp Card | nab.com.au | 0 |
| 22 | `coles_rewards_mastercard` | Coles Rewards Mastercard | coles.com.au | 99 |
| 23 | `hsbc_star_alliance` | HSBC Star Alliance Credit Card | hsbc.com.au | 499 |
| 24 | `qantas_premier_platinum` | Qantas Premier Platinum | qantasmoney.com.au | 399 |
| 25 | `anz_rewards_platinum` | ANZ Rewards Platinum | anz.com.au | 149 |
| 26 | `nab_low_fee` | NAB Low Fee Credit Card | nab.com.au | 49 |
| 27 | `amex_platinum_au` | American Express Platinum Card | americanexpress.com | 1450 |
| 28 | `amex_velocity_platinum_au` | Amex Velocity Platinum | americanexpress.com.au | 440 |
| 29 | `amex_qantas_ultimate_au` | Amex Qantas Ultimate | americanexpress.com.au | 450 |
| 30 | `amex_essential_au` | Amex Essential | americanexpress.com.au | 108 |
| 31 | `amex_velocity_escape_au` | Amex Velocity Escape | americanexpress.com.au | 0 |
| 32 | `anz_rewards_travel_adventures` | ANZ Rewards Travel Adventures | anz.com.au | 175 |
| 33 | `commbank_awards` | CommBank Awards | commbank.com.au | 96 |
| 34 | `nab_qantas_rewards_premium` | NAB Qantas Rewards Premium | nab.com.au | 295 |
| 35 | `st_george_amplify_platinum` | St.George Amplify Platinum | stgeorge.com.au | 175 |
| 36 | `bank_of_melbourne_amplify_signature` | Bank of Melbourne Amplify Signature | bankofmelbourne.com.au | 295 |
| 37 | `bank_sa_amplify_signature` | BankSA Amplify Signature | banksa.com.au | 295 |
| 38 | `bankwest_more_rewards_platinum` | Bankwest More Rewards Platinum | bankwest.com.au | 160 |
| 39 | `bankwest_qantas_world` | Bankwest Qantas World Mastercard | bankwest.com.au | 320 |
| 40 | `virgin_money_velocity_high_flyer` | Virgin Money Velocity High Flyer | virginmoney.com.au | 289 |
| 41 | `virgin_money_velocity_flyer` | Virgin Money Velocity Flyer | virginmoney.com.au | 129 |
| 42 | `bendigo_qantas_mastercard` | Bendigo Qantas Mastercard | bendigobank.com.au | 149 |
| 43 | `suncorp_clear_options_platinum` | Suncorp Clear Options Platinum | suncorp.com.au | 129 |
| 44 | `kogan_money_credit_card` | Kogan Money Credit Card | koganmoney.com.au | 0 |
| 45 | `coles_no_fee_mastercard` | Coles No Annual Fee Mastercard | coles.com.au | 0 |
| 46 | `woolworths_everyday_platinum` | Woolworths Everyday Platinum | woolworths.com.au | 49 |
| 47 | `david_jones_amex_platinum` | David Jones Amex Platinum | americanexpress.com.au | 295 |
| 48 | `qantas_premier_everyday` | Qantas Premier Everyday | qantasmoney.com.au | 99 |
| 49 | `macquarie_reward_visa_platinum` | Macquarie Reward Visa Platinum | macquarie.com.au | 149 |
| 50 | `anz_first` | ANZ First | anz.com.au | 30 |
| 51 | `anz_platinum` | ANZ Platinum | anz.com.au | 87 |
| 52 | `anz_low_interest` | ANZ Low Interest | anz.com.au | 58 |
| 53 | `commbank_low_rate` | CommBank Low Rate | commbank.com.au | 72 |
| 54 | `commbank_low_fee` | CommBank Low Fee | commbank.com.au | 36 |
| 55 | `commbank_interest_free` | CommBank Interest Free | commbank.com.au | 120 |
| 56 | `nab_low_rate` | NAB Low Rate Card | nab.com.au | 99 |
| 57 | `nab_rewards_classic` | NAB Rewards Classic | nab.com.au | 95 |
| 58 | `nab_qantas_rewards` | NAB Qantas Rewards Card | nab.com.au | 95 |
| 59 | `westpac_altitude` | Westpac Altitude Card | westpac.com.au | 100 |
| 60 | `westpac_low_rate` | Westpac Low Rate | westpac.com.au | 59 |
| 61 | `macquarie_platinum` | Macquarie Platinum Credit Card | macquarie.com.au | 149 |
| 62 | `bankwest_breeze` | Bankwest Breeze Mastercard | bankwest.com.au | 49 |
| 63 | `bankwest_platinum_basic` | Bankwest Platinum Mastercard | bankwest.com.au | 0 |
| 64 | `bendigo_ready` | Bendigo Ready Credit Card | bendigobank.com.au | 0 |
| 65 | `bendigo_platinum` | Bendigo Platinum Visa | bendigobank.com.au | 89 |
| 66 | `suncorp_standard` | Suncorp Clear Options Standard | suncorp.com.au | 55 |
| 67 | `hsbc_premier` | HSBC Premier World Mastercard | hsbc.com.au | 199 |
| 68 | `hsbc_gold` | HSBC Gold Credit Card | hsbc.com.au | 79 |
| 69 | `st_george_vertigo` | St.George Vertigo Card | stgeorge.com.au | 55 |
| 70 | `bank_of_melbourne_vertigo` | Bank of Melbourne Vertigo Card | bankofmelbourne.com.au | 55 |
| 71 | `bank_sa_vertigo` | BankSA Vertigo Card | banksa.com.au | 55 |
| 72 | `imb_bank_platinum` | IMB Bank Platinum Mastercard | imb.com.au | 129 |
| 73 | `great_southern_bank_platinum` | Great Southern Bank Platinum Credit Card | greatsouthernbank.com.au | 149 |
| 74 | `heritage_bank_gold` | Heritage Bank Gold Low Rate | heritage.com.au | 0 |
| 75 | `beyond_bank_platinum` | Beyond Bank Platinum Visa | beyondbank.com.au | 59 |
| 76 | `newcastle_permanent_platinum` | Newcastle Permanent Platinum Mastercard | newcastlepermanent.com.au | 49 |
| 77 | `greater_bank_platinum` | Greater Bank Platinum Visa | greater.com.au | 0 |
| 78 | `peoples_choice_visa` | People’s Choice Visa Credit Card | peopleschoice.com.au | 59 |
| 79 | `racv_rewards` | RACV Rewards Credit Card | racv.com.au | 0 |
| 80 | `racq_rewards` | RACQ Rewards Credit Card | racq.com.au | 129 |
| 81 | `raa_rewards` | RAA Rewards Credit Card | raa.com.au | 0 |
| 82 | `boq_platinum` | BOQ Platinum Visa | boq.com.au | 149 |
| 83 | `boq_blue` | BOQ Blue Visa | boq.com.au | 89 |
| 84 | `myer_credit_card` | Myer Credit Card | myer.com.au | 69 |
| 85 | `amex_qantas_discovery_au` | Amex Qantas Discovery | americanexpress.com.au | 0 |
| 86 | `amex_cashback_au` | Amex Essential Cashback | americanexpress.com.au | 0 |
| 87 | `amex_platinum_business_au` | Amex Platinum Business Card | americanexpress.com.au | 1750 |
| 88 | `latitude_infinity` | Latitude Infinity Credit Card | latitudefinancial.com.au | 0 |
| 89 | `latitude_eco` | Latitude Eco Mastercard | latitudefinancial.com.au | 49 |
| 90 | `qantas_premier_titanium` | Qantas Premier Titanium | qantasmoney.com.au | 1200 |
| 91 | `virgin_money_no_fee` | Virgin Money No Annual Fee Card | virginmoney.com.au | 0 |
| 92 | `coles_platinum_mastercard` | Coles Platinum Mastercard | coles.com.au | 29 |
| 93 | `woolworths_qantas_platinum` | Woolworths Qantas Platinum Card | woolworths.com.au | 169 |
| 94 | `david_jones_amex_basic` | David Jones American Express Card | americanexpress.com.au | 99 |
| 95 | `humm90_mastercard` | Humm90 Mastercard | humm90.com.au | 119 |
| 96 | `bank_australia_visa` | Bank Australia Visa Credit Card | bankaustralia.com.au | 0 |
| 97 | `teachers_mutual_visa` | Teachers Mutual Bank Visa Credit Card | tmbank.com.au | 0 |
| 98 | `police_bank_visa` | Police Bank Visa Credit Card | policebank.com.au | 0 |
| 99 | `defence_bank_visa` | Defence Bank Visa Credit Card | defencebank.com.au | 45 |
| 100 | `mycard_rewards` | MyCard Rewards | mycard.com.au | 199 |
| 101 | `mycard_premier` | MyCard Premier | mycard.com.au | 300 |
| 102 | `mycard_prestige` | MyCard Prestige | mycard.com.au | 700 |
| 103 | `mycard_simplicity` | MyCard Simplicity | mycard.com.au | 0 |
| 104 | `mycard_clear` | MyCard Clear | mycard.com.au | 149 |
| 105 | `mycard_premier_qantas` | MyCard Premier Qantas | mycard.com.au | 350 |
| 106 | `mycard_prestige_qantas` | MyCard Prestige Qantas | mycard.com.au | 749 |
| 107 | `latitude_go_mastercard` | Latitude GO Mastercard | latitudefinancial.com.au | 131 |
| 108 | `latitude_gem_visa` | Latitude Gem Visa | latitudefinancial.com.au | 69 |
| 109 | `latitude_low_rate` | Latitude Low Rate Mastercard | latitudefinancial.com.au | 69 |
| 110 | `westpac_altitude_qantas_black` | Westpac Altitude Qantas Black | westpac.com.au | 370 |
| 111 | `westpac_altitude_qantas_platinum` | Westpac Altitude Qantas Platinum | westpac.com.au | 250 |
| 112 | `amex_qantas_business` | American Express Qantas Business Rewards | americanexpress.com.au | 450 |
| 113 | `commbank_neo` | CommBank Neo | commbank.com.au | 180 |
| 114 | `pn_bank_visa_platinum` | P&N Bank Visa Platinum | pnbank.com.au | 99 |
| 115 | `qudos_visa_platinum` | Qudos Bank Visa Platinum | qudosbank.com.au | 189 |
| 116 | `qudos_lifestyle` | Qudos Bank Lifestyle | qudosbank.com.au | 0 |
| 117 | `westpac_flex` | Westpac Flex Mastercard | westpac.com.au | 0 |
| 118 | `bank_first_visa_platinum` | Bank First Visa Platinum | bankfirst.com.au | 99 |
| 119 | `bankvic_visa` | BankVic Visa Credit Card | bankvic.com.au | 0 |
| 120 | `hume_bank_visa` | Hume Bank Visa Credit Card | humebank.com.au | 0 |
| 121 | `unity_bank_visa` | Unity Bank Visa Credit Card | unitybank.com.au | 0 |
| 122 | `gateway_bank_visa` | Gateway Bank Visa Platinum | gatewaybank.com.au | 49 |
| 123 | `regional_australia_bank_visa` | Regional Australia Bank Visa | regionalaustraliabank.com.au | 0 |
| 124 | `move_bank_visa` | MOVE Bank Visa Credit Card | movebank.com.au | 0 |
| 125 | `australian_military_bank_visa` | Australian Military Bank Visa | australianmilitarybank.com.au | 0 |
| 126 | `summerland_bank_visa` | Summerland Bank Visa Credit Card | summerland.com.au | 0 |
| 127 | `gc_mutual_visa` | G&C Mutual Bank Visa | gcmutual.bank | 0 |
| 128 | `bank_of_us_visa` | Bank of us Visa Credit Card | bankofus.com.au | 0 |
| 129 | `credit_union_sa_visa` | Credit Union SA Visa | creditunionsa.com.au | 0 |
| 130 | `bcu_visa` | bcu Visa Credit Card | bcu.com.au | 0 |
| 131 | `queensland_country_bank_visa` | Queensland Country Bank Visa | queenslandcountry.bank | 0 |
| 132 | `community_first_visa` | Community First Bank Visa | communityfirst.com.au | 0 |
| 133 | `qbank_visa` | QBANK Visa Credit Card | qbank.com.au | 0 |
| 134 | `police_credit_union_visa` | Police Credit Union Visa | policecu.com.au | 0 |
| 135 | `illawarra_credit_union_visa` | Illawarra Credit Union Visa | illawarracu.com.au | 0 |
| 136 | `southern_cross_credit_union_visa` | Southern Cross Credit Union Visa | sccu.com.au | 0 |
| 137 | `the_capricornian_visa` | The Capricornian Visa | capricornian.com.au | 0 |
| 138 | `woolworths_team_bank_visa` | Woolworths Team Bank Visa | woolworthsteambank.com.au | 0 |
| 139 | `reliance_bank_visa` | Reliance Bank Visa | reliancebank.com.au | 0 |
| 140 | `horizon_bank_visa` | Horizon Bank Visa | horizonbank.com.au | 0 |
| 141 | `orange_credit_union_visa` | Orange Credit Union Visa | orangecu.com.au | 0 |
| 142 | `warwick_credit_union_visa` | Warwick Credit Union Visa | wcu.com.au | 0 |
| 143 | `bankwaw_visa` | WAW Bank Visa | waw.com.au | 0 |
| 144 | `border_bank_visa` | Border Bank Visa | borderbank.com.au | 0 |
| 145 | `transport_mutual_visa` | Transport Mutual Credit Union Visa | transportmutual.com.au | 0 |
| 146 | `first_option_bank_visa` | First Option Bank Visa | firstoption.com.au | 0 |
| 147 | `the_mac_visa` | The Mac Credit Union Visa | themaccu.com.au | 0 |
| 148 | `family_first_credit_union_visa` | Family First Credit Union Visa | familyfirst.com.au | 0 |
| 149 | `coastline_credit_union_visa` | Coastline Credit Union Visa | coastline.com.au | 0 |
| 150 | `northern_inland_credit_union_visa` | Northern Inland Credit Union Visa | nicu.com.au | 0 |
| 151 | `hsbc_cash_plus` | HSBC Cash Plus Credit Card | hsbc.com.au | 99 |
| 152 | `bankwest_qantas_platinum` | Bankwest Qantas Platinum | bankwest.com.au | 160 |
| 153 | `velocity_frequent_flyer_card` | Virgin Australia Velocity Flyer Card | virginmoney.com.au | 129 |
| 154 | `bendigo_bright_card` | Bendigo Bright Credit Card | bendigobank.com.au | 0 |
| 155 | `kogan_first_mastercard` | Kogan First Credit Card | koganmoney.com.au | 0 |
| 156 | `commbank_awards_platinum` | CommBank Awards Platinum | commbank.com.au | 240 |
| 157 | `anz_frequent_flyer_platinum` | ANZ Frequent Flyer Platinum | anz.com.au | 295 |
| 158 | `westpac_altitude_rewards_black` | Westpac Altitude Rewards Black | westpac.com.au | 250 |
| 159 | `nab_rewards_signature` | NAB Rewards Signature Card | nab.com.au | 295 |
| 160 | `hsbc_premier_world_elite` | HSBC Premier World Elite Mastercard | hsbc.com.au | 0 |
| 161 | `bankwest_more_platinum` | Bankwest More Platinum Mastercard | bankwest.com.au | 160 |
| 162 | `st_george_amplify_rewards_signature` | St.George Amplify Rewards Signature | stgeorge.com.au | 279 |
| 163 | `virgin_money_high_flyer` | Virgin Money High Flyer Credit Card | virginmoney.com.au | 289 |
| 164 | `macquarie_rate_saver` | Macquarie Rate Saver Credit Card | macquarie.com.au | 0 |
| 165 | `citibank_premier_au` | Citi Premier Credit Card AU | citibank.com.au | 300 |


### 🇨🇳 China (147)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `icbc_universal` | ICBC 工银生肖信用卡 | icbc.com.cn | 0 |
| 2 | `icbc_platinum` | ICBC 工银白金信用卡 | icbc.com.cn | 3600 |
| 3 | `icbc_unipay_dual` | ICBC 工银标准信用卡 | icbc.com.cn | 100 |
| 4 | `ccb_longcard` | CCB 龙卡标准信用卡 | ccb.com | 0 |
| 5 | `ccb_unionsupreme` | CCB 尊享白金信用卡 | ccb.com | 3600 |
| 6 | `abc_kins_gold` | ABC 金穗标准信用卡 | abchina.com | 160 |
| 7 | `boc_standard_gold` | BOC 中银标准信用卡 | boc.cn | 100 |
| 8 | `cmb_all_currency_white` | CMB 招商银行全币种国际白金卡 | cmbchina.com | 0 |
| 9 | `boc_air_china_visa` | BOC 中国银行国航知音联名卡 | boc.cn | 0 |
| 10 | `ccb_jd_joy` | CCB 建设银行京东Joy联名卡 | ccb.com | 0 |
| 11 | `abc_national_treasure` | ABC 农业银行国家宝藏联名卡 | abchina.com | 0 |
| 12 | `icbc_forbiddencity` | ICBC 工商银行故宫联名卡 | icbc.com.cn | 0 |
| 13 | `spdb_bilibili` | SPDB 浦发银行Bilibili联名卡 | spdb.com.cn | 0 |
| 14 | `ceb_tiktok` | CEB 光大银行抖音联名卡 | cebbank.com | 0 |
| 15 | `bocom_eleme` | BOCOM 交通银行饿了么联名卡 | bankcomm.com | 0 |
| 16 | `citic_ihg_gold` | CITIC 中信银行IHG联名金卡 | citicbank.com.cn | 0 |
| 17 | `guangfa_meituan` | GF 广发银行美团联名卡 | cgbchina.com.cn | 0 |
| 18 | `minsheng_skypass_visa` | CMBC 民生银行大韩航空联名卡 | cmbc.com.cn | 0 |
| 19 | `pingan_costco` | PAB 平安银行Costco联名卡 | pingan.com | 0 |
| 20 | `pab_auto_owner` | PAB 平安银行车主信用卡 | pingan.com | 300 |
| 21 | `industrial_bank_taobao` | CIB 兴业银行淘宝联名卡 | cib.com.cn | 0 |
| 22 | `czbank_donkey_card` | CZBank 浙商银行驴妈妈联名卡 | czbank.com | 0 |
| 23 | `nb_starbucks` | NB 南京银行星巴克联名卡 | njcb.com.cn | 0 |
| 24 | `bos_disney` | BOS 上海银行迪士尼联名卡 | bankofshanghai.com | 0 |
| 25 | `bob_happy_travel` | BOB 北京银行悦行白金卡 | bankofbeijing.com.cn | 0 |
| 26 | `hxb_gundam` | HXB 华夏银行高达联名卡 | hxb.com.cn | 0 |
| 27 | `cmbc_bilibili` | CMBC 民生银行Bilibili联名卡 | cmbc.com.cn | 0 |
| 28 | `cmbc_ladies_card` | CMBC 民生银行女人优游信用卡 | cmbc.com.cn | 0 |
| 29 | `cmb_young_card` | CMB 招商银行YOUNG卡 | cmbchina.com | 0 |
| 30 | `icbc_visa_infinite` | ICBC 工银Visa无限卡 | icbc.com.cn | 2000 |
| 31 | `boc_world_elite` | BOC 中行世界之极卡 | boc.cn | 3600 |
| 32 | `ccb_muse_card` | CCB龙卡MUSE信用卡 | ccb.com | 0 |
| 33 | `abc_visa_signature` | ABC 农行Visa金穗全币种卡 | abchina.com | 0 |
| 34 | `spdb_ae_white_3` | SPDB 浦发美运白金卡 | spdb.com.cn | 3600 |
| 35 | `ceb_luxury_white` | CEB 光大奢享白金卡 | cebbank.com | 1188 |
| 36 | `bocom_white_point` | BOCOM 交行白金信用卡 | bankcomm.com | 1000 |
| 37 | `citic_safari_card` | CITIC 中信Safari卡 | citicbank.com.cn | 480 |
| 38 | `guangfa_nba_card` | GF 广发NBA联名信用卡 | cgbchina.com.cn | 0 |
| 39 | `industrial_pass_card` | CIB 兴业行卡标准版 | cib.com.cn | 2600 |
| 40 | `pab_pingan_bank_card` | PAB 平安标准卡 | pingan.com | 0 |
| 41 | `hxb_elite_platinum_4` | HXB 华夏精英尊尚白金卡 | hxb.com.cn | 680 |
| 42 | `czbank_standard_gold` | CZBank 浙商标准金卡 | czbank.com | 0 |
| 43 | `nb_city_card` | NB 南京银行城市卡 | njcb.com.cn | 0 |
| 44 | `bos_shanghai_card` | BOS 上海银行标准卡 | bankofshanghai.com | 0 |
| 45 | `bob_world_platinum` | BOB 北京银行世界白金卡 | bankofbeijing.com.cn | 0 |
| 46 | `huaxia_elite_platinum_4` | Huaxia 华夏精英白金卡 | hxb.com.cn | 0 |
| 47 | `cmb_bird_card` | CMB 招商银行百鸟朝凤信用卡 | cmbchina.com | 0 |
| 48 | `spdb_angry_birds` | SPDB 浦发愤怒的小鸟联名卡 | spdb.com.cn | 0 |
| 49 | `bos_coffee_card` | BOS 上海银行咖啡联名卡 | bankofshanghai.com | 0 |
| 50 | `minsheng_travel_platinum` | CMBC 民生商旅白金信用卡 | cmbc.com.cn | 600 |
| 51 | `icbc_meituan_card` | ICBC 工行美团联名信用卡 | icbc.com.cn | 0 |
| 52 | `boc_standard_gold_2` | BOC 中银标准信用卡金卡 | boc.cn | 100 |
| 53 | `ccb_longcard_gold` | CCB 龙卡标准信用卡金卡 | ccb.com | 160 |
| 54 | `abc_kins_standard` | ABC 金穗标准信用卡 | abchina.com | 80 |
| 55 | `cmb_all_currency_visa` | CMB 招行全币种国际VISA卡 | cmbchina.com | 0 |
| 56 | `spdb_standard_white` | SPDB 浦发标准白金卡 | spdb.com.cn | 680 |
| 57 | `ceb_standard_white` | CEB 光大标准白金卡 | cebbank.com | 680 |
| 58 | `cib_standard_white` | CIB 兴业标准白金卡 | cib.com.cn | 680 |
| 59 | `pab_standard_white` | PAB 平安标准白金卡 | pingan.com | 680 |
| 60 | `psbc_dingsheng_platinum` | PSBC 邮储鼎盛白金信用卡 | psbc.com | 2600 |
| 61 | `psbc_dingzhi_platinum` | PSBC 邮储鼎致白金信用卡 | psbc.com | 2600 |
| 62 | `psbc_unionpay_standard` | PSBC 邮储银联标准信用卡 | psbc.com | 0 |
| 63 | `jsb_standard` | JSB 江苏银行标准信用卡 | jsbchina.cn | 0 |
| 64 | `srcb_xinyi` | SRCB 上海农商银行鑫意信用卡 | srcb.com | 0 |
| 65 | `gzcb_card` | GZB 广州银行信用卡 | gzcb.com.cn | 0 |
| 66 | `cmb_classic_white` | CMB 招商银行经典白金卡 | cmbchina.com | 3600 |
| 67 | `cmb_jd_plus` | CMB 招商银行京东PLUS联名卡 | cmbchina.com | 0 |
| 68 | `citic_yan` | CITIC 中信银行颜卡 | citicbank.com.cn | 0 |
| 69 | `bocom_y_power` | BOCOM 交通银行Y-POWER卡 | bankcomm.com | 0 |
| 70 | `pingan_byou` | PAB 平安由你卡 | pingan.com | 0 |
| 71 | `cgb_zhenqing` | CGB 广发真情卡 | cgbchina.com.cn | 0 |
| 72 | `boc_great_wall` | BOC 中国银行长城环球通信用卡 | boc.cn | 0 |
| 73 | `ccb_dragon_amex` | CCB 建设银行龙卡美国运通卡 | ccb.com | 580 |
| 74 | `abc_jcb_gold` | ABC 农业银行金穗JCB金卡 | abchina.com | 0 |
| 75 | `icbc_marvel` | ICBC 工商银行漫威信用卡 | icbc.com.cn | 0 |
| 76 | `bocom_disney` | BOCOM 交通银行迪士尼卡 | bankcomm.com | 0 |
| 77 | `spdb_simple_white` | SPDB 浦发银行简约白金卡 | spdb.com.cn | 360 |
| 78 | `ceb_sunshine` | CEB 光大银行阳光信用卡 | cebbank.com | 0 |
| 79 | `cib_xingdongli` | CIB 兴业银行兴动力卡 | cib.com.cn | 0 |
| 80 | `hxb_youth` | HXB 华夏银行青春信用卡 | hxb.com.cn | 0 |
| 81 | `cmbc_qq` | CMBC 民生银行QQ联名卡 | cmbc.com.cn | 0 |
| 82 | `citic_i_platinum` | CITIC 中信银行i白金卡 | citicbank.com.cn | 200 |
| 83 | `spdb_dream` | SPDB 浦发银行梦卡 | spdb.com.cn | 0 |
| 84 | `cmb_hello_kitty` | CMB 招商银行Hello Kitty卡 | cmbchina.com | 0 |
| 85 | `guangfa_visa_gold` | CGB 广发Visa金卡 | cgbchina.com.cn | 0 |
| 86 | `cmb_taobao` | CMB 招商银行淘宝联名卡 | cmbchina.com | 0 |
| 87 | `citic_starbucks` | CITIC 中信银行星巴克联名卡 | citicbank.com.cn | 0 |
| 88 | `cmb_doraemon` | CMB 招商银行哆啦A梦JCB卡 | cmbchina.com | 0 |
| 89 | `icbc_e_card` | ICBC 工商银行e卡 | icbc.com.cn | 0 |
| 90 | `spdb_jd` | SPDB 浦发银行京东联名卡 | spdb.com.cn | 0 |
| 91 | `bocom_starbucks` | BOCOM 交通银行星巴克卡 | bankcomm.com | 0 |
| 92 | `pingan_aoyou` | PAB 平安傲游信用卡 | pingan.com | 0 |
| 93 | `cmbc_netease` | CMBC 民生银行网易联名卡 | cmbc.com.cn | 0 |
| 94 | `boc_ufan` | BOC 中国银行UFan卡 | boc.cn | 0 |
| 95 | `cgb_diy` | CGB 广发DIY信用卡 | cgbchina.com.cn | 0 |
| 96 | `abc_taobao` | ABC 农业银行淘宝联名卡 | abchina.com | 0 |
| 97 | `ceb_disney` | CEB 光大银行迪士尼联名卡 | cebbank.com | 0 |
| 98 | `icbc_alipay` | ICBC 工商银行支付宝联名卡 | icbc.com.cn | 0 |
| 99 | `nb_youth` | NBCB 宁波银行汇通青春卡 | nbcb.com.cn | 0 |
| 100 | `cib_credit_easy` | CIB 兴业银行信用易卡 | cib.com.cn | 0 |
| 101 | `cmb_classic_platinum` | CMB Classic Platinum Card | cmbchina.com | 3600 |
| 102 | `bocom_yuyi_white` | BOCOM Yuyi White Platinum Card | bankcomm.com | 500 |
| 103 | `guangfa_highspeed_white` | CGB High-Speed Rail Platinum Card | cgbchina.com.cn | 800 |
| 104 | `spdb_ae_white` | SPDB American Express Platinum Card | spdb.com.cn | 3600 |
| 105 | `citic_yicard_white` | CITIC YiCard Platinum Card | citicbank.com | 480 |
| 106 | `abc_youran_white` | ABC Youran Platinum Card | abchina.com | 300 |
| 107 | `boc_greatwall_crossborder` | BOC Great Wall Cross-Border Mastercard | boc.cn | 0 |
| 108 | `icbc_global_travel` | ICBC Global Travel Platinum Card | icbc.com.cn | 2000 |
| 109 | `pingan_car_owner_gold` | PAB Car Owner Platinum Card | pingan.com | 300 |
| 110 | `industrial_bank_xingdong` | CIB Xingdong Platinum Card | cib.com.cn | 500 |
| 111 | `icbc_constellation_card` | ICBC Constellation Credit Card | icbc.com.cn | 0 |
| 112 | `boc_air_china_olympic` | BOC Air China Platinum Card | boc.cn | 800 |
| 113 | `ccb_long_joy_white` | CCB Long Card Joy Platinum Card | ccb.com | 580 |
| 114 | `abc_national_treasure_white` | ABC National Treasure Platinum Card | abchina.com | 500 |
| 115 | `spdb_bilibili_card` | SPDB Bilibili Co-branded Credit Card | spdb.com.cn | 0 |
| 116 | `ceb_tiktok_card` | CEB Douyin Co-branded Credit Card | cebbank.com | 0 |
| 117 | `citic_ihg_premier` | CITIC IHG One Rewards Platinum Card | citicbank.com | 480 |
| 118 | `guangfa_meituan_card` | CGB Meituan Co-branded Credit Card | cgbchina.com.cn | 0 |
| 119 | `pingan_costco_card` | PAB Costco Co-branded Credit Card | pingan.com | 0 |
| 120 | `icbc_universal_gold` | ICBC Zodiac Gold Card | icbc.com.cn | 200 |
| 121 | `icbc_wechat_card` | ICBC WeChat Co-branded Card | icbc.com.cn | 0 |
| 122 | `icbc_jd_joy` | ICBC JD Joy Co-branded Card | icbc.com.cn | 0 |
| 123 | `icbc_marvel_card` | ICBC Marvel Co-branded Card | icbc.com.cn | 0 |
| 124 | `ccb_dragon_card_gold` | CCB Dragon Standard Gold Card | ccb.com | 160 |
| 125 | `ccb_supreme_white` | CCB Supreme Platinum Card | ccb.com | 3600 |
| 126 | `ccb_bilibili_card` | CCB Bilibili Co-branded Card | ccb.com | 0 |
| 127 | `ccb_meituan_card` | CCB Meituan Co-branded Card | ccb.com | 0 |
| 128 | `ccb_etc_card` | CCB Dragon ETC Car Owner Card | ccb.com | 200 |
| 129 | `abc_taobao_card` | ABC Taobao Co-branded Card | abchina.com | 0 |
| 130 | `boc_greatwall_globetrotter` | BOC Great Wall Globetrotter White Card | boc.cn | 800 |
| 131 | `boc_pinduoduo_card` | BOC Pinduoduo Co-branded Card | boc.cn | 0 |
| 132 | `cmb_bilibili_card` | CMB Bilibili Co-branded Card | cmbchina.com | 0 |
| 133 | `bocom_eleme_card` | BOCOM Eleme Co-branded Card | bankcomm.com | 0 |
| 134 | `bocom_kind_white` | BOCOM Yuyi White Card Red Edition | bankcomm.com | 500 |
| 135 | `bocom_standard_gold` | BOCOM Standard Gold Card | bankcomm.com | 140 |
| 136 | `spdb_dream_card` | SPDB Dream Card Standard White | spdb.com.cn | 0 |
| 137 | `spdb_jd_card` | SPDB JD Co-branded Card | spdb.com.cn | 0 |
| 138 | `citic_standard_white` | CITIC Standard Platinum Card | citicbank.com | 480 |
| 139 | `citic_qq_vip` | CITIC QQ Super VIP Card | citicbank.com | 0 |
| 140 | `guangfa_鼎极白金` | CGB Dingji Platinum Card | cgbchina.com.cn | 800 |
| 141 | `minsheng_standard_white` | CMBC Standard Platinum Card | cmbc.com.cn | 600 |
| 142 | `ceb_阳光标准金卡` | CEB Sunshine Standard Gold Card | cebbank.com | 200 |
| 143 | `ceb_jd_joy` | CEB JD Joy Co-branded Card | cebbank.com | 0 |
| 144 | `cib_taobao_card` | CIB Taobao Co-branded Card | cib.com.cn | 0 |
| 145 | `cib_pass_white` | CIB Pass Platinum Card | cib.com.cn | 900 |
| 146 | `czb_rainbow_card` | CZB Rainbow Credit Card | czbank.com | 0 |
| 147 | `hb_elite_platinum_4` | HXB Elite Platinum Card | hxb.com.cn | 600 |


### 🇹🇼 Taiwan (156)

| # | id | name | issuer | annual fee |
|--:|----|------|--------|-----------:|
| 1 | `hsbc_live_plus` | HSBC Live+ Cash Back | hsbc.com.tw | 2000 |
| 2 | `taishin_richart` | Taishin Richart Card | taishinbank.com.tw | 3000 |
| 3 | `dbs_eco` | DBS eco Card | dbs.com.tw | 3000 |
| 4 | `hsbc_diamond` | HSBC Diamond Card | hsbc.com.tw | 2000 |
| 5 | `hsbc_cashback_visa` | HSBC Cash Back Visa Platinum | hsbc.com.tw | 2000 |
| 6 | `feb_happy_plus` | Far Eastern Bank Happy+ Card | feib.com.tw | 2000 |
| 7 | `amex_centurion_platinum` | Amex Centurion Platinum | americanexpress.com.tw | 36800 |
| 8 | `feb_happy` | Far Eastern Bank Happy Card | feib.com.tw | 1200 |
| 9 | `feb_happy_travel` | Far Eastern Bank Happy Travel Card | feib.com.tw | 2000 |
| 10 | `esun_pi_wallet` | E.Sun Pi Wallet Card | esunbank.com.tw | 3000 |
| 11 | `sinopac_protection` | SinoPac Protection Card | sinopac.com | 1500 |
| 12 | `sinopac_dual_currency` | SinoPac Dual Currency Card | sinopac.com | 1500 |
| 13 | `sinopac_green_cashback` | SinoPac Green Cash Back Card | sinopac.com | 1500 |
| 14 | `first_ileo` | First Bank iLEO Card | firstbank.com.tw | 1200 |
| 15 | `first_ipass` | First Bank iPass Card | firstbank.com.tw | 1200 |
| 16 | `sinopac_daway` | SinoPac DAWAY Card | sinopac.com | 1500 |
| 17 | `feb_world_business` | Far Eastern Bank World Business Card | feib.com.tw | 10000 |
| 18 | `feb_cest_moi` | Far Eastern Bank C'est Moi Card | feib.com.tw | 2000 |
| 19 | `amex_eva_centurion_platinum` | Amex EVA Air Centurion Platinum | americanexpress.com.tw | 36800 |
| 20 | `cathay_asia_miles_titanium` | Cathay United Asia Miles Titanium | cathaybk.com.tw | 1800 |
| 21 | `cathay_asia_miles_lixiang` | Cathay United Asia Miles Li-Xiang | cathaybk.com.tw | 0 |
| 22 | `cathay_asia_miles_platinum` | Cathay United Asia Miles Platinum | cathaybk.com.tw | 600 |
| 23 | `cathay_asia_miles_world` | Cathay United Asia Miles World Card | cathaybk.com.tw | 8000 |
| 24 | `taishin_friday` | Taishin friDay Card | taishinbank.com.tw | 1500 |
| 25 | `taishin_mitsukoshi` | Taishin Shin Kong Mitsukoshi | taishinbank.com.tw | 1500 |
| 26 | `fubon_j` | Taipei Fubon J Card | fubon.com | 1800 |
| 27 | `fubon_ju` | Taipei Fubon JU Card | fubon.com | 1800 |
| 28 | `taishin_infinite` | Taishin Infinite Card | taishinbank.com.tw | 10000 |
| 29 | `rakuten_tiger` | Rakuten Tiger Card | rakuten.com.tw | 0 |
| 30 | `rakuten_fly` | Rakuten Fly Card | rakuten.com.tw | 0 |
| 31 | `rakuten_panda_j` | Rakuten Panda J Card | rakuten.com.tw | 0 |
| 32 | `first_living_green` | First Bank Living Green Card | firstbank.com.tw | 1200 |
| 33 | `first_travel` | First Bank Travel Card | firstbank.com.tw | 2000 |
| 34 | `first_icash` | First Bank icash Card | firstbank.com.tw | 1200 |
| 35 | `sinopac_sport` | SinoPac Sport Card | sinopac.com | 1500 |
| 36 | `ctbc_line_pay` | CTBC Line Pay Card | ctbcbank.com | 1500 |
| 37 | `esun_unicard` | E.Sun Unicard | esunbank.com.tw | 3000 |
| 38 | `esun_u_bear` | E.Sun U Bear Card | esunbank.com.tw | 3000 |
| 39 | `esun_kumamon` | E.Sun Kumamon Card | esunbank.com.tw | 3000 |
| 40 | `taishin_everrich_infinite` | Taishin Everrich Infinite Card | taishinbank.com.tw | 10000 |
| 41 | `sinopac_jcb_cashback` | SinoPac JCB Cash Back Card | sinopac.com | 1500 |
| 42 | `taishin_pxmart` | Taishin PX Mart Card | taishinbank.com.tw | 1500 |
| 43 | `taishin_mercuries_life` | Taishin Mercuries Life Card | taishinbank.com.tw | 1500 |
| 44 | `taishin_everrich` | Taishin Everrich Card | taishinbank.com.tw | 1500 |
| 45 | `taishin_tsann_kuen` | Taishin Tsann Kuen Card | taishinbank.com.tw | 1500 |
| 46 | `taishin_cathay_flying` | Taishin Cathay Pacific Flying | taishinbank.com.tw | 1800 |
| 47 | `taishin_cathay_titanium` | Taishin Cathay Pacific Titanium | taishinbank.com.tw | 600 |
| 48 | `taishin_cathay_world` | Taishin Cathay Pacific World | taishinbank.com.tw | 8000 |
| 49 | `taishin_business` | Taishin Business Card | taishinbank.com.tw | 1500 |
| 50 | `hsbc_traveler_signature` | HSBC Traveler Signature | hsbc.com.tw | 2500 |
| 51 | `cathay_cube` | Cathay United CUBE Card | cathaybk.com.tw | 0 |
| 52 | `fubon_momo` | Fubon momo Card | fubon.com | 0 |
| 53 | `taishin_jkopay` | Taishin JKO Pay Card | taishinbank.com.tw | 0 |
| 54 | `taishin_flygo` | Taishin FlyGo Card | taishinbank.com.tw | 0 |
| 55 | `ctbc_foodpanda` | CTBC foodpanda Card | ctbcbank.com | 0 |
| 56 | `union_lai` | Union Bank Lai Points Card | unionbank.com.tw | 0 |
| 57 | `nextbank_dajiang` | Next Bank Da Jiang Card | nextbank.com.tw | 0 |
| 58 | `obank_orange` | O-Bank O! Range Card | o-bank.com | 0 |
| 59 | `shanghai_minions` | SCSB Minions Card | scsb.com.tw | 0 |
| 60 | `mega_liduo` | Mega Lots Signature Card | megabank.com.tw | 0 |
| 61 | `hncb_sny` | Hua Nan SnY Card | hncb.com.tw | 0 |
| 62 | `yuanta_diamond` | Yuanta Diamond Card | yuantabank.com.tw | 0 |
| 63 | `scb_cashback` | Standard Chartered Cashback Signature | sc.com.tw | 0 |
| 64 | `esun_only` | E.SUN Only Card | esunbank.com.tw | 0 |
| 65 | `kgi_cashback` | KGI Cashback Signature | kgibank.com.tw | 0 |
| 66 | `taishin_gogo` | Taishin @GoGo Card | taishinbank.com.tw | 0 |
| 67 | `chb_mylove` | Chang Hwa My Love Cashback Card | bankchb.com | 0 |
| 68 | `skbank_global` | Shin Kong Global Cashback Card | skbank.com.tw | 0 |
| 69 | `tbb_sustainable_life` | TBB Sustainable Life Card | tbb.com.tw | 0 |
| 70 | `bot_cashback` | Bank of Taiwan Cashback Card | bot.com.tw | 0 |
| 71 | `tcb_cashback` | TCB Cashback Card | tcb-bank.com.tw | 0 |
| 72 | `landbank_jcb` | Land Bank JCB Card | landbank.com.tw | 0 |
| 73 | `ctbc_costco` | CTBC Costco Co-branded Card | ctbcbank.com | 0 |
| 74 | `cathay_koko` | Cathay United KOKO Combo | cathaybk.com.tw | 0 |
| 75 | `ctbc_the_royal` | CTBC The Royal Signature | ctbcbank.com | 3600 |
| 76 | `esun_e_card` | E.SUN e Card | esunbank.com.tw | 0 |
| 77 | `cathay_eva` | Cathay United EVA Air Co-branded Card | cathaybk.com.tw | 1800 |
| 78 | `esun_world_card` | E.SUN World Card | esunbank.com.tw | 3600 |
| 79 | `fubon_digital_life` | Fubon Digital Life Card | fubon.com | 0 |
| 80 | `taishin_world` | Taishin World Card | taishinbank.com.tw | 3600 |
| 81 | `ctbc_dream_infinite` | CTBC Dream Card Infinite | ctbcbank.com | 20000 |
| 82 | `union_jihe` | Union Bank Jihe Card | unionbank.com.tw | 0 |
| 83 | `kgi_evolution` | KGI Evolution Cashback Card | kgibank.com.tw | 0 |
| 84 | `mega_e` | Mega e-Swipe Signature Card | megabank.com.tw | 0 |
| 85 | `hncb_ishopping` | Hua Nan i-Shopping Life Card | hncb.com.tw | 0 |
| 86 | `tbb_ipass` | TBB iPASS Co-branded Card | tbb.com.tw | 0 |
| 87 | `scsb_cashback` | SCSB Cashback Card | scsb.com.tw | 0 |
| 88 | `skbank_emma` | Shin Kong emma Card | skbank.com.tw | 0 |
| 89 | `entie_cashback` | Entie Bank Cashback Card | entiebank.com.tw | 0 |
| 90 | `ktb_card` | King’s Town Bank Credit Card | ktb.com.tw | 0 |
| 91 | `sunny_bank_card` | Sunny Bank Credit Card | sunnybank.com.tw | 0 |
| 92 | `bok_card` | Bank of Kaohsiung Credit Card | bok.com.tw | 0 |
| 93 | `panhsin_card` | Bank of Panhsin Credit Card | bop.com.tw | 0 |
| 94 | `taichung_bank_card` | Taichung Commercial Bank Credit Card | tcbbank.com.tw | 0 |
| 95 | `cota_bank_card` | COTA Commercial Bank Credit Card | cotabank.com.tw | 0 |
| 96 | `ctbc_ana` | CTBC ANA Co-branded Card | ctbcbank.com | 1800 |
| 97 | `first_ieco` | First Bank iECO Card | firstbank.com.tw | 0 |
| 98 | `esun_dual_currency` | E.SUN Dual Currency Card | esunbank.com.tw | 0 |
| 99 | `rakuten_world` | Rakuten Card World | rakuten.com.tw | 0 |
| 100 | `yuanta_digital` | Yuanta Digital Diamond Card | yuantabank.com.tw | 0 |
| 101 | `fubon_j_card` | Fubon J Card | fubon.com | 0 |
| 102 | `fubon_momo_card` | Fubon momo Card | fubon.com | 0 |
| 103 | `union_jihe_card` | Union Bank Jihe Card | ubot.com.tw | 0 |
| 104 | `union_laidian_card` | Union Bank Lai Points Card | ubot.com.tw | 0 |
| 105 | `ctbc_linepay_card` | CTBC LINE Pay Card | ctbcbank.com | 0 |
| 106 | `sinopac_sport_card` | SinoPac SPORT Card | sinopac.com | 0 |
| 107 | `sinopac_daway_card` | SinoPac DAWAY Card | sinopac.com | 0 |
| 108 | `dbs_eco_card` | DBS eco Card | dbs.com.tw | 0 |
| 109 | `taishin_gogo_card` | Taishin @GoGo Card | taishinbank.com.tw | 0 |
| 110 | `cathay_cube_card` | Cathay United CUBE Card | cathaybk.com.tw | 0 |
| 111 | `hsbc_live_plus_tw` | HSBC Live+ Cash Back Card | hsbc.com.tw | 0 |
| 112 | `ctbc_foodpanda_card` | CTBC foodpanda Co-branded Card | ctbcbank.com | 0 |
| 113 | `taishin_flygo_card` | Taishin FlyGo Card | taishinbank.com.tw | 0 |
| 114 | `sinopac_daway_line` | SinoPac DAWAY LINE Pay Card | sinopac.com | 0 |
| 115 | `nextbank_dajiang_card` | Next Bank Da Jiang Card | nextbank.com.tw | 0 |
| 116 | `first_ileo_card` | First Bank iLEO Card | firstbank.com.tw | 0 |
| 117 | `yuanta_diamond_card` | Yuanta Diamond Card | yuantabank.com.tw | 0 |
| 118 | `hncb_sny_card` | Hua Nan SnY Credit Card | hncb.com.tw | 0 |
| 119 | `shanghai_minions_card` | SCSB Minions Card | scsb.com.tw | 0 |
| 120 | `cathay_koko_combo` | Cathay United KOKO Combo Card | cathaybk.com.tw | 0 |
| 121 | `cathay_eva_air_co` | Cathay EVA Air Co-branded Card | cathaybk.com.tw | 2400 |
| 122 | `ctbc_costco_card` | CTBC Costco Co-branded Card | ctbcbank.com | 0 |
| 123 | `ctbc_the_royal_signature` | CTBC The Royal Signature Card | ctbcbank.com | 0 |
| 124 | `ctbc_ana_card` | CTBC ANA Co-branded Card | ctbcbank.com | 2000 |
| 125 | `fubon_open_possible` | Fubon Open Possible Card | fubon.com | 0 |
| 126 | `taishin_richart_card` | Taishin Richart Card | taishinbank.com.tw | 0 |
| 127 | `taishin_rose_giving` | Taishin Rose Giving Card | taishinbank.com.tw | 0 |
| 128 | `taishin_street_pay` | Taishin Street Pay Card | taishinbank.com.tw | 0 |
| 129 | `esun_only_card` | E.SUN Only Card | esunbank.com.tw | 0 |
| 130 | `sinopac_protection_card` | SinoPac Protection Card | sinopac.com | 0 |
| 131 | `dbs_everyday_card` | DBS Everyday Titanium Card | dbs.com.tw | 0 |
| 132 | `dbs_flyer_world` | DBS Flyer World Card | dbs.com.tw | 3600 |
| 133 | `hsbc_travel_titanium` | HSBC Travel Titanium Card | hsbc.com.tw | 2500 |
| 134 | `feb_happy_card` | Far Eastern Happy Go Card | feib.com.tw | 0 |
| 135 | `union_green_card` | Union Bank Green Card | ubot.com.tw | 0 |
| 136 | `first_ipass_card` | First Bank iPASS Card | firstbank.com.tw | 0 |
| 137 | `first_ieco_card` | First Bank iECO Card | firstbank.com.tw | 0 |
| 138 | `mega_liduo_card` | Mega Lots Signature Card | megabank.com.tw | 0 |
| 139 | `mega_e_card` | Mega e-Swipe Signature Card | megabank.com.tw | 0 |
| 140 | `mega_gogoro_card` | Mega Gogoro Co-branded Card | megabank.com.tw | 0 |
| 141 | `skbank_global_cashback` | Shin Kong Global Cashback Card | skbank.com.tw | 0 |
| 142 | `skbank_emma_card` | Shin Kong emma Card | skbank.com.tw | 0 |
| 143 | `tbb_ipass_card` | TBB iPASS Card | tbb.com.tw | 0 |
| 144 | `yuanta_digital_diamond` | Yuanta Digital Diamond Card | yuantabank.com.tw | 0 |
| 145 | `scb_cashback_signature` | Standard Chartered Cashback Signature | sc.com/tw | 0 |
| 146 | `kgi_cashback_signature` | KGI Cashback Signature Card | kgibank.com.tw | 0 |
| 147 | `kgi_evolution_card` | KGI Evolution Card | kgibank.com.tw | 0 |
| 148 | `rakuten_world_card` | Rakuten World Card | card.rakuten.com.tw | 0 |
| 149 | `rakuten_jcb_card` | Rakuten JCB Card | card.rakuten.com.tw | 0 |
| 150 | `entie_cashback_card` | Entie Cashback Card | entiebank.com.tw | 0 |
| 151 | `ktb_credit_card` | King Town Bank Credit Card | ktb.com.tw | 0 |
| 152 | `bok_credit_card` | Bank of Kaohsiung Credit Card | bok.com.tw | 0 |
| 153 | `panhsin_credit_card` | Bank of Panhsin Credit Card | panhsin.com.tw | 0 |
| 154 | `bot_cashback_card` | Bank of Taiwan Cashback Card | bot.com.tw | 0 |
| 155 | `tcb_cashback_card` | TCB Cashback Card | tcb-bank.com.tw | 0 |
| 156 | `landbank_jcb_card` | Land Bank JCB Card | landbank.com.tw | 0 |


