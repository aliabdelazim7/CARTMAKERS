# CartMakers — Brand Entity SEO

## الهدف

ربط الصيغ التالية بكيان تجاري واحد:

- `CartMakers` — الاسم الرسمي.
- `Cart Makers` — صيغة إنجليزية شائعة عند الكتابة بمسافة.
- `كارت ميكرز` — الصيغة العربية الصوتية.

الهدف ليس تكرار الكلمات بلا سياق، بل جعل الصفحة والمصادر الخارجية تشير بوضوح إلى أن الصيغ الثلاثة تعني نفس الشركة.

## ما تم تنفيذه

- إضافة `alternateName` إلى Organization وWebSite.
- إنشاء صفحة تعريف مستقلة `/about` تشرح الاسم الرسمي والصيغ البديلة في نص قابل للقراءة.
- ربط صفحة About من صفحات الموقع وprerender.
- إضافة الصفحة إلى Sitemap وRoute Manifest واختبار Browser smoke.
- الحفاظ على `CartMakers` كاسم الموقع الأساسي في `WebSite.name` و`og:site_name`.

## قواعد الاستخدام

استخدم `CartMakers` كاسم أساسي في الشعار، العنوان، وGoogle Business Profile. استخدم `Cart Makers` و`كارت ميكرز` في صفحة About، المقالات، التوقيعات، وProfiles عندما تكون الصيغة طبيعية. لا تنشئ صفحة منفصلة لكل طريقة كتابة، ولا تكرر الأسماء في كل عنوان أو فقرة.

يجب أن تكون كل الإشارات الخارجية متسقة في الاسم والدومين والروابط الرسمية. لا نشتري روابط، ولا ننشئ Profiles وهمية، ولا نضيف Reviews غير حقيقية.

## مصادر Google

Google توضح أن `WebSite` structured data على الصفحة الرئيسية هو الإشارة الأهم لتفضيل اسم الموقع، وأن `alternateName` يمكن أن يتضمن اسمًا بديلًا شائعًا. [1]

Google توضح كذلك أن Organization schema يمكن أن يحتوي على `name` و`alternateName` و`sameAs` و`logo` لمساعدة محرك البحث على فهم الكيان وتمييزه. [2]

Google تحذر من Keyword Stuffing وDoorway Abuse؛ لذلك صيغ الاسم موجودة في سياقات مفيدة وليست في قوائم متكررة أو صفحات متطابقة. [3]

## الخطوات الخارجية

1. توحيد الاسم الرسمي في Google Business Profile وFacebook وInstagram وTikTok وLinkedIn.
2. إضافة وصف قصير طبيعي يذكر `CartMakers`، ويمكن أن يوضح مرة واحدة أن الاسم يُكتب أحيانًا `Cart Makers` أو «كارت ميكرز».
3. استخدام الدومين الرسمي `https://www.cart-makers.com/` في كل الحسابات.
4. طلب Reviews حقيقية من العملاء باستخدام الاسم الرسمي، مع عدم كتابة المراجعة نيابة عن العميل.
5. مراقبة Search Console على الاستعلامات الثلاثة وتحديث صفحة About بناءً على ظهورها الفعلي.

## References

[1]: https://developers.google.com/search/docs/appearance/site-names "Google Search Central: Site names"
[2]: https://developers.google.com/search/docs/appearance/structured-data/organization "Google Search Central: Organization structured data"
[3]: https://developers.google.com/search/docs/essentials/spam-policies "Google Search Central: Spam policies"
