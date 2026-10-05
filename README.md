# CartMakers

CartMakers marketing site: **React/Vite frontend + PHP serverless contact endpoint**.

## Stack

- React 19 + Vite
- Lucide icons
- Vercel static build (`dist`)
- PHP 8.5 serverless endpoint through `vercel-php@0.9.0`

Vercel does not provide PHP as a first-party runtime; the PHP endpoint uses the community runtime documented at https://github.com/vercel-community/php.

## Local development

```bash
npm install
npm run dev
```

The contact form posts to `/api/contact`. The PHP function validates the payload and returns JSON. Connect it to the chosen CRM/email provider before production lead capture; Vercel's serverless filesystem is ephemeral.

## Build

```bash
npm run build
```

## Deploy

Push `main` to GitHub and link `aliabdelazim7/CARTMAKERS` to a Vercel project. Vercel builds `dist` and exposes `api/contact.php` through `/api/contact`.
