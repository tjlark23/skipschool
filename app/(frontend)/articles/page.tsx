import Link from 'next/link'
import type { Metadata } from 'next'
import { getPublishedArticles } from '@/lib/payload'
import { breadcrumbSchema } from '@/lib/seo'

export const metadata: Metadata = {
  title: 'Articles | AI Homeschool Guides, Reviews & Tutorials',
  description: 'Practical guides, tool reviews, and tutorials for homeschool parents using AI. Written by Ashley Larkin, a real homeschool mom.',
}

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'

const categoryConfig: Record<string, { color: string; bg: string; emoji: string; label: string }> = {
  'ai-for-parents': { color: 'text-teal', bg: 'bg-teal-bg', emoji: '🤖', label: 'AI for Parents' },
  'ai-for-kids': { color: 'text-purple-600', bg: 'bg-purple-50', emoji: '🧒', label: 'AI for Kids' },
  'review': { color: 'text-coral', bg: 'bg-coral-bg', emoji: '🔍', label: 'The Review' },
  'esa-guide': { color: 'text-amber-600', bg: 'bg-amber-50', emoji: '💰', label: 'ESA Guide' },
  'comparison': { color: 'text-emerald-600', bg: 'bg-emerald-50', emoji: '⚖️', label: 'Comparison' },
  'our-week': { color: 'text-pink-600', bg: 'bg-pink-50', emoji: '🏠', label: 'Our Week' },
  'the-download': { color: 'text-teal', bg: 'bg-teal-bg', emoji: '⚡', label: 'The Download' },
  'tutorial': { color: 'text-blue-600', bg: 'bg-blue-50', emoji: '💻', label: 'Tutorial' },
  'community': { color: 'text-violet-600', bg: 'bg-violet-50', emoji: '👥', label: 'Community' },
  'data': { color: 'text-sky-600', bg: 'bg-sky-50', emoji: '📊', label: 'Data' },
}

export default async function ArticlesPage() {
  let articles: any[] = []

  try {
    const res = await getPublishedArticles(50)
    articles = res.docs
  } catch {
    // CMS not connected
  }

  const showPlaceholder = articles.length === 0
  const displayArticles = showPlaceholder ? placeholderArticles : articles

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(breadcrumbSchema([
            { name: 'Home', url: SITE_URL },
            { name: 'Articles', url: `${SITE_URL}/articles` },
          ])),
        }}
      />

      <div className="px-7 py-8 max-w-5xl mx-auto">
        <header className="mb-8">
          <h1 className="font-serif font-bold text-3xl mb-2">Articles</h1>
          <p className="text-gray-500 text-sm leading-relaxed max-w-xl">
            Practical guides, honest reviews, and step-by-step tutorials for homeschool parents using AI. Everything Ashley tests with her own kids before recommending it to yours.
          </p>
        </header>

        {/* Category Filters */}
        <div className="flex flex-wrap gap-2 mb-8">
          <span className="px-3 py-1.5 rounded-full bg-teal text-white text-xs font-semibold cursor-pointer">All</span>
          {Object.entries(categoryConfig).map(([key, cat]) => (
            <span key={key} className="px-3 py-1.5 rounded-full bg-white border border-gray-200 text-xs font-medium text-gray-600 cursor-pointer hover:border-teal hover:text-teal transition-colors">
              {cat.emoji} {cat.label}
            </span>
          ))}
        </div>

        {/* Article Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {displayArticles.map((article: any, i: number) => {
            const cat = categoryConfig[article.category] || categoryConfig['ai-for-parents']
            return (
              <Link
                key={article.slug || i}
                href={`/articles/${article.slug}`}
                className="bg-white border border-gray-200 rounded-xl overflow-hidden hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5 group"
              >
                <div className={`w-full h-[160px] ${cat.bg} flex items-center justify-center text-4xl`}>
                  {cat.emoji}
                </div>
                <div className="p-4">
                  <div className={`text-[10px] font-bold uppercase tracking-wider mb-1 ${cat.color}`}>
                    {cat.label}
                  </div>
                  <h2 className="font-serif font-bold text-base leading-tight mb-2 group-hover:text-teal transition-colors line-clamp-2">
                    {article.title}
                  </h2>
                  <p className="text-xs text-gray-500 leading-relaxed line-clamp-2 mb-3">
                    {article.excerpt || ''}
                  </p>
                  <div className="flex items-center justify-between text-[10px] text-gray-400">
                    <span>{article.author?.name || 'Ashley Larkin'}</span>
                    <span>{article.readTime ? `${article.readTime} min read` : ''}</span>
                  </div>
                </div>
              </Link>
            )
          })}
        </div>
      </div>
    </>
  )
}

const placeholderArticles = [
  { slug: 'plan-homeschool-week-claude', category: 'ai-for-parents', title: 'How I Plan Our Entire Homeschool Week in 15 Minutes with Claude', excerpt: 'Every Sunday night, after the kids are in bed, I open Claude and build our whole week.', readTime: 6, author: { name: 'Ashley Larkin' } },
  { slug: 'khanmigo-review-30-days', category: 'review', title: 'Khanmigo After 30 Days: The Good, the Frustrating, and What I\'d Pay For', excerpt: 'We used Khanmigo every school day for a month. Here\'s what actually happened.', readTime: 8, author: { name: 'Ashley Larkin' } },
  { slug: 'texas-esa-guide', category: 'esa-guide', title: 'Texas ESA: Your Step-by-Step Guide to Getting $10,474 for Your Kids', excerpt: 'Applications are open. Here\'s exactly how to apply and what it covers.', readTime: 10, author: { name: 'Ashley Larkin' } },
  { slug: 'ai-tools-kids-use-alone', category: 'ai-for-kids', title: '5 AI Tools My Kids Actually Use (Without Me Standing Over Them)', excerpt: 'These are the ones I don\'t have to micromanage.', readTime: 5, author: { name: 'Ashley Larkin' } },
  { slug: 'beast-academy-vs-saxon', category: 'comparison', title: 'Beast Academy vs. Saxon Math: Which One Is Actually Better?', excerpt: 'Two very different approaches to math. We\'ve tried both.', readTime: 7, author: { name: 'Ashley Larkin' } },
  { slug: 'our-real-schedule', category: 'our-week', title: 'What Our Homeschool Schedule Actually Looks Like (Messy Version)', excerpt: 'No Pinterest-perfect day here. This is the real one.', readTime: 4, author: { name: 'Ashley Larkin' } },
]
