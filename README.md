# IMPORTANT: CSS-FIXED EDITION

Every HTML page now includes its own CSS and JavaScript. Even if GitHub Pages fails to resolve `assets/style.css`, the design still renders. The `assets/` folder should still be uploaded for logo and favicon.

**Upload the CONTENTS of this ZIP into the repository root.** GitHub should show `index.html`, `articles.html`, `articles/`, and `assets/` at the top level. Do not upload only the ZIP file or the outer folder.

If the live website still looks unstyled, make sure you are viewing the GitHub Pages published URL, **not the GitHub source code preview**, and hard-refresh with Ctrl+F5.

---

# Cloudwise Journal — GitHub Pages website

A complete, static English-language cloud management **blog** (not a services website).

## What is included

- Responsive, original editorial homepage and logo/favicon.
- Eight original, long-form cloud-management articles.
- Searchable article library with interactive category filters.
- About, Contact, Privacy, Terms, Editorial Disclaimer and 404 pages.
- SEO titles, page descriptions, Open Graph tags, robots.txt and a nojekyll file.
- Zero backend, database, npm, deployment keys, paid APIs or build tools.

## Publish to GitHub Pages

1. Create a new public repository (for example, `cloudwise-journal`).
2. Open this ZIP and upload **the contents of the `cloudwise-journal` folder** to the repository root. `index.html` must be in the root, not nested within another folder.
3. In GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, `main` and `/ (root)`, then save.
5. Visit `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/` after GitHub finishes publishing. All internal links are relative, so both project pages and a custom domain can work.

## Before making it public

- The **Contact** page intentionally has no fabricated email address. Replace the placeholder with your real public contact address or a GitHub Issues link.
- Replace the publication name and branding if desired. Brand text is in HTML; logo is `assets/logo.svg`.
- Review all content and legal pages to ensure they reflect your real publication, jurisdiction, and tools.
- The site uses Google Fonts; if you need a zero-third-party-request site, remove the CSS `@import` rule. System fallback fonts are already configured.
- The 8 article dates are set to **November 20, 2026**. Change them if you publish on another date.
- If you add analytics, AdSense, advertising cookies, or forms, update your Privacy Policy and relevant compliance setup first.
- The template does **not** claim a newsletter exists or offer fake services.

## Optional SEO configuration

When your final URL is known, update `robots.txt` to include `Sitemap: https://YOUR-LIVE-DOMAIN/sitemap.xml`. You may also add canonical and `og:url` tags to each page. Generate or regenerate a production sitemap with the `generate_sitemap.py` script (see below).

`python generate_sitemap.py https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`

This updates `sitemap.xml` and `robots.txt`. Commit the changes and redeploy.

## Editing articles

Each guide is a standalone HTML file in `articles/`. To add an article, duplicate one article page, edit its title, meta description, body, category, and related-article links; then add a corresponding card to `articles.html` and optionally `index.html`. Regenerate sitemap after additions.

## Notes

The built-in article search is client-side and filters the eight existing article cards; it is not a site-wide crawl or full-text search.

All visual diagrams and layout are bundled locally as SVG/CSS; there is no externally fetched stock photography.
