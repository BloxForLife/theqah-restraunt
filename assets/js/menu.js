/* Menu page: builds the menu from data/menu.json, the category jump bar and the search box.
   To change items or prices, edit data/menu.json (not this file). */
(function () {
  "use strict";

  var doc = document.documentElement;
  var lang = doc.lang === "en" ? "en" : "ar";
  var root = doc.getAttribute("data-root") || "";
  var mount = document.querySelector("[data-menu]");
  var nav = document.querySelector("[data-cat-nav]");
  var input = document.getElementById("menu-search");
  var countEl = document.querySelector("[data-result-count]");
  var tools = document.querySelector(".menu-tools");
  if (!mount) return;

  var T = {
    ar: {
      currency: "ر.س", currencySr: "ريال", kcal: "سعرة حرارية", items: "عدد الأصناف",
      results: "عدد النتائج: ", none: "لا توجد أصناف تطابق «%s». جرّب كلمة أخرى.",
      unavailable: "غير متوفر حالياً", error: "تعذّر تحميل المنيو. حدّث الصفحة، أو اتصل بنا للطلب."
    },
    en: {
      currency: "SAR", currencySr: "SAR", kcal: "kcal", items: "Items",
      results: "", none: "No items match “%s”. Try another word.",
      unavailable: "Not available right now", error: "The menu could not be loaded. Please refresh the page, or call us to order."
    }
  }[lang];

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  // Search: make Arabic spelling variants match (أ/إ/آ → ا, ة → ه, شاورما/شورما, ...)
  function norm(s) {
    return String(s || "").toLowerCase()
      .replace(/[ً-ٰٟـ]/g, "")
      .replace(/[أإآٱ]/g, "ا").replace(/ة/g, "ه").replace(/ى/g, "ي").replace(/ؤ/g, "و").replace(/ئ/g, "ي")
      .replace(/شاورما/g, "شورما").replace(/بيزا/g, "بيتزا").replace(/بيبروني/g, "ببروني")
      .replace(/موازريلا|موزاريلا/g, "موزريلا")
      .replace(/ساندويتش|ساندوتش|سندويتش|ساندويش|سندوتش/g, "سندويش")
      .replace(/shawerma|shawurma|shwarma/g, "shawarma").replace(/pepperoni/g, "peperoni")
      .replace(/[^\p{L}\p{N}\s]/gu, " ").replace(/\s+/g, " ").trim();
  }

  function money(p) {
    var n = String(Math.round(Number(p) * 100) / 100);
    var wrap = el("span", "price");
    var shown = el("span", null, lang === "ar" ? n + " " + T.currency : T.currency + " " + n);
    shown.setAttribute("aria-hidden", "true");
    wrap.appendChild(shown);
    wrap.appendChild(el("span", "sr-only", n + " " + T.currencySr));
    return wrap;
  }

  function itemNode(item, cat) {
    var li = el("li", "item");
    if (item.available === false) li.classList.add("is-unavailable");
    var body = el("div", "item-body");
    body.appendChild(el("h3", "item-name", item.name[lang] || item.name.ar));
    if (lang === "en" && item.name.ar) {
      var alt = el("p", "item-alt", item.name.ar);
      alt.lang = "ar";
      alt.dir = "rtl";
      body.appendChild(alt);
    }
    var desc = item.description && item.description[lang];
    if (desc) body.appendChild(el("p", "item-desc", desc));
    var meta = el("p", "item-meta");
    meta.appendChild(money(item.price));
    if (item.calories) meta.appendChild(el("span", "kcal", item.calories + " " + T.kcal));
    if (item.available === false) meta.appendChild(el("span", "tag", T.unavailable));
    body.appendChild(meta);
    li.appendChild(body);

    if (item.image) {
      var img = el("img", "item-img");
      img.src = root + item.image;
      img.alt = "";                 // the item name is right next to the photo
      img.width = 360;
      img.height = 270;
      img.loading = "lazy";
      img.decoding = "async";
      li.appendChild(img);
    } else {
      var ph = el("span", "item-img item-img--none");
      ph.setAttribute("aria-hidden", "true");
      li.appendChild(ph);
    }
    li._search = norm([item.name.ar, item.name.en, item.description && item.description.ar,
      item.description && item.description.en, cat.name.ar, cat.name.en].join(" "));
    return li;
  }

  function render(menu) {
    document.querySelectorAll("[data-price-note]").forEach(function (n) {
      if (menu.price_note && menu.price_note[lang]) n.textContent = menu.price_note[lang];
    });
    mount.innerHTML = "";
    var sections = [];
    menu.categories.forEach(function (cat) {
      if (!cat.items || !cat.items.length) return;
      var sec = el("section", "cat");
      sec.id = "cat-" + cat.id;
      sec.setAttribute("aria-labelledby", "h-" + cat.id);
      var h = el("h2", "cat-title", cat.name[lang] || cat.name.ar);
      h.id = "h-" + cat.id;
      var cnt = el("span", "cat-count");
      cnt.appendChild(el("span", "sr-only", T.items + ": "));
      cnt.appendChild(document.createTextNode(cat.items.length));
      h.appendChild(cnt);
      sec.appendChild(h);
      var ul = el("ul", "items");
      cat.items.forEach(function (item) { ul.appendChild(itemNode(item, cat)); });
      sec.appendChild(ul);
      mount.appendChild(sec);

      var chip = el("a", "chip", cat.name[lang] || cat.name.ar);
      chip.href = "#cat-" + cat.id;
      chip.setAttribute("data-cat", cat.id);
      var li = el("li");
      li.appendChild(chip);
      nav.appendChild(li);
      sections.push({ sec: sec, chip: chip, li: li, items: Array.prototype.slice.call(ul.children) });
    });
    var none = el("p", "no-results");
    none.hidden = true;
    mount.appendChild(none);

    setupSearch(sections, none);
    setupSpy(sections);

    if (location.hash) {
      var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) target.scrollIntoView();
    }
  }

  function setupSearch(sections, none) {
    var timer;
    function run() {
      var q = norm(input.value);
      var words = q ? q.split(" ") : [];
      var total = 0;
      sections.forEach(function (s) {
        var shown = 0;
        s.items.forEach(function (li) {
          var hit = words.every(function (w) { return li._search.indexOf(w) !== -1; });
          li.hidden = !hit;
          if (hit) shown++;
        });
        s.sec.hidden = shown === 0;
        s.li.hidden = shown === 0;
        total += shown;
      });
      if (!words.length) {
        countEl.textContent = "";
      } else if (lang === "ar") {
        countEl.textContent = T.results + total;
      } else {
        countEl.textContent = total + (total === 1 ? " result" : " results");
      }
      none.hidden = !(words.length && total === 0);
      none.textContent = T.none.replace("%s", input.value.trim());
    }
    input.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(run, 120);
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { input.value = ""; run(); }
    });
    // keep the search box out of the way of the on-screen keyboard "Go" key
    input.form && input.form.addEventListener("submit", function (e) { e.preventDefault(); input.blur(); });
  }

  // Highlight the category you are looking at in the jump bar
  function setupSpy(sections) {
    function setToolsHeight() {
      if (tools) doc.style.setProperty("--tools-h", tools.offsetHeight + "px");
    }
    setToolsHeight();
    window.addEventListener("resize", setToolsHeight);
    if (!("IntersectionObserver" in window)) return;
    var current;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var s = sections.filter(function (x) { return x.sec === en.target; })[0];
        if (!s || s === current) return;
        if (current) { current.chip.classList.remove("is-active"); current.chip.removeAttribute("aria-current"); }
        current = s;
        s.chip.classList.add("is-active");
        s.chip.setAttribute("aria-current", "true");
        var bar = nav.parentElement, r = s.chip.getBoundingClientRect(), b = bar.getBoundingClientRect();
        bar.scrollBy({ left: (r.left + r.width / 2) - (b.left + b.width / 2), behavior: "smooth" });
      });
    }, { rootMargin: "-" + ((tools && tools.offsetHeight) || 120) + "px 0px -65% 0px" });
    sections.forEach(function (s) { io.observe(s.sec); });
  }

  fetch(root + "data/menu.json", { cache: "no-cache" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(render)
    .catch(function () {
      mount.innerHTML = "";
      var p = el("p", "menu-error", T.error);
      mount.appendChild(p);
    });
})();
