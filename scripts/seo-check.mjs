import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

const origin = 'https://www.cart-makers.com';
const sitemap = await readFile(new URL('../public/sitemap.xml', import.meta.url), 'utf8');
const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(match => match[1]);
const failures = [];

for (const url of urls) {
  const pathname = new URL(url).pathname;
  const file = pathname === '/' ? 'dist/index.html' : `dist${pathname}/index.html`;
  let html;
  try {
    html = await readFile(join(process.cwd(), file), 'utf8');
  } catch {
    failures.push(`${pathname}: missing prerender file ${file}`);
    continue;
  }

  const title = html.match(/<title>([^<]+)<\/title>/)?.[1] || '';
  const description = html.match(/<meta name="description" content="([^"]*)"/)?.[1] || '';
  const canonical = html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] || '';
  const headings = [...html.matchAll(/<h1\b[^>]*>([\s\S]*?)<\/h1>/g)].length;
  const schema = html.match(/<script id="cartmakers-schema" type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1];

  if (!title || title.length < 20 || title.length > 70) failures.push(`${pathname}: title length ${title.length}`);
  if (!description || description.length < 50 || description.length > 170) failures.push(`${pathname}: description length ${description.length}`);
  if (canonical !== `${origin}${pathname}`) failures.push(`${pathname}: canonical ${canonical}`);
  if (headings !== 1) failures.push(`${pathname}: expected 1 H1, found ${headings}`);
  if (!schema) failures.push(`${pathname}: missing cartmakers-schema`);
  else {
    try { JSON.parse(schema); } catch { failures.push(`${pathname}: invalid JSON-LD`); }
  }
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`SEO check passed for ${urls.length} prerendered routes.`);
