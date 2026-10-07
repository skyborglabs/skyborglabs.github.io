# SKYBORG ENTERPRISE LLC website

Official company and game-development website for https://www.skyborglabs.com.
Contact: admin@skyborglabs.com.

The site presents Slingshot Wrestling as a pre-production project, with original concept art, a 15-second animated concept preview, company information, support, and a website/email Privacy Policy. No finished game, release date, playable demo, or automated newsletter service is claimed.

## Editing and building

- `build.py`: shared layouts, page content, routes, and metadata.
- `site-config.json`: confirmed domain and public business identity.
- `styles.css` and `script.js`: responsive layout, mobile navigation, image dialogs.
- Image/video/caption files at repository root: source media.
- `dist/`: generated static website; do not edit generated files.
- `validate.py`: local links, metadata, headings, image alternatives, and sitemap checks.

```sh
python3 build.py
python3 validate.py
python3 -m http.server 4173 --directory dist
```

No Python packages, JavaScript framework, database, or backend are needed. The public website consists of ordinary HTML, CSS, JavaScript, and local media. Python runs only during development/build.

## GitHub Pages

Repository: https://github.com/skyborglabs/skyborglabs.github.io
Select **Settings → Pages → Source → GitHub Actions**. The included `.github/workflows/pages.yml` builds and deploys `dist/` on pushes to `main`, or when run manually.
Set the Pages custom domain to `www.skyborglabs.com`, then configure DNS at Porkbun. See LAUNCH-NOTES.md. CNAME alone does not complete DNS or Google ownership verification.

## Contact and privacy

The public website provides the studio's confirmed business email and a dedicated privacy page. Newsletter signup has been removed. Connect a real mailing provider with consent, unsubscribe, and updated disclosures before adding a subscription form; no simulated form or manual subscription button is published.

No analytics, cookies, third-party embeds, ad SDKs, checkout, or tracking scripts are added by the website code. Update the policy if services are added. No blanket open-source license has been applied to the company logo or site assets.
