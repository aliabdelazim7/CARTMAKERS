

## 26. Floating WhatsApp contact button — 2026-10-30

تمت إضافة زر WhatsApp عائم وثابت يظهر مرة واحدة في كل الصفحات العامة، بما فيها الصفحة الرئيسية، Portfolio، صفحات المشاريع، Policies، الخدمات، Insights، وAbout. الزر يستخدم الرقم الرسمي `+20 15 58334626` والرابط `https://wa.me/201558334626` مع رسالة بداية جاهزة، ويدعم `aria-label` و`title` وتسجيل حدث `whatsapp_clicked` بموقع `floating`.

على الديسكتوب يظهر الزر كـpill بعنوان «كلّمنا على واتساب»، وعلى الموبايل يتحول إلى زر دائري 48×48 داخل منطقة آمنة أسفل يمين الشاشة، مع مراعاة `safe-area-inset-bottom` وعدم التداخل مع زر التشخيص الموجود أسفل اليسار.

تم التحقق بعد التعديل من:

- `npm run build`
- `npm run test:seo` — نجح على 30 Route.
- `npm run test:browser` — نجح على 17 Route variant.
- اختبار DOM بعد hydration — زر واحد ورابط WhatsApp صحيح في `/` و`/portfolio` و`/projects/velora` و`/policies` و`/services/ecommerce` و`/insights`.
