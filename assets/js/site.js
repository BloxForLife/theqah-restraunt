/* Shared script for every page.
   Reads config.js (window.SITE_CONFIG) and fills in phone/WhatsApp/map links,
   the address, the opening-hours table and the live "Open now / Closed" badge.
   You should not need to edit this file: change config.js instead. */
(function () {
  "use strict";

  var cfg = window.SITE_CONFIG;
  if (!cfg) return;

  var doc = document.documentElement;
  var lang = doc.lang === "en" ? "en" : "ar";
  var DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
  var DAY_NAMES = {
    ar: ["الأحد", "الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"],
    en: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  };
  var T = {
    ar: {
      openNow: "مفتوح الآن", closesAt: "يغلق الساعة", closingSoon: "يغلق قريباً، الساعة",
      closedNow: "مغلق الآن", opensAt: "يفتح الساعة", opensTomorrow: "يفتح غداً الساعة",
      opensOn: "يفتح يوم", at: "الساعة", everyDay: "يومياً", closedDay: "مغلق", today: "اليوم"
    },
    en: {
      openNow: "Open now", closesAt: "closes at", closingSoon: "closing soon, at",
      closedNow: "Closed now", opensAt: "opens at", opensTomorrow: "opens tomorrow at",
      opensOn: "opens", at: "at", everyDay: "Every day", closedDay: "Closed", today: "Today"
    }
  }[lang];

  function $all(sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); }

  /* ---------- links ---------- */
  var mapsDir = "https://www.google.com/maps/dir/?api=1&destination=" + cfg.map.lat + "," + cfg.map.lng;
  var links = {
    call: cfg.phone ? "tel:+" + cfg.phone : "",
    whatsapp: cfg.whatsapp ? "https://wa.me/" + cfg.whatsapp + "?text=" + encodeURIComponent((cfg.whatsappMessage || {})[lang] || "") : "",
    directions: mapsDir,
    maps: cfg.map.googleMapsUrl || mapsDir,
    snapchat: cfg.links.snapchat,
    instagram: cfg.links.instagram,
    tiktok: cfg.links.tiktok,
    hungerstation: cfg.links.hungerstation
  };
  $all("[data-link]").forEach(function (el) {
    var url = links[el.getAttribute("data-link")];
    if (!url) {
      // hide the link, or its list item / wrapper if it has one
      var box = el.closest("[data-link-box]") || el;
      box.hidden = true;
      return;
    }
    el.href = url;
    if (/^https?:/.test(url)) {
      el.target = "_blank";
      el.rel = "noopener";
    }
  });

  /* ---------- text ---------- */
  var texts = {
    phone: cfg.phoneDisplay,
    address: cfg.address[lang],
    plusCode: cfg.map.plusCode + " " + cfg.city[lang],
    name: cfg.name[lang]
  };
  $all("[data-text]").forEach(function (el) {
    var v = texts[el.getAttribute("data-text")];
    if (v) el.textContent = v;
  });
  $all("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- map ---------- */
  $all("iframe[data-map]").forEach(function (f) {
    f.src = "https://maps.google.com/maps?q=" + cfg.map.lat + "," + cfg.map.lng + "&z=17&hl=" + lang + "&output=embed";
  });

  /* ---------- opening hours ---------- */
  function toMin(hhmm) {
    var p = hhmm.split(":");
    return (+p[0]) * 60 + (+p[1]);
  }

  // Time as shown to people: "12:00 ظهراً" / "12:00 PM"
  function fmt(hhmm) {
    var m = toMin(hhmm) % 1440, h = Math.floor(m / 60), mm = String(m % 60).padStart(2, "0");
    var h12 = (h % 12) || 12;
    if (lang === "en") return h12 + ":" + mm + " " + (h < 12 ? "AM" : "PM");
    var part = h < 12 ? "صباحاً" : h < 15 ? "ظهراً" : h < 18 ? "عصراً" : "مساءً";
    return h12 + ":" + mm + " " + part;
  }

  // The day's shift in minutes from that day's midnight. Close after midnight -> close > 1440.
  function shift(dayIndex) {
    var d = cfg.hours[DAYS[dayIndex]];
    if (!d || d.closed || !d.open || !d.close) return null;
    var o = toMin(d.open), c = toMin(d.close);
    return { open: o, close: c <= o ? c + 1440 : c, raw: d };
  }

  // Current day and minute in the restaurant's time zone
  function nowThere(date) {
    var parts = new Intl.DateTimeFormat("en-US", {
      timeZone: cfg.timezone, weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23"
    }).formatToParts(date || new Date());
    var get = function (t) { return parts.filter(function (p) { return p.type === t; })[0].value; };
    return {
      day: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(get("weekday")),
      min: (+get("hour") % 24) * 60 + (+get("minute"))
    };
  }

  function status(now) {
    var y = shift((now.day + 6) % 7);           // yesterday's shift that runs past midnight
    if (y && y.close > 1440 && now.min < y.close - 1440) {
      return { open: true, close: y.raw.close, left: y.close - 1440 - now.min };
    }
    var t = shift(now.day);
    if (t && now.min >= t.open && now.min < t.close) {
      return { open: true, close: t.raw.close, left: t.close - now.min };
    }
    for (var i = 0; i < 8; i++) {                // next opening time
      var d = (now.day + i) % 7, s = shift(d);
      if (!s || (i === 0 && now.min >= s.open)) continue;
      return { open: false, opens: s.raw.open, inDays: i, day: d };
    }
    return { open: false };
  }

  function renderStatus() {
    var now = nowThere();
    var s = status(now);
    var label, detail;
    if (s.open) {
      label = T.openNow;
      detail = (s.left <= 30 ? T.closingSoon : T.closesAt) + " " + fmt(s.close);
    } else {
      label = T.closedNow;
      if (s.opens == null) detail = "";
      else if (s.inDays === 0) detail = T.opensAt + " " + fmt(s.opens);
      else if (s.inDays === 1) detail = T.opensTomorrow + " " + fmt(s.opens);
      else detail = T.opensOn + " " + DAY_NAMES[lang][s.day] + " " + T.at + " " + fmt(s.opens);
    }
    $all("[data-open-status]").forEach(function (el) {
      el.classList.toggle("is-open", !!s.open);
      el.classList.toggle("is-closed", !s.open);
      el.innerHTML = "";
      var dot = document.createElement("span");
      dot.className = "status-dot";
      dot.setAttribute("aria-hidden", "true");
      var b = document.createElement("strong");
      b.textContent = label;
      el.appendChild(dot);
      el.appendChild(b);
      if (detail) {
        var sp = document.createElement("span");
        sp.className = "status-detail";
        sp.textContent = " · " + detail;
        el.appendChild(sp);
      }
    });
    // highlight today's row in the hours table (a shift that runs past midnight still counts as yesterday's)
    var todayIdx = now.day;
    var yShift = shift((now.day + 6) % 7);
    if (yShift && yShift.close > 1440 && now.min < yShift.close - 1440) todayIdx = (now.day + 6) % 7;
    $all("[data-hours] tr").forEach(function (tr) {
      var days = (tr.getAttribute("data-days") || "").split(",");
      var hit = days.indexOf(String(todayIdx)) !== -1;
      tr.classList.toggle("is-today", hit);
      if (hit) tr.setAttribute("aria-current", "date"); else tr.removeAttribute("aria-current");
    });
  }

  // Group days with the same hours: "Every day" or "Sunday – Thursday"
  function hourGroups() {
    var groups = [];
    for (var i = 0; i < 7; i++) {
      var d = cfg.hours[DAYS[i]] || {};
      var key = d.closed || !d.open ? "closed" : d.open + "-" + d.close;
      var last = groups[groups.length - 1];
      if (last && last.key === key) last.days.push(i);
      else groups.push({ key: key, days: [i], d: d });
    }
    return groups;
  }
  function hoursText(d) {
    return d.closed || !d.open ? T.closedDay : fmt(d.open) + " – " + fmt(d.close);
  }
  function daysText(days) {
    if (days.length === 7) return T.everyDay;
    if (days.length === 1) return DAY_NAMES[lang][days[0]];
    return DAY_NAMES[lang][days[0]] + " – " + DAY_NAMES[lang][days[days.length - 1]];
  }

  $all("[data-hours]").forEach(function (table) {
    var tbody = document.createElement("tbody");
    hourGroups().forEach(function (g) {
      var tr = document.createElement("tr");
      tr.setAttribute("data-days", g.days.join(","));
      var th = document.createElement("th");
      th.scope = "row";
      th.textContent = daysText(g.days);
      var td = document.createElement("td");
      td.textContent = hoursText(g.d);
      tr.appendChild(th);
      tr.appendChild(td);
      tbody.appendChild(tr);
    });
    table.innerHTML = "";
    table.appendChild(tbody);
  });
  $all("[data-hours-summary]").forEach(function (el) {
    el.textContent = hourGroups().map(function (g) { return daysText(g.days) + ": " + hoursText(g.d); }).join(" · ");
  });

  renderStatus();
  setInterval(renderStatus, 30 * 1000);
  document.addEventListener("visibilitychange", function () { if (!document.hidden) renderStatus(); });

  /* ---------- schema.org structured data (for Google) ---------- */
  var canonical = document.querySelector('link[rel="canonical"]');
  var home = canonical ? canonical.href.replace(/(en\/)?(menu\.html)?$/, "") : location.origin + "/";
  var byHours = {};
  DAYS.forEach(function (day) {
    var d = cfg.hours[day];
    if (!d || d.closed || !d.open) return;
    var k = d.open + "-" + d.close;
    (byHours[k] = byHours[k] || { open: d.open, close: d.close, days: [] }).days.push(day.charAt(0).toUpperCase() + day.slice(1));
  });
  var data = {
    "@context": "https://schema.org",
    "@type": "Restaurant",
    "@id": home + "#restaurant",
    name: cfg.name[lang],
    alternateName: cfg.name[lang === "ar" ? "en" : "ar"],
    url: home + (lang === "en" ? "en/" : ""),
    logo: home + "icon-512.png",
    image: [home + "assets/img/og-image.jpg", home + "assets/img/storefront-1600.webp"],
    telephone: "+" + cfg.phone,
    address: {
      "@type": "PostalAddress",
      streetAddress: cfg.address[lang].split(/[،,]\s*/).slice(0, -1).join(lang === "ar" ? "، " : ", "),
      addressLocality: cfg.city[lang],
      addressRegion: cfg.region[lang],
      addressCountry: cfg.country
    },
    geo: { "@type": "GeoCoordinates", latitude: cfg.map.lat, longitude: cfg.map.lng },
    hasMap: cfg.map.googleMapsUrl,
    openingHoursSpecification: Object.keys(byHours).map(function (k) {
      var h = byHours[k];
      return { "@type": "OpeningHoursSpecification", dayOfWeek: h.days, opens: h.open, closes: h.close };
    }),
    servesCuisine: lang === "ar" ? ["مشاوي", "شاورما", "فطائر", "بيتزا"] : ["Grills", "Shawarma", "Fatayer", "Pizza"],
    hasMenu: home + (lang === "en" ? "en/" : "") + "menu.html",
    acceptsReservations: false,
    currenciesAccepted: "SAR",
    sameAs: [cfg.links.snapchat, cfg.links.instagram].filter(Boolean)
  };
  if (cfg.postalCode) data.address.postalCode = cfg.postalCode;
  var ld = document.createElement("script");
  ld.type = "application/ld+json";
  ld.textContent = JSON.stringify(data);
  document.head.appendChild(ld);
})();
