from pathlib import Path
from html import escape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'social-post-pack-after-pins'
LOGO = ROOT / 'brand-kit-clean/01-core/logo/cartmakers-new-logo-dark.png'
LOGO_LIGHT = ROOT / 'brand-kit-clean/01-core/logo/cartmakers-new-logo.webp'
FONT_REG = Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf')
FONT_BOLD = Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf')

CSS = f'''\
@font-face{{font-family:NotoArabic;src:url("{FONT_REG.as_uri()}")}}\
@font-face{{font-family:NotoArabic;src:url("{FONT_BOLD.as_uri()}");font-weight:700}}\
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1350px}} body{{font-family:NotoArabic,Arial,sans-serif;overflow:hidden}}\
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;padding:70px 76px;display:flex;flex-direction:column;justify-content:space-between;direction:rtl}}\
.dark{{background:#101828;color:#f7f8f5}} .light{{background:#f7f8f5;color:#101828}}\
.lime{{color:#c7f36b}} .muted{{color:rgba(247,248,245,.68)}} .light .muted{{color:rgba(16,24,40,.62)}}\
.top{{display:flex;align-items:center;justify-content:space-between;direction:ltr;position:relative;z-index:5}} .logo{{width:190px;height:auto;object-fit:contain}}\
.series{{font:700 19px Arial,sans-serif;letter-spacing:2px;color:#c7f36b}} .light .series{{color:#56745e}} .num{{font:700 25px Arial,sans-serif;opacity:.65}}\
.main{{position:relative;z-index:3}} .eyebrow{{font:700 18px Arial,sans-serif;letter-spacing:2px;direction:ltr;text-align:right;color:#c7f36b;margin-bottom:28px}} .light .eyebrow{{color:#56745e}}\
.h1{{font-size:74px;line-height:1.18;font-weight:700;letter-spacing:-2px;margin:0 0 28px}} .h2{{font-size:55px;line-height:1.28;font-weight:700;margin:0 0 24px}}\
.lead{{font-size:28px;line-height:1.75;max-width:820px;margin:0}} .body{{font-size:24px;line-height:1.75;margin:0}}\
.line{{height:3px;width:130px;background:#c7f36b;margin:30px 0}} .light .line{{background:#101828}}\
.footer{{display:flex;justify-content:space-between;align-items:end;direction:rtl;position:relative;z-index:5;font-size:19px}} .url{{font:700 18px Arial,sans-serif;direction:ltr}}\
.pill{{display:inline-flex;border:1px solid rgba(199,243,107,.8);padding:14px 24px;border-radius:40px;font-size:20px;color:#c7f36b}} .light .pill{{border-color:#101828;color:#101828}}\
.rings{{position:absolute;width:720px;height:720px;border:1px solid rgba(199,243,107,.20);border-radius:50%;left:-220px;bottom:-260px;z-index:1}} .rings:before,.rings:after{{content:'';position:absolute;border:1px solid rgba(199,243,107,.14);border-radius:50%}} .rings:before{{width:540px;height:540px;left:88px;top:88px}} .rings:after{{width:340px;height:340px;left:188px;top:188px}}\
.mock{{width:820px;height:370px;border:12px solid #26354c;border-radius:20px;background:white;box-shadow:0 30px 70px rgba(0,0,0,.25);margin:35px auto 0;direction:ltr;position:relative;z-index:3}} .bar{{height:42px;background:#e8ece8;display:flex;gap:8px;align-items:center;padding:0 16px}} .dot{{width:10px;height:10px;border-radius:50%;background:#a8b6ac}} .screen{{padding:28px;display:grid;grid-template-columns:1.1fr .9fr;gap:20px}} .hero{{height:240px;border-radius:14px;background:linear-gradient(135deg,#102038,#c7f36b);position:relative}} .hero:after{{content:'COMMERCE';position:absolute;bottom:22px;left:24px;font:700 26px Arial;color:white}} .side{{display:grid;gap:14px}} .side div{{background:#edf3ee;border-radius:10px}}\
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:35px}} .card{{border:1px solid rgba(247,248,245,.22);padding:28px 25px;min-height:210px;background:rgba(255,255,255,.05)}} .light .card{{border-color:rgba(16,24,40,.14);background:#fff}} .card b{{display:block;color:#c7f36b;font:700 17px Arial,sans-serif;letter-spacing:1px;margin-bottom:16px}} .light .card b{{color:#537c63}} .card h3{{font-size:28px;line-height:1.35;margin:0 0 10px}} .card p{{font-size:19px;line-height:1.65;margin:0;color:rgba(247,248,245,.68)}} .light .card p{{color:rgba(16,24,40,.62)}}\
.list{{margin-top:24px}} .item{{display:flex;align-items:flex-start;gap:18px;border-bottom:1px solid rgba(247,248,245,.18);padding:23px 0}} .light .item{{border-color:rgba(16,24,40,.14)}} .check{{font:700 32px Arial;color:#c7f36b;min-width:42px}} .light .check{{color:#537c63}} .item h3{{font-size:29px;margin:0 0 6px}} .item p{{font-size:20px;line-height:1.6;margin:0;color:rgba(247,248,245,.66)}} .light .item p{{color:rgba(16,24,40,.62)}}\
.flow{{display:flex;align-items:stretch;gap:0;margin-top:54px;direction:ltr}} .flowitem{{flex:1;position:relative;padding:25px 13px;text-align:center;border:1px solid rgba(199,243,107,.32);min-height:170px}} .flowitem:not(:last-child):after{{content:'→';position:absolute;right:-22px;top:56px;color:#c7f36b;font:700 28px Arial;z-index:4}} .flowitem strong{{display:block;color:#c7f36b;font:700 17px Arial;margin-bottom:16px}} .flowitem span{{font-size:21px;line-height:1.45;display:block;direction:rtl}}\
.badge{{font:700 18px Arial;letter-spacing:2px;color:#537c63;margin-bottom:18px}} .quote{{border-right:5px solid #c7f36b;padding-right:24px;margin-top:30px}} .quote p{{font-size:31px;line-height:1.55;margin:0;font-weight:700}}\
'''

def html(title, series, num, body, theme='dark', kind='standard'):
    logo = (LOGO if theme == 'dark' else LOGO_LIGHT).as_uri()
    if kind == 'flow':
        visual = '<div class="flow"><div class="flowitem"><strong>01</strong><span>Social</span></div><div class="flowitem"><strong>02</strong><span>Store</span></div><div class="flowitem"><strong>03</strong><span>Catalog</span></div><div class="flowitem"><strong>04</strong><span>Checkout</span></div><div class="flowitem"><strong>05</strong><span>Repeat</span></div></div>'
    elif kind == 'mock':
        visual = '<div class="mock"><div class="bar"><i class="dot"></i><i class="dot"></i><i class="dot"></i></div><div class="screen"><div class="hero"></div><div class="side"><div></div><div></div><div></div><div></div></div></div></div>'
    elif kind == 'rings':
        visual = '<div class="rings"></div>'
    else:
        visual = ''
    return f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="slide {theme}"><div class="top"><img class="logo" src="{logo}"><span class="series">{escape(series)}</span><span class="num">{num:02d}</span></div>{visual}<div class="main">{body}</div><div class="footer"><span>CARTMAKERS</span><span class="url">cart-makers.com</span></div></section></body></html>'''

def standard(title, subtitle='', eyebrow='COMMERCE DIAGNOSTIC', cta='احجز جلسة تشخيص', theme='dark', kind='rings'):
    cls = 'lime' if theme == 'dark' else ''
    return f'<div class="eyebrow">{escape(eyebrow)}</div><h1 class="h1">{title}</h1><p class="lead muted">{subtitle}</p><div class="line"></div><span class="pill">{cta}</span>'

def checklist(title, items, theme='light', cta='احفظها وراجع متجرك'):
    lis = ''.join(f'<div class="item"><span class="check">{i+1:02d}</span><div><h3>{t}</h3></div></div>' for i,t in enumerate(items))
    return f'<div class="eyebrow">COMMERCE CHECKLIST</div><h2 class="h2">{title}</h2><div class="list">{lis}</div><div class="line"></div><span class="pill">{cta}</span>'

def card_grid(title, cards, theme='light', eyebrow='COMMERCE REVIEW', cta='اسأل عن حالتك'):
    cs=''.join(f'<div class="card"><b>{i+1:02d}</b><h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(cards))
    return f'<div class="eyebrow">{eyebrow}</div><h2 class="h2">{title}</h2><div class="cards">{cs}</div><div class="line"></div><span class="pill">{cta}</span>'

def flow_page(title, subtitle, active):
    return f'<div class="eyebrow">COMMERCE FLOW</div><h2 class="h2">{title}</h2><p class="body muted">{subtitle}</p><div class="flow">' + ''.join(f'<div class="flowitem" style="background:{"rgba(199,243,107,.20)" if x==active else "transparent"}"><strong>{i:02d}</strong><span>{x}</span></div>' for i,x in enumerate(['Social','Store','Catalog','Checkout','Delivery','Repeat'],1)) + '</div><div class="line"></div><span class="pill">راجع مسار التجارة</span>'

def make_post(slug, title, caption, slides):
    folder=OUT/slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder/'caption.md').write_text(f'# {title}\n\n{caption}\n', encoding='utf-8')
    for idx, (series, body, theme, kind) in enumerate(slides,1):
        p=folder/f'{idx:02d}.html'
        p.write_text(html(title, series, idx, body, theme, kind), encoding='utf-8')

posts = [
('01-reel-before-ads','عندك زيارات ومفيش طلبات؟', '''## Reel Cover\n\n**النص داخل الفيديو:** عندك زيارات ومفيش طلبات؟ متبدأش بالإعلانات.\n\nقبل زيادة الزيارات، راجع المنتج، السعر، الشحن، الثقة، والـCheckout.\n\n**CTA:** راجع مسار الطلب قبل ما تزود الزيارات.''', [('DIAGNOSTIC REEL', standard('عندك زيارات<br><span class="lime">ومفيش طلبات؟</span>','متبدأش بالإعلانات قبل ما تراجع مسار الطلب من المنتج حتى الـCheckout.','COMMERCE DIAGNOSTIC','راجع مسار الطلب'), 'dark','rings')]),
('02-product-page-checklist','5 نقاط تراجعها قبل زيادة ميزانية الإعلانات', '''## Carousel\n\n**Caption:** قبل ما تزود الزيارات، تأكد أن صفحة المنتج تساعد على القرار. احفظ القائمة وراجع منتجًا واحدًا اليوم.\n\n**CTA:** احفظها لمراجعة صفحة منتج واحدة اليوم.''', [('PRODUCT PAGE','<div class="eyebrow">PRODUCT PAGE</div><h1 class="h1">5 نقاط تراجعها<br><span class="lime">قبل الإعلانات</span></h1><p class="lead muted">صفحة المنتج ليست معرض صور فقط؛ هي جزء من قرار الشراء.</p><div class="line"></div><span class="pill">اسحب للمراجعة</span>','dark','rings'),('PRODUCT PAGE','<div class="eyebrow">01 / CLARITY</div><h2 class="h2">هل يفهم العميل المنتج من أول نظرة؟</h2><p class="lead muted">الاسم، الفائدة، والصورة الرئيسية يجب أن تقود إلى فهم سريع.</p>','dark','mock'),('PRODUCT PAGE','<div class="eyebrow">02 / COST</div><h2 class="h2">هل السعر والشحن واضحان؟</h2><p class="lead muted">المعلومة المتأخرة قد توقف القرار قبل الـCheckout.</p>','light','mock'),('PRODUCT PAGE','<div class="eyebrow">03 / TRUST</div><h2 class="h2">هل صفحة المنتج تجيب عن الأسئلة؟</h2><div class="list"><div class="item"><span class="check">04</span><div><h3>صور الاستخدام والمقاس</h3></div></div><div class="item"><span class="check">05</span><div><h3>خطوة تالية واضحة على الموبايل</h3></div></div></div><div class="line"></div><span class="pill">احفظها وراجع متجرك</span>','light','standard')]),
('03-clean-proof','المشكلة أحيانًا في ترتيب المعلومة', '''## Clean Proof\n\n**Caption:** أحيانًا لا تحتاج الصفحة إلى عناصر أكثر؛ تحتاج إلى ترتيب أوضح للمعلومة. استخدم Screenshot حقيقيًا أو Concept معلّمًا بوضوح، وحدد ملاحظة واحدة فقط.\n\n**CTA:** اسأل عن حالتك.''', [('CLEAN PROOF', standard('المشكلة أحيانًا<br><span class="lime">في ترتيب المعلومة.</span>','حدد نقطة واحدة في الصفحة: زر غير واضح، شحن متأخر، أو وصف لا يساعد على القرار.','COMMERCE REVIEW','اسأل عن حالتك'), 'dark','mock')]),
('04-platform-choice','Shopify ولا WooCommerce؟', '''## Reel Cover\n\n**النص داخل الفيديو:** Shopify ولا WooCommerce؟ السؤال ده مش أول سؤال.\n\nالمنصة أداة. القرار يبدأ من طريقة البيع، الدفع، الشحن، ومن سيدير المتجر.\n\n**CTA:** ابدأ من طريقة البيع.''', [('PLATFORM DECISION', standard('Shopify ولا<br><span class="lime">WooCommerce؟</span>','السؤال الأول ليس المنصة. السؤال: كيف تبيع؟ ومن سيدير التشغيل؟','PLATFORM DECISION','ابدأ من طريقة البيع'), 'dark','rings')]),
('05-social-to-repeat','من Social إلى Repeat', '''## Carousel\n\n**Caption:** كل مرحلة في رحلة التجارة لها وظيفة. حدد أين يتوقف العميل قبل أن تختار الحل.\n\n**CTA:** حدد المرحلة التي تحتاج مراجعة أولًا.''', [('COMMERCE FLOW', flow_page('أين يتوقف<br><span class="lime">العميل؟</span>','من أول Click حتى إعادة الشراء، كل مرحلة تؤثر في القرار.','Social'), 'dark','flow'),('COMMERCE FLOW', flow_page('الرسالة لا تطابق<br><span class="lime">ما سيجده العميل.</span>','مراجعة البداية تمنع انقطاع الرحلة بين الإعلان والصفحة.','Store'), 'dark','flow'),('COMMERCE FLOW', flow_page('الاختيار يحتاج<br><span class="lime">وضوحًا.</span>','Catalog منظم يساعد العميل على المقارنة بدل التشتت.','Catalog'), 'dark','flow'),('COMMERCE FLOW', flow_page('الدفع خطوة<br><span class="lime">حساسة.</span>','راجع الشحن، الدفع، التأكيد، وما سيحدث بعد الطلب.','Checkout'), 'dark','flow')]),
('06-checkout-friction','3 أسباب تجعل العميل يخرج قبل الدفع', '''## Reel Cover\n\n**النص داخل الفيديو:** 3 حاجات بتخلّي العميل يخرج قبل الدفع.\n\nحقول كثيرة، تكلفة شحن متأخرة، وعدم وضوح التأكيد والاستبدال.\n\n**CTA:** راجع Checkout قبل رفع الميزانية.''', [('CHECKOUT REVIEW', card_grid('3 أسباب للتوقف<br><span class="lime">قبل الدفع</span>', [('حقول كثيرة','كل خطوة إضافية تحتاج سببًا واضحًا.'),('شحن غير واضح','المفاجأة في النهاية تضعف القرار.'),('تأكيد غير كافٍ','العميل يحتاج أن يعرف ماذا سيحدث بعد الطلب.')], 'dark','CHECKOUT FRICTION','راجع Checkout'), 'dark','standard')]),
('07-case-note','Case Note: القرار قبل الزخرفة', '''## Case Note\n\n**Caption:** كل Case Study تبدأ بتحدٍ واضح، ثم قرار، ثم تنفيذ. لا نعرض نتيجة غير موثقة؛ نعرض طريقة التفكير وما يمكن تعلمه.\n\n**CTA:** شاهد الحالة كاملة في Portfolio.''', [('CASE NOTE', card_grid('القرار قبل<br><span class="lime">الزخرفة.</span>', [('التحدي','ما الذي كان يحتاج إلى وضوح؟'),('القرار','ماذا تغير في البنية أو الرسالة؟'),('الدرس','ما الذي يمكن تطبيقه في متجر آخر؟'),('الدليل','Screenshot مصرح به أو Concept واضح.')], 'light','CASE NOTE','شاهد الحالة'), 'light','standard')]),
('08-store-or-site','هل تحتاج متجرًا أم موقعًا تعريفيًا؟', '''## Carousel\n\n**Caption:** ليس كل مشروع يحتاج نفس البنية. القرار يعتمد على طريقة البيع والهدف من الرحلة.\n\n**CTA:** احفظها قبل بدء المشروع.''', [("PROJECT TYPE", standard('متجر أم موقع<br><span class="lime">تعريفي؟</span>','اختيار البنية يبدأ من الهدف، وليس من شكل القالب.','PROJECT TYPE','احفظها قبل بدء المشروع'), 'dark','rings'),('PROJECT TYPE','<div class="eyebrow">01 / COMMERCE</div><h2 class="h2">لو العميل يختار<br>ويدفع</h2><p class="lead muted">تحتاج رحلة تجارة واضحة من المنتج حتى التأكيد.</p>','dark','mock'),('PROJECT TYPE','<div class="eyebrow">02 / LEAD GENERATION</div><h2 class="h2">لو الهدف جمع Leads</h2><p class="lead muted">تحتاج موقعًا يشرح القيمة ويقود إلى تواصل مناسب.</p>','light','standard'),('PROJECT TYPE','<div class="eyebrow">03 / BOTH</div><h2 class="h2">لو عندك الاثنين</h2><p class="lead muted">افصل المسارات بدل حشر كل شيء في الصفحة الأولى.</p><div class="line"></div><span class="pill">ابدأ من الـBrief</span>','light','standard')]),
('09-bts-brief','أول قرار في المشروع ليس اختيار اللون', '''## BTS\n\n**Caption:** التصميم يأتي بعد فهم ما يجب أن يراه العميل وما يجب أن يفعله. كل قرار بصري له وظيفة داخل الرحلة.\n\n**CTA:** استكشف طريقة العمل.''', [('BEHIND THE SCENES', standard('أول قرار في المشروع<br><span class="lime">ليس اختيار اللون.</span>','نبدأ بالـBrief، الجمهور، العرض، الصفحات، والتتبع قبل الزخرفة.','BEHIND THE SCENES','استكشف طريقة العمل'), 'dark','mock')]),
('10-followers-myth','قلة الطلبات لا تعني دائمًا أنك تحتاج متابعين أكثر', '''## Reel Cover\n\n**النص داخل الفيديو:** قلة الطلبات مش معناها دائمًا إنك محتاج Followers أكثر.\n\nافصل بين الوصول، جودة الزيارات، وضوح العرض، وسهولة الشراء.\n\n**CTA:** ابدأ بالسؤال: أين يتوقف العميل؟''', [('GROWTH NOTE', standard('المشكلة ليست دائمًا<br><span class="lime">في عدد المتابعين.</span>','راجع جودة الزيارة، وضوح العرض، وسهولة الشراء قبل زيادة الوصول.','GROWTH NOTE','أين يتوقف العميل؟'), 'dark','rings')]),
('11-launch-checklist','راجع هذه الأشياء قبل أن تقول: المتجر جاهز', '''## Carousel\n\n**Caption:** الإطلاق ليس نهاية العمل؛ هو بداية رحلة القياس والتحسين. راجع الأساسيات قبل استقبال الطلبات.\n\n**CTA:** احفظها ليوم الإطلاق.''', [('LAUNCH CHECKLIST', checklist('المتجر جاهز؟<br><span class="ink">راجع أولًا.</span>', ['المنتج والسعر والصور والمخزون','الدفع والشحن والاستبدال','تجربة موبايل كاملة','رسائل الطلب والتأكيد','Events وقياس واضح'], 'light','احفظها ليوم الإطلاق'), 'light','standard')]),
('12-diagnostic-cta','مش محتاج تبدأ من الصفر', '''## Conversion Post\n\n**Caption:** لو عندك متجر شغال لكن الطلبات أو البيانات لا تتحرك كما تتوقع، لا تبدأ بإعادة بناء كل شيء. ابدأ بتحديد أكبر تسريب، ثم رتب ما يستحق التنفيذ أولًا.\n\n**CTA:** احجز جلسة تشخيص من الرابط في Bio.''', [('DIAGNOSTIC', standard('مش محتاج<br><span class="lime">تبدأ من الصفر.</span>','ابدأ من الوضع الحالي وحدد أكبر نقطة احتكاك في المتجر أو الـCheckout أو التتبع.','COMMERCE DIAGNOSTIC','احجز جلسة تشخيص'), 'dark','rings')]),
]

# Fix intentionally quoted entries in post 8 after Python literal creation.
for p in posts:
    make_post(*p)

# Root readme and index
(OUT/'README.md').write_text('''# CartMakers — Social Post Pack After Pinned Posts\n\nحزمة أول 12 منشورًا بعد الـPinned Posts.\n\n- المقاس: 1080×1350 لكل صورة.\n- كل مجلد يحتوي `caption.md` وملفات HTML مصدر وPNG جاهز للنشر.\n- منشورات الـCarousel تحتوي شرائح مرقمة منفصلة.\n- أغطية الـReels موجودة كصورة واحدة، ونص الفيديو في `caption.md`.\n- النصوص لا تحتوي نتائج أو Reviews مختلقة.\n\nابدأ بالنشر بهذا الترتيب: 01، 02، 03. ثم راقب الحفظ والمشاركة والرسائل قبل تعديل الـHooks للمجموعة التالية.\n''', encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=1)
    for html_file in sorted(OUT.glob('*/*.html')):
        page.goto(html_file.as_uri(), wait_until='networkidle')
        png = html_file.with_suffix('.png')
        page.locator('.slide').screenshot(path=str(png))
    browser.close()

print(f'Built {len(list(OUT.glob("*/*.png")))} PNG assets in {OUT}')
