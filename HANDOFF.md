

---

## 20. تنفيذ الأولويات — 2026-10-10

تم تنفيذ دفعة التطوير التالية بالترتيب:

### الأداء والتحميل

- إزالة تحميل Google Fonts الخارجي من `src/styles.css`.
- إضافة أوزان الخطوط المستخدمة محليًا داخل `public/fonts/` مع `font-display: swap`.
- الحفاظ على Critical Shell في `index.html` لمنع FOUC وظهور HTML الخام قبل hydration.
- إبقاء صور الـPortfolio بصيغة WebP مع أبعاد صريحة وLazy Loading للعناصر غير الأساسية.

### صفحات الخدمات

تمت إضافة صفحات قابلة للفهرسة ومربوطة داخليًا:

- `/services/wordpress`
- `/services/shopify`
- `/services/checkout`
- `/services/tracking`
- `/services/website`

كل صفحة تحتوي على وصف مستقل، مخرجات، طريقة عمل، CTA، وروابط لخدمات مرتبطة.

### مركز المعرفة

تمت إضافة:

- `/insights`
- `/insights/checkout-audit`
- `/insights/launch-checklist`
- `/insights/woocommerce-or-shopify`
- `/insights/why-visits-dont-convert`

المحتوى تعليمي وعملي، ولا يتضمن أرقام أداء أو Reviews غير موثقة.

### التحويلات والقياس

تم إضافة أحداث Meta Pixel مخصصة قابلة للمراجعة:

- `brief_started`
- `brief_submitted`
- `whatsapp_clicked`
- `service_cta_clicked`
- `insight_cta_clicked`

ويظل نموذج التواصل معتمدًا على Telegram Environment Variables الموجودة في إعدادات النشر.

### SEO وPrerender

- توسعة `sitemap.xml` إلى 29 URL عامة.
- تحديث `public/manus-routes.json`.
- توسعة `scripts/prerender.mjs` لتوليد HTML أولي لصفحات الخدمات والمقالات والمشاريع.
- إضافة JSON-LD لكل Route مع أنواع Service وArticle وCreativeWork حيث يناسب.
- نجاح `npm run test:seo` على 29 Route.
- نجاح Browser smoke بعد hydration على 16 Route variant.

### ملفات تشغيل إضافية

- `LOCAL_SEO_CHECKLIST.md`: خطوات Google Business Profile والـReviews والـMentions التي تحتاج حساب Google وبيانات حقيقية.
- `PERFORMANCE_BASELINE.md`: سجل الأداء والأوامر والأهداف التالية.
- `SEO_GROWTH_ROADMAP.md`: خارطة النمو الأصلية لمدة 90 يومًا.

### ما يحتاج إجراءً خارجيًا

1. إعادة إرسال `https://www.cart-makers.com/sitemap.xml` في Google Search Console بعد النشر.
2. طلب فهرسة الصفحات الجديدة المهمة، خصوصًا `/services/ecommerce` و`/services/checkout` و`/insights`.
3. إعداد Google Business Profile أو مراجعته من الحساب المالك.
4. إضافة Reviews حقيقية فقط بعد موافقة أصحابها.
5. تشغيل Lighthouse على Production بعد اكتمال Vercel deployment وتسجيل النتائج في `PERFORMANCE_BASELINE.md`.
