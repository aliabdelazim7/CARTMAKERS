# CartMakers Arabic-first Website Plan

## Goal
Transform the current small landing page into a conversion-focused Arabic-first company site that demonstrates CartMakers can build serious commerce websites and systems.

## Design movement
Editorial Commerce Lab: confident Arabic typography, dark ink surfaces, electric-lime signals, generous whitespace, asymmetric flow maps, browser frames, product/catalog moments, and practical proof over decorative agency clichés.

## Core principles
1. Explain the commercial problem before listing technology.
2. Make the offer architecture and starting ranges easy to compare.
3. Show the full system: storefront → checkout → payment/COD → delivery → tracking → retention.
4. Use Arabic as the primary language with concise English product names where they are actual offer names.
5. Make the website itself demonstrate the product quality: motion, performance, accessibility, proof, and clear scope.

## Visual and interaction system
- **Color philosophy:** Ink Navy creates trust and technical depth; Electric Lime is the owned action signal; Cloud gives the work room to breathe; Slate keeps explanations calm and readable.
- **Layout paradigm:** asymmetric editorial sections, split flows, browser-frame proof, and scroll-led transitions instead of centered card grids everywhere.
- **Signature elements:** checkout journey path, live browser/product frames, lime measurement signals.
- **Interaction philosophy:** every animation explains a commerce step or reduces decision friction; no decorative motion without meaning.
- **Animation:** short reveal transitions, scroll progress, hover lift, subtle image zoom, and prefers-reduced-motion fallbacks.
- **Typography:** IBM Plex Sans Arabic for Arabic content, Manrope for English brand/system labels, DM Mono for metadata and process markers.
- **Brand essence:** a practical Egyptian-first commerce systems studio for brands with real demand; sharp, commercial, trustworthy.
- **Brand voice:** direct, specific, anti-hype. Examples: “مش بنركب Theme ونمشي.” and “من أول Click لحد Repeat Purchase.”
- **Wordmark/logo:** use the official CartMakers primary/light logos and symbol without distortion.
- **Signature brand color:** Electric Lime `#C7F36B`.

## Offer system
- Commerce Readiness Sprint — entry diagnostic and prioritized fixes.
- Launch Lite — constrained fast store launch.
- Commerce Launch — fixed-scope website/store build with integrations and QA.
- Growth Loop — monthly post-launch optimization, CRO, tracking, CRM, and merchandising.
- Marketing retainers — structured add-on packages only after baseline/tracking readiness.

Prices are presented as starting ranges and remain subject to scope, integrations, content readiness, and third-party fees.

## Information architecture
Single long-form conversion page with anchored sections: Home, interactive commerce journey, proof/selected work, لماذا CartMakers, الخدمات, الباقات, المنهجية, المنصات, القطاعات, interactive diagnostic, FAQ, Contact. Separate routes: `/portfolio`, `/projects/:slug`, and `/en` for an English-first summary page.

## Frontend/backend
React/Vite renders the Arabic RTL site. PHP remains the Vercel serverless contact endpoint at `/api/contact`; it validates the lead brief, selected offer, and honeypot field, and sends to Telegram without pretending that Vercel's ephemeral filesystem is a database.

## Project structure
- `src/main.jsx` — content, section structure, interactions, diagnostic, filters, form state, route-specific rendering.
- `src/styles.css` — Arabic-first RTL visual system, motion, accessible focus states, and responsive layout.
- `public/manus-routes.json` — route declaration for `/`, `/portfolio`, `/projects/:slug`, and `/en`.
- `api/contact.php` — validated lead endpoint.
- `vercel.json` — Vite build and community PHP runtime.
- `public/robots.txt` and `public/sitemap.xml` — crawler discovery.
