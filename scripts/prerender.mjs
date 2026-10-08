import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';

const dist = new URL('../dist/', import.meta.url);
const base = await readFile(new URL('index.html', dist), 'utf8');
const origin = 'https://www.cart-makers.com';
const socialImage = `${origin}/assets/cartmakers-new-logo.webp`;

const projects = [
  ['velora', 'Velora Flowers', 'متجر زهور ومناسبات يضع المناسبة والتوصيل وتجربة الهدية في مقدمة الرحلة.'],
  ['vervac', 'Vervac Animal Care', 'تجربة متجر واسعة تجمع المنتجات وقصة العلامة وتصنيفات العناية بالحيوانات.'],
  ['black-horses', 'Black Horses', 'تجربة Corporate تقود الزائر من الوعد الهندسي إلى الخدمات والمشاريع.'],
  ['sandy-collection', 'Sandy Collection', 'واجهة متجر مجوهرات تعتمد على الصورة والكولكشن والسعر لتقريب قرار الشراء.'],
  ['eg-moms-recipes', "Eg Mom's Recipes", 'تجربة Editorial تحمل قصة أكل بيتي مصري وتحوّلها إلى وصفات قابلة للاكتشاف.'],
  ['pharaohs-stone', 'Pharaohs Stone', 'موقع شركة مقاولات عربية يشرح التخصصات ويعرض نماذج من المشاريع.'],
  ['islamisch-akademisch', 'Islamisch Akademisch', 'أكاديمية ألمانية اللغة للتعلم الفردي في القرآن والتجويد والدراسات الإسلامية.'],
  ['ufuqar', 'Ufuqar News Magazine', 'بوابة أخبار عربية تعتمد على الأخبار العاجلة والأقسام المتعددة والمحتوى اليومي.'],
  ['selim-marketing', 'Selim Marketing', 'متجر عربي للخدمات التسويقية يقسم العرض حسب المنصة ويقرب قرار الشراء.'],
  ['9ten', '9TEN Store', 'متجر RTL للأحذية يقسم التجربة إلى رجالي ونسائي ويقود إلى المنتجات الجديدة.'],
  ['la-maison-francaise', 'La Maison Française', 'Landing Page موجهة للأهل تشرح التعلم والمتابعة والخطوة الأولى.'],
  ['opreva', 'OPREVA', 'متجر Skincare يربط عرض المنتجات بالمكونات والفئات والعروض.'],
  ['ms-uniforms', 'MS Uniforms', 'تجربة Catalog لمنتجات طبية تعتمد على المقاسات والألوان والتصنيفات.'],
  ['quran-academy', 'Quran Academy', 'Landing Page تعليمية تشرح البرامج وتضع التسجيل في مقدمة الرحلة.'],
  ['shopping-online-store', 'Shopping Online Store', 'متجر عربي لمعدات التخييم والمغامرات يعرض المنتجات ومحتوى يساعد على الاختيار.']
];

function esc(value) {
  return String(value).replace(/[&<>"']/g, ch => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[ch]));
}
function replaceMeta(html, selector, value) {
  return html.replace(selector, (full, before, after) => `${before}${esc(value)}${after}`);
}
function page({ lang = 'ar', dir = 'rtl', title, description, path, body, type = 'website' }) {
  let html = base
    .replace('<html lang="ar" dir="rtl">', `<html lang="${lang}" dir="${dir}">`)
    .replace(/(<title>)[^<]*(<\/title>)/, `$1${esc(title)}$2`)
    .replace(/(<meta name="description" content=")[^"]*(" \/>)/, `$1${esc(description)}$2`)
    .replace(/(<link rel="canonical" href=")[^"]*(" \/>)/, `$1${origin}${path}$2`)
    .replace(/(<meta property="og:type" content=")[^"]*(" \/>)/, `$1${type}$2`)
    .replace(/(<meta property="og:title" content=")[^"]*(" \/>)/, `$1${esc(title)}$2`)
    .replace(/(<meta property="og:description" content=")[^"]*(" \/>)/, `$1${esc(description)}$2`)
    .replace(/(<meta property="og:url" content=")[^"]*(" \/>)/, `$1${origin}${path}$2`)
    .replace(/(<meta property="og:locale" content=")[^"]*(" \/>)/, `$1${lang === 'en' ? 'en_US' : 'ar_EG'}$2`)
    .replace(/(<meta name="twitter:title" content=")[^"]*(" \/>)/, `$1${esc(title)}$2`)
    .replace(/(<meta name="twitter:description" content=")[^"]*(" \/>)/, `$1${esc(description)}$2`)
    .replace('<div id="root"></div>', `<div id="root">${body}</div>`)
    .replace(/\s*<noscript>[\s\S]*?<\/noscript>/, '');
  const pageUrl = `${origin}${path}`;
  const organization = { '@type': 'Organization', '@id': `${origin}/#organization`, name: 'CartMakers', description: 'شركة متخصصة في بناء وتطوير المواقع والمتاجر الإلكترونية وأنظمة التجارة للبراندات النامية.', url: origin, logo: `${origin}/assets/cartmakers-new-logo.webp` };
  const schema = path === '/'
    ? [{ '@context': 'https://schema.org', ...organization }, { '@context': 'https://schema.org', '@type': 'WebSite', '@id': `${origin}/#website`, name: 'CartMakers', url: origin, inLanguage: 'ar-EG', publisher: { '@id': `${origin}/#organization` } }]
    : type === 'article'
      ? { '@context': 'https://schema.org', '@type': 'CreativeWork', '@id': `${pageUrl}#project`, name: title, description, url: pageUrl, image: socialImage, inLanguage: 'ar-EG', publisher: { '@id': `${origin}/#organization` } }
      : { '@context': 'https://schema.org', '@type': 'WebPage', '@id': `${pageUrl}#webpage`, name: title, description, url: pageUrl, inLanguage: 'ar-EG', publisher: { '@id': `${origin}/#organization` }, isPartOf: { '@id': `${origin}/#website` } };
  return html.replace('</head>', `<script id="cartmakers-schema" type="application/ld+json">${JSON.stringify(schema)}</script>\n  </head>`);
}

const homeBody = `<main lang="ar" dir="rtl"><h1>CartMakers — أنظمة تجارة تشتغل وتكبر</h1><p>نبني ونحسن المتاجر والمواقع وأنظمة التجارة للبراندات النامية: المتجر، Checkout، الدفع، التوصيل، التتبع والنمو.</p><h2>نصلح الرحلة من أول Click لحد Repeat Purchase.</h2><p><a href="/portfolio">شاهد أعمال CartMakers</a> · <a href="/#contact">ابدأ من هنا</a></p></main>`;
const portfolioBody = `<main lang="ar" dir="rtl"><h1>أعمال CartMakers — مواقع ومتاجر يمكن مراجعتها</h1><p>مجموعة من مشاريع Ecommerce وCorporate وEducation وEditorial نستخدمها كمرجع بصري لفهم طريقة بناء تجربة أوضح.</p><ul>${projects.map(([slug, title, summary]) => `<li><a href="/projects/${slug}">${esc(title)}</a> — ${esc(summary)}</li>`).join('')}</ul></main>`;

const ecommerceBody = `<main lang="ar" dir="rtl"><h1>تطوير متجر إلكتروني | CartMakers</h1><p>نبني ونطوّر متاجر إلكترونية أوضح من الـCatalog حتى الـCheckout والدفع والشحن والقياس.</p><h2>ما الذي نبنيه؟</h2><ul><li>بنية كتالوج وتصفح تساعد على الاختيار</li><li>Cart وCheckout أقل احتكاكًا</li><li>دفع وCOD وشحن ضمن نطاق واضح</li><li>Tracking أساسي قبل التوسع</li></ul><p><a href="/#contact">اطلب مكالمة</a> · <a href="/portfolio">استكشف الأعمال المرجعية</a></p></main>`;

const policyBody = `<main lang="ar" dir="rtl"><h1>سياسات التعامل مع CartMakers</h1><p>توضح هذه الصفحة الدفعة المقدمة، نطاق العمل، التعديلات، التسليم، الملكية، ومسؤوليات العميل وCartMakers.</p><h2>الدفعة المقدمة</h2><p>يتم سداد 50% عند البداية لتأكيد الحجز وبدء التنفيذ، و50% قبل الإطلاق أو التسليم النهائي.</p><p><a href="/#contact">اطلب مكالمة</a> · <a href="/">ارجع إلى الموقع</a></p></main>`;

const pages = [
  ['', page({ title: 'CartMakers | تصميم وتطوير المواقع والمتاجر الإلكترونية', description: 'CartMakers بتبني وتطوّر المواقع والمتاجر الإلكترونية وأنظمة التجارة من الـCheckout حتى التتبع والنمو.', path: '/', body: homeBody })],
  ['portfolio', page({ title: 'نماذج CartMakers | أعمال المواقع والمتاجر الإلكترونية', description: 'استكشف نماذج CartMakers في المتاجر الإلكترونية والمواقع المؤسسية والتعليمية والتحريرية.', path: '/portfolio', body: portfolioBody })],
  ['policies', page({ title: 'سياسات CartMakers | الدفع ونطاق العمل', description: 'سياسات التعامل مع CartMakers: الدفع، الديبوزيت، النطاق، التسليم، الملكية ومسؤوليات العميل.', path: '/policies', body: policyBody })],
  ['services/ecommerce', page({ title: 'تطوير متجر إلكتروني | CartMakers', description: 'نبني ونطوّر متاجر إلكترونية أوضح من الـCatalog حتى الـCheckout والدفع والشحن والقياس.', path: '/services/ecommerce', body: ecommerceBody })]
];
for (const [slug, projectTitle, summary] of projects) {
  pages.push([`projects/${slug}`, page({ title: `${projectTitle} | مرجع متجر وموقع — CartMakers`, description: summary, path: `/projects/${slug}`, body: `<main lang="ar" dir="rtl"><h1>${esc(projectTitle)}</h1><p>${esc(summary)}</p><p><a href="/portfolio">ارجع إلى كل الأعمال</a> · <a href="/#contact">ابدأ مشروعك</a></p></main>`, type: 'article' })]);
}
for (const [route, html] of pages) {
  const target = route ? join(dist.pathname, route, 'index.html') : join(dist.pathname, 'index.html');
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, html);
}
console.log(`Prerendered ${pages.length} public routes.`);
