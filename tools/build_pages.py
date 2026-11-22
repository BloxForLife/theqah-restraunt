"""Builds the HTML pages (Arabic + English) from one template, so both languages always match.

    python3 tools/build_pages.py

Writes: index.html, menu.html, en/index.html, en/menu.html, 404.html, sitemap.xml, robots.txt

THE RESTAURANT OWNER NEVER NEEDS TO RUN THIS.
Phone, hours, address and links live in config.js; the menu lives in data/menu.json.
Run this only if you change the page layout or wording below, or the website address (SITE_URL).
"""
import datetime
import html
import os
import re
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# The public address of the website. Change this if you move to your own domain, then run this script.
SITE_URL = "https://bloxforlife.github.io/theqah-restraunt/"

e = html.escape

# ---------------------------------------------------------------- words on the pages
S = {
    "ar": {
        "dir": "rtl", "locale": "ar_SA", "other": "en", "other_label": "English", "other_lang_name": "English",
        "name": "مطعم ثقة الشام",
        "skip": "تخطَّ إلى المحتوى",
        "nav_label": "القائمة الرئيسية",
        "nav_menu": "المنيو", "nav_order": "اطلب", "nav_visit": "الموقع والأوقات",
        "home_title": "مطعم ثقة الشام | مشاوي وشاورما وفطائر وبيتزا في النعيرية",
        "home_desc": "مطعم ثقة الشام في حي الفيصلية بالنعيرية: مشاوي على الفحم، شاورما، فطائر وبيتزا. تصفّح المنيو والأسعار، واتصل أو اطلب عبر واتساب أو هنقرستيشن.",
        "menu_title": "المنيو والأسعار | مطعم ثقة الشام - النعيرية",
        "menu_desc": "منيو مطعم ثقة الشام كامل بالأسعار: سندويشات، صحون مشاوي، شاورما، برجر، بيتزا، فطائر، مقبلات، فطور ومشروبات.",
        "og_alt": "واجهة مطعم ثقة الشام ليلاً مع اللوحة المضيئة",
        "eyebrow": "مطعم ثقة الشام · النعيرية",
        "h1": 'مشاوي <span class="accent">على الأصول</span>،<br>ومعجنات طازجة يوميًا',
        "lead": "شيش طاووق وكباب وأوصال على الفحم، وشاورما، وفطائر، وبيتزا. على شارع الأمير سلطان في حي الفيصلية.",
        "cta_call": "اتصل واطلب", "cta_wa": "اطلب عبر واتساب", "cta_menu": "تصفّح المنيو كامل",
        "hero_alt": "أسياخ شيش طاووق على الفحم في مطبخ مطعم ثقة الشام",
        "kitchen_h": "من مطبخنا", "kitchen_sub": "صور نشرها المطعم على سناب شات.",
        "tiles": [
            ("plates", "grill-skewers", "المشاوي على الفحم", None,
             "شيش طاووق، كباب لحم ودجاج، أوصال، وكيلو مشويات مشكل.", "أسياخ دجاج وكباب لحم على الفحم", "عرض الصحون"),
            ("sandwiches", "shawarma", "الشاورما", None,
             "صغير، صاروخ، جامبو 40 سم، صامولي، وصحون شاورما عربي.", "سيخ شاورما الدجاج في المطعم", "عرض السندويشات"),
            ("pizza", "pizza", "البيتزا", "«مخبوزة بحب»",
             "بثلاثة أحجام، من المارجريتا إلى بيتزا ثقة الشام.", "بيتزا ببروني خارجة من الفرن", "عرض البيتزا"),
            ("fatayer", "fatayer", "الفطائر والمعجنات", "«معجنات طازجة يوميًا»",
             "زعتر، لبنة، جبن، لحم، سبانخ، محمرة، وقوارب الجبن.", "فطائر مخبوزة على صواني المطعم", "عرض الفطائر"),
        ],
        "order_h": "اطلب الآن", "order_sub": "اتصل، أو أرسل طلبك على واتساب، أو اطلب توصيل من التطبيق.",
        "oc_call": "اتصل بنا", "oc_wa": "واتساب", "oc_wa_d": "أرسل طلبك برسالة",
        "oc_app": "هنقرستيشن", "oc_app_d": "توصيل عبر التطبيق",
        "order_note": "أسعار التوصيل في التطبيق قد تختلف عن أسعار المطعم.",
        "visit_h": "زورونا", "hours_h": "ساعات العمل",
        "directions": "الاتجاهات إلى المطعم", "open_maps": "افتح في خرائط Google",
        "store_alt": "واجهة مطعم ثقة الشام ليلاً: اللوحة المضيئة، الواجهة الزجاجية، وفرن القبة",
        "store_cap": "واجهة المطعم، من صفحة المطعم على خرائط Google.",
        "map_title": "خريطة موقع مطعم ثقة الشام",
        "snap_h": "تابعنا", "snap_sub": "يومياتنا في المطبخ على سناب شات.",
        "snap_alt1": "تشكيل عجينة الفطائر يدوياً", "snap_alt2": "بيتزا جاهزة على طاولة المطبخ",
        "snap_card": "نشارك صور الأكل والعروض الجديدة أول بأول.",
        "footer_hours": "ساعات العمل", "footer_follow": "روابطنا", "price_note": "الأسعار قد تختلف في المطعم.",
        "ab_label": "اتصال سريع", "ab_call": "اتصل", "ab_wa": "واتساب", "ab_menu": "المنيو", "ab_dir": "الموقع",
        "menu_h1": "المنيو", "menu_lead": "سندويشات، صحون مشاوي وشاورما، برجر، بيتزا، فطائر، مقبلات، فطور ومشروبات.",
        "search_label": "ابحث في المنيو", "search_ph": "ابحث: شاورما، زعتر، بيتزا…",
        "cats_label": "أقسام المنيو", "loading": "جاري تحميل المنيو…",
        "noscript": "لعرض المنيو، فعّل JavaScript في المتصفح، أو اتصل بنا للطلب.",
        "logo_alt": "مطعم ثقة الشام",
        "home_link_label": "مطعم ثقة الشام: الصفحة الرئيسية",
    },
    "en": {
        "dir": "ltr", "locale": "en_US", "other": "ar", "other_label": "العربية", "other_lang_name": "Arabic",
        "name": "Thiqat Al-Sham Restaurant",
        "skip": "Skip to content",
        "nav_label": "Main",
        "nav_menu": "Menu", "nav_order": "Order", "nav_visit": "Location & hours",
        "home_title": "Thiqat Al-Sham Restaurant | Grills, Shawarma, Fatayer & Pizza in Al-Nu'ayriyah",
        "home_desc": "Thiqat Al-Sham Restaurant in Al-Faisaliyah, Al-Nu'ayriyah: charcoal grills, shawarma, fatayer and pizza. See the menu and prices, then call, order on WhatsApp or through HungerStation.",
        "menu_title": "Menu & Prices | Thiqat Al-Sham Restaurant, Al-Nu'ayriyah",
        "menu_desc": "The full Thiqat Al-Sham menu with prices: sandwiches, grill plates, shawarma, burgers, pizza, fatayer, appetizers, breakfast and drinks.",
        "og_alt": "Thiqat Al-Sham Restaurant storefront at night with its lit sign",
        "eyebrow": "Thiqat Al-Sham Restaurant · Al-Nu'ayriyah",
        "h1": 'Grills done <span class="accent">the proper way</span>.<br>Pastries fresh every day.',
        "lead": "Shish tawook, kebab and meat awsal over charcoal, plus shawarma, fatayer and pizza. On Prince Sultan St in Al-Faisaliyah.",
        "cta_call": "Call to order", "cta_wa": "Order on WhatsApp", "cta_menu": "See the full menu",
        "hero_alt": "Shish tawook skewers over charcoal in the Thiqat Al-Sham kitchen",
        "kitchen_h": "From our kitchen", "kitchen_sub": "Photos posted by the restaurant on Snapchat.",
        "tiles": [
            ("plates", "grill-skewers", "Charcoal grills", None,
             "Shish tawook, meat and chicken kebab, meat awsal, and the mixed-grill kilo.", "Chicken and meat kebab skewers over charcoal", "See the plates"),
            ("sandwiches", "shawarma", "Shawarma", None,
             "Small, Sarookh, 40 cm Jumbo, Samoli, and Arabic shawarma plates.", "The chicken shawarma spit at the restaurant", "See the sandwiches"),
            ("pizza", "pizza", "Pizza", "“Baked with love”",
             "Three sizes, from margherita to the Thiqat Al-Sham pizza.", "Pepperoni pizza fresh from the oven", "See the pizza"),
            ("fatayer", "fatayer", "Fatayer & pastries", "“Fresh pastries every day”",
             "Za'atar, labneh, cheese, meat, spinach, muhammara, and cheese boats.", "Baked fatayer on the restaurant's trays", "See the fatayer"),
        ],
        "order_h": "Order now", "order_sub": "Call us, send your order on WhatsApp, or get delivery through the app.",
        "oc_call": "Call us", "oc_wa": "WhatsApp", "oc_wa_d": "Send your order as a message",
        "oc_app": "HungerStation", "oc_app_d": "Delivery through the app",
        "order_note": "Delivery prices in the app may differ from in-store prices.",
        "visit_h": "Visit us", "hours_h": "Opening hours",
        "directions": "Get directions", "open_maps": "Open in Google Maps",
        "store_alt": "Thiqat Al-Sham storefront at night: lit sign, glass front and dome oven",
        "store_cap": "The storefront, from the restaurant's Google Maps listing.",
        "map_title": "Map showing Thiqat Al-Sham Restaurant",
        "snap_h": "Follow us", "snap_sub": "Daily life in our kitchen, on Snapchat.",
        "snap_alt1": "Shaping fatayer dough by hand", "snap_alt2": "Pizzas ready on the kitchen counter",
        "snap_card": "We post our food and new offers as they happen.",
        "footer_hours": "Opening hours", "footer_follow": "Find us", "price_note": "Prices may vary in store.",
        "ab_label": "Quick contact", "ab_call": "Call", "ab_wa": "WhatsApp", "ab_menu": "Menu", "ab_dir": "Directions",
        "menu_h1": "Menu", "menu_lead": "Sandwiches, grill and shawarma plates, burgers, pizza, fatayer, appetizers, breakfast and drinks.",
        "search_label": "Search the menu", "search_ph": "Search: shawarma, za'atar, pizza…",
        "cats_label": "Menu sections", "loading": "Loading the menu…",
        "noscript": "To see the menu, please turn on JavaScript, or call us to order.",
        "logo_alt": "Thiqat Al-Sham Restaurant",
        "home_link_label": "Thiqat Al-Sham Restaurant: home",
    },
}

# ---------------------------------------------------------------- icons (inline sprite)
USED_ICONS = ["phone", "whatsapp", "snapchat", "instagram", "map-pin", "clock", "search", "navigation",
              "shopping-bag", "arrow-right", "utensils-crossed"]


def sprite():
    out = []
    for name in USED_ICONS:
        for kind in ("line", "fill"):
            p = os.path.join(HERE, "icons", f"{name}.{kind}.svg")
            if os.path.exists(p):
                inner = open(p, encoding="utf-8").read().strip()
                if kind == "line":
                    attrs = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
                else:
                    attrs = 'fill="currentColor"'
                out.append(f'<symbol id="i-{name}" viewBox="0 0 24 24" {attrs}>{inner}</symbol>')
    return '<svg xmlns="http://www.w3.org/2000/svg" style="display:none">' + "".join(out) + "</svg>"


def icon(name, cls=""):
    return f'<svg class="icon {cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'


# ---------------------------------------------------------------- page parts
def urls(lang, page):
    base = SITE_URL + ("en/" if lang == "en" else "")
    return base + ("menu.html" if page == "menu" else "")


def head(lang, page, root):
    s = S[lang]
    title = s["menu_title"] if page == "menu" else s["home_title"]
    desc = s["menu_desc"] if page == "menu" else s["home_desc"]
    canon = urls(lang, page)
    fonts = (["plex-arabic-400", "kufi-800"] if lang == "ar" else ["plex-latin-400", "plex-latin-700"])
    preload = "".join(f'<link rel="preload" href="{root}assets/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>\n'
                      for f in fonts)
    if page == "home":
        preload += f'<link rel="preload" href="{root}assets/img/hero-grill.webp" as="image" type="image/webp" fetchpriority="high">\n'
    scripts = f'<script src="{root}config.js" defer></script>\n<script src="{root}assets/js/site.js" defer></script>\n'
    if page == "menu":
        scripts += f'<script src="{root}assets/js/menu.js" defer></script>\n'
    return f"""<!doctype html>
<html lang="{lang}" dir="{s['dir']}" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="ar" href="{urls('ar', page)}">
<link rel="alternate" hreflang="en" href="{urls('en', page)}">
<link rel="alternate" hreflang="x-default" href="{urls('ar', page)}">
<meta name="theme-color" content="#1c1a17">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(s['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(s['og_alt'])}">
<meta property="og:locale" content="{s['locale']}">
<meta property="og:locale:alternate" content="{S[s['other']]['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.ico" sizes="48x48">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
{preload}<link rel="stylesheet" href="{root}assets/css/site.css">
{scripts}</head>
"""


def header(lang, page, root):
    s = S[lang]
    home = "./"
    other_root = "../" if lang == "en" else "en/"
    other_href = other_root + ("menu.html" if page == "menu" else "")
    cur = ' aria-current="page"' if page == "menu" else ""
    home_prefix = "" if page == "home" else "./"
    return f"""<body class="has-action-bar">
{sprite()}
<a class="skip" href="#main">{s['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{home}"><img src="{root}assets/img/logo.svg" width="200" height="58" alt="{e(s['home_link_label'])}"></a>
    <nav class="main-nav" aria-label="{s['nav_label']}">
      <a href="menu.html"{cur}>{s['nav_menu']}</a>
      <a class="nav-extra" href="{home_prefix}#order">{s['nav_order']}</a>
      <a class="nav-extra" href="{home_prefix}#visit">{s['nav_visit']}</a>
    </nav>
    <a class="lang-link" href="{other_href}" hreflang="{s['other']}" lang="{s['other']}">{s['other_label']}</a>
  </div>
</header>
"""


def footer(lang, page, root):
    s = S[lang]
    other_root = "../" if lang == "en" else "en/"
    if page == "menu":
        third = f'<a data-link="directions" href="#">{icon("navigation", "icon-line")}<span>{s["ab_dir"]}</span></a>'
    else:
        third = f'<a href="menu.html">{icon("utensils-crossed", "icon-line")}<span>{s["ab_menu"]}</span></a>'
    return f"""<footer class="site-footer on-night">
  <div class="wrap footer-grid">
    <div>
      <img class="footer-logo" src="{root}assets/img/logo.svg" width="170" height="50" alt="{e(s['logo_alt'])}" loading="lazy">
      <p data-text="address"></p>
      <p><a data-link="call" href="#"><span class="ltr" data-text="phone"></span></a></p>
    </div>
    <div>
      <h2>{s['footer_hours']}</h2>
      <p data-hours-summary></p>
      <p class="status" data-open-status aria-live="polite"></p>
    </div>
    <div>
      <h2>{s['footer_follow']}</h2>
      <ul class="footer-links">
        <li data-link-box><a data-link="snapchat" href="#">{icon('snapchat')}Snapchat</a></li>
        <li data-link-box><a data-link="instagram" href="#">{icon('instagram')}Instagram</a></li>
        <li data-link-box><a data-link="hungerstation" href="#">{icon('shopping-bag', 'icon-line')}{s['oc_app']}</a></li>
        <li data-link-box><a data-link="maps" href="#">{icon('map-pin', 'icon-line')}{s['open_maps']}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>{s['price_note']}</p>
    <p>© <span data-year>2026</span> {s['name']}</p>
    <a href="{other_root}{'menu.html' if page == 'menu' else ''}" hreflang="{s['other']}" lang="{s['other']}">{s['other_label']}</a>
  </div>
</footer>
<nav class="action-bar" aria-label="{s['ab_label']}">
  <a class="ab-call" data-link="call" href="#">{icon('phone', 'icon-line')}<span>{s['ab_call']}</span></a>
  <a class="ab-wa" data-link="whatsapp" data-link-box href="#">{icon('whatsapp')}<span>{s['ab_wa']}</span></a>
  {third}
</nav>
</body>
</html>
"""


def home_main(lang, root):
    s = S[lang]
    img = root + "assets/img/"
    tiles = ""
    for cat, photo, title, quote, text, alt, more in s["tiles"]:
        q = f'<p class="quote">{e(quote)}</p>' if quote else ""
        tiles += f"""
        <li class="tile"><a href="menu.html#cat-{cat}">
          <img src="{img}{photo}.webp" width="480" height="600" alt="{e(alt)}" loading="lazy" decoding="async">
          <div class="tile-text"><h3>{e(title)}</h3>{q}<p>{e(text)}</p><span class="tile-more">{e(more)} {icon('arrow-right', 'icon-line flip')}</span></div>
        </a></li>"""
    return f"""<main id="main">
  <section class="hero on-night" aria-labelledby="hero-title">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">{s['eyebrow']}</p>
        <h1 id="hero-title">{s['h1']}</h1>
        <p class="lead">{s['lead']}</p>
        <p class="status status-pill" data-open-status aria-live="polite"></p>
        <div class="cta-row">
          <a class="btn btn-call" data-link="call" href="#order">{icon('phone', 'icon-line')}<span>{s['cta_call']}</span></a>
          <a class="btn btn-wa" data-link="whatsapp" data-link-box href="#order">{icon('whatsapp')}<span>{s['cta_wa']}</span></a>
        </div>
        <a class="text-link" href="menu.html">{s['cta_menu']} {icon('arrow-right', 'icon-line flip')}</a>
      </div>
      <figure class="hero-photo arch">
        <img src="{img}hero-grill.webp" width="480" height="640" alt="{e(s['hero_alt'])}" fetchpriority="high" decoding="async">
      </figure>
    </div>
  </section>

  <section class="section kitchen" aria-labelledby="kitchen-title">
    <div class="wrap">
      <div class="section-head">
        <div><h2 id="kitchen-title">{s['kitchen_h']}</h2><div class="rule"></div></div>
        <p class="section-sub">{s['kitchen_sub']}</p>
      </div>
      <ul class="tiles">{tiles}
      </ul>
    </div>
  </section>

  <section class="section order" id="order" aria-labelledby="order-title">
    <div class="wrap">
      <div class="section-head">
        <div><h2 id="order-title">{s['order_h']}</h2><div class="rule"></div></div>
        <p class="section-sub">{s['order_sub']}</p>
      </div>
      <div class="order-grid">
        <a class="order-card oc-call" data-link="call" href="#">
          <span class="oc-icon">{icon('phone', 'icon-line')}</span>
          <span class="oc-title">{s['oc_call']}</span>
          <span class="oc-detail"><span class="ltr" data-text="phone"></span></span>
        </a>
        <a class="order-card oc-wa" data-link="whatsapp" data-link-box href="#">
          <span class="oc-icon">{icon('whatsapp')}</span>
          <span class="oc-title">{s['oc_wa']}</span>
          <span class="oc-detail">{s['oc_wa_d']}</span>
        </a>
        <a class="order-card oc-app" data-link="hungerstation" data-link-box href="#">
          <span class="oc-icon">{icon('shopping-bag', 'icon-line')}</span>
          <span class="oc-title">{s['oc_app']}</span>
          <span class="oc-detail">{s['oc_app_d']}</span>
        </a>
      </div>
      <p class="note">{s['order_note']}</p>
    </div>
  </section>

  <section class="section visit" id="visit" aria-labelledby="visit-title">
    <div class="wrap visit-grid">
      <div class="visit-info">
        <h2 id="visit-title">{s['visit_h']}</h2><div class="rule"></div>
        <p class="address" data-text="address"></p>
        <p class="plus-code"><span class="ltr" data-text="plusCode"></span></p>
        <div class="cta-row">
          <a class="btn btn-dark" data-link="directions" href="#">{icon('navigation', 'icon-line')}<span>{s['directions']}</span></a>
          <a class="btn btn-line" data-link="maps" href="#">{icon('map-pin', 'icon-line')}<span>{s['open_maps']}</span></a>
        </div>
        <h3>{s['hours_h']}</h3>
        <p class="status status-light" data-open-status aria-live="polite"></p>
        <table class="hours" data-hours><caption class="sr-only">{s['hours_h']}</caption></table>
      </div>
      <figure class="visit-photo">
        <img src="{img}storefront-800.webp" srcset="{img}storefront-800.webp 800w, {img}storefront-1600.webp 1600w"
             sizes="(min-width: 900px) 600px, 100vw" width="1600" height="900" alt="{e(s['store_alt'])}" loading="lazy" decoding="async">
        <figcaption>{s['store_cap']}</figcaption>
      </figure>
      <div class="visit-map">
        <iframe data-map title="{e(s['map_title'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </section>

  <section class="section snap on-night" aria-labelledby="snap-title">
    <div class="wrap">
      <div class="section-head">
        <div><h2 id="snap-title">{s['snap_h']}</h2><div class="rule"></div></div>
        <p class="section-sub">{s['snap_sub']}</p>
      </div>
      <div class="snap-grid">
        <figure><img src="{img}fatayer-dough.webp" width="480" height="640" alt="{e(s['snap_alt1'])}" loading="lazy" decoding="async"></figure>
        <figure><img src="{img}pizzas-row.webp" width="480" height="640" alt="{e(s['snap_alt2'])}" loading="lazy" decoding="async"></figure>
        <div class="snap-card">
          <p class="handle">@thiqat.sa</p>
          <p>{s['snap_card']}</p>
          <div class="social-buttons">
            <a class="btn btn-call" data-link="snapchat" data-link-box href="#">{icon('snapchat')}<span>Snapchat</span></a>
            <a class="btn btn-ghost" data-link="instagram" data-link-box href="#">{icon('instagram')}<span>Instagram</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
"""


def menu_main(lang, root):
    s = S[lang]
    return f"""<main id="main">
  <section class="menu-hero on-night" aria-labelledby="menu-title">
    <div class="wrap">
      <h1 id="menu-title">{s['menu_h1']}</h1>
      <p class="lead">{s['menu_lead']}</p>
      <p class="price-note">{icon('clock', 'icon-line')}<span data-price-note>{s['price_note']}</span></p>
      <p class="status" data-open-status aria-live="polite"></p>
      <div class="cta-row">
        <a class="btn btn-call" data-link="call" href="#">{icon('phone', 'icon-line')}<span>{s['cta_call']}</span></a>
        <a class="btn btn-wa" data-link="whatsapp" data-link-box href="#">{icon('whatsapp')}<span>{s['cta_wa']}</span></a>
      </div>
    </div>
  </section>
  <div class="menu-tools">
    <div class="wrap">
      <form class="search" role="search" action="#">
        <label class="sr-only" for="menu-search">{s['search_label']}</label>
        {icon('search', 'icon-line')}
        <input id="menu-search" type="search" placeholder="{e(s['search_ph'])}" autocomplete="off" enterkeyhint="search">
      </form>
      <nav class="cat-nav" aria-label="{s['cats_label']}"><ul data-cat-nav></ul></nav>
    </div>
  </div>
  <div class="wrap menu-body">
    <p class="result-count" data-result-count aria-live="polite"></p>
    <div data-menu><p class="loading">{s['loading']}</p></div>
    <noscript><p class="menu-error">{s['noscript']}</p></noscript>
  </div>
</main>
"""


def page(lang, kind):
    root = "../" if lang == "en" else ""
    main = home_main(lang, root) if kind == "home" else menu_main(lang, root)
    return head(lang, kind, root) + header(lang, kind, root) + main + footer(lang, kind, root)


# ---------------------------------------------------------------- 404 (works at any folder depth)
def notfound():
    a, b = S["ar"], S["en"]
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found — {a['name']}</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#1c1a17">
<script>
  // Works on GitHub Pages (site in a sub-folder) and on Netlify / your own domain (site at the root).
  var base = /\\.github\\.io$/.test(location.hostname) ? "/" + location.pathname.split("/")[1] + "/" : "/";
  document.write('<base href="' + base + '">');
</script>
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body class="on-night">
<main class="notfound wrap">
  <div>
    <img src="assets/img/logo.svg" width="220" height="64" alt="{a['logo_alt']}" style="margin:0 auto 28px">
    <h1>الصفحة غير موجودة</h1>
    <p>الرابط الذي فتحته غير موجود. يمكنك العودة إلى الصفحة الرئيسية أو تصفّح المنيو.</p>
    <div class="cta-row">
      <a class="btn btn-call" href="./">الصفحة الرئيسية</a>
      <a class="btn btn-ghost" href="menu.html">المنيو</a>
    </div>
    <div lang="en" dir="ltr" style="margin-top:48px">
      <h2 style="font-size:1.4rem">Page not found</h2>
      <p>This link does not exist. Go to the home page or see the menu.</p>
      <div class="cta-row">
        <a class="btn btn-ghost" href="en/">Home (English)</a>
        <a class="btn btn-ghost" href="en/menu.html">Menu (English)</a>
      </div>
    </div>
  </div>
</main>
</body>
</html>
"""


def sitemap():
    today = datetime.date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for kind in ("home", "menu"):
        for lang in ("ar", "en"):
            out.append("  <url>")
            out.append(f"    <loc>{urls(lang, kind)}</loc>")
            out.append(f"    <lastmod>{today}</lastmod>")
            for alt in ("ar", "en"):
                out.append(f'    <xhtml:link rel="alternate" hreflang="{alt}" href="{urls(alt, kind)}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{urls("ar", kind)}"/>')
            out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def robots():
    # Search engines only read robots.txt at the root of a domain, so this file takes effect
    # with Netlify or your own domain. On a github.io sub-folder it is harmless but ignored.
    path = urlparse(SITE_URL).path
    return f"""User-agent: *
Allow: /
Disallow: {path}research/
Disallow: {path}tools/

Sitemap: {SITE_URL}sitemap.xml
"""


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


if __name__ == "__main__":
    write("index.html", page("ar", "home"))
    write("menu.html", page("ar", "menu"))
    write("en/index.html", page("en", "home"))
    write("en/menu.html", page("en", "menu"))
    write("404.html", notfound())
    write("sitemap.xml", sitemap())
    write("robots.txt", robots())
