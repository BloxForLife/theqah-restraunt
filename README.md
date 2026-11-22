# مطعم ثقة الشام — Thiqat Al-Sham Restaurant website

The website for **مطعم ثقة الشام** (Thiqat Al-Sham Restaurant), Prince Sultan bin Abdulaziz St, Al-Faisaliyah, Al-Nu'ayriyah.

- Arabic first (right-to-left), with a full English version in `/en/`.
- Plain HTML, CSS and JavaScript. No framework, no database, no server code, no build step for normal edits.
- You change **two files** to run it:
  - `config.js`: phone, WhatsApp, opening hours, address, map pin, links
  - `data/menu.json`: menu items, prices, descriptions, photos

---

## 1. What is where

| Path | What it is | Do you edit it? |
|---|---|---|
| `config.js` | Phone, WhatsApp, opening hours, address, map pin, social and delivery links | **Yes** |
| `data/menu.json` | The menu: categories, items, prices, descriptions, photos | **Yes** |
| `assets/menu/` | One photo per menu item (`<item id>.webp`) | Only to change photos |
| `assets/img/` | Logo (`logo.svg`), restaurant photos, share image (`og-image.jpg`) | Rarely |
| `index.html`, `menu.html` | Arabic home page and menu page | No (see section 7) |
| `en/index.html`, `en/menu.html` | English home page and menu page | No (see section 7) |
| `404.html` | "Page not found" page | No |
| `assets/css/site.css` | Design | No |
| `assets/js/site.js` | Fills in phone/WhatsApp/map, hours table, live "Open now / Closed" badge, Google data | No |
| `assets/js/menu.js` | Builds the menu, category bar and search | No |
| `sitemap.xml`, `robots.txt`, `site.webmanifest`, favicons | For Google and phones | No |
| `research.md`, `research/`, `credits.json` | Where every fact, price and photo came from | Reference only |
| `tools/` | Page generator for a web developer | No |

---

## 2. Change the phone, WhatsApp, hours or links (`config.js`)

Open `config.js` and change the value between the quotes. Every page updates.

```js
phone: "966502619361",        // 966 + the number without the first 0
phoneDisplay: "050 261 9361", // how it is written on the page
whatsapp: "966502619361",     // "" hides every WhatsApp button
```

**Opening hours** use the 24-hour clock, Saudi time:

```js
hours: {
  sunday:    { open: "12:00", close: "02:00" },   // 12 noon to 2 AM
  ...
  friday:    { open: "13:30", close: "02:00" },   // example: a different Friday time
}
```

- If `close` is earlier than `open`, the restaurant closes **after midnight**. The site understands this: at 1:30 AM it shows **Open now**, and at 3 AM it shows **Closed · opens at 12:00 PM**.
- To close a whole day, write `friday: { closed: true },`
- The badge always uses Saudi time (Asia/Riyadh), even if a visitor's phone is set to another country.

**Links:** set any link to `""` to hide it everywhere (for example `tiktok: ""`).

Keep the quotes `"..."` and the commas at the end of lines. If the page stops showing the phone or hours after an edit, a comma or quote was probably deleted.

---

## 3. Edit the menu (`data/menu.json`)

Each item looks like this (fields the site uses are marked):

```json
{
  "id": "shish-tawook-small",
  "name": { "ar": "شيش طاووق صغير", "en": "Shish Tawook, Small" },          ← shown
  "price": 10,                                                              ← shown (SAR)
  "description": { "ar": "سيخ قطع شيش طاووق متبلة بنكهة مميزة", "en": "..." }, ← shown if not empty
  "calories": null,                                                         ← shown if a number
  "image": "assets/menu/shish-tawook-small.webp",                           ← shown; null = no photo
  "available": true,                                                        ← false = greyed out, "Not available right now"
  "source": "...", "price_hungerstation": 13, ...                           ← notes only, not shown
}
```

**Change a price:** edit the number after `"price":` (no quotes, e.g. `12` or `12.5`).

**Item sold out for a while:** set `"available": false`. Set it back to `true` later.

**Remove an item:** delete its whole `{ ... }` block and the comma before or after it.

**Add an item:** copy an existing item block inside the right category, paste it after a comma, then change:
- `id`: a new, unique name in English letters with dashes, e.g. `"chicken-shawarma-plate-xl"`
- `name`, `price` and `description`
- `image`: a photo path, or `null`

You can delete the note fields you don't know (`source`, `en_name_status`, etc.) from the new item.

**Rename a category or change its order:** edit `"name"` inside the category, or move the whole category block. The jump bar follows the file order.

**Change the price note** ("Prices may vary in store") at the top of the file, under `price_note`.

**Check your edit:** paste the whole file into a JSON checker (search "JSON validator") before saving. If the menu page says *"The menu could not be loaded"*, the file has a typing mistake, usually a missing comma or an extra comma after the last item.

**Change a menu photo:**
1. Make the photo landscape (4:3 is best), about 360×270 px. The free site [squoosh.app](https://squoosh.app) can resize and save it as WebP.
2. Put it in `assets/menu/`.
3. Set the item's `"image"` to `"assets/menu/your-file-name.webp"`.

Use a new file name when you replace a photo, so phones don't keep showing the old one.

---

## 4. Preview on your computer

Opening `index.html` by double-clicking will **not** show the menu, because browsers block reading `menu.json` from a file. Start a tiny local server in this folder instead:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Or just push your change and look at the live site after a minute.

---

## 5. Put the site online for free

### Option A: GitHub Pages
1. Push this repository to GitHub, with the site files on the `main` branch.
2. On GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch"**, then choose branch **main** and folder **/ (root)**. Save.
3. After about a minute the site is live at `https://<your-username>.github.io/<repository-name>/`.
4. From then on, every change you commit to `main` (even an edit in GitHub's web editor) goes live by itself.

The page addresses in the HTML, `sitemap.xml` and `robots.txt` are set to
`https://bloxforlife.github.io/theqah-restraunt/`. If the final address is different, see section 6.

### Option B: Netlify
1. Sign in at [netlify.com](https://www.netlify.com) and choose **Add new site → Import an existing project**. Pick this GitHub repository.
2. Build command: *leave empty*. Publish directory: `.` (the root).
3. Deploy. Every push updates the site.

`_headers` sets caching for fonts and photos on Netlify. GitHub Pages ignores it.

---

## 6. Using your own domain (e.g. thiqat-alsham.com)

1. Connect the domain in GitHub Pages (**Settings → Pages → Custom domain**) or in Netlify (**Domain management**).
2. Open `tools/build_pages.py` and change `SITE_URL` to the new address (ending with `/`).
3. Run `python3 tools/build_pages.py`. It rewrites the 4 pages, `404.html`, `sitemap.xml` and `robots.txt` with the new address.
4. In Google Search Console, add the site and submit `sitemap.xml`.

---

## 7. For a web developer

- The 4 pages, `404.html`, `sitemap.xml` and `robots.txt` are **generated** by `tools/build_pages.py` from one template. That keeps Arabic and English identical in structure. Change the wording or layout there, then run it. Don't edit the HTML by hand, or the next run will overwrite your changes.
- Nothing about the restaurant is hard-coded in the HTML. Phone, hours, address and links come from `config.js`, and the menu from `data/menu.json`, both at page load.
- Google's structured data (schema.org `Restaurant`: address, phone, geo, hours, menu link) is built from `config.js` by `assets/js/site.js`.
- Icons are an inline SVG sprite built from `tools/icons/`.
- CSS uses logical properties (`margin-inline-start`, etc.), so one stylesheet serves RTL and LTR.
- Fonts are self-hosted:
  - IBM Plex Sans Arabic 400/700 (Arabic + Latin)
  - Noto Kufi Arabic 800, cut down to Arabic letters (9 KB), for Arabic headings

### Checked before launch (2026-11-22)

- Lighthouse, mobile:
  - Performance 98–99
  - Accessibility 100
  - Best Practices 100
  - SEO 100
- axe accessibility scan: no violations on any page, mobile or desktop.
- No sideways scrolling at 320, 390, 768, 1024 or 1366 px.
- Open/Closed badge tested at 01:30, 01:45, 02:00, 03:00, 11:59, 12:00 and 23:30 Riyadh time. It was also tested with the visitor's phone set to New York time.

---

## 8. Where things came from

- Every fact (address, hours, phone, links) is listed with its sources and status in **`research.md`**.
- Things still waiting for the owner are in section 7 of that file.
- Every menu item keeps the URL where it was found (`source`, `date_found`).
- **Prices** come from the restaurant's own online menu and are marked `"price_status": "unconfirmed"` until the owner confirms them. That is why the site says *"Prices may vary in store."*
- **Photos** were all published by the restaurant itself, on its Snapchat, Google Maps listing and online menu. Each file's origin is in **`credits.json`**.
- **Logo:** a clean vector redraw of the restaurant's logo, approved by the site owner.
- **Fonts:**
  - IBM Plex Sans Arabic, © IBM, SIL Open Font License 1.1
  - Noto Kufi Arabic, © Google, SIL Open Font License 1.1
  - License texts are in `assets/fonts/`.
- **Icons:** [Lucide](https://lucide.dev) (ISC License) and [Simple Icons](https://simpleicons.org) (CC0). See `tools/icons/LICENSES.txt`.
