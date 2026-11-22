/* ==========================================================================
   SITE SETTINGS  —  إعدادات الموقع
   --------------------------------------------------------------------------
   This is the ONLY file you need to edit to change the phone number,
   WhatsApp, opening hours, address, map pin or social/delivery links.
   Every page reads from here, so a change here updates the whole site.

   هذا هو الملف الوحيد اللي تحتاج تعدّله لتغيير رقم الجوال، الواتساب،
   أوقات الدوام، العنوان، موقع الخريطة، أو روابط التواصل والتوصيل.

   Rules: keep the quotes "..." and the commas at the end of lines.
   The menu (items and prices) is NOT here: it is in data/menu.json
   ========================================================================== */

window.SITE_CONFIG = {

  /* ---------- Name ---------- */
  name: {
    ar: "مطعم ثقة الشام",
    en: "Thiqat Al-Sham Restaurant"
  },

  /* ---------- Phone ----------
     phone:        international format, digits only (Saudi = 966, without the first 0)
     phoneDisplay: how the number is written on the page                          */
  phone: "966502619361",
  phoneDisplay: "050 261 9361",

  /* ---------- WhatsApp ----------
     Same format as phone. Leave empty ("") to hide every WhatsApp button.
     whatsappMessage is the text that appears ready-typed when a customer opens WhatsApp. */
  whatsapp: "966502619361",
  whatsappMessage: {
    ar: "السلام عليكم، أبغى أطلب من مطعم ثقة الشام",
    en: "Hello, I would like to order from Thiqat Al-Sham Restaurant"
  },

  /* ---------- Opening hours ----------
     24-hour clock, "HH:MM", Saudi time (Asia/Riyadh).
     If "close" is earlier than "open" (for example open "12:00", close "02:00"),
     the restaurant closes after midnight, on the next day. That is handled for you.
     To close a whole day, write:   friday: { closed: true },                       */
  timezone: "Asia/Riyadh",
  hours: {
    sunday:    { open: "12:00", close: "02:00" },
    monday:    { open: "12:00", close: "02:00" },
    tuesday:   { open: "12:00", close: "02:00" },
    wednesday: { open: "12:00", close: "02:00" },
    thursday:  { open: "12:00", close: "02:00" },
    friday:    { open: "12:00", close: "02:00" },
    saturday:  { open: "12:00", close: "02:00" }
  },

  /* ---------- Address ---------- */
  address: {
    ar: "شارع الأمير سلطان بن عبدالعزيز، حي الفيصلية، النعيرية",
    en: "Prince Sultan bin Abdulaziz St, Al-Faisaliyah, Al-Nu'ayriyah"
  },
  city: { ar: "النعيرية", en: "Al-Nu'ayriyah" },
  region: { ar: "المنطقة الشرقية", en: "Eastern Province" },
  country: "SA",
  postalCode: "",            // 37451 is shown on Google but not confirmed yet. Fill in when confirmed.

  /* ---------- Map pin ----------
     lat / lng: the restaurant's exact spot (Google plus code FFC9+QR).
     googleMapsUrl: the restaurant's own Google Maps listing (reviews, photos).      */
  map: {
    lat: 27.4718889,
    lng: 48.4695686,
    plusCode: "FFC9+QR",
    googleMapsUrl: "https://www.google.com/maps/place/%D9%85%D8%B7%D8%B9%D9%85+%D8%AB%D9%82%D8%A9+%D8%A7%D9%84%D8%B4%D8%A7%D9%85/@27.4718889,48.4695686,17z/data=!4m6!3m5!1s0x3fccbbdc5f69e09d:0x84b90311b2f79988!8m2!3d27.4718889!4d48.4695686!16s%2Fg%2F11yrlkz3ks"
  },

  /* ---------- Links ----------
     Leave a link empty ("") to hide it everywhere on the site.                      */
  links: {
    snapchat: "https://www.snapchat.com/@thiqat.sa",
    instagram: "https://www.instagram.com/thiqat.sa",
    tiktok: "",              // the old TikTok link no longer works
    hungerstation: "https://hungerstation.com/sa-ar/restaurant/alnuayreayh/al-faisaliyah/180455"
  }
};
