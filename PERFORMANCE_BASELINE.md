

## قياس Production بعد نشر SEO growth — 2026-10-10

تم تشغيل Lighthouse Performance على الصفحة الرئيسية بعد النشر:

| الوضع | Performance | FCP | LCP | TBT | CLS |
|---|---:|---:|---:|---:|---:|
| Mobile simulated | 56 | 2.6s | 3.1s | 1,450ms | 0.007 |
| Desktop simulated | 39 | 2.1s | 2.6s | 1,500ms | 0.008 |

النتيجة: **CLS جيد جدًا وFCP/LCP تحسنا إلى نطاق قابل للعمل، لكن TBT ما زال مرتفعًا** بسبب JavaScript والتفاعلات الكثيفة في الصفحة الرئيسية. المرحلة التالية للأداء يجب أن تركز على تقسيم JavaScript، تأجيل Meta Pixel إلى idle/load، وتقليل كود الصفحة الرئيسية قبل مطاردة تحسينات صور إضافية.
