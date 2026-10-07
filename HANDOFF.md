# CartMakers — Handoff Guide

> هذا الملف هو نقطة البداية لأي مطوّر أو Agent سيكمل العمل على المشروع بعد الآن.
>
> **آخر تحديث:** 2026-10-07
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
- نموذج تواصل وWhatsApp CTA.
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
- نموذج طلب مكالمة سريع: الاسم ورقم العميل فقط، مع ملخص الباقة المختارة قبل الإرسال؛ البريد والرسالة وباقي التفاصيل اختيارية داخليًا وتُستكمل في المكالمة. الاسم ورقم العميل مطلوبان، والرقم يصل إلى Telegram.
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
- Canonical URL باستخدام:
  - `https://cartmakers.vercel.app`
- Open Graph metadata.
- Twitter Card metadata.
- `og:locale` و`og:locale:alternate`.
- Meta keywords مرتبطة بالخدمات.
- JSON-LD مبسط للصفحات prerendered.
- Sitemap وRobots.
- `404` حقيقي للمشروع غير الموجود بعد إزالة rewrites العامة للصفحات.
- HTML أولي يحتوي على محتوى قابل للقراءة قبل تنفيذ React في صفحات الـinner routes.

**قبل أي تغيير في الـdomain:** يجب تحديث كل هذه الملفات/الأماكن:

- `index.html`
- `src/main.jsx` داخل `SITE_URL` وmetadata logic.
- `scripts/prerender.mjs` داخل `origin`.
- `public/sitemap.xml`.
- `public/robots.txt`.

---

## 10. نتائج الأداء الأخيرة

آخر قياس Lighthouse موثق بعد نشر commit `93ea30a`:

| البيئة | Performance | Accessibility | Best Practices | SEO |
|---|---:|---:|---:|---:|
| Mobile 375px | **95** | **100** | **100** | **100** |
| Desktop | **99** | **100** | **100** | **100** |

قياسات الموبايل:

- FCP: 2.2s
- LCP: 2.2s
- Speed Index: 2.7s
- TBT: 100ms
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
- نموذج طلب المكالمة بحقلَي الاسم ورقم العميل فقط والـserver-side validation.
- إرسال payload بالاسم والرقم فقط إلى `/api/contact` مع ملخص الباقة.
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
https://cartmakers.vercel.app/
```

آخر commit منشور:

```text
d9af675 — Temporarily hide marketing add-ons
```

آخر تحديثات مرتبطة قبله:
- `da26518` — Simplify form to request callback.
- `f30517d` — Require customer phone in brief form.

حالة آخر Vercel deployment وقت كتابة هذا الملف (Production deployment `dpl_67D14YZLunEarsp7o9i76CmN2sMD`):

```text
READY / production
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
- التأكد من إعداد domain رسمي إذا أصبح متاحًا بدل `vercel.app`.
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
