# Research: مطعم ثقة الشام / Thiqat Al-Sham Restaurant

Phase 1 research for the restaurant website. Checked on **2026-11-21**; HungerStation data added **2026-11-22** (Asia/Riyadh).

**Status key**
- **VERIFIED**: confirmed by 2+ independent sources, or by the restaurant's own source plus another source, or confirmed by Blox (site owner, lives next to the restaurant).
- **UNVERIFIED**: only one source, or could not be opened. Do not publish until confirmed.

Screenshots of key sources: `research/evidence/`. Menu data: `data/menu.json`. HungerStation data: `research/hungerstation-2026-11-22.json`. Image sources: `credits.json`.

---

## 1. Sources used

| Code | Source | URL | Who published it | Result |
|---|---|---|---|---|
| **G** | Google Maps listing | [Place page](https://www.google.com/maps/place/%D9%85%D8%B7%D8%B9%D9%85+%D8%AB%D9%82%D8%A9+%D8%A7%D9%84%D8%B4%D8%A7%D9%85/@27.4718889,48.4695686,17z/data=!4m6!3m5!1s0x3fccbbdc5f69e09d:0x84b90311b2f79988!8m2!3d27.4718889!4d48.4695686!16s%2Fg%2F11yrlkz3ks) (place id `0x3fccbbdc5f69e09d:0x84b90311b2f79988`) | Google, with an owner photo | Opened (signed-out "limited view": only today's hours shown) |
| **M** | Restaurant's own online menu | https://thiqat-alshaam.menus-sa.com/ar and `/en` | Restaurant (linked as "Website" on G) | Opened: full menu, prices, links |
| **SC** | Snapchat @thiqat.sa | https://www.snapchat.com/@thiqat.sa | Restaurant | Opened: bio, 49 story snaps (15–21 Nov 2026), 29 Spotlight posts (6–19 Nov 2026) |
| **HS** | HungerStation branch 180455 | https://hungerstation.com/sa-ar/restaurant/alnuayreayh/al-faisaliyah/180455 | Restaurant's delivery listing | Blocked from this cloud session (Cloudflare 403). **Read on 2026-11-22 18:50 by Claude in Blox's own browser** (Arabic + English pages); data in `research/hungerstation-2026-11-22.json` |
| **OSM** | OpenStreetMap reverse geocode | https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=27.4718889&lon=48.4695686 | OpenStreetMap | Opened |
| **IG** | Instagram @thiqat.sa | https://www.instagram.com/thiqat.sa | (linked from M; printed on pizza box) | **Could not open** (login wall) |
| **TT** | TikTok @thiqat.sa | https://www.tiktok.com/@thiqat.sa | (linked from M) | Opened: **"Couldn't find this account"** |
| — | Jahez, Keeta, The Chefz, Mrsool, Talabat, X, Facebook | web searches | — | **No listing/account found** |

---

## 2. Facts table

| Fact | Value | Source URLs | Date checked | Status |
|---|---|---|---|---|
| Name (Arabic) | مطعم ثقة الشام | G; M; SC; HS; storefront sign (G owner photo); pizza box (SC post 18 Nov 2026) | 2026-11-21 | **VERIFIED** |
| Name (English) | Thiqat Al-Sham (restaurant writes "Thiqat Al Sham" / "Thiqat Al-Sham"; handle `thiqat.sa`; subdomain `thiqat-alshaam`) | M (English items "Thiqat Al-Sham sauce", "Thiqat Al Sham pizza"); HS ("Thiqat Al Sham Restaurant"); SC handle | 2026-11-22 | **VERIFIED** |
| Cuisine | Levantine-style charcoal grills, shawarma, fatayer/pastries, plus pizza, burgers and breakfast | M (menu); HS (tags "Fast Food", "Arabic"); SC (posts of grill, shawarma, fatayer, pizza) | 2026-11-22 | **VERIFIED** |
| "Syrian" | No source says "Syrian". The name means "Trust of the Levant". | — | 2026-11-21 | **UNVERIFIED**: not used on site |
| Their own words (taglines) | "🥐 معجنات طازجة يوميًا" (fresh pastries daily), "🔥 مشاوي على الأصول" (grills done the proper way), "مخبوزة بحب" (baked with love, printed on pizza box), "شورما طازا" (fresh shawarma), "نسعد بخدمتكم" | SC bio; SC posts 17–19 Nov 2026 | 2026-11-21 | **VERIFIED** (restaurant's own text) |
| Street | Prince Sultan bin Abdulaziz St (الأمير سلطان بن عبد العزيز), Al-Nu'ayriyah | G; SC post 17 Nov 2026 ("مطعم ثقة الشام – الأمير سلطان بن عبد العزيز"); OSM | 2026-11-21 | **VERIFIED** |
| District | Al-Faisaliyah (حي الفيصلية) | G; OSM; HS (address "الفيصلية, النعيرية" and URL slug `al-faisaliyah`); **confirmed by Blox** | 2026-11-22 | **VERIFIED**. Conflict: SC bio says "حي الخليج" (see §3) |
| Postal code | 37451 | G only | 2026-11-21 | **UNVERIFIED** |
| Plus code / pin | FFC9+QR Nairyah → 27.4718889, 48.4695686 | G; HS map location 27.47188, 48.46959 (same spot); confirmed by Blox | 2026-11-22 | **VERIFIED** |
| Phone | +966 50 261 9361 (0502619361) | G; M (WhatsApp link); SC bio; pizza box | 2026-11-21 | **VERIFIED** |
| WhatsApp | +966502619361 (`https://wa.me/966502619361`) | M (`wa.me/+966502619361`) only. The pizza box shows the number next to a plain phone icon, not a WhatsApp logo. **Blox tested the website's WhatsApp button and it works** (2026-11-22). | 2026-11-22 | **VERIFIED** (restaurant's own link + tested by Blox) |
| Opening hours | **12:00–02:00** (12 noon–2 AM), Asia/Riyadh | G (12 PM–2 AM); SC image post 17 Nov 2026 ("من 12 الظهر الى 2 صباحاً", from Wed 18 Nov); confirmed by Blox | 2026-11-21 | **VERIFIED** (conflict: M still says 14:00, see §3). HS does not show hours. |
| Open every day incl. Friday | Assumed daily | No source lists days separately | 2026-11-22 | **UNVERIFIED** |
| Logo | Blue + yellow Arabic lettering "مطعم / ثقة / الشام" | M (585×702 screenshot of a design canvas); **HS (clean 1484×853 version)**; avatar of the Google account that posted the storefront photo; matches storefront sign | 2026-11-22 | **VERIFIED**. Clean vector redraw approved; HS version is the reference. |
| Brand colours | Blue ≈ `#00A0D4`, yellow ≈ `#F8DC10` (sampled from the clean HS logo) | HS logo; M logo; storefront sign photo | 2026-11-22 | **VERIFIED** (measured) |
| Menu: items & categories | 176 items in 9 categories (§4). HS lists 129 of them; no HS item is missing from M. | M; HS | 2026-11-22 | **VERIFIED** |
| Menu: prices | Restaurant menu (M): 1–120 SAR. HS is higher on 128 of 129 shared items, by 1–8 SAR (mostly +3 or +4); one item 1 SAR cheaper on HS. | M; HS | 2026-11-22 | **UNCONFIRMED** (all 176). The pattern fits M = in-store prices and HS = delivery prices. Site shows M prices. |
| Item descriptions | 119 of 176 items now have one: 6 from M (the restaurant's own), 113 from HS. Where HS had only English, or its English was wrong/cut off, we translated or rewrote it; each item's `description_source` says so. 57 items have none (not on HS). | M; HS | 2026-11-22 | **VERIFIED** source text (nothing invented) |
| "وتش" items | Means **pizza sandwich** (HS English: "Zinger Pizza Sandwich", "Sausage Pizza Style Sandwich Meal") | HS | 2026-11-22 | **VERIFIED** (HS); English names updated |
| What a "meal" includes | Burger, fajita, codo and samoli meals: fries/potatoes + a drink. Pizza-sandwich meals: Pepsi + fries. | HS descriptions; M (pizza-sandwich meals) | 2026-11-22 | **VERIFIED** for those items. Zinger and "bomb" meals: **UNVERIFIED**. Blox (2026-11-22): "probably some fries and a coke, but not confirmed; don't add." Nothing added. |
| Calories | HS shows calories for most items, but some look wrong (e.g. Medium/Large Mixed Cheese Pizza both 420; Large Mixed Grill 480 vs Small 849). Stored as `calories_hungerstation`, **not shown on the site**. M's own calories (6 items) are shown. Blox (2026-11-22): not yet OK to show the HS numbers. | HS; M | 2026-11-22 | **UNVERIFIED** (HS values, hidden) |
| Snapchat | @thiqat.sa, "مطعم ثقة الشام", active (last update 21 Nov 2026) | M (link); SC | 2026-11-21 | **VERIFIED** |
| Instagram | @thiqat.sa | M (link `instagram.com/thiqat.sa`); pizza box prints Instagram + Snapchat icons next to "thiqat.sa" (SC post 18 Nov 2026, `research/source-images/snapchat/st41_f*.jpg`) | 2026-11-22 | **VERIFIED** (two of the restaurant's own sources). I could not open the profile (login wall), but **Blox tested the website's Instagram link and it works** (2026-11-22). |
| TikTok | @thiqat.sa | M (link); TT says account not found | 2026-11-21 | Dead link, **not used** (Blox: drop it) |
| HungerStation | Branch 180455, Al-Faisaliyah: https://hungerstation.com/sa-ar/restaurant/alnuayreayh/al-faisaliyah/180455 | G ("Place an order" target); HS page read 2026-11-22 | 2026-11-22 | **VERIFIED** |
| Other delivery apps | None found (Jahez, Keeta, The Chefz, Mrsool, Talabat) | web searches | 2026-11-21 | Not found |
| Ratings | Google 4.2 (33 reviews); HS 4.5 (64 ratings) | G; HS | 2026-11-22 | Noted only. **Not shown on site** (they change) |
| Women-owned | Google attribute "Identifies as women-owned" | G only | 2026-11-21 | **UNVERIFIED**: not used |
| Opening date | Cake reading roughly "… افتتاح مطعم ثقة الشام" posted 6 Nov 2026; Snapchat created 1 Oct 2025; menu-site logo uploaded 25 Sep 2025 | SC; M metadata | 2026-11-21 | **UNVERIFIED** (my reading of handwriting) |
| Coming soon | "كرسبي فرايز" (Crispy Fries), not on menu yet | SC post 17 Nov 2026 | 2026-11-21 | Restaurant's own post; not added to menu |
| Customer reviews | Not used. No reviews or testimonials will appear on the site. | — | — | — |

---

## 3. Conflicts and how they were resolved

| # | Topic | What the sources say | Resolution |
|---|---|---|---|
| 1 | **Opening time** | M: **14:00**–02:00. G: **12 PM**–2 AM (Saturday shown). SC image post 17 Nov 2026, 20:32: "ابتداءً من غداً الاربعاء الدوام من 12 الظهر الى 2 صباحاً نسعد بخدمتكم" (from Wed 18 Nov, **12 noon**–2 AM). | **12:00–02:00**: matches G and the restaurant's newest post; confirmed by Blox. The menu site (M) is out of date. |
| 2 | **District** | G, OSM, HS: **Al-Faisaliyah**. SC bio and SC "address" field: **حي الخليج**. | **Al-Faisaliyah**, confirmed by Blox (lives next to it). |
| 3 | **Map pin** | G and HS: FFC9+QR (27.4718889, 48.4695686). M's map button (`maps.app.goo.gl/71kKec4p9uvUj9vUA`) drops a pin at FG9G+C24 (27.4685, 48.5250833), about 5.5 km east in Al-Khaleej (OSM). | **FFC9+QR**, confirmed by Blox. The menu site's pin is probably an older location; tell the owner to update it. |
| 4 | **Prices** | HS is higher than M on 128 of 129 shared items (usually +3/+4 SAR). | Site shows M's prices with the note "Prices may vary in store". HS prices kept in `price_hungerstation` for reference. |
| 5 | **English item names** | M's English names are machine-translated; 17 are wrong or missing (§5). | Corrected in `menu.json`; originals kept in `en_name_from_restaurant`. |
| 6 | **Menu photos** | Most photos on M look like stock/manufacturer images (e.g. Pepsi cans, reused pizza photos). | **Approved by Blox**: the owner uses them, so we use them. Logged in `credits.json`. |
| 7 | **Phone link** | M's call button is `tel:502619361` (missing 0/+966). | Site uses `tel:+966502619361`. Tell the owner their menu-site call button is broken. |
| 8 | **Shawarma on HS** | 14 shawarma items appear on HS's English page but not its Arabic page. | Kept on our menu (they are on M). **Resolved by Blox (2026-11-22):** none are unavailable, all shawarma items stay listed as available. |

---

## 4. Menu summary (`data/menu.json`)

Items and prices copied from **M** (the restaurant's own online menu) on 2026-11-21. Every item has `source`, `date_found`, `price_status: "unconfirmed"`, `price_hungerstation` (or null), and the photo URL in `image_source`.

| Category (AR / EN) | Items | Price range (SAR) | On HungerStation |
|---|---|---|---|
| سندويشات / Sandwiches | 17 | 8–20 | 17 |
| صحون / Plates | 23 | 5–120 | 22 |
| برجر / Burgers | 12 | 11–26 | 8 |
| البيتزا / Pizza | 48 | 11–31 | 42 |
| مقبلات / Appetizers | 6 | 1–20 | 6 |
| الفطائر / Fatayer & Pastries | 27 | 1–50 | 18 |
| صوصات / Sauces | 9 | 2–8 | 8 |
| مشروبات / Drinks | 17 | 1–3 | 8 |
| الافطار / Breakfast | 17 | 1–35 | 0 |
| **Total** | **176** | | **129** |

- **Descriptions:** 119 items. Nothing was invented. HungerStation's generic soft-drink and fries blurbs were not used. The 57 items without a description are left empty for the owner to fill.
- **English names:** 122 identical to the restaurant's, 37 spelling-fixed, 17 corrected (§5).

---

## 5. English names I corrected (owner should review)

| Arabic | Restaurant's English | Used on site |
|---|---|---|
| شيش طاووق صغير | large chiken awsal | Shish Tawook, Small |
| شيش طاووق جامبو | larg chiken awsal | Shish Tawook, Jumbo |
| شاورما صاروخ | shawarma medium | Rocket Shawarma (HS: "Sarookh Shawarma", a medium sandwich) |
| شاورما صامولي | shawarma sandwich | Samoli Shawarma |
| وجبة شاورما صامولي | shawarma sandwich meal | Samoli Shawarma Meal |
| كيلو مشويات مشكل | mashawie 1k | Mixed Grill (1 kg) |
| قارب لبنة | Brick boat | Labneh Boat |
| كينزا ببسي صغير 185 م | A small cola treasure | Kinza Cola, Small (185 ml) |
| كينزا ببسي كبير 360 م | kinza | Kinza Cola, Large (360 ml) |
| صحن بيض عيون | A plate of eggs | Sunny-Side-Up Eggs |
| قنبلة برجر دجاج | (Arabic only) | Chicken Burger Bomb |
| وتش بيتزا زنجر / شورما / نقانق, and the 3 "وجبه" versions (6 items) | (Arabic only) | Zinger / Shawarma / Sausage **Pizza Sandwich** (Meal), following HS's English |

---

## 6. Photos and logo (`credits.json`)

| What | Where from | Use |
|---|---|---|
| Logo, clean 1484×853 | HS listing (logo slot) | Reference for the clean SVG redraw (approved) |
| Logo, 585×702 screenshot of a design canvas | M | Backup reference |
| Storefront at night, 1600×900 | G, posted Nov 2026 by account "مطعم ثقة الشام" (logo avatar) | Location section / hero |
| Shawarma spit, 1242×2208 | SC image post 8 Nov 2026 | Food photo |
| 76 still frames from 19 of their videos (480–540 px wide): charcoal skewers, shawarma, fatayer, dough shaping, pizzas, branded box | SC stories/Spotlight 7–19 Nov 2026 | Food photos (Spotlight frames have a Snapchat watermark to crop) |
| 171 item photos | M | Menu item thumbnails (approved) |

**Excluded:** two SC posts carrying a **TikTok watermark** (likely reposted from someone else's TikTok), "Day in my…" collages (possible third-party template), and HS item photos and cover (we use M's photos; the HS cover is a cheese-pizza photo also on M).

**Quality warning:** the Snapchat videos are only 480–540 px wide, so they will look soft as full-width banners on large screens. Better originals from the owner (straight from their phone) would improve the site.

---

## 7. Questions for the owner before going live

1. **Friday:** same hours (12:00–02:00)? Their menu site still shows 14:00–02:00, so they should update it.
2. **Breakfast:** the menu has a breakfast category, but the shop opens at noon. When is breakfast served?
3. **Prices:** all 176 are "unconfirmed". Are the online-menu prices the in-store prices? (HungerStation's are higher.)
4. ~~**Instagram @thiqat.sa and WhatsApp:** is Instagram active? Is 0502619361 on WhatsApp?~~ *Answered: Blox tested both links on the website (2026-11-22) and they work.*
5. **Meals:** what comes with the Zinger meals and the "bomb" (قنبلة) meals? *Blox: probably fries and a Coke, not confirmed. Nothing is written on the site until the owner says.*
6. ~~**Shawarma:** HungerStation's Arabic page hides all 14 shawarma items. Are any of them unavailable?~~ *Answered by Blox: all available.*
7. **Calories:** OK to show HungerStation's calorie numbers? Several look wrong, so they're hidden for now. *Blox: not yet. They stay hidden.*
8. **Original logo file** and **original phone photos/videos**, if they have them (higher quality).
9. **Their own fixes:** the menu site's map pin (FG9G+C24), call button (`tel:502619361`) and hours (14:00) are wrong, the TikTok link is dead, and the Snapchat bio says حي الخليج.
10. **Postal code** 37451: correct?
11. **Women-owned** (Google attribute) and **opening date**: only mention if the owner wants.

---

## 8. How the website uses this research (Phase 2, 2026-11-22)

- **Shown on the site:** name, address (street + Al-Faisaliyah + Al-Nu'ayriyah), map pin FFC9+QR, phone, WhatsApp button, hours 12:00–02:00 every day, Snapchat, Instagram, HungerStation, the full menu (M prices, with "Prices may vary in store"), the 6 calorie values from M, and the restaurant's own taglines ("مشاوي على الأصول", "معجنات طازجة يوميًا", "مخبوزة بحب").
- **Linked although UNVERIFIED:** "open every day incl. Friday" (in `config.js`, easy to change). WhatsApp was unverified at build time; Blox tested it on 2026-11-22 and it works.
- **Links tested by Blox (2026-11-22):** Call, WhatsApp, Snapchat, Instagram, HungerStation, directions and Google Maps all work.
- **Not shown:** postal code, HS calories, HS prices, ratings, reviews, "women-owned", opening date, "Syrian", TikTok, meal contents for Zinger/bomb meals.
- **Photos:** only the restaurant's own (Snapchat posts, Google owner photo, its own online-menu photos). Each website image file is listed in `credits.json` (`used_on_site_as`, `site_files`).

