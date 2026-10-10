# CartMakers — Performance Baseline

## التحقق المنفذ في 2026-10-10

- تم إزالة Google Fonts `@import` من CSS.
- تم حفظ أوزان الخطوط المستخدمة محليًا داخل `public/fonts/` مع `font-display: swap`.
- صور الـPortfolio تستخدم WebP وأبعادًا صريحة، مع `loading="lazy"` للعناصر غير الأساسية.
- الـHero لا يستخدم `reveal` حتى لا يتأخر أكبر عنصر مرئي.
- تم الحفاظ على Critical Shell في `index.html` لمنع ظهور HTML غير منسق قبل تحميل React.

## حجم البناء الحالي

| العنصر | الحجم التقريبي |
|---|---:|
| JavaScript production bundle | 313 KB |
| CSS production bundle | 45 KB |
| Portfolio images | 668 KB |
| Local font files | 1.5 MB |

## اختبارات الجودة

```bash
npm run build
npm run test:seo
npm run test:browser
```

النتيجة الحالية:

- `SEO check passed for 29 prerendered routes.`
- `Browser smoke passed after hydration for 16 route variants.`
- تم اختبار الصفحة مع تعطيل JavaScript سابقًا للتأكد من عدم ظهور HTML خام في أول لحظة.

## الخطوة التالية بعد النشر

شغّل Lighthouse على Production من جهاز أو CI مستقر، وسجل Mobile وDesktop لكل من `/` و`/services/ecommerce` و`/portfolio`. لا تستخدم نتيجة Lighthouse واحدة كبديل عن بيانات Search Console وCrUX.

الأهداف:

- LCP أقل من 2.5 ثانية.
- INP أقل من 200ms.
- CLS أقل من 0.1.
- رفع Performance Mobile تدريجيًا إلى 85+.
