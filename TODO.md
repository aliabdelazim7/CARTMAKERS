# CartMakers WordPress Migration — Outcome TODO

## 1. Preserve the original implementation

- Keep the existing React/Vite application and all original source files intact until the WordPress migration is verified.
- Use the current website as the visual and content source of truth; do not redesign or replace real content with placeholders.

## 2. Deliver an installable custom theme

- Create a standalone theme with `style.css`, `functions.php`, `index.php`, `header.php`, `footer.php`, `front-page.php`, `page.php`, `single.php`, `archive.php`, `search.php`, `404.php`, template parts, CSS, JavaScript, images, fonts, and documentation.
- Make the theme installable through WordPress Dashboard → Appearance → Themes → Add New Theme → Upload Theme.

## 3. Make the website editable from WordPress Admin

- Make global logo, favicon, colors, contact data, social links, header and footer editable.
- Make homepage hero, CTAs, services, packages, proof, testimonials, FAQ and contact content editable.
- Provide a Portfolio CPT with project URL, image, description, category, ordering, platform and feature fields.
- Provide a Services CPT with editable title, description, outcomes and steps.
- Provide a Testimonials CPT with client, brand, quote, image, rating and approval fields.
- Support native WordPress Posts, categories, tags, featured images and SEO-friendly URLs.

## 4. Preserve functionality and security

- Keep navigation, internal/external links, responsive behavior, animations and key interactions.
- Implement an authenticated-safe contact submission flow with nonce, honeypot, sanitization and email delivery; support optional Telegram settings without hardcoding secrets.
- Enqueue assets through WordPress APIs and use escaping, capability checks and direct-file guards.

## 5. Preserve SEO and performance

- Use semantic HTML, correct headings, dynamic titles, canonical URLs, Open Graph, Twitter cards and Organization/WebSite/CreativeWork/Service schema where appropriate.
- Keep routes and content crawler-visible without JavaScript.
- Use local official assets and fonts, responsive images, lazy loading for non-critical images and reduced-motion support.

## 6. Documentation and package

- Add installation, configuration, content-management and required-plugin documentation.
- Add a migration/content import tool that seeds the existing CartMakers portfolio and services without overwriting existing posts.
- Produce a theme ZIP and a companion core-plugin ZIP.

## 7. Validation evidence

- Run PHP syntax checks for all PHP files.
- Validate ZIP contents and required theme headers.
- Run the original React build and tests to ensure the preserved source still works.
- Document the remaining staging-only checks: activation, admin editing, uploads, database-backed form delivery, responsive browser checks and WordPress debug logs.
