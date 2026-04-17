# Skip School - skipschool.ai
Live: https://skipschool.com

**The AI Playbook for Homeschool Parents**

Static site deployed on Vercel. All HTML files in the root directory.

## Deployment
- Connected to Vercel project: skipschool
- Auto-deploys from `main` branch
- Domain: skipschool.ai

## Structure
- `*.html` - Article and review pages
- `index.html` - Homepage
- `subscribe.html` - Subscribe page
- `api/subscribe.js` - Serverless function for Beehiiv subscription
- `images/` - All site images (WebP + fallback)
- `about/`, `contact/` - Info pages
- `topics/` - Topic category pages
- `vercel.json` - Vercel configuration (rewrites, headers, clean URLs)
- `sitemap.xml` - Sitemap for search engines
- `robots.txt` - Crawler instructions
