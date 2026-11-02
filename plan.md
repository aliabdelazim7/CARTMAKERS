# CartMakers — Custom WordPress Theme Migration Plan

## Goal

تحويل موقع CartMakers الحالي المبني بـ React/Vite إلى قالب WordPress مستقل قابل للتثبيت، مع الحفاظ على الهوية البصرية، الصفحات، المحتوى، الـRTL، التفاعلات الأساسية، والـSEO. سيظل تطبيق React الأصلي محفوظًا في مكانه كمرجع احتياطي حتى اكتمال التحقق من القالب.

## Approved implementation approach

سيتم تسليم مكوّنين متكاملين:

1. `wordpress-theme/cartmakers-theme/`: قالب العرض، القوالب، الـCSS، الـJavaScript، الأصول، والـCustomizer.
2. `wordpress-plugin/cartmakers-core/`: الوظائف التجارية القابلة للنقل، Custom Post Types، الحقول، الإعدادات، استيراد المحتوى، ومعالجة نموذج التواصل.

الفصل بين القالب والـCore يمنع فقدان المشاريع والخدمات عند تغيير القالب لاحقًا، ويضع منطق الأعمال خارج ملفات العرض.

## Design and fidelity

سيُعاد استخدام CSS الحالي والألوان والخطوط والأصول الرسمية بدل إعادة التصميم. الهوية هي Editorial Commerce Lab: Ink Navy `#101828`، Electric Lime `#C7F36B`، Cloud، RTL عربي أولًا، Manrope وIBM Plex Sans Arabic وDM Mono، ومساحات وتدفقات تشبه النسخة الحالية.

## Editable architecture

- Homepage: Theme Options وCustomizer للـHero، الرسائل، الـCTA، التواصل، الألوان، الشعار، والروابط.
- Portfolio: CPT باسم `cm_project` مع الصورة البارزة، الرابط الخارجي، التصنيف، الـtag، الملخص، الـbrief، الـinsight، المنصة، والـfeatures.
- Services: CPT باسم `cm_service` مع العنوان، الوصف، المخرجات، الخطوات، وCTA.
- Testimonials: CPT باسم `cm_testimonial` مع اسم العميل، البراند، النص، الصورة، التقييم، والموافقة على العرض.
- Insights: WordPress Posts native مع التصنيفات والوسوم والصور.
- Pages: WordPress Pages مع قوالب About وPolicies وPortfolio وInsights.
- Contact: endpoint آمن عبر `admin-post.php`، nonce، honeypot، sanitization، `wp_mail`، واختياريًا Telegram من الإعدادات.

## Public routes

سيحافظ القالب على `/`، `/about`، `/portfolio`، `/projects/{slug}`، `/services/{slug}`، `/insights`، `/insights/{post}`، `/policies`، وصفحات WordPress الاعتيادية، مع canonical وOpen Graph وJSON-LD متوافق مع إضافات SEO الشائعة.

## Project structure

- `wordpress-theme/cartmakers-theme/`: ملفات PHP الخاصة بالقالب و`assets/`.
- `wordpress-plugin/cartmakers-core/`: CPTs، settings، fields، importer، contact handler.
- `wordpress-theme/cartmakers-theme/docs/`: التثبيت والإدارة وخريطة المحتوى.
- `wordpress-theme/cartmakers-theme/assets/`: نسخ من الأصول الرسمية الحالية.

## Constraints

لا يوجد WordPress runtime أو قاعدة بيانات داخل Sandbox الحالي، لذلك سيتم اختبار syntax PHP، بنية ZIP، وجود القوالب والأصول، وفحوصات static. تفعيل القالب واختبار لوحة WordPress ورفع الصور والنموذج النهائي يحتاجان WordPress staging فعليًا.
