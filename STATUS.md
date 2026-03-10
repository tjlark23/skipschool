# Skip School Site Status

## Last Updated: 2026-03-10
## Live URL: https://skipschool.ai
## Stack: Static HTML/CSS/JS on Vercel (auto-deploy from Git)
## Repo: github.com/tjlark23/skipschool (push to main = deploy)

## Current State
- 128 HTML pages deployed (127 in sitemap + 404)
- 25 tool review pages (all expanded to 843-1344 words)
- 40+ article pages (all expanded to 400-1508 words)
- 15 articles (07-25) expanded to 1015-1508 words each
- 7 hero articles expanded to 660-1987 words
- 50 AI Prompts page with all 50 copy-paste prompts (2278 words)
- 7 comparison pages (Khan vs IXL, ChatGPT vs Claude, etc.)
- 12 directory/brand pages
- 11 state ESA guide pages + Texas ESA guide
- Ashley Larkin author page
- Subscribe page restored to original design (phone mockup, stars, social proof)
- Homepage sponsor bar fixed to navy per approved design
- Beehiiv API integration working via /api/subscribe
- All 127 sitemap URLs returning 200
- Zero broken internal links
- sitemap.xml, robots.txt, llms.txt all in place

## Known Issues
- Homepage sponsor bar is self-promo CTA, not real sponsor
- No contact page (footer links to mailto:hello@skipschool.ai)

## Completed This Session
- [x] Restored subscribe page from backup (phone mockup, 5 stars, social proof)
- [x] Fixed homepage sponsor bar from yellow to navy
- [x] Regenerated 31 missing pages into Git repo
- [x] Fixed footer links: /about -> /about-ashley-larkin, /contact -> mailto
- [x] Fixed homepage topic tile links to real pages
- [x] Rebuilt sitemap.xml with all 127 URLs
- [x] Added llms.txt with structured page listing
- [x] Fixed 4 broken internal links in generated pages
- [x] Expanded articles 07-25 from ~300 to 1015-1508 words each (15 articles)
- [x] Expanded all 25 tool reviews from ~170-519 to 843-1344 words each
- [x] Expanded 50-ai-prompts-homeschool from 9 prompts to all 50 (2278 words)

## Completed This Session (Curriculum System)
- [x] Built curriculum packet generation system (v4 design)
- [x] Created SKILL.md with TEKS alignment, tier structure, v4 design rules
- [x] Created K-5 scope and sequence (36 weeks per grade, Math + ELA)
- [x] Created page templates reference (every worksheet page type)
- [x] Created focus area banks for Tier 2 supplements
- [x] Created v4 HTML/CSS template (two-bar header, 5-color system, Try This boxes, Extension Page)
- [x] Created generate_packet.py (JSON content to styled HTML renderer)
- [x] Generated sample Grade 3 Week 1 packet as proof of pipeline
- [x] All files committed to Git

## Next Steps
- [ ] Ashley reviews Grade 3 Week 1 sample against her originals
- [ ] Generate Grade 1 Week 1 sample for Charlie
- [ ] Build intake form (Typeform)
- [ ] Wire up payment (Stripe/Gumroad)
- [ ] Wire up delivery (Beehiiv or email)
- [ ] Beta launch with founding member pricing
- [ ] Add real testimonials when available
