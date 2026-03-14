# Verification -- Skip School

## Work Mode
A (static HTML site deployed to Vercel)

## Build/Run Command
No build step. Static HTML files deployed directly:
```bash
cd site/files/src
vercel deploy --prod --yes
```
Verify pages: `curl -s -o /dev/null -w "%{http_code}" https://skipschool.ai/[path]`

## Live URL
https://skipschool.ai

## Required Page/Route Checks
- [ ] / (homepage loads)
- [ ] /ai-homeschool-complete-guide (deep article)
- [ ] /texas-esa-guide (deep article)
- [ ] /50-ai-prompts-homeschool (deep article)
- [ ] /articles-index (article listing)
- [ ] /tools-index (tools listing)
- [ ] /guides-index (guides listing)
- [ ] /directory-index (directory listing)
- [ ] /about (about page)
- [ ] /contact (contact page)
- [ ] /review-khan-academy (sample tool review)
- [ ] /review-claude-ai (sample tool review)
- [ ] /topics/ai-tools (topic category page)
- [ ] Any path that does not exist returns branded 404 page

## Required Flow Checks
- [ ] All internal links use clean URLs (no .html extensions)
- [ ] Cross-linking: articles link to related tool reviews and other articles
- [ ] Tool reviews have "Compare With" sections linking to other reviews
- [ ] Subscribe CTA links redirect correctly (Beehiiv)
- [ ] Navigation menu works on all pages
- [ ] Footer present on all pages

## Responsive Checks
- [ ] Homepage at 375px
- [ ] Article page at 375px
- [ ] Tool review page at 375px
- [ ] Navigation/menu at 375px

## SEO Checks (Public Pages Only)
- [ ] Title tags on all public pages
- [ ] Meta descriptions on all public pages
- [ ] OG tags for social sharing on all pages
- [ ] Twitter card tags on all pages
- [ ] sitemap.xml accessible and lists 103+ URLs
- [ ] robots.txt accessible
- [ ] All images have alt text
- [ ] Google Fonts loaded non-render-blocking
- [ ] PageSpeed Performance >= 90

## Protected Scope
- site/files/src/vercel.json (routing, rewrites, cache headers)
- site/files/src/sitemap.xml
- site/files/src/robots.txt
- Brand voice / Ashley's writing style
- skipschool/payload.config.ts (CMS config)
- skipschool/collections/ (Payload schemas)
- Database file (*.db)

## Design Style
Custom brand: Teal #0D7377, Coral #E8724A, Cream #FAF7F2, Dark #1A1A2E, Gold #D4A843. Fraunces (headings) + DM Sans (body). Colored category bars on articles. Clean, warm, education-focused aesthetic.

## Project-Specific Checks
- [ ] No base64 images (all images as separate files in /images/)
- [ ] All images use WebP format with fallbacks
- [ ] Images below fold use lazy loading
- [ ] HTML files under 100KB each
- [ ] No fake testimonials or placeholder content
- [ ] No .html extensions in any internal links
- [ ] Every article has practical takeaway / "do this now" section
- [ ] Content passes anti-slop checklist (no banned words/phrases)
- [ ] ZIP backup created after every deploy
- [ ] Ahrefs health score at 90+ (needs re-crawl to confirm)
