import Link from 'next/link'
import type { Metadata } from 'next'
import { getTools } from '@/lib/payload'
import { breadcrumbSchema, faqSchema } from '@/lib/seo'

export const metadata: Metadata = {
  title: 'AI Homeschool Directory | 200+ Tools, Curriculum & Resources',
  description: 'Browse 200+ AI tutoring platforms, curriculum providers, enrichment programs, and ESA-approved services. Every tool reviewed by a real homeschool family.',
}

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'

const categories = [
  { slug: 'all', label: 'All Tools', emoji: '📚' },
  { slug: 'ai-tutoring', label: 'AI Tutoring', emoji: '🤖' },
  { slug: 'ai-assistant', label: 'AI Assistants', emoji: '💬' },
  { slug: 'curriculum', label: 'Curriculum', emoji: '📘' },
  { slug: 'k8-platform', label: 'K-8 Platforms', emoji: '🎓' },
  { slug: 'math', label: 'Math', emoji: '🧮' },
  { slug: 'reading-writing', label: 'Reading & Writing', emoji: '✍️' },
  { slug: 'enrichment', label: 'Enrichment', emoji: '🎨' },
  { slug: 'testing', label: 'Testing', emoji: '📝' },
  { slug: 'esa-approved', label: 'ESA-Approved', emoji: '💰' },
  { slug: 'co-ops', label: 'Co-ops', emoji: '👥' },
]

const badgeConfig: Record<string, { label: string; color: string }> = {
  'daily-use': { label: 'We Use This Daily', color: 'bg-teal' },
  'free-trial': { label: 'Free Trial', color: 'bg-emerald-500' },
  'new': { label: 'New', color: 'bg-coral' },
  'best-math': { label: 'Best for Math', color: 'bg-amber-500' },
  'best-reading': { label: 'Best for Reading', color: 'bg-blue-500' },
  'recommended': { label: 'Skip School Recommended', color: 'bg-gold' },
  'esa-approved': { label: 'ESA Approved', color: 'bg-emerald-600' },
}

const directoryFaqs = [
  { question: 'What AI tools are best for homeschool parents?', answer: 'Top AI tools for homeschool parents in 2026 include Khanmigo for tutoring ($44/mo), Claude for lesson planning ($20/mo), LittleLit for K-8 ($15/mo), and Beast Academy for math ($13/mo). Skip School\'s directory has 200+ reviewed tools with ratings and pricing.' },
  { question: 'Are these tools ESA-approved?', answer: 'Many tools in the Skip School directory are approved for Education Savings Account (ESA) spending. Filter by "ESA-Approved" to see tools you can pay for with your state\'s ESA funds. Texas ESA covers up to $10,474 per child per year.' },
  { question: 'How does Skip School review tools?', answer: 'Ashley Larkin tests every tool with her own kids before it goes in the directory. Ratings are based on real usage, not press releases. Reviews include pros, cons, pricing, age ranges, and honest takes on what works and what doesn\'t.' },
  { question: 'What curriculum providers work with AI?', answer: 'Several curriculum providers integrate AI features, including Khan Academy (Khanmigo), Beast Academy Online, and newer platforms like LittleLit and SchoolHouse Anywhere. The directory lets you filter by AI-integrated curriculum.' },
]

export default async function DirectoryPage() {
  let tools: any[] = []

  try {
    const res = await getTools(undefined, 100)
    tools = res.docs
  } catch {
    // CMS not connected
  }

  const showPlaceholder = tools.length === 0
  const displayTools = showPlaceholder ? placeholderTools : tools

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema([
        { name: 'Home', url: SITE_URL },
        { name: 'Directory', url: `${SITE_URL}/directory` },
      ])) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema(directoryFaqs)) }} />

      <div className="px-7 py-8 max-w-6xl mx-auto">
        <header className="mb-8">
          <h1 className="font-serif font-bold text-3xl mb-2">AI Homeschool Directory</h1>
          <p className="text-gray-500 text-sm leading-relaxed max-w-xl">
            200+ AI tools, curriculum providers, enrichment programs, and ESA-approved services. Every listing reviewed by a real homeschool family.
          </p>
        </header>

        {/* Category Filters */}
        <div className="flex flex-wrap gap-2 mb-8">
          {categories.map((cat) => (
            <Link
              key={cat.slug}
              href={cat.slug === 'all' ? '/directory' : `/directory?category=${cat.slug}`}
              className="px-3 py-1.5 rounded-full bg-white border border-gray-200 text-xs font-medium text-gray-600 hover:border-teal hover:text-teal transition-colors"
            >
              {cat.emoji} {cat.label}
            </Link>
          ))}
        </div>

        {/* Tool Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayTools.map((tool: any, i: number) => {
            const badge = tool.badge ? badgeConfig[tool.badge] : null
            return (
              <Link
                key={tool.slug || i}
                href={`/directory/${tool.slug}`}
                className="bg-white border border-gray-200 rounded-xl overflow-hidden hover:border-teal hover:shadow-lg transition-all hover:-translate-y-0.5 group"
              >
                <div className="h-[100px] bg-teal-bg flex items-center justify-center text-4xl relative">
                  {tool.emoji || '🎓'}
                  {badge && (
                    <span className={`absolute top-2 right-2 px-2 py-0.5 rounded text-[9px] font-bold text-white ${badge.color}`}>
                      {badge.label}
                    </span>
                  )}
                </div>
                <div className="p-4">
                  <div className="flex items-center justify-between mb-1">
                    <h2 className="text-sm font-bold group-hover:text-teal transition-colors">{tool.name}</h2>
                    {tool.rating && (
                      <span className="text-xs text-amber-500 font-semibold">★ {tool.rating}</span>
                    )}
                  </div>
                  <p className="text-[11px] text-gray-500 leading-snug mb-2 line-clamp-2">
                    {tool.description}
                  </p>
                  <div className="flex items-center justify-between">
                    <span className="text-sm font-bold text-teal">{tool.pricing?.price || tool.price || 'Free'}</span>
                    {tool.ageRange?.display && (
                      <span className="text-[10px] text-gray-400">{tool.ageRange.display}</span>
                    )}
                  </div>
                  {tool.ashleyTake && (
                    <p className="text-[10px] text-teal italic mt-2 border-t border-gray-100 pt-2 line-clamp-1">
                      &ldquo;{tool.ashleyTake}&rdquo;
                    </p>
                  )}
                </div>
              </Link>
            )
          })}
        </div>

        {/* FAQ Section */}
        <section className="mt-16 max-w-3xl mx-auto" aria-label="Directory FAQ">
          <h2 className="font-serif font-bold text-xl mb-6">Frequently Asked Questions</h2>
          {directoryFaqs.map((faq, i) => (
            <div key={i} className="border-b border-gray-100 py-4">
              <h3 className="font-semibold text-sm mb-2">{faq.question}</h3>
              <p className="text-sm text-gray-500 leading-relaxed">{faq.answer}</p>
            </div>
          ))}
        </section>
      </div>
    </>
  )
}

const placeholderTools = [
  { slug: 'khanmigo', name: 'Khanmigo', description: 'AI tutor from Khan Academy. Guided practice for math, science, humanities. Works alongside your curriculum.', price: '$44/mo', rating: 4.2, emoji: '🎓', badge: 'free-trial', ageRange: { display: 'Ages 5-18' }, ashleyTake: 'Best for math practice. My 10-year-old uses it independently.' },
  { slug: 'claude', name: 'Claude', description: 'AI assistant for lesson planning, curriculum design, and custom prompts. The tool that powers our whole week.', price: '$20/mo', rating: 4.5, emoji: '🤖', badge: 'daily-use', ageRange: { display: 'Parents' }, ashleyTake: 'The single tool I couldn\'t homeschool without.' },
  { slug: 'littlelit', name: 'LittleLit', description: 'Full K-8 AI platform. Adaptive reading, writing, and comprehension. Kids can use it independently.', price: '$15/mo', rating: 4.0, emoji: '📚', badge: 'new', ageRange: { display: 'Ages 5-14' }, ashleyTake: 'New but impressive. Reading comprehension features are solid.' },
  { slug: 'beast-academy', name: 'Beast Academy', description: 'Rigorous math curriculum disguised as a comic book. Builds problem-solving skills other programs skip.', price: '$13/mo', rating: 4.6, emoji: '🧮', badge: 'best-math', ageRange: { display: 'Ages 6-13' }, ashleyTake: 'My kids actually beg to do math with this one.' },
  { slug: 'outschool', name: 'Outschool', description: 'Live online classes taught by independent teachers. Every subject imaginable. Great for socialization.', price: 'Varies', rating: 4.1, emoji: '🎨', badge: 'recommended', ageRange: { display: 'Ages 3-18' }, ashleyTake: 'We use this for art and social studies. Quality varies by teacher.' },
  { slug: 'chatgpt', name: 'ChatGPT', description: 'General AI assistant from OpenAI. Useful for older kids and parents. Less specialized than Claude for education.', price: '$20/mo', rating: 3.8, emoji: '💬', ageRange: { display: 'Ages 13+' }, ashleyTake: 'Good but not as strong as Claude for lesson planning.' },
  { slug: 'ixl', name: 'IXL', description: 'Adaptive practice platform for math, language arts, science, and social studies. Tracks mastery by standard.', price: '$13/mo', rating: 4.0, emoji: '📊', badge: 'esa-approved', ageRange: { display: 'Ages 4-18' }, ashleyTake: 'Solid for drill practice. Not exciting but effective.' },
  { slug: 'duolingo', name: 'Duolingo', description: 'Language learning app with gamified lessons. Free tier is generous. Kids love the streaks.', price: 'Free', rating: 4.3, emoji: '🗣️', ageRange: { display: 'Ages 5+' }, ashleyTake: 'Both my kids do this voluntarily. That says something.' },
  { slug: 'mystery-science', name: 'Mystery Science', description: 'Video-based science lessons with hands-on activities. Engaging for elementary and middle school.', price: '$10/mo', rating: 4.4, emoji: '🔬', badge: 'recommended', ageRange: { display: 'Ages 5-12' }, ashleyTake: 'My favorite science resource. The experiments actually work.' },
]
