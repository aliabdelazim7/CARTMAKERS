import { spawn, spawnSync } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const baseUrl = 'http://127.0.0.1:4175';
const chromium = process.env.CHROMIUM_PATH || '/usr/bin/chromium';
const routes = [
  { path: '/', title: 'تصميم وتطوير المواقع والمتاجر الإلكترونية', canonical: '/' },
  { path: '/portfolio', title: 'أعمال المواقع والمتاجر الإلكترونية', canonical: '/portfolio' },
  { path: '/portfolio/', title: 'أعمال المواقع والمتاجر الإلكترونية', canonical: '/portfolio' },
  { path: '/projects/velora', title: 'Velora Flowers', canonical: '/projects/velora' },
  { path: '/projects/velora/', title: 'Velora Flowers', canonical: '/projects/velora' },
  { path: '/services/ecommerce', title: 'تطوير متجر إلكتروني', canonical: '/services/ecommerce' },
];

const server = spawn('npm', ['run', 'preview', '--', '--host', '127.0.0.1', '--port', '4175'], {
  stdio: ['ignore', 'pipe', 'pipe'],
  env: { ...process.env, BROWSER: 'none' },
});
let serverOutput = '';
server.stdout.on('data', chunk => { serverOutput += chunk.toString(); });
server.stderr.on('data', chunk => { serverOutput += chunk.toString(); });

async function waitForServer() {
  for (let attempt = 0; attempt < 40; attempt += 1) {
    try {
      const response = await fetch(`${baseUrl}/`);
      if (response.ok) return;
    } catch {}
    await delay(250);
  }
  throw new Error(`Preview server did not start.\n${serverOutput}`);
}

function inspect(path) {
  const result = spawnSync(chromium, [
    '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
    '--disable-dev-shm-usage', '--virtual-time-budget=3500', '--dump-dom', `${baseUrl}${path}`,
  ], { encoding: 'utf8', maxBuffer: 12 * 1024 * 1024 });
  if (result.status !== 0) throw new Error(`${path}: Chromium exited with ${result.status}\n${result.stderr}`);
  return result.stdout;
}

try {
  await waitForServer();
  const failures = [];
  for (const route of routes) {
    const html = inspect(route.path);
    const title = html.match(/<title>([^<]*)<\/title>/)?.[1] || '';
    const canonical = html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] || '';
    const h1Count = [...html.matchAll(/<h1\b/g)].length;
    const schemaCount = [...html.matchAll(/<script id="cartmakers-schema"/g)].length;
    const expectedCanonical = `https://www.cart-makers.com${route.canonical}`;
    if (!title.includes(route.title)) failures.push(`${route.path}: title mismatch (${title})`);
    if (canonical !== expectedCanonical) failures.push(`${route.path}: canonical mismatch (${canonical})`);
    if (h1Count !== 1) failures.push(`${route.path}: expected 1 H1, found ${h1Count}`);
    if (schemaCount !== 1) failures.push(`${route.path}: expected 1 JSON-LD block, found ${schemaCount}`);
  }
  if (failures.length) {
    console.error(failures.join('\n'));
    process.exitCode = 1;
  } else {
    console.log(`Browser smoke passed after hydration for ${routes.length} route variants.`);
  }
} finally {
  server.kill('SIGTERM');
}
