from pathlib import Path
import shutil, textwrap

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'CartMakers-social-content-pack-final'
if OUT.exists(): shutil.rmtree(OUT)
(OUT/'01-pinned-carousels').mkdir(parents=True)
(OUT/'02-posts-and-reels').mkdir(parents=True)
(OUT/'03-final-reference-style-reels').mkdir(parents=True)

shutil.copytree(ROOT/'social-carousels', OUT/'01-pinned-carousels', dirs_exist_ok=True)
shutil.copytree(ROOT/'social-post-pack-after-pins', OUT/'02-posts-and-reels', dirs_exist_ok=True)
shutil.copytree(ROOT/'reference-style-reels-final', OUT/'03-final-reference-style-reels', dirs_exist_ok=True)

captions={
'01-about': {
 'title':'CartMakers — من نحن؟','type':'Pinned Carousel','hook':'المتجر الجيد لا يبدأ من الشكل؛ يبدأ من فهم طريقة البيع.','caption':'في CartMakers نعمل على بناء أنظمة تجارة رقمية أوضح، من تجربة المستخدم والمنتج إلى الدفع والقياس.\n\nنحن لا نتعامل مع الموقع كصفحة منفصلة؛ بل كجزء من رحلة كاملة يجب أن تساعد العميل على الفهم، الاختيار، وإتمام الطلب.\n\nهذا هو دورنا: تحويل التعقيد إلى تجربة منظمة قابلة للنمو.','cta':'تابع السلسلة وتعرّف على طريقة عملنا.','ad':'هل تحتاج إلى شريك يفهم التجارة الرقمية كمنظومة كاملة؟ تعرّف على CartMakers.','headline':'نبني تجارب تجارة أوضح','hashtags':'#CartMakers #كارت_ميكرز #Ecommerce #DigitalCommerce #UX'},
'02-problems': {
 'title':'المشكلات التي نساعد في حلها','type':'Pinned Carousel','hook':'الزيارات ليست المشكلة دائمًا. أحيانًا المشكلة في الرحلة.','caption':'قد يكون لديك منتج جيد وزيارات كافية، لكن الطلب لا يكتمل بسبب نقطة احتكاك واحدة: كتالوج غير واضح، Checkout مربك، شحن يظهر متأخرًا، أو بيانات لا تشرح ما يحدث.\n\nنبدأ بتحديد نقطة التسريب قبل اقتراح أي حل.','cta':'احفظ الكاروسيل وراجع أكبر نقطة احتكاك في رحلتك.','ad':'أين يتوقف عميلك؟ اكتشف نقاط الاحتكاك قبل زيادة ميزانية الإعلانات.','headline':'اكتشف نقطة التسريب','hashtags':'#CartMakers #EcommerceGrowth #ConversionRateOptimization #تجارة_إلكترونية'},
'03-workflow': {
 'title':'كيف نعمل؟','type':'Pinned Carousel','hook':'قبل اختيار الألوان والمنصة، نحدد القرار الذي يجب أن يتخذه العميل.','caption':'نبدأ بفهم طريقة البيع والجمهور، ثم نرتب الرسالة والرحلة، وبعدها نبني ونختبر ونقيس.\n\nكل خطوة لها وظيفة واضحة: تقليل الالتباس، تحسين التجربة، وربط التنفيذ بهدف تجاري يمكن متابعته.','cta':'استكشف طريقة العمل واحجز جلسة تشخيص عند الحاجة.','ad':'من الـBrief إلى الإطلاق والقياس: شاهد كيف تتحول الفكرة إلى نظام تجارة منظم.','headline':'من الفكرة إلى نظام قابل للنمو','hashtags':'#CartMakers #WebDesign #EcommerceSystems #DigitalStrategy'},
'01-reel-before-ads': {
 'title':'عندك زيارات ومفيش طلبات؟','type':'Reference Style Reel','hook':'عندك زيارات ومفيش طلبات؟ متبدأش بالإعلانات.','caption':'قبل أن تزيد الزيارات، راجع أين تتوقف الرحلة.\n\nالمنتج، السعر، الشحن، الثقة، والـCheckout أجزاء من قرار واحد. إذا كانت نقطة واحدة غير واضحة، فقد تزيد الزيارات بينما تظل الطلبات ثابتة.\n\nابدأ بتشخيص المسار من أول صفحة المنتج حتى تأكيد الطلب.','cta':'احفظ الفيديو وراجع مسار الطلب عندك.','ad':'عندك زيارات بدون طلبات؟ قبل زيادة الميزانية، اكتشف نقطة الاحتكاك في المنتج أو الشحن أو الـCheckout.','headline':'لا تزود الزيارات قبل التشخيص','hashtags':'#CartMakers #Ecommerce #Conversion #Checkout #كارت_ميكرز'},
'02-product-page-checklist': {
 'title':'5 نقاط في صفحة المنتج','type':'Carousel + Reference Style Reel','hook':'قبل ما تزود ميزانية الإعلانات، راجع صفحة المنتج.','caption':'صفحة المنتج ليست مساحة لعرض المعلومات فقط؛ هي المكان الذي يتخذ فيه العميل قراره.\n\nراجع هذه النقاط:\n1. هل يفهم المنتج من أول نظرة؟\n2. هل السعر والشحن واضحان؟\n3. هل الصور تجيب عن أسئلة الاستخدام؟\n4. هل يوجد دليل ثقة مناسب؟\n5. هل الخطوة التالية واضحة على الموبايل؟\n\nالتفاصيل الصغيرة قد تحدد إذا كان العميل سيكمل أو يغادر.','cta':'احفظ القائمة وراجع منتجًا واحدًا اليوم.','ad':'قبل تشغيل إعلان جديد، اختبر صفحة المنتج: وضوح المنتج، السعر، الشحن، الثقة، والخطوة التالية.','headline':'راجع صفحة المنتج أولًا','hashtags':'#CartMakers #ProductPage #EcommerceTips #ConversionRate'},
'03-clean-proof': {
 'title':'المشكلة أحيانًا في ترتيب المعلومة','type':'Proof Post + Reference Style Reel','hook':'المشكلة ليست دائمًا في عدد العناصر؛ أحيانًا في ترتيبها.','caption':'عندما تظهر المعلومة المهمة في المكان الخطأ، يضطر العميل إلى البحث بدل اتخاذ القرار.\n\nزر غير واضح، شحن يظهر في النهاية، أو وصف طويل بلا ترتيب؛ كلها نقاط يمكن أن تزيد التردد حتى لو كان المنتج مناسبًا.\n\nابدأ بنقطة واحدة: ما المعلومة التي يحتاجها العميل الآن؟','cta':'أرسل لنا نقطة الاحتكاك التي تلاحظها في صفحتك.','ad':'هل صفحتك مزدحمة أم غير واضحة؟ أحيانًا لا تحتاج عناصر أكثر، بل ترتيبًا يخدم قرار الشراء.','headline':'الوضوح يحسن الرحلة','hashtags':'#CartMakers #UXDesign #EcommerceUX #ConversionOptimization'},
'04-platform-choice': {
 'title':'Shopify ولا WooCommerce؟','type':'Reference Style Reel','hook':'Shopify ولا WooCommerce؟ السؤال ده مش أول سؤال.','caption':'المنصة أداة داخل منظومة أكبر. قبل الاختيار، نراجع طريقة البيع، الدفع، الشحن، المحتوى، ومن سيدير المتجر يوميًا.\n\nالقرار الصحيح ليس المنصة الأكثر شهرة؛ بل المنصة التي تناسب طريقة التشغيل والرحلة التي يحتاجها العميل.','cta':'اكتب «منصة» إذا كنت تريد Checklist مقارنة عملية.','ad':'Shopify أم WooCommerce؟ اختَر بعد فهم طريقة البيع والتشغيل، لا قبل ذلك.','headline':'اختَر المنصة بعد فهم الرحلة','hashtags':'#CartMakers #Shopify #WooCommerce #EcommerceStrategy'},
'05-social-to-repeat': {
 'title':'من Social إلى Repeat — أين يتوقف العميل؟','type':'Carousel','hook':'العميل لا ينتقل من الإعلان إلى الطلب تلقائيًا.','caption':'كل مرحلة في رحلة التجارة لها وظيفة:\n\nSocial يجذب الانتباه.\nStore يوضح العرض.\nCatalog يسهل الاختيار.\nCheckout يطمئن العميل.\nDelivery يحدد ما بعد الطلب.\n\nإذا توقفت الرحلة، لا تبدأ بتغيير كل شيء. حدد المرحلة التي تحتاج إلى مراجعة أولًا.','cta':'اكتب المرحلة التي ترى فيها أكبر تسريب.','ad':'من أول ظهور الإعلان حتى تكرار الشراء: حدّد أين تتوقف الرحلة قبل أن تغيّر الحل.','headline':'أين يتوقف عميلك؟','hashtags':'#CartMakers #CustomerJourney #EcommerceFunnel #Growth'},
'06-checkout-friction': {
 'title':'3 أسباب تجعل العميل يخرج قبل الدفع','type':'Educational Reel','hook':'ثلاث نقاط قد تجعل العميل يخرج قبل الدفع.','caption':'راجع الـCheckout قبل أن ترفع الميزانية:\n\n1. حقول كثيرة أو غير مفهومة.\n2. تكلفة الشحن تظهر متأخرًا.\n3. عدم وضوح الدفع والتأكيد والاستبدال.\n\nكل خطوة إضافية أو معلومة متأخرة تزيد الاحتكاك في أكثر لحظة حساسية داخل الرحلة.','cta':'راجع Checkout على الموبايل قبل تشغيل الحملة التالية.','ad':'قبل أن تدفع أكثر للحصول على زيارات، تأكد أن الـCheckout لا يطلب من العميل مجهودًا زائدًا.','headline':'قلل احتكاك الـCheckout','hashtags':'#CartMakers #Checkout #EcommerceConversion #UX'},
'07-case-note': {
 'title':'Case Note: القرار قبل الزخرفة','type':'Case Note','hook':'المشروع القوي لا يبدأ بالزخرفة؛ يبدأ بقرار واضح.','caption':'في كل Case Note نركز على ثلاثة أشياء:\n\nالتحدي: ما الذي كان يحتاج إلى وضوح؟\nالقرار: ما الذي تغير في البنية أو الرسالة؟\nالدرس: ماذا يمكن لصاحب متجر آخر أن يتعلمه؟\n\nلا نعرض أرقامًا غير موثقة. نعرض طريقة التفكير التي تقود إلى تنفيذ أفضل.','cta':'شاهد الحالة كاملة في Portfolio.','ad':'كيف يتحول التحدي إلى قرار تصميم وتجربة؟ شاهد طريقة التفكير خلف المشروع.','headline':'القرار قبل الزخرفة','hashtags':'#CartMakers #CaseStudy #DesignStrategy #Ecommerce'},
'08-store-or-site': {
 'title':'هل تحتاج متجرًا أم موقعًا تعريفيًا؟','type':'Carousel','hook':'ليس كل مشروع يحتاج متجرًا. وليس كل مشروع يكفيه موقع تعريفي.','caption':'إذا كان العميل يختار منتجًا ويدفع، فأنت تحتاج رحلة تجارة.\n\nإذا كان الهدف شرح الشركة وجمع Leads، فأنت تحتاج موقعًا تعريفيًا.\n\nوإذا كان لديك الهدفان، فافصل المسارات بدل وضع كل شيء في الصفحة الأولى. القرار يعتمد على طريقة البيع، لا على شكل الموقع فقط.','cta':'احفظ الكاروسيل قبل بدء مشروعك.','ad':'متجر أم موقع تعريفي؟ ابدأ من هدف الرحلة وطريقة البيع، ثم اختَر البنية المناسبة.','headline':'اختَر البنية الصحيحة','hashtags':'#CartMakers #WebsiteStrategy #EcommerceWebsite #LeadGeneration'},
'09-bts-brief': {
 'title':'أول قرار في المشروع ليس اختيار اللون','type':'BTS','hook':'قبل اللون والخط، هناك سؤال أهم: ماذا يجب أن يفعل العميل؟','caption':'التصميم يأتي بعد فهم الجمهور، العرض، الصفحات، والتتبع.\n\nكل قرار بصري يجب أن يخدم وظيفة داخل الرحلة: يشرح، يطمئن، يوجه، أو يسهل الإجراء.\n\nلهذا يبدأ المشروع بـBrief واضح، وليس بلوحة ألوان فقط.','cta':'استكشف طريقة العمل قبل بدء التنفيذ.','ad':'الهوية مهمة، لكن وضوح الرحلة يأتي أولًا. شاهد كيف نبدأ المشروع من الـBrief.','headline':'التصميم يبدأ بالاستراتيجية','hashtags':'#CartMakers #BTS #WebDesign #DigitalStrategy'},
'10-followers-myth': {
 'title':'قلة الطلبات لا تعني دائمًا أنك تحتاج متابعين أكثر','type':'Educational Reel','hook':'قلة الطلبات مش معناها دائمًا إنك محتاج Followers أكثر.','caption':'افصل بين خمسة أشياء: الوصول، جودة الزيارات، وضوح العرض، سهولة الشراء، والقياس.\n\nقد تحتاج إلى جمهور أكبر، لكن قد تحتاج أولًا إلى تجربة أوضح ومسار يمكن قياسه. زيادة الوصول لا تعالج دائمًا نقطة التسريب.','cta':'ابدأ بالسؤال: أين يتوقف العميل؟','ad':'قبل أن تبحث عن Followers أكثر، اعرف هل المشكلة في الوصول أم في العرض أم في تجربة الشراء.','headline':'المشكلة ليست دائمًا في المتابعين','hashtags':'#CartMakers #EcommerceGrowth #DigitalMarketing #Conversion'},
'11-launch-checklist': {
 'title':'راجع هذه الأشياء قبل أن تقول: المتجر جاهز','type':'Checklist Carousel','hook':'المتجر ليس جاهزًا لمجرد أن الصفحة الرئيسية اكتملت.','caption':'قبل الإطلاق، راجع:\n\nالمنتج والسعر والصور والمخزون.\nالدفع والشحن والاستبدال.\nتجربة موبايل كاملة.\nرسائل الطلب والتأكيد.\nEvents أساسية وقياس واضح.\n\nالإطلاق بداية رحلة القياس والتحسين، وليس نهاية العمل.','cta':'احفظ القائمة ليوم الإطلاق.','ad':'هل متجرك جاهز فعلًا؟ راجع الأساسيات قبل استقبال أول طلب.','headline':'قائمة ما قبل الإطلاق','hashtags':'#CartMakers #StoreLaunch #EcommerceChecklist #متجر_إلكتروني'},
'12-diagnostic-cta': {
 'title':'مش محتاج تبدأ من الصفر','type':'Conversion Post','hook':'قبل إعادة بناء كل شيء، اكتشف أكبر تسريب.','caption':'إذا كان لديك متجر شغال لكن الطلبات أو البيانات لا تتحرك كما تتوقع، لا تبدأ بإعادة بناء كل شيء.\n\nابدأ بتحديد أكبر نقطة احتكاك: المنتج، العرض، الـCheckout، التتبع، أو رحلة ما بعد الطلب. بعد ذلك رتّب ما يستحق التنفيذ أولًا.\n\nجلسة التشخيص تساعدك على تحويل المشكلة الكبيرة إلى قرارات قابلة للتنفيذ.','cta':'احجز جلسة تشخيص من الرابط في Bio.','ad':'لا تعِد بناء متجرك قبل أن تعرف أين يتوقف العميل. ابدأ بجلسة تشخيص.','headline':'ابدأ بالتشخيص','hashtags':'#CartMakers #DiagnosticSession #CRO #EcommerceConsulting'},
}

def md(item):
 return f'''# {item["title"]}\n\n- **النوع:** {item["type"]}\n\n## Hook\n\n> {item["hook"]}\n\n## Caption جاهز للنشر\n\n{item["caption"]}\n\n## CTA\n\n**{item["cta"]}**\n\n## نسخة قصيرة للحملات\n\n**Primary Text:** {item["ad"]}\n\n**Headline:** {item["headline"]}\n\n**CTA المقترح:** تواصل معنا / احجز جلسة تشخيص / تعرّف على المزيد\n\n## Hashtags\n\n{item["hashtags"]}\n\n## ملاحظة تنفيذية\n\nلا تستخدم ادعاءات أو أرقام نتائج غير موثقة. اختبر الـHook والنسخة الإعلانية على أكثر من صيغة، ثم اعتمد النسخة التي تحقق أفضل حفظ ومشاهدة كاملة ورسائل ذات جودة.\n'''

# Add captions to pinned carousel folders.
for key in ['01-about','02-problems','03-workflow']:
 (OUT/'01-pinned-carousels'/key/'caption.md').write_text(md(captions[key]),encoding='utf-8')
# Rewrite captions in the full post pack with the campaign-ready versions.
for key in [f'{i:02d}-{name}' for i,name in [(1,'reel-before-ads'),(2,'product-page-checklist'),(3,'clean-proof'),(4,'platform-choice'),(5,'social-to-repeat'),(6,'checkout-friction'),(7,'case-note'),(8,'store-or-site'),(9,'bts-brief'),(10,'followers-myth'),(11,'launch-checklist'),(12,'diagnostic-cta')]]:
 (OUT/'02-posts-and-reels'/key/'caption.md').write_text(md(captions[key]),encoding='utf-8')
# Add a matching caption for each final reel in a clearly named captions folder.
final_captions=OUT/'03-final-reference-style-reels'/'captions'
final_captions.mkdir(parents=True,exist_ok=True)
for key, filename in {
 '01-reel-before-ads':'01-commerce-diagnostic.md',
 '02-product-page-checklist':'02-product-page-checklist.md',
 '03-clean-proof':'03-clean-proof.md',
 '04-platform-choice':'04-platform-choice.md',
}.items():
 (final_captions/filename).write_text(md(captions[key]),encoding='utf-8')

index='''# CartMakers — Full Social Content Pack\n\nحزمة تسليم كاملة للاستخدام في Instagram وFacebook والحملات الإعلانية.\n\n## المحتويات\n\n- `01-pinned-carousels/`: الكاروسيلات الثلاثة المثبتة، ملفات المصدر، صور الشرائح، وكابشن كل كاروسيل.\n- `02-posts-and-reels/`: الـ12 أصلًا بعد الـPinned Posts، بما يشمل الصور، الكاروسيلات، ملفات HTML المصدر، الفيديوهات، الصوت، وكابشن كل أصل.\n- `03-final-reference-style-reels/`: الريلز الأربعة النهائية بأسلوب الفيديو المرجعي مع كابشن كل Reel.\n\n## داخل كل Caption\n\n- Hook قوي.\n- Caption جاهز للنشر.\n- CTA واحد واضح.\n- نسخة قصيرة للحملات: Primary Text + Headline.\n- Hashtags مناسبة.\n- ملاحظة تمنع استخدام نتائج أو أرقام غير موثقة.\n\n## ملاحظة نشر\n\nلا تنشر كل الأصول دفعة واحدة. استخدم 3 منشورات أسبوعيًا، واختبر الـHooks والنسخ الإعلانية حسب الحفظ، المشاهدة الكاملة، المشاركات، والرسائل ذات الجودة.\n'''
(OUT/'CONTENT_INDEX.md').write_text(index,encoding='utf-8')
print(f'Built {OUT}')
