# Skip School

## What This Is
Skip School (SkipSchool.ai) is a national homeschool + AI education media brand. Newsletter-first business with a content-rich website. Written in Ashley Larkin's voice (homeschool mom, AI-curious, practical, warm but direct). Targets homeschool parents ages 28-50. Content pillars: AI Tools (40%), Curriculum (25%), ESA/School Choice Money (15%), Community (20%). 70% national / 30% local content split.

## Work Mode
A (live production site is static HTML deployed to Vercel)

Note: A Payload CMS + Next.js 15 app exists in `skipschool/` subdirectory but is NOT the production deployment. The live site at skipschool.ai is 104 static HTML pages deployed via Vercel CLI from `site/files/src/`.

## Design Style
Custom brand design:
- Colors: Teal #0D7377, Coral #E8724A, Cream #FAF7F2, Dark #1A1A2E, Gold #D4A843
- Fonts: Fraunces (headings) + DM Sans (body) via Google Fonts
- Warm, approachable, education-focused aesthetic
- Colored category bars on articles (blue=math/STEM, green=nature/reading, purple=methods, red=special needs, teal=lifestyle)
- Clean URLs (no .html extensions), Vercel rewrites

## Tech Stack
**Live site (production):**
- Static HTML pages (104 pages)
- Tailwind CSS (CDN)
- Google Fonts (Fraunces, DM Sans)
- Vercel (hosting, clean URLs, rewrites)
- Deployed via `vercel deploy --prod` from `site/files/src/`

**CMS app (not in production):**
- Next.js 15 (App Router) in `skipschool/` subdirectory
- Payload CMS 3 (headless CMS) with SQLite
- Collections: Articles, Tools, Authors, Tags, Media, Prompts, Sponsors, Users
- TypeScript, Tailwind CSS

**Content/operations stack:**
- Beehiiv (newsletter platform)
- Google Drive (content drafts)
- Meta Ads (subscriber acquisition)
- Canva (design templates)

## How To Run
**Live site (static HTML):**
No local dev server needed. Files are in `site/files/src/`. Deploy with:
```bash
cd site/files/src
vercel deploy --prod --yes
```

**CMS app (if needed):**
```bash
cd skipschool
npm install
npm run dev
```
Runs on http://localhost:3000. Admin panel at /admin.

## Project Structure
```
skip-school/
  CLAUDE.md, progress.md, VERIFICATION.md
  skip-school-project-instructions.md    # Content engine instructions (Ashley's voice, content pillars)
  skip-school-business-bible.md          # Business strategy source of truth
  site/files/src/                        # LIVE SITE - 104 static HTML pages deployed to Vercel
  skipschool/                            # Payload CMS + Next.js app (NOT production)
  deploy/                                # Build scripts (Python) for generating pages
  articles-pages/                        # Article source files
  backups/                               # Site backups, handoff docs, brand assets
```

## Project-Specific Rules
1. Ashley's voice is non-negotiable. Run the anti-slop checklist before any content. See skip-school-project-instructions.md for banned words/phrases.
2. NEVER use base64 images. Always separate files in /images/.
3. NEVER deploy without verifying every internal link returns 200.
4. ALWAYS create a downloadable ZIP backup after every deploy.
5. Every img needs alt text, lazy loading below fold, WebP format.
6. No fake testimonials, no placeholder content, no "coming soon."
7. HTML under 100KB, Google Fonts non-render-blocking, OG + Twitter meta tags.
8. Clean URLs everywhere - no .html extensions in internal links.
9. The SQLite database file in skipschool/ must never be committed.
10. Never be political about education. Pro-homeschool, NOT anti-public-school.

## Protected Scope
- site/files/src/vercel.json (routing, rewrites, cache headers)
- site/files/src/sitemap.xml (103+ URLs)
- site/files/src/robots.txt
- skipschool/payload.config.ts (CMS configuration, if CMS app is used)
- skipschool/collections/ (Payload collection schemas)
- Database file (*.db) - never commit
- Brand voice / Ashley's writing style (skip-school-project-instructions.md)

## Known Issues
- ~40 articles (numbered 26-66) have thin content (200-400 words), need expansion to 800-1500 words
- Only 25 tool reviews exist; target is 50
- 6 topic category pages are link-only, need introductory content
- Homepage testimonials section was removed (had fake names); needs real ones
- Subscriber count on homepage uses generic text; needs real number
- Ahrefs health score was 34 due to 41 broken links; fixed but needs re-crawl to confirm 90+
- Payload CMS app in skipschool/ is not the production deployment
