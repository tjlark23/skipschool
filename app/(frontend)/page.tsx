import Link from 'next/link'
import { getPublishedArticles, getFeaturedArticle, getFeaturedTools, getFeaturedPrompt, getActiveSponsor } from '@/lib/payload'
import { NewsletterSignup } from '@/components/NewsletterSignup'

// Category display config
const categoryConfig: Record<string, { color: string; bg: string; emoji: string }> = {
  'ai-for-parents': { color: 'text-teal', bg: 'bg-teal-bg', emoji: '🤖' },
  'ai-for-kids': { color: 'text-purple-600', bg: 'bg-purple-50', emoji: '🧒' },
  'review': { color: 'text-coral', bg: 'bg-coral-bg', emoji: '🔍' },
  'esa-guide': { color: 'text-amber-600', bg: 'bg-amber-50', emoji: '💰' },
  'comparison': { color: 'text-emerald-600', bg: 'bg-emerald-50', emoji: '⚖️' },
  'our-week': { color: 'text-pink-600', bg: 'bg-pink-50', emoji: '🏠' },
  'the-download': { color: 'text-teal', bg: 'bg-teal-bg', emoji: '⚡' },
  'tutorial': { color: 'text-blue-600', bg: 'bg-blue-50', emoji: '💻' },
  'community': { color: 'text-violet-600', bg: 'bg-violet-50', emoji: '👥' },
  'data': { color: 'text-sky-600', bg: 'bg-sky-50', emoji: '📊' },
}

const categoryLabels: Record<string, string> = {
  'ai-for-parents': 'AI for Parents',
  'ai-for-kids': 'AI for Kids',
  'review': 'The Review',
  'esa-guide': 'ESA Guide',
  'comparison': 'Comparison',
  'our-week': 'Our Week',
  'the-download': 'The Download',
  'tutorial': 'Tutorial',
  'community': 'Community',
  'data': 'Data',
}

export default async function HomePage() {
  // Fetch data from Payload CMS
  // In development before DB is connected, these will return empty arrays
  let articles: any[] = []
  let featuredArticle: any = null
  let featuredTools: any[] = []
  let featuredPrompt: any = null
  let sponsor: any = null

  try {
    const [articlesRes, featured, toolsRes, prompt, sponsorRes] = await Promise.allSettled([
      getPublishedArticles(7),
      getFeaturedArticle(),
      getFeaturedTools(4),
      getFeaturedPrompt(),
      getActiveSponsor('presenting'),
    ])

    articles = articlesRes.status === 'fulfilled' ? articlesRes.value.docs : []
    featuredArticle = featured.status === 'fulfilled' ? featured.value : null
    featuredTools = toolsRes.status === 'fulfilled' ? toolsRes.value.docs : []
    featuredPrompt = prompt.status === 'fulfilled' ? prompt.value : null
    sponsor = sponsorRes.status === 'fulfilled' ? sponsorRes.value : null
  } catch {
    // CMS not connected yet - that's fine, we'll show placeholder content
  }

  // Use placeholder data if CMS is empty (pre-launch)
  const showPlaceholder = articles.length === 0

  return (
    <>
      {/* Sponsor Bar */}
      <div className="bg-charcoal py-3 px-7 flex items-center justify-center gap-4">
        <span className="uppercase tracking-widest text-white/30 font-bold text-[9px]">Presented by</span>
        <div className="w-7 h-7 rounded-full bg-white/10 flex items-center justify-center text-xs font-bold text-teal-light">
          K
        </div>
        <span className="text-[13px] text-white/80">
          <strong className="text-white font-semibold">Khanmigo</strong> &mdash; AI tutoring for every subject. Try free for 30 days.
        </span>
        <a href="#" className="text-coral text-xs font-semibold hover:underline ml-1">Learn More &rarr;</a>
      </div>

      <div className="px-7 py-5">
        {/* ═══ HERO THREE-COLUMN GRID ═══ */}
        <div className="grid grid-cols-1 lg:grid-cols-[1.2fr_1.9fr_1.2fr] gap-5 mb-7">

          {/* LEFT COLUMN: Start Here + Article Feed + ESA Alert */}
          <div>
            {/* Start Here Widget */}
            <Link href="/start-here" className="block bg-teal rounded-xl p-4 mb-3.5 group hover:shadow-lg transition-all hover:-translate-y-0.5">
              <div className="text-2xl mb-1.5">🚀</div>
              <h3 className="font-serif font-bold text-base text-white mb-1">New to AI Homeschooling?</h3>
              <p className="text-xs text-white/70 leading-snug mb-2.5">
                Step-by-step guide: which tools to use, how to set them up, and how to build your first AI-powered week.
              </p>
              <span className="inline-block text-xs font-bold text-white border border-white/40 rounded-md px-3.5 py-1.5 group-hover:bg-white/15 transition-colors">
                Start Here &rarr;
              </span>
            </Link>

            {/* Article Feed Header */}
            <div className="flex items-center justify-between mb-2">
              <h2 className="font-serif font-bold text-[15px]">Latest</h2>
              <Link href="/articles" className="text-[11px] font-semibold text-teal hover:underline">All Articles &rarr;</Link>
            </div>

            {/* Article Feed Items */}
            {(showPlaceholder ? placeholderArticles : articles).map((article: any, i: number) => {
              const cat = categoryConfig[article.category] || categoryConfig['ai-for-parents']
              return (
                <Link
                  key={article.slug || i}
                  href={`/articles/${article.slug}`}
                  className="flex items-center gap-2.5 py-1.5 border-b border-gray-100 last:border-b-0 hover:opacity-80 transition-opacity"
                >
                  <div className={`w-[52px] h-[52px] rounded-lg ${cat.bg} flex items-center justify-center text-[22px] flex-shrink-0`}>
                    {cat.emoji}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className={`flex items-center gap-1 text-[10px] font-bold ${cat.color} mb-0.5`}>
                      <span className={`w-[5px] h-[5px] rounded-full ${cat.color.replace('text-', 'bg-')}`} />
                      {categoryLabels[article.category] || article.category}
                    </div>
                    <div className="text-[13px] font-semibold leading-tight line-clamp-2">
                      {article.title}
                    </div>
                  </div>
                </Link>
              )
            })}

            {/* ESA Alert */}
            <Link href="/esa-guides/texas" className="block bg-gradient-to-br from-amber-100 to-amber-200 rounded-xl p-3.5 mt-2.5 border border-amber-300 hover:shadow-lg transition-all hover:-translate-y-0.5">
              <div className="text-[10px] font-bold uppercase tracking-wider text-coral mb-1">⚠ ESA Deadline</div>
              <div className="text-[17px] font-serif font-bold mb-0.5">March 17, 2026</div>
              <div className="text-xs font-semibold leading-tight mb-0.5">Texas ESA applications close in 19 days</div>
              <div className="text-[11px] text-gray-500">$10,474 per child &middot; Read our guide &rarr;</div>
            </Link>
          </div>

          {/* CENTER COLUMN: Hero Article + Signup + Tool Cards */}
          <div>
            {/* Hero Article */}
            <div className="w-full rounded-xl overflow-hidden mb-2.5 h-[200px] bg-gradient-to-br from-teal to-teal-dark flex items-center justify-center text-6xl">
              🤖
            </div>
            <div className="flex items-center gap-1 text-[10px] font-bold text-teal mb-0.5">
              <span className="w-[5px] h-[5px] rounded-full bg-teal" />
              AI for Parents
            </div>
            <h1 className="font-serif font-bold text-[22px] leading-tight mb-1.5">
              {featuredArticle?.title || 'How I Plan Our Entire Homeschool Week in 15 Minutes with Claude'}
            </h1>
            <p className="text-[13px] text-gray-500 leading-relaxed">
              {featuredArticle?.excerpt || 'Every Sunday night, after the kids are in bed, I open Claude and build our whole week. Here\'s the exact workflow and the three tricks that took me weeks to figure out.'}
            </p>
            <div className="text-[11px] text-gray-400 mt-1.5">
              <strong>Ashley Larkin</strong> &middot; Feb 26, 2026 &middot; 6 min read
            </div>

            {/* Newsletter Signup */}
            <NewsletterSignup variant="inline" className="mt-3.5" />

            {/* Tool Cards */}
            <section className="mt-3.5" aria-label="Featured AI tools for homeschool parents">
              <div className="flex items-center justify-between mb-2.5">
                <h2 className="font-serif font-bold text-[15px]">What We&apos;re Using Right Now</h2>
                <Link href="/directory" className="text-[11px] font-semibold text-teal hover:underline">Full Directory &rarr;</Link>
              </div>
              <div className="grid grid-cols-2 gap-2.5">
                {(showPlaceholder ? placeholderTools : featuredTools).map((tool: any, i: number) => (
                  <Link
                    key={tool.slug || i}
                    href={`/directory/${tool.slug}`}
                    className="bg-white border border-gray-200 rounded-xl overflow-hidden hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5 group relative"
                  >
                    <div className={`h-[90px] flex items-center justify-center text-4xl ${tool.bgColor || 'bg-teal-bg'} relative`}>
                      {tool.emoji || '🎓'}
                      {tool.badgeText && (
                        <span className={`absolute top-2 right-2 px-2 py-0.5 rounded text-[9px] font-bold text-white ${tool.badgeColor || 'bg-teal'}`}>
                          {tool.badgeText}
                        </span>
                      )}
                    </div>
                    <div className="p-3">
                      <div className="text-sm font-bold mb-0.5">{tool.name}</div>
                      <div className="text-[11px] text-gray-500 leading-snug mb-1.5 line-clamp-2">
                        {tool.description}
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-[13px] font-bold text-teal">{tool.pricing?.price || tool.price}</span>
                        <span className="text-[11px] text-gray-400">{tool.ratingDisplay || ''}</span>
                      </div>
                      <span className="inline-block text-[10px] font-bold text-teal border border-teal rounded px-2 py-0.5 mt-1.5 group-hover:bg-teal group-hover:text-white transition-colors">
                        {tool.ctaText || 'Read Our Review →'}
                      </span>
                    </div>
                  </Link>
                ))}
              </div>
            </section>
          </div>

          {/* RIGHT COLUMN: Prompt of the Week + Quiz */}
          <div>
            {/* Prompt Widget */}
            <div className="bg-white border border-gray-200 rounded-xl p-3.5 mb-3">
              <span className="inline-block bg-coral text-white text-[9px] font-bold px-2 py-0.5 rounded uppercase tracking-wider mb-1.5">
                Prompt of the Week
              </span>
              <h3 className="font-serif font-bold text-[15px] leading-tight mb-1">
                {featuredPrompt?.title || 'Turn Any Obsession Into a Full Week of Learning'}
              </h3>
              <p className="text-xs text-gray-500 leading-snug mb-2.5">
                {featuredPrompt?.description || 'My 7-year-old spent three days talking about volcanoes. Instead of fighting it, I turned it into our whole week.'}
              </p>
              <div className="bg-charcoal rounded-lg p-3.5 relative mb-2">
                <pre className="font-mono text-[10.5px] text-gray-300 leading-relaxed whitespace-pre-wrap break-words">
                  {featuredPrompt?.prompt || `You are a creative homeschool curriculum
designer. My child is [AGE] years old
and is obsessed with [INTEREST].

Create a one-week unit study connecting
their interest to:
- Math (real-world problems)
- Science (experiments or concepts)
- Reading (book recs at their level)
- Writing (one fun project)
- History or Geography connection

Make it feel like play, not school.
Include one field trip idea and one
hands-on project.`}
                </pre>
              </div>
              <Link href="/prompts" className="text-[11px] text-teal font-semibold hover:underline">
                Browse 100+ prompts in the library &rarr;
              </Link>
            </div>

            {/* Quiz Card */}
            <div className="bg-gradient-to-br from-purple-100 to-purple-200 border border-purple-300 rounded-xl p-4 hover:shadow-lg transition-all hover:-translate-y-0.5 cursor-pointer">
              <div className="text-2xl mb-1.5">🧠</div>
              <h3 className="font-serif font-bold text-sm text-charcoal mb-0.5">What&apos;s Your AI Readiness Score?</h3>
              <p className="text-[11px] text-gray-500 leading-snug mb-2">
                2-minute quiz. Find out which AI tools match your family&apos;s needs and get a personalized setup plan.
              </p>
              <span className="inline-block text-[11px] font-bold text-purple-600 border border-purple-600 rounded-md px-3 py-1 hover:bg-purple-600 hover:text-white transition-colors">
                Take the Quiz &rarr;
              </span>
            </div>
          </div>
        </div>

        {/* ═══ BELOW FOLD: The Feed ═══ */}
        <section className="mb-7" aria-label="Curated education news">
          <div className="flex items-center justify-between mb-3.5 pb-2 border-b-2 border-charcoal">
            <h2 className="font-serif font-bold text-lg">The Feed</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
            <FeedCard source="Washington Post" title="Grade Inflation Hits 30-Year High While Test Scores Keep Falling" comment="File this under 'reasons we homeschool'" />
            <FeedCard source="Anthropic Blog" title="Teach For All Partners with Anthropic to Bring AI to 100K+ Teachers" comment="If schools are adopting it, imagine what you can do at home" />
            <FeedCard source="EdWeek Research" title="44% of Homeschool Families Now Use AI Tools Regularly, Up From 12% in 2023" comment="We're ahead of the curve on this one" />
          </div>
        </section>

        {/* More Articles */}
        <section className="mb-7" aria-label="More articles from Skip School">
          <div className="flex items-center justify-between mb-3.5 pb-2 border-b-2 border-charcoal">
            <h2 className="font-serif font-bold text-lg">More From Skip School</h2>
            <Link href="/articles" className="text-xs font-semibold text-teal hover:underline">All Articles &rarr;</Link>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
            {placeholderMoreArticles.map((a, i) => (
              <Link key={i} href={`/articles/${a.slug}`} className="bg-white border border-gray-200 rounded-xl overflow-hidden hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5">
                <div className={`w-full h-[130px] ${a.bg} flex items-center justify-center text-3xl`}>{a.emoji}</div>
                <div className="p-3">
                  <div className="text-[10px] font-bold text-coral uppercase tracking-wider mb-0.5">{a.cat}</div>
                  <div className="font-serif font-bold text-sm leading-tight line-clamp-2 mb-1.5">{a.title}</div>
                  <div className="text-[10px] text-gray-400">{a.readTime}</div>
                </div>
              </Link>
            ))}
          </div>
        </section>

        {/* Directory Preview */}
        <section className="mb-7" aria-label="Browse the AI homeschool directory">
          <div className="flex items-center justify-between mb-3.5 pb-2 border-b-2 border-charcoal">
            <h2 className="font-serif font-bold text-lg">Browse the Directory</h2>
            <Link href="/directory" className="text-xs font-semibold text-teal hover:underline">Full Directory &rarr;</Link>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
            {directoryCategories.map((cat) => (
              <Link key={cat.slug} href={`/directory?category=${cat.slug}`} className="bg-white border border-gray-200 rounded-xl p-4 text-center hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5">
                <div className="text-2xl mb-1.5">{cat.emoji}</div>
                <div className="text-[13px] font-bold mb-0.5">{cat.name}</div>
                <div className="text-[11px] text-gray-400">{cat.count} listings</div>
              </Link>
            ))}
          </div>
        </section>
      </div>

      {/* About Strip */}
      <section className="bg-white border-y border-gray-200 py-8 px-7" aria-label="About Skip School">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="font-serif font-bold text-base mb-1.5">Built by a Homeschool Family</h3>
            <p className="text-[13px] text-gray-500 leading-relaxed">
              Skip School isn&apos;t a tech company pretending to understand education. It&apos;s a real homeschool family sharing what works. Every tool gets tested with our own kids. Every prompt gets used in our own week.
            </p>
          </div>
          <div>
            <div className="text-[11px] text-teal font-semibold mb-1">Ashley Larkin, Editor</div>
            <p className="text-[13px] text-gray-500 leading-relaxed">
              Homeschool mom in Williamson County, Texas. Writes every issue. Tests every tool. If she wouldn&apos;t use it in her own home, it doesn&apos;t make the newsletter.
            </p>
          </div>
          <div>
            <div className="text-[11px] text-teal font-semibold mb-1">TJ Larkin, AI & Technology</div>
            <p className="text-[13px] text-gray-500 leading-relaxed">
              Builds the AI systems, tests the platforms, and finds the tools so Ashley can focus on teaching. If it involves prompts or figuring out how the tech works, that&apos;s TJ.
            </p>
          </div>
        </div>
      </section>
    </>
  )
}

function FeedCard({ source, title, comment }: { source: string; title: string; comment: string }) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl p-4 hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5 cursor-pointer">
      <div className="text-[10px] text-gray-400 uppercase tracking-wider font-semibold mb-1">{source}</div>
      <div className="font-serif font-bold text-sm leading-tight mb-1.5">{title}</div>
      <div className="text-xs text-teal italic">{comment}</div>
    </div>
  )
}

// ═══ PLACEHOLDER DATA (used before CMS is populated) ═══

const placeholderArticles = [
  { slug: 'plan-homeschool-week-claude', category: 'ai-for-parents', title: 'How I Plan Our Entire Homeschool Week in 15 Minutes with Claude' },
  { slug: 'khanmigo-review-30-days', category: 'review', title: 'Khanmigo After 30 Days: The Good, the Frustrating, and What I\'d Pay For' },
  { slug: 'texas-esa-guide', category: 'esa-guide', title: 'Texas ESA: Your Step-by-Step Guide to Getting $10,474 for Your Kids' },
  { slug: 'ai-tools-kids-use-alone', category: 'ai-for-kids', title: '5 AI Tools My Kids Actually Use (Without Me Standing Over Them)' },
  { slug: 'beast-academy-vs-saxon', category: 'comparison', title: 'Beast Academy vs. Saxon Math: Which One Is Actually Better?' },
  { slug: 'our-real-schedule', category: 'our-week', title: 'What Our Homeschool Schedule Actually Looks Like (Messy Version)' },
  { slug: 'new-ai-tools-this-week', category: 'the-download', title: 'Three New AI Tools for Education That Launched This Week' },
]

const placeholderTools = [
  { slug: 'khanmigo', name: 'Khanmigo', description: 'AI tutor from Khan Academy. Guided practice for math, science, humanities. Works alongside your curriculum.', price: '$44/mo', ratingDisplay: '★ 4.2 · AI Tutor', emoji: '🎓', bgColor: 'bg-teal-bg', badgeText: 'Free 30-Day Trial', badgeColor: 'bg-emerald-500', ctaText: 'Read Our Review →' },
  { slug: 'claude', name: 'Claude', description: 'AI assistant for lesson planning, curriculum design, and custom prompts. The tool that powers our whole week.', price: '$20/mo', ratingDisplay: '★ 4.5 · AI Assistant', emoji: '🤖', bgColor: 'bg-teal-bg', badgeText: 'We Use This Daily', badgeColor: 'bg-teal', ctaText: 'See Our Setup Guide →' },
  { slug: 'littlelit', name: 'LittleLit', description: 'Full K-8 AI platform. Adaptive reading, writing, and comprehension. Kids can use it independently.', price: '$15/mo', ratingDisplay: '★ 4.0 · K-8 Platform', emoji: '📚', bgColor: 'bg-coral-bg', badgeText: 'New', badgeColor: 'bg-coral', ctaText: 'Read Our Review →' },
  { slug: 'beast-academy', name: 'Beast Academy', description: 'Rigorous math curriculum disguised as a comic book. Builds problem-solving skills other programs skip.', price: '$13/mo', ratingDisplay: '★ 4.6 · Math', emoji: '🧮', bgColor: 'bg-amber-50', badgeText: 'Best for Math', badgeColor: 'bg-amber-500', ctaText: 'Read Our Review →' },
]

const placeholderMoreArticles = [
  { slug: 'homeschool-ai-spending', cat: 'Data', title: 'Homeschool Families Spent $2.3B on AI Tools Last Year', readTime: '4 min read', emoji: '📊', bg: 'bg-sky-50' },
  { slug: 'arizona-esa-expanded', cat: 'ESA Guide', title: 'Arizona Just Expanded Its ESA. Here\'s What Changed.', readTime: '5 min read', emoji: '🗺️', bg: 'bg-coral-bg' },
  { slug: 'claude-project-setup', cat: 'Tutorial', title: 'Set Up a Claude Project for Your Homeschool (Exact Steps)', readTime: '8 min read', emoji: '💻', bg: 'bg-amber-50' },
  { slug: 'new-ai-tools-this-week', cat: 'The Download', title: 'Three New AI Ed Tools That Launched This Week', readTime: '3 min read', emoji: '⚡', bg: 'bg-teal-bg' },
]

const directoryCategories = [
  { slug: 'ai-tutoring', emoji: '🤖', name: 'AI Tutoring', count: 24 },
  { slug: 'curriculum', emoji: '📘', name: 'Curriculum', count: 47 },
  { slug: 'enrichment', emoji: '🎨', name: 'Enrichment', count: 83 },
  { slug: 'esa-approved', emoji: '💰', name: 'ESA-Approved', count: 31 },
  { slug: 'testing', emoji: '📝', name: 'Testing', count: 15 },
  { slug: 'co-ops', emoji: '👥', name: 'Co-ops', count: 28 },
]
