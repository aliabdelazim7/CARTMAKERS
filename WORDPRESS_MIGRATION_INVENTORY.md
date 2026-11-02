# CartMakers — Migration Inventory

## Existing source

The current production source is a React/Vite application. `src/main.jsx` contains route selection, site packages, contact/social settings, portfolio data, homepage sections, diagnostic state, package selection, FAQ state, Meta Pixel events and the contact request flow. `src/seoContent.jsx` contains the indexable service and insight data. `src/styles.css` contains the RTL design system, local font declarations, responsive breakpoints, motion, cards, package controls, portfolio and form styles. `scripts/prerender.mjs` produces crawler-visible initial HTML for the public routes.

## Public content mapped into WordPress

The homepage is represented by `front-page.php`, with editable hero/contact settings and dynamic services/projects. Project detail pages are represented by `single-cm_project.php`; project content is stored in the `cm_project` Custom Post Type. Service detail pages are represented by `single-cm_service.php`; service content is stored in `cm_service`. Insights are represented by native WordPress Posts and `page-insights.php`. About, Portfolio and Policies have dedicated page templates.

## Assets

The official logo variants, favicon, social cover, local fonts and existing portfolio WebP images are copied into `wordpress-theme/cartmakers-theme/assets/`. The original CSS is retained as `assets/css/cartmakers-original.css` and its font paths are made relative to the Theme ZIP so it does not depend on the original Vite public root.

## Interactions mapped

The migration keeps the RTL navigation, CTA anchors, project links, service links, package presentation, portfolio cards, WhatsApp CTA, email contact, responsive layout and reveal script. The WordPress form uses a nonce, honeypot, sanitization, `wp_mail`, and optional Telegram notification. Advanced React-only diagnostic state and package estimator behavior are not silently faked in PHP; the current theme provides the editable Brief flow and package presentation, while a staging pass should decide whether the diagnostic should be implemented as a small WordPress script or a form plugin integration.

## Verification boundary

The React source build, SEO check and browser smoke test pass after the migration files are added. PHP syntax and WordPress admin/database behavior cannot be executed in this Sandbox because no PHP CLI or WordPress runtime is installed. Staging activation and form delivery remain explicitly documented as required before replacing the live deployment.
