# SKIP SCHOOL SITE HANDOFF — March 9, 2026

## CURRENT STATE

**Live at:** skipschool.ai
**Deployed via:** Vercel CLI (`vercel deploy --prod --token [in memory]`)
**Total pages:** 104 HTML pages, all returning 200
**PageSpeed scores:** Performance 91 / Accessibility 96 / Best Practices 100 / SEO 100
**Ahrefs:** Was 34 health score due to 41 broken links. Should now be 90+ (zero 404s). Re-crawl needed.

## WHAT'S ON THE SITE

### Pages with DEEP content (800-2000+ words, real prompts, specific tools):
- Homepage (index.html)
- ai-homeschool-complete-guide.html
- texas-esa-guide.html
- 50-ai-prompts-homeschool.html
- homeschool-kids-ai-five-years-ahead.html
- 05-ai-curriculum-builder.html
- 06-chatgpt-vs-claude-homeschool.html
- 09-first-week-ai-homeschool.html
- 10-khan-academy-guide.html
- about/index.html
- contact/index.html

### Pages with MEDIUM content (400-800 words, real but shorter):
- 07-socialization-myth.html
- 08-morning-routine-ai.html
- 11-homeschool-on-budget.html
- 12-ai-reading-list-by-age.html
- 13-teach-kids-use-ai.html
- 14-homeschool-field-trip-ideas.html
- 15-charlotte-mason-ai.html
- 16-classical-education-ai.html
- 17-homeschool-writing-ai.html
- 18-ai-science-experiments.html
- 19-high-school-ai.html
- 20-special-needs-ai.html
- 21-ai-math-help.html
- 22-screen-time-balance.html
- 23-state-homeschool-laws.html
- 24-homeschool-co-op-guide.html
- 25-ai-for-reluctant-learner.html

### Pages with THIN content (200-400 words, need expansion):
- All remaining article pages numbered 26-66
- 6 topic category pages (topics/ai-tools, topics/curriculum, etc.)

### 25 Tool Review Pages (all have real, deep content):
- review-math-academy, review-khan-academy, review-claude-ai, review-ixl
- review-outschool, review-duolingo, review-chatgpt, review-beast-academy
- review-teaching-textbooks, review-prodigy-math, review-time4learning
- review-alpha-school, review-singapore-math, review-saxon-math
- review-math-u-see, review-easy-peasy, review-abcmouse, review-perplexity-ai
- review-google-gemini, review-bookshark, review-the-good-and-beautiful
- review-splashlearn, review-curiosity-stream, review-libby-app, review-notion

### Index pages:
- articles-index.html, guides-index.html, tools-index.html, directory-index.html

### Infrastructure:
- 404.html (branded "This page skipped school too")
- sitemap.xml (103 URLs)
- robots.txt
- vercel.json (cleanUrls, rewrites for /tools /articles /guides /directory, cache headers, subscribe redirect)
- /images/ directory with WebP + fallback images

## WHAT NEEDS TO BE DONE NEXT

### Priority 1: Expand thin article content
~40 articles (numbered 26-66) have real but thin content (200-400 words). Each should be expanded to 800-1500 words with:
- Ashley's voice (first person, specific, honest, short paragraphs)
- At least one copy-paste prompt per article
- Real tool names with prices
- Practical "do this now" takeaways
- Internal links to relevant review pages and other articles

The articles that need the most expansion (currently just 1-3 paragraphs):
26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66

### Priority 2: More tool reviews (get to 50)
Current: 25 reviews. Target: 50. Candidates:
- CTC Math, Thinkwell, Art of Problem Solving (older students)
- Sonlight, BJU Press, Abeka (faith-based curricula)
- Calvert, K12, Connections Academy (accredited online schools)
- Scratch, Code.org, Codecademy (coding)
- Canva for Education, Google Arts & Culture
- Starfall, PBS Kids (free early learning)
- Homeschool Panda, Schoolhouse Teachers
- Brave Writer, Institute for Excellence in Writing (writing-specific)

### Priority 3: Topic category pages need real content
The 6 pages at /topics/[category]/ currently just list links to articles. They should have introductory content explaining the category, curated article recommendations, and relevant tool reviews.

### Priority 4: Homepage polish
- Testimonials section was removed (had fake names). Add real ones when available from actual subscribers.
- Subscriber count was changed to generic text. Update with real number once you have it.

## DEPLOYMENT PROCESS

```
cd /home/claude/skipschool-deploy
# Make changes to files
vercel deploy --prod --token [stored in memory] --yes
# Verify: curl -s -o /dev/null -w "%{http_code}" https://skipschool.ai/[path]
# ALWAYS create backup zip and present_files after deploy
```

## CRITICAL RULES (stored in Claude's memory)
1. NEVER use base64 images. Always separate files in /images/
2. NEVER deploy without verifying every internal link returns 200
3. ALWAYS create a downloadable ZIP backup after every deploy
4. ALWAYS present_files the backup so TJ can download it
5. Every img needs alt text, lazy loading below fold, WebP format
6. No fake testimonials, no placeholder content, no "coming soon"
7. HTML under 100KB, Google Fonts non-render-blocking, OG + Twitter meta tags
8. Run PageSpeed audit before any major deployment
