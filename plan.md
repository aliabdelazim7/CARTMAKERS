# CartMakers Arabic-first Website Plan

## Goal
Transform the current small landing page into a conversion-focused Arabic-first company site that demonstrates CartMakers can build serious commerce websites and systems.

## Design movement
Editorial Arabic commerce studio: confident typography, dark ink surfaces, electric-lime signals, generous whitespace, asymmetric flow maps, and practical proof over decorative agency clichés.

## Core principles
1. Explain the commercial problem before listing technology.
2. Make the offer architecture and starting ranges easy to compare.
3. Show the full system: storefront → checkout → payment/COD → delivery → tracking → retention.
4. Use Arabic as the primary language with concise English product names where they are actual offer names.

## Information architecture
Single long-form conversion page with anchored sections: Home, لماذا CartMakers, الخدمات, الباقات, المنهجية, المنصات, القطاعات, أعمال تجريبية/طريقة التفكير, FAQ, Contact. This keeps launch simple while making the company feel complete; sections are represented in `public/manus-routes.json` as the root page.

## Offer system
- Commerce Readiness Sprint — entry diagnostic and prioritized fixes.
- Commerce Launch — fixed-scope website/store build with integrations and QA.
- Growth Loop — monthly post-launch optimization, CRO, tracking, CRM, and merchandising.
- Marketing retainers — structured add-on packages only after baseline/tracking readiness.

Prices are presented as starting ranges and remain subject to scope, integrations, content readiness, and third-party fees.

## Frontend/backend
React/Vite renders the Arabic RTL site. PHP remains the Vercel serverless contact endpoint at `/api/contact`; it validates the lead brief and is ready to connect to a CRM/email provider without pretending that Vercel's ephemeral filesystem is a database.

## Project structure
- `src/main.jsx` — content, section structure, interactions, form state.
- `src/styles.css` — Arabic-first RTL visual system and responsive layout.
- `public/manus-routes.json` — route declaration.
- `api/contact.php` — validated lead endpoint.
- `vercel.json` — Vite build and community PHP runtime.
