# CartMakers — Handoff Guide

> هذا الملف هو نقطة البداية لأي مطوّر أو Agent سيكمل العمل على المشروع بعد الآن.
>
> **آخر تحديث:** 2026-10-08
> **اللغة الأساسية للمشروع:** العربية RTL  

---

## 1. تعريف المشروع

CartMakers هو موقع شركة تبني وتحسن أنظمة التجارة الإلكترونية والمواقع للبراندات النامية، مع تركيز على:

- Storefronts والمواقع والمتاجر.
- Checkout وCOD والتشغيل والتوصيل.
- Tracking وAnalytics وGrowth.
- مواقع WordPress/WooCommerce.
- Shopify / سلة / زد حسب احتياج المشروع.
- تحسين تجربة البيع من أول Click حتى Repeat Purchase.

الموقع ليس صفحة خدمات تقليدية فقط؛ هو موقع تسويقي تفاعلي يحتوي على باقات، Diagnostic، Portfolio، FAQ، Contact Brief، وTestimonials.

---

## 2. المسارات الحالية

| المسار | الوظيفة |
|---|---|
| `/` | الصفحة الرئيسية العربية RTL |
| `/portfolio` | صفحة جميع الأعمال مع الفلاتر |
| `/policies` | صفحة السياسات والاتفاق التجاري |
| `/projects/:slug` | صفحة مشروع تفصيلية |
| `/api/contact` | Endpoint نموذج التواصل |
| `/sitemap.xml` | Sitemap للمسارات العامة |
| `/robots.txt` | قواعد الزحف وربط الـSitemap |
| `/manus-routes.json` | Route manifest الخاص بالمنصة |

صفحات المشاريع الموجودة في الـsitemap:

- `velora`
- `vervac`
- `black-horses`
- `sandy-collection`
- `eg-moms-recipes`
- `pharaohs-stone`
- `islamisch-akademisch`
- `ufuqar`
- `selim-marketing`
- `9ten`
- `la-maison-francaise`
- `opreva`
- `ms-uniforms`
- `quran-academy`
- `shopping-online-store`

---

## 3. هيكل الملفات المهم

```text
CARTMAKERS/
├── index.html                  # HTML الأساسي وSEO metadata
├── package.json                # أوامر npm والاعتمادات
├── vercel.json                 # إعداد Vercel وAPI rewrite
├── README.md                   # التوثيق العام
├── plan.md                     # قرارات وخطة المشروع
├── HANDOFF.md                  # هذا الملف
├── api/
│   └── contact.php             # استقبال نموذج التواصل وإرساله
├── public/
│   ├── assets/                 # اللوجو والـbrand assets
│   ├── portfolio/              # صور المشاريع بصيغة WebP
│   ├── robots.txt
│   ├── sitemap.xml
│   └── manus-routes.json
├── scripts/
│   └── prerender.mjs           # إنشاء HTML أولي لكل route وقت الـbuild
└── src/
    ├── main.jsx                # React app، البيانات، الصفحات والتفاعلات
    └── styles.css              # التصميم، RTL، responsive، animations
```

---

## 4. التشغيل المحلي

من داخل مجلد المشروع:

```bash
npm ci
npm run dev -- --host 0.0.0.0 --port 4173
```

ثم افتح:

```text
http://127.0.0.1:4173/
http://127.0.0.1:4173/portfolio
http://127.0.0.1:4173/projects/velora
```

لبناء نسخة الإنتاج:

```bash
npm run build
```

أمر `build` ينفذ مرحلتين:

1. `vite build`
2. `node scripts/prerender.mjs`

وتنتج المرحلة الثانية ملفات HTML داخل `dist/` للمسارات الداخلية، مثل:

```text
dist/portfolio/index.html
dist/projects/velora/index.html
```

لتشغيل نسخة الإنتاج محليًا:

```bash
npm run build
npm run preview -- --host 0.0.0.0 --port 4174
```

---

## 5. الهوية البصرية

تم استخدام هوية CartMakers من Brand Starter Kit:

- اللون الأساسي الداكن: `#101828`
- اللون المميز الأخضر: `#C7F36B`
- الخلفية الفاتحة: `#F7F8F5`
- اللوجو الأساسي في:
  - `public/assets/cartmakers-primary.svg`
  - `public/assets/cartmakers-primary-light.svg`
- رمز اللوجو:
  - `public/assets/cartmakers-symbol.svg`

**مهم:** لا تستخدم نصًا عاديًا بدل اللوجو، ولا تضف CSS عامة مثل `img { width: ... }` قد تصغر اللوجو. يوجد class واضح اسمه `.brand-logo`.

### آخر تحديث للهوية — 2026-10-08

- تم استبدال اللوجو المرئي في الـHeader والـFooter وصفحات Portfolio/Projects/Policies باللوجو المرفق الجديد.
- الملفات الحالية المستخدمة:
  - `public/assets/cartmakers-new-logo.webp` — اللوجو الكامل المرفق بعد قص المساحات البيضاء الزائدة.
  - `public/assets/cartmakers-new-mark.webp` — نسخة مربعة من رمز العربة للاستخدام كـfavicon.
- تم تحديث `index.html` و`src/main.jsx` و`scripts/prerender.mjs` وبيانات Open Graph/Twitter/Schema لاستخدام اللوجو الجديد.
- تم ضبط أبعاد `.brand-logo` لتناسب الـwordmark الجديد، مع مراجعة احتواء الموبايل.
- ملفات SVG القديمة ما زالت موجودة كأصول legacy، لكنها لم تعد مستخدمة في الواجهة أو الـSEO.
- تم إصلاح أيقونة التاب بعد ملاحظة ظهورها بشكل غير واضح: الملف الحالي `public/assets/cartmakers-favicon.png` بصيغة PNG شفافة ومقاس 48×48، ومعلن في `index.html` مع cache-busting `?v=2`.
- تم إضافة `apple-touch-icon` بنفس الأيقونة.
- عنوان التاب الرئيسي أصبح مختصرًا وواضحًا: `CartMakers | أنظمة التجارة والنمو`، وتم توحيده في الـprerender و`updateSeo()`.
- تم تحديث أصول السوشيال باستخدام اللوجو المرفق الحالي، وليس الـSVG القديم الموجود في الـStarter Kit.
- داخل الريبو يوجد `brand-social/Social Profile Pic/` ويحتوي على `cartmakers-profile-1080.png` و`cartmakers-cover-1640x856.png`.
- تم تجهيز نسخة حزمة هوية محدثة باسم `CartMakers-brand-starter-kit-updated.zip` تحتوي على نفس المجلد، بالإضافة إلى نسخة اللوجو المرفق الأصلية والنسخة المحسنة.

الخطوط الحالية محملة من Google Fonts داخل `src/styles.css`:

- IBM Plex Sans Arabic
- Manrope
- DM Mono

---

## 6. الباقات الحالية

الباقات التي يجب أن تظل متزامنة بين العربي والإنجليزي والـDiagnostic:

### Starter

- السعر المبدئي: 4,000 جنيه.
- صفحة رئيسية + 4 صفحات داخلية.
- Responsive للموبايل.
- WordPress وTheme مناسب.
- نموذج تواصل؛ لا يوجد حاليًا رقم WhatsApp أو رابط `wa.me` ثابت داخل الموقع.
- تسليم وإرشادات تشغيل.

### Business

- السعر المبدئي: 7,000 جنيه.
- حتى 8 صفحات مخصصة.
- تصميم UI كامل للبراند.
- WordPress + إعدادات SEO أساسية.
- Leads وTracking أساسي.
- رفع المحتوى وQA قبل الإطلاق.

### Commerce

- السعر المبدئي: 9,000 جنيه.
- WooCommerce كامل.
- حتى 20 منتجًا عند التسليم.
- Cart وCheckout وCOD.
- إعداد الدفع والشحن حسب المتاح.
- Tracking وHandover.

### Add-ons

الإضافات محفوظة في الكود لكنها **مخفية مؤقتًا من واجهة العميل** لتقليل التشتت أثناء طلب المكالمة. التحكم في ظهورها موجود في `src/main.jsx` عبر: `SHOW_MARKETING_ADDONS = false`.

- Media Buying — حسب الميزانية والنطاق.
- Social & Content — حسب القنوات والمخرجات.
- Creative & Design — حسب عدد الـAssets.
- Tracking & Analytics — +2,500 جنيه.
- CRO & Checkout Fixes — +3,500 جنيه.
- Product Photography — حسب العدد والموقع.

**قاعدة مهمة:** لا تعيد أسماء الباقات القديمة مثل `Launch Lite` أو `Growth Loop` أو `Commerce Launch` داخل الـDiagnostic أو النصوص الجديدة. الأسماء الحالية هي Starter وBusiness وCommerce.

---

## 7. المكونات والتفاعلات الموجودة

داخل `src/main.jsx` توجد التفاعلات الآتية:

- تبديل نوع الموقع: WordPress أو Shopify / سلة / زد.
- اختيار الباقة وتحديث الملخص والسعر.
- بيانات Add-ons موجودة، لكن قسمها مخفي مؤقتًا عبر `SHOW_MARKETING_ADDONS = false` لتبسيط مسار العميل.
- Commerce Diagnostic وتوصية Starter/Business/Commerce.
- Portfolio slider.
- Portfolio filters، ومنها E-commerce.
- FAQ accordion.
- WhatsApp: لا يوجد رابط فعلي حاليًا (`wa.me` أو `api.whatsapp.com`). عبارات WhatsApp الموجودة هي Copy/CTA فقط وليست تكاملًا قابلًا للنقر. لإضافته يلزم رقم WhatsApp الرسمي ورسالة البداية ثم تحديث الأزرار والـCTA واختبار الرابط على Production.
- إدارة metadata حسب الصفحة عبر `updateSeo()`.
- IntersectionObserver للـreveal animations في الأقسام أسفل الـHero.

**مهم للأداء:** لا تضف class `reveal` إلى الـHero أو أي عنصر LCP أعلى الشاشة. الـHero حاليًا يرسم فورًا لتحسين LCP ومنع Layout Shift، بينما animations مخصصة للأقسام اللاحقة.

---

## 8. Testimonials

يوجد حاليًا Review واحد فقط منشور بدون صورة:

- محمد صبحي — LocalBrand Startup.

النص منشور بصياغة عربية طبيعية وتم اختباره على Production.

**قاعدة ثقة مهمة:** لا يتم اختلاق Reviews ونسبتها إلى أشخاص أو شركات حقيقية. لإضافة Review جديد يجب أن يرسل صاحب المشروع أو الفريق:

1. اسم الشخص.
2. اسم الشركة أو نوع النشاط.
3. نص التجربة.
4. تأكيد الموافقة على النشر.

يمكن إضافة نصوص تجريبية فقط إذا كانت معلّمة بوضوح كـ`Sample testimonial` أو `نموذج توضيحي` وليست Social Proof حقيقية.

---

## 9. تحسينات SEO التي تم تنفيذها

تم تنفيذ الآتي:

- Route-specific HTML وقت البناء عبر `scripts/prerender.mjs`.
- Metadata منفصلة للـPortfolio وصفحات المشاريع.
- الدومين الرسمي الحالي هو `https://www.cart-makers.com`.
- تم تحديث الـcanonical وOpen Graph وSitemap وRobots لاستخدام الدومين الرسمي.
- Open Graph metadata.
- Twitter Card metadata.
- `og:locale` و`og:locale:alternate`.
- Meta keywords مرتبطة بالخدمات.
- JSON-LD مبسط للصفحات prerendered.
- Sitemap وRobots.
- Google Search Console verification tag داخل الـHTML الأساسي.
- Robots metadata صريحة تسمح بالفهرسة ومعاينة الصور والنصوص.
- Sitemap يتضمن `/policies` مع `lastmod`.
- JSON-LD أقوى للـOrganization وWebSite وصفحات المشاريع.
- `404` حقيقي للمشروع غير الموجود بعد إزالة rewrites العامة للصفحات.
- HTML أولي يحتوي على محتوى قابل للقراءة قبل تنفيذ React في صفحات الـinner routes.

### Google Search Console — آخر حالة

- تم وضع كود التحقق داخل `index.html`:
  `numI3mJ990GYjj5Pj2YUkmehjy1X0hsIfVqxfyZ7f_k`.
- الـSitemap الرسمي الذي يجب تقديمه في Search Console هو:
  `https://www.cart-makers.com/sitemap.xml`.
- بعد ظهور رسالة `Couldn't fetch` في Search Console، تم فحص الرابط مباشرة باستخدام User-Agents الخاصة بـGoogle وكانت النتيجة:
  - HTTP `200`.
  - `Content-Type: application/xml; charset=utf-8`.
  - XML صالح وقابل للتحليل.
  - 18 URL داخل الملف.
  - `/policies` موجودة داخل الـSitemap.
- تم تثبيت Headers صريحة في `vercel.json` لـ`/sitemap.xml` و`/robots.txt` مع Cache-Control لمدة ساعة.
- بعد النشر الأخير، الفحص المباشر أعاد `status=200` و`xml=valid` عند استخدام `Googlebot`.
- إذا بقيت الحالة القديمة في Search Console، احذف الإدخال وأعد إضافة `sitemap.xml` ثم انتظر إعادة القراءة؛ الحالة القديمة لا تعكس بالضرورة الاستجابة الحالية.

### خطوات Search Console التالية

1. افتح **Sitemaps** داخل Property الدومين الرسمي.
2. أعد إرسال `sitemap.xml`.
3. استخدم **URL Inspection** واطلب الفهرسة للصفحة الرئيسية و`/portfolio` و`/policies`.
4. بعد بدء الزيارات، راقب **Pages / Indexing** و**Performance / Queries**.

> لا يوجد في الكود ما يضمن ظهور الموقع فورًا في Google؛ قرار الفهرسة وتوقيته بيد Google وقد يستغرق من ساعات إلى عدة أيام.

**قبل أي تغيير في الـdomain:** يجب تحديث كل هذه الملفات/الأماكن:

- `index.html`
- `src/main.jsx` داخل `SITE_URL` وmetadata logic.
- `scripts/prerender.mjs` داخل `origin`.
- `public/sitemap.xml`.
- `public/robots.txt`.

---

## 10. نتائج الأداء الأخيرة

آخر قياس Lighthouse على `https://www.cart-makers.com/` بتاريخ 2026-10-08:

| البيئة | Performance | Accessibility | Best Practices | SEO |
|---|---:|---:|---:|---:|
| Mobile 375px | **91** | **100** | **100** | **100** |
| Desktop | **88** | **100** | **100** | **100** |

قياسات الموبايل:

- FCP: 2.3s
- LCP: 2.3s
- Speed Index: 5.7s
- TBT: 70ms
- CLS: 0.022

تم اكتشاف وإصلاح مشكلتين مهمتين:

1. الـhoneypot كان يستخدم `left:-10000px` ويسبب horizontal overflow في RTL.
2. الـHero كان مخفيًا بـ`opacity:0` أثناء animation، مما أخّر LCP وسبب Layout Shift.

قاعدة مستقبلية: لا تستخدم عناصر off-screen بـ`left:-10000px`. استخدم visually-hidden pattern مثل الموجود في `.form-trap`.

---

## 11. اختبارات UI/UX المنفذة

تم اختبار:

- Home على desktop.
- Mobile Lighthouse عند عرض 375px.
- `/portfolio`.
- صفحة مشروع تفصيلية.
- تبديل الباقات والمنصات.
- Add-ons.
- FAQ.
- Diagnostic.
- Portfolio E-commerce filter.
- الروابط الداخلية.
- الصور الأساسية.
- صفحة Policies مستقلة بالعربية توضح الديبوزيت 50%، النطاق، التعديلات، التسليم، الإلغاء، الملكية، السرية، ومسؤوليات الطرفين.
- مراجعة قنوات التواصل: لا يوجد رابط WhatsApp فعلي حاليًا (`wa.me` أو `api.whatsapp.com`)؛ أي ظهور لكلمة WhatsApp داخل المحتوى هو وصف تسويقي أو تسمية لقناة التواصل.
- إخفاء قسم Add-ons من الواجهة مع إبقاء البيانات والكود قابلين للإرجاع.
- الـhorizontal overflow.
- أزرار بدون labels.
- ظهور الـHero.
- ظهور Review الموجود.

آخر فحص DOM على Production أعاد:

```text
horizontalOverflow: false
failedInternalLinks: 0
unlabeledButtons: 0
heroVisible: true
```

ملاحظة: أداة screenshot الخاصة بـWebdev لم تكن متاحة لأن هوية مشروع Webdev غير متوفرة في الجلسة؛ لذلك تم الاعتماد على Lighthouse mobile + browser click-through + DOM checks.

---

## 12. GitHub وVercel

الريبو:

```text
https://github.com/aliabdelazim7/CARTMAKERS
```

الفرع الأساسي:

```text
main
```

الموقع:
```text
https://www.cart-makers.com/
```

`https://cart-makers.com` يحوّل إلى `https://www.cart-makers.com` بحالة 308.
رابط `https://cartmakers.vercel.app` القديم لم يعد هو العنوان الأساسي للموقع.

آخر commit منشور:
```text
7ba679b — Fix browser favicon and tab title
```

التحديثات المرتبطة الأخيرة:
- `e0a4035` — Update project handoff for callback flow.
- `d9af675` — Temporarily hide marketing add-ons.
- `da26518` — Simplify form to request callback.

آخر تحديثات مرتبطة أقدم:
- `f30517d` — Require customer phone in brief form.

حالة آخر Vercel deployment وقت كتابة هذا الملف (Production deployment `dpl_9kHFt6o1qZ7pYTLLs5whYAscMvC5`، مبني من Commit `c4fdb38`):

```text
تم التحقق من الاستجابة Live على `https://www.cart-makers.com/sitemap.xml` بعد هذا النشر: `200 / application/xml / XML valid`.
```

**قاعدة العمل المطلوبة:** أي تعديل جديد يجب أن يمر بهذا الترتيب:

```bash
npm run build
git diff --check
git add <files>
git commit -m "Clear commit message"
git push origin main
```

ثم يتم التأكد من Vercel deployment واختبار الرابط العام.

---

## 13. Checklist قبل أي تعديل كبير

1. اقرأ `HANDOFF.md` و`plan.md`.
2. افحص الحالة:

   ```bash
   git status --short --branch
   git log -5 --oneline --decorate
   ```

3. لا تغيّر الباقات دون تحديث العربي والإنجليزي والـDiagnostic.
4. لا تضف Reviews غير مؤكدة على أنها حقيقية.
5. لا تغيّر الـdomain أو canonical دون تحديث كل مصادر SEO.
6. لا تضف animation إلى Hero أو LCP element.
7. بعد تعديل React أو CSS شغّل:

   ```bash
   npm run build
   git diff --check
   ```

8. اختبر `/` و`/portfolio` وصفحة مشروع واحدة.
9. اختبر Lighthouse على Mobile وDesktop إذا كان التعديل بصريًا أو متعلقًا بالأداء.
10. ارفع كل تحديث إلى GitHub وتأكد من Vercel.

---

## 14. أولويات مقترحة بعد ذلك

### أولوية عالية

- إضافة Reviews حقيقية بعد الحصول على موافقة أصحابها.
- ربط Google Search Console وقياس Queries وIndex Coverage.
- تحسين font loading إذا أمكن self-hosting بدون تدهور بصري.

### أولوية متوسطة

- إضافة صفحات خدمة مستقلة قابلة للفهرسة مثل:
  - `/services/ecommerce`
  - `/services/wordpress`
  - `/services/checkout`
  - `/services/tracking`
- إضافة Case Study حقيقية لكل مشروع مهم.
- إضافة FAQ schema فقط إذا ظل المحتوى مطابقًا تمامًا للظاهر للمستخدم.

### أولوية منخفضة

- تقسيم `src/main.jsx` إلى components وdata modules أصغر.
- إضافة automated Playwright/Cypress smoke tests.
- تحسين إدارة الصور عبر responsive `srcset` إذا زاد عدد المشاريع أو أضيفت صور أكبر.

---

## 15. لا تفعل هذه الأشياء

- لا ترجع rewrites العامة من `/portfolio` أو `/projects` إلى `/` بدون فهم تأثيرها على prerender والـ404.
- لا تعيد إضافة تبديل لغة أو مسار `/en` بدون قرار جديد واضح من صاحب المشروع.
- لا تحذف `scripts/prerender.mjs` من أمر build.
- لا تغيّر اسم الباقة الحالية إلى اسم قديم.
- لا تستخدم شهادات أو Reviews مختلقة.
- لا تضف `overflow-x:hidden` كحل سريع قبل فهم سبب overflow؛ تم إصلاح السبب الحقيقي في `.form-trap`.
- لا تضغط أو تستبدل اللوجو الرسمي بملف غير متوافق.
- لا تعتمد على Lighthouse وحده؛ افحص أيضًا HTML الخام والـbrowser DOM والروابط.
