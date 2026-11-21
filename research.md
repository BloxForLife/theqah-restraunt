# Research: مطعم ثقة الشام / Thiqat Al-Sham Restaurant

Phase 1 research for the restaurant website. Everything here was checked on **2026-11-21** (Asia/Riyadh).

**Status key**
- **VERIFIED**: confirmed by 2+ independent sources, or by the restaurant's own source plus another source, or confirmed by Blox (site owner, lives next to the restaurant).
- **UNVERIFIED**: only one source, or could not be opened. Do not publish until confirmed.
- **DECIDED**: sources disagree; Blox chose the value on 2026-11-21. The conflict is noted.

Screenshots of every key source are in `research/evidence/`. Menu data is in `data/menu.json`. Image sources are in `credits.json`.

---

## 1. Sources used

| Code | Source | URL | Who published it | Result |
|---|---|---|---|---|
| **G** | Google Maps listing | [Place page](https://www.google.com/maps/place/%D9%85%D8%B7%D8%B9%D9%85+%D8%AB%D9%82%D8%A9+%D8%A7%D9%84%D8%B4%D8%A7%D9%85/@27.4718889,48.4695686,17z/data=!4m6!3m5!1s0x3fccbbdc5f69e09d:0x84b90311b2f79988!8m2!3d27.4718889!4d48.4695686!16s%2Fg%2F11yrlkz3ks) (place id `0x3fccbbdc5f69e09d:0x84b90311b2f79988`) | Google, with an owner photo | Opened (signed-out "limited view": only today's hours shown) |
| **M** | Restaurant's own online menu | https://thiqat-alshaam.menus-sa.com/ar and `/en` | Restaurant (linked as "Website" on G) | Opened: full menu, prices, links |
| **SC** | Snapchat @thiqat.sa | https://www.snapchat.com/@thiqat.sa | Restaurant | Opened: bio, 49 story snaps (15–21 Nov 2026), 29 Spotlight posts (6–19 Nov 2026) |
| **HS** | HungerStation branch 180455 | https://hungerstation.com/sa-ar/restaurant/alnuayreayh/al-faisaliyah/180455 | HungerStation | **Blocked** (Cloudflare 403). Link confirmed via G's "Place an order" button and search-engine titles |
| **OSM** | OpenStreetMap reverse geocode | https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=27.4718889&lon=48.4695686 | OpenStreetMap | Opened |
| **IG** | Instagram @thiqat.sa | https://www.instagram.com/thiqat.sa | (linked from M; printed on pizza box) | **Could not open** (login wall) |
| **TT** | TikTok @thiqat.sa | https://www.tiktok.com/@thiqat.sa | (linked from M) | Opened: **"Couldn't find this account"** |
| — | Jahez, Keeta, The Chefz, Mrsool, Talabat, X, Facebook | web searches | — | **No listing/account found** |

---

## 2. Facts table

| Fact | Value | Source URLs | Date checked | Status |
|---|---|---|---|---|
| Name (Arabic) | مطعم ثقة الشام | G; M; SC; storefront sign (G owner photo); pizza box (SC post 18 Nov 2026) | 2026-11-21 | **VERIFIED** |
| Name (English) | Thiqat Al-Sham (restaurant writes "Thiqat Al Sham" / "Thiqat Al-Sham"; handle `thiqat.sa`; subdomain `thiqat-alshaam`) | M (English menu items "Thiqat Al-Sham sauce", "Thiqat Al Sham pizza"); SC handle | 2026-11-21 | **VERIFIED** |
| Cuisine | Levantine-style charcoal grills, shawarma, fatayer/pastries, plus pizza, burgers and breakfast | M (menu); SC (posts of grill, shawarma, fatayer, pizza) | 2026-11-21 | **VERIFIED** |
| "Syrian" | No source says "Syrian". The name means "Trust of the Levant". | — | 2026-11-21 | **UNVERIFIED**: not used on site |
| Their own words (taglines) | "🥐 معجنات طازجة يوميًا" (fresh pastries daily), "🔥 مشاوي على الأصول" (grills done the proper way), "مخبوزة بحب" (baked with love, printed on pizza box), "شورما طازا" (fresh shawarma), "نسعد بخدمتكم" | SC bio; SC posts 17–19 Nov 2026 | 2026-11-21 | **VERIFIED** (restaurant's own text) |
| Street | Prince Sultan bin Abdulaziz St (الأمير سلطان بن عبد العزيز), Al-Nu'ayriyah | G; SC post 17 Nov 2026 ("مطعم ثقة الشام – الأمير سلطان بن عبد العزيز"); OSM | 2026-11-21 | **VERIFIED** |
| District | Al-Faisaliyah (حي الفيصلية) | G; OSM; HS URL slug `al-faisaliyah`; **confirmed by Blox** | 2026-11-21 | **VERIFIED**. Conflict: SC bio says "حي الخليج" (see §3) |
| Postal code | 37451 | G only | 2026-11-21 | **UNVERIFIED** |
| Plus code / pin | FFC9+QR Nairyah → 27.4718889, 48.4695686 | G; confirmed by Blox | 2026-11-21 | **VERIFIED** |
| Phone | +966 50 261 9361 (0502619361) | G; M (WhatsApp link); SC bio; pizza box | 2026-11-21 | **VERIFIED** |
| WhatsApp | +966502619361 (`https://wa.me/966502619361`) | M (`wa.me/+966502619361`) only. The pizza box shows the number next to a plain phone icon, not a WhatsApp logo. | 2026-11-21 | **UNVERIFIED** (one source, though it is the restaurant's own) |
| Opening hours | **14:00–02:00** (2 PM–2 AM), Asia/Riyadh | M (14:00–02:00); **set by Blox** | 2026-11-21 | **DECIDED** (conflict: G and SC say 12:00, see §3) |
| Open every day incl. Friday | Assumed daily | No source lists days separately | 2026-11-21 | **UNVERIFIED** |
| Logo | Blue + yellow Arabic lettering "مطعم / ثقة / الشام" with dark drop shadow | M (logo image); same image is the avatar of the Google account that posted the storefront photo; matches storefront sign | 2026-11-21 | **VERIFIED**. File is a low-quality screenshot, so a clean redraw was approved |
| Brand colours | Sky blue ≈ `#00A8EC`, yellow ≈ `#F5E62D` (sampled from logo) | M logo; storefront sign photo | 2026-11-21 | **VERIFIED** (measured) |
| Menu: items & categories | 176 items in 9 categories (§4) | M; HS listing categories in search results (فطائر، بيتزا، ساندويتشات، برجر، مقبلات، صوصات) | 2026-11-21 | **VERIFIED** (items from restaurant's own menu) |
| Menu: prices | 1–120 SAR | M only (HS blocked) | 2026-11-21 | **UNCONFIRMED** (all 176) |
| Snapchat | @thiqat.sa, "مطعم ثقة الشام", active (last update 21 Nov 2026) | M (link); SC | 2026-11-21 | **VERIFIED** |
| Instagram | @thiqat.sa | M (link `instagram.com/thiqat.sa`); pizza box prints Instagram + Snapchat icons next to "thiqat.sa" (SC post 18 Nov 2026, `research/source-images/snapchat/st41_f*.jpg`) | 2026-11-21 | **VERIFIED** (two of the restaurant's own sources). The profile page itself could not be opened (login wall). |
| TikTok | @thiqat.sa | M (link); TT says account not found | 2026-11-21 | Dead link, **not used** (Blox: drop it) |
| HungerStation | Branch 180455, Al-Faisaliyah: https://hungerstation.com/sa-ar/restaurant/alnuayreayh/al-faisaliyah/180455 | G ("Place an order" target); search-engine titles "منيو التوصيل من مطعم ثقة الشام" (id 180455) | 2026-11-21 | **VERIFIED** (link only; page content blocked) |
| Other delivery apps | None found (Jahez, Keeta, The Chefz, Mrsool, Talabat) | web searches | 2026-11-21 | Not found |
| Google rating | 4.2 (33 reviews) | G | 2026-11-21 | Noted only. **Not shown on site** (changes over time) |
| Women-owned | Google attribute "Identifies as women-owned" | G only | 2026-11-21 | **UNVERIFIED**: not used |
| Opening date | Cake reading roughly "… افتتاح مطعم ثقة الشام" posted 6 Nov 2026; Snapchat created 1 Oct 2025; menu-site logo uploaded 25 Sep 2025 | SC; M metadata | 2026-11-21 | **UNVERIFIED** (my reading of handwriting) |
| Coming soon | "كرسبي فرايز" (Crispy Fries), not on menu yet | SC post 17 Nov 2026 | 2026-11-21 | Restaurant's own post; not added to menu |
| Customer reviews | Not used. No reviews or testimonials will appear on the site. | — | — | — |

---

## 3. Conflicts and how they were resolved

| # | Topic | What the sources say | Resolution |
|---|---|---|---|
| 1 | **Opening time** | M: **14:00**–02:00. G: **12 PM**–2 AM (Saturday shown). SC image post 17 Nov 2026, 20:32: "ابتداءً من غداً الاربعاء الدوام من 12 الظهر الى 2 صباحاً نسعد بخدمتكم" (from Wed 18 Nov, **12 noon**–2 AM). | **Blox chose 14:00–02:00.** Note: the restaurant's newest post says 12:00. |
| 2 | **District** | G, OSM, HS URL: **Al-Faisaliyah**. SC bio and SC "address" field: **حي الخليج**. | **Al-Faisaliyah**, confirmed by Blox (lives next to it). |
| 3 | **Map pin** | G: FFC9+QR (27.4718889, 48.4695686). M's map button (`maps.app.goo.gl/71kKec4p9uvUj9vUA`) drops a pin at FG9G+C24 (27.4685, 48.5250833), about 5.5 km east in Al-Khaleej (OSM). | **FFC9+QR**, confirmed by Blox. The menu site's pin is probably an older location; tell the owner to update it. |
| 4 | **English item names** | M's English names are machine-translated; 17 are wrong or missing (§5). | Corrected in `menu.json`; originals kept in `en_name_from_restaurant`. |
| 5 | **Menu photos** | Most photos on M look like stock/manufacturer images (e.g. Pepsi cans, reused pizza photos). | **Approved by Blox**: the owner uses them, so we use them. Logged in `credits.json`. |
| 6 | **Phone link** | M's call button is `tel:502619361` (missing 0/+966). | Site uses `tel:+966502619361`. Tell the owner their menu-site call button is broken. |

---

## 4. Menu summary (`data/menu.json`)

Copied from **M** (the restaurant's own online menu) on 2026-11-21. Every item has `source`, `date_found`, `price_status: "unconfirmed"`, and the photo URL in `image_source`.

| Category (AR / EN) | Items | Price range (SAR) |
|---|---|---|
| سندويشات / Sandwiches | 17 | 8–20 |
| صحون / Plates | 23 | 5–120 |
| برجر / Burgers | 12 | 11–26 |
| البيتزا / Pizza | 48 | 11–31 |
| مقبلات / Appetizers | 6 | 1–20 |
| الفطائر / Fatayer & Pastries | 27 | 1–50 |
| صوصات / Sauces | 9 | 2–8 |
| مشروبات / Drinks | 17 | 1–3 |
| الافطار / Breakfast | 17 | 1–35 |
| **Total** | **176** | |

- **Descriptions:** only 6 items have a description written by the restaurant (the "وتش" pizzas: ingredients and calories). All other descriptions are left **empty** on purpose. Nothing was invented. The owner can fill them in `menu.json`.
- **English names:** 122 identical to the restaurant's, 37 spelling-fixed, 17 corrected (§5).

---

## 5. English names I corrected (owner should review)

| Arabic | Restaurant's English | Used on site |
|---|---|---|
| شيش طاووق صغير | large chiken awsal | Shish Tawook, Small |
| شيش طاووق جامبو | larg chiken awsal | Shish Tawook, Jumbo |
| شاورما صاروخ | shawarma medium | Rocket Shawarma |
| شاورما صامولي | shawarma sandwich | Samoli Shawarma |
| وجبة شاورما صامولي | shawarma sandwich meal | Samoli Shawarma Meal |
| كيلو مشويات مشكل | mashawie 1k | Mixed Grill (1 kg) |
| قارب لبنة | Brick boat | Labneh Boat |
| كينزا ببسي صغير 185 م | A small cola treasure | Kinza Cola, Small (185 ml) |
| كينزا ببسي كبير 360 م | kinza | Kinza Cola, Large (360 ml) |
| صحن بيض عيون | A plate of eggs | Sunny-Side-Up Eggs |
| قنبلة برجر دجاج | (Arabic only) | Chicken Burger Bomb |
| وتش بيتزا زنجر / شورما / نقانق, and the 3 "وجبه" versions (6 items) | (Arabic only) | Watsh Pizza (Meal), Zinger / Shawarma / Sausage. **"وتش" transliterated; ask the owner what it means** |

---

## 6. Photos and logo (`credits.json`)

| What | Where from | Use |
|---|---|---|
| Logo (585×702 JPEG, screenshot of a design canvas) | M | Redraw as clean SVG (approved) |
| Storefront at night, 1600×900 | G, posted Nov 2026 by account "مطعم ثقة الشام" (logo avatar) | Location section / hero |
| Shawarma spit, 1242×2208 | SC image post 8 Nov 2026 | Food photo |
| 76 still frames from 19 of their videos (480–540 px wide): charcoal skewers, shawarma, fatayer, dough shaping, pizzas, branded box | SC stories/Spotlight 7–19 Nov 2026 | Food photos (Spotlight frames have a Snapchat watermark to crop) |
| 171 item photos | M | Menu item thumbnails (approved) |

**Excluded:** two SC posts carrying a **TikTok watermark** (likely reposted from someone else's TikTok), and "Day in my…" collages (possible third-party template).

**Quality warning:** the Snapchat videos are only 480–540 px wide, so they will look soft as full-width banners on large screens. Better originals from the owner (straight from their phone) would improve the site.

---

## 7. Questions for the owner before going live

1. **Hours:** the site will say 14:00–02:00, but their Snapchat (17 Nov) and Google say 12:00. Which is right? Same hours on Friday?
2. **Breakfast:** the menu has a breakfast category, but the shop opens in the afternoon. When is breakfast served?
3. **Prices:** all 176 are "unconfirmed". Are the online-menu prices the in-store prices?
4. **"وتش" pizzas:** what is the English name?
5. **Instagram @thiqat.sa and WhatsApp:** their menu site and pizza box point to Instagram @thiqat.sa, but I couldn't open it. Is it active? Is 0502619361 on WhatsApp? (Both will be linked; please confirm.)
6. **Meals ("وجبة"):** what comes with a meal? Only the وتش meals say "+ Pepsi + fries".
7. **Original logo file** and **original phone photos/videos**, if they have them (higher quality).
8. **Their own fixes:** the menu site's map pin (FG9G+C24) and call button (`tel:502619361`) are wrong, the TikTok link is dead, and the Snapchat bio says حي الخليج.
9. **Postal code** 37451: correct?
10. **Women-owned** (Google attribute) and **opening date**: only mention if the owner wants.
