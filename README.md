# Skip School (skipschool.ai)

The AI Playbook for Homeschool Parents. Built with Payload CMS + Next.js.

## Quick Deploy to Vercel

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial Skip School site"
git remote add origin https://github.com/YOUR_USERNAME/skipschool.git
git push -u origin main
```

### Step 2: Deploy on Vercel
1. Go to vercel.com/new
2. Import your GitHub repo
3. Add environment variables:
   - `PAYLOAD_SECRET` = any random 32+ character string (use a password generator)
   - `DATABASE_URI` = `file:./skipschool.db` (for SQLite, works immediately)
   - `NEXT_PUBLIC_SITE_URL` = `https://skipschool.ai`
4. Click Deploy

### Step 3: Point Your Domain
1. In Vercel dashboard > Settings > Domains
2. Add `skipschool.ai`
3. Update DNS at your domain registrar:
   - A record: `76.76.21.21`
   - CNAME: `cname.vercel-dns.com`

### Step 4: Access the CMS
1. Go to `skipschool.ai/admin`
2. Create your first admin user
3. Start adding articles, tools, and prompts

## Database Options

**SQLite (default, simplest):** Works out of the box. Data stored in a file. Good for getting started. Note: Vercel's serverless functions use read-only filesystem, so for production you'll want to switch to Postgres.

**Vercel Postgres (recommended for production):**
1. In Vercel dashboard, go to Storage > Create > Postgres
2. Copy the connection string
3. Install adapter: `npm install @payloadcms/db-vercel-postgres`
4. Update `payload.config.ts` to use `vercelPostgresAdapter` instead of `sqliteAdapter`
5. Update `DATABASE_URI` env var with Postgres connection string

**Neon Postgres (free alternative):**
1. Create account at neon.tech
2. Create a database
3. Same steps as Vercel Postgres but use Neon's connection string

## Project Structure

```
skipschool/
├── app/
│   ├── (frontend)/          # Public website pages
│   │   ├── page.tsx          # Homepage
│   │   ├── layout.tsx        # Site layout, nav, footer, SEO
│   │   ├── articles/         # Article listing + detail pages
│   │   └── directory/        # Directory listing + detail pages
│   └── (payload)/            # CMS admin panel + API
├── collections/              # Payload CMS content types
│   ├── Articles.ts           # Blog posts, reviews, guides
│   ├── Tools.ts              # Directory listings
│   ├── Prompts.ts            # AI prompt library
│   ├── Authors.ts            # Content authors
│   ├── Tags.ts               # Article tags
│   ├── Sponsors.ts           # Ad placements
│   ├── Media.ts              # Image uploads
│   └── Users.ts              # Admin users
├── components/               # Shared React components
├── lib/
│   ├── payload.ts            # CMS data access functions
│   └── seo.ts                # JSON-LD structured data generators
├── styles/globals.css        # Tailwind + brand fonts
├── payload.config.ts         # Payload CMS configuration
├── tailwind.config.ts        # Brand colors and typography
└── next.config.mjs           # Next.js + Payload integration
```

## Content Management

### Adding Articles
1. Go to /admin > Articles > Create New
2. Fill in title, slug, category, content
3. Add SEO fields and FAQ items
4. Set status to "Published" and save

### Adding Directory Tools
1. Go to /admin > Tools > Create New
2. Fill in name, slug, category, pricing, description
3. Add Ashley's Take, pros/cons, rating
4. Check "Featured" to show on homepage

### Adding Prompts
1. Go to /admin > Prompts > Create New
2. Add title, the actual prompt text, subject, age range
3. Check "Featured" to show on homepage widget

## SEO

Every page includes:
- JSON-LD structured data (Organization, Article, Product, FAQ, Breadcrumb)
- Open Graph tags
- Geo meta tags (Williamson County, TX)
- Semantic HTML with proper heading hierarchy
- FAQ sections matching FAQPage schema

## Tech Stack
- Next.js 15 (React framework)
- Payload CMS 3 (headless CMS, embedded)
- SQLite / Postgres (database)
- Tailwind CSS 3 (styling)
- Vercel (hosting)
