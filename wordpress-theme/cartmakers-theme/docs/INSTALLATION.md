# CartMakers WordPress Theme — Installation

## What is included

- `cartmakers-theme.zip`: the visual theme and editable templates.
- `cartmakers-core.zip`: the companion plugin that owns portfolio, services, testimonials, settings, importer and contact handling.

This is the compatibility build. It includes a WordPress theme screenshot, guarded settings fallbacks, PHP 7.4-compatible syntax, and a non-destructive activation path.

The original React/Vite website remains in the repository as the source reference and is not deleted by this migration.

## Installation

1. If the earlier package caused a Critical Error, temporarily activate a default WordPress theme from the recovery email or hosting file manager first.
2. In WordPress, open **Plugins → Add New → Upload Plugin** and upload the new `cartmakers-core.zip`.
3. Activate **CartMakers Core** first.
4. Go to **Appearance → Themes → Add New → Upload Theme** and upload the new `cartmakers-theme.zip`.
5. Activate **CartMakers Commerce Systems**.
5. Go to **Settings → Permalinks** and press **Save Changes** once so the custom post type URLs are flushed.
6. Go to **Tools → CartMakers Importer** and import the known CartMakers project/service entries. The importer does not overwrite existing entries.
7. Add the project images through the WordPress Media Library and set them as Featured Images.
8. Create WordPress pages with slugs `about`, `portfolio`, `insights`, and `policies`; the theme provides dedicated templates for them. Set the homepage under **Settings → Reading**.

## Global settings

Open **Settings → CartMakers Settings** to edit the email, international WhatsApp digits, social URLs, hero title/description and optional Telegram credentials. Telegram values are stored as WordPress options and are never printed in public HTML. The form always sends through `wp_mail`; Telegram is an additional notification when configured.

Use **Appearance → Customize → CartMakers Brand** for the primary and accent colors. Upload the logo through the native Site Logo control when preferred.

## Portfolio

Open **Portfolio Projects → Add New**. Use the title, editor, excerpt and Featured Image for the public project. The Project Details box controls the external URL, category label, tag, platform, brief, insight and feature list. Use **Page Attributes → Order** to control the ordering on the homepage and archive.

## Services

Open **Services → Add New**. The content editor contains the main service description. The Service Details box accepts a label, outcomes (one per line) and steps in the format `Step title — Step description`.

## Testimonials

Open **Testimonials → Add New**. Add the quote in the editor, then use the details box for client name, brand, rating and approval. Only approved, real testimonials should be published by the site owner.

## Contact form

The form uses WordPress `admin-post.php`, a nonce, sanitization and a honeypot field. It emails the WordPress administration email. Configure SMTP through the hosting or a trusted SMTP plugin for reliable delivery. No API secret is included in the theme.

## SEO

The theme outputs semantic HTML, title-tag support, descriptions, featured-image Open Graph data, Organization schema on the homepage and crawler-visible content. It is compatible with common SEO plugins; if one is active, its canonical/title output should be treated as the source of truth and duplicate plugin settings should be avoided.

## Staging-only verification

The Sandbox does not include a WordPress runtime or database. Before production use, activate both packages on staging and verify activation, menus, Customizer fields, importer, Media Library images, portfolio/service editing, contact delivery, responsive layouts, PHP debug logs and all intended redirects.
