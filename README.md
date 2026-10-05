# CartMakers

موقع CartMakers الرسمي: **React/Vite بواجهة عربية أولًا + PHP Serverless Contact API**.

## ما يعرضه الموقع

- CartMakers كـ Commerce Operations & Growth Studio، وليس Web Design Agency عامة.
- المشكلة التجارية: الطلب يضيع بين السوشيال والـCheckout والدفع والتوصيل والقياس.
- الخدمات: الموقع/المتجر، الدفع والتشغيل، التتبع والنمو.
- الباقات:
  - Commerce Readiness Sprint — يبدأ من 15,000 جنيه.
  - Commerce Launch — يبدأ من 45,000 جنيه.
  - Growth Loop — يبدأ من 20,000 جنيه شهريًا.
- المنهجية: نفهم → نرتب → نبني → نكبر.
- المنصات والسياقات: WooCommerce، Shopify، Zid، GA4، Meta Pixel، WhatsApp، D2C، Retail، B2B، Clinics/Services.
- FAQ ونموذج Brief عربي مربوط بـ `/api/contact`.

## Stack

- React + Vite
- IBM Plex Sans Arabic + Manrope + DM Mono
- Lucide icons
- Vercel static build (`dist`)
- PHP 8.5 serverless endpoint through `vercel-php@0.9.0`

Vercel لا يوفر PHP كـruntime رسمي؛ Endpoint الـPHP يستخدم community runtime الموثق في https://github.com/vercel-community/php.

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## ملاحظة تجارية

الأسعار المعروضة Starting From لتوضيح مستوى الاستثمار وليست عرضًا نهائيًا. السعر النهائي يتحدد حسب النطاق والتكاملات والمحتوى والـQA. قبل استقبال Leads حقيقية يجب ربط Endpoint بـCRM أو Email provider لأن filesystem الخاص بالـserverless مؤقت.
