import type { Metadata } from 'next'
import Link from 'next/link'
import { notFound } from 'next/navigation'
import { getArticleBySlug, getPublishedArticles } from '@/lib/payload'
import { articleSchema, faqSchema, breadcrumbSchema } from '@/lib/seo'
import { NewsletterSignup } from '@/components/NewsletterSignup'

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'

interface PageProps {
  params: Promise<{ slug: string }>
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params
  let article: any = null
  try {
    article = await getArticleBySlug(slug)
  } catch {}

  if (!article) {
    return { title: 'Article Not Found' }
  }

  return {
    title: article.seo?.metaTitle || article.title,
    description: article.seo?.metaDescription || article.excerpt,
    openGraph: {
      title: article.title,
      description: article.excerpt,
      type: 'article',
      publishedTime: article.publishedAt,
      authors: [article.author?.name || 'Ashley Larkin'],
    },
  }
}

export default async function ArticlePage({ params }: PageProps) {
  const { slug } = await params
  let article: any = null

  try {
    article = await getArticleBySlug(slug)
  } catch {
    // CMS not connected - show placeholder
  }

  // If no CMS, show a placeholder article page
  if (!article) {
    return <PlaceholderArticle slug={slug} />
  }

  return (
    <>
      {/* Structured Data */}
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema(article)) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema([
        { name: 'Home', url: SITE_URL },
        { name: 'Articles', url: `${SITE_URL}/articles` },
        { name: article.title, url: `${SITE_URL}/articles/${slug}` },
      ])) }} />
      {article.faq?.length > 0 && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema(article.faq)) }} />
      )}

      <article className="max-w-3xl mx-auto px-7 py-8">
        {/* Breadcrumb */}
        <nav className="text-xs text-gray-400 mb-6">
          <Link href="/" className="hover:text-teal">Home</Link>
          <span className="mx-1.5">/</span>
          <Link href="/articles" className="hover:text-teal">Articles</Link>
          <span className="mx-1.5">/</span>
          <span className="text-gray-600">{article.title}</span>
        </nav>

        <header className="mb-8">
          <div className="text-xs font-bold text-coral uppercase tracking-wider mb-2">
            {article.category}
          </div>
          <h1 className="font-serif font-bold text-3xl md:text-4xl leading-tight mb-3">
            {article.title}
          </h1>
          {article.excerpt && (
            <p className="text-gray-500 text-base leading-relaxed mb-4">{article.excerpt}</p>
          )}
          <div className="flex items-center gap-3 text-sm text-gray-400">
            <span className="font-medium text-charcoal">{article.author?.name || 'Ashley Larkin'}</span>
            <span>&middot;</span>
            {article.publishedAt && <span>{new Date(article.publishedAt).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</span>}
            {article.readTime && <><span>&middot;</span><span>{article.readTime} min read</span></>}
          </div>
        </header>

        {/* Article Content - rendered from Lexical rich text */}
        <div className="prose prose-lg max-w-none">
          {/* Payload Lexical content would be rendered here */}
          <p className="text-gray-500 italic">Content renders from Payload CMS rich text editor.</p>
        </div>

        {/* Newsletter Signup */}
        <div className="my-10">
          <NewsletterSignup variant="inline" />
        </div>

        {/* FAQ Section */}
        {article.faq?.length > 0 && (
          <section className="mt-10 border-t border-gray-200 pt-8" aria-label="Frequently asked questions">
            <h2 className="font-serif font-bold text-xl mb-4">Frequently Asked Questions</h2>
            {article.faq.map((faq: any, i: number) => (
              <div key={i} className="border-b border-gray-100 py-4">
                <h3 className="font-semibold text-sm mb-2">{faq.question}</h3>
                <p className="text-sm text-gray-500 leading-relaxed">{faq.answer}</p>
              </div>
            ))}
          </section>
        )}
      </article>
    </>
  )
}

function PlaceholderArticle({ slug }: { slug: string }) {
  return (
    <article className="max-w-3xl mx-auto px-7 py-8">
      <nav className="text-xs text-gray-400 mb-6">
        <Link href="/" className="hover:text-teal">Home</Link>
        <span className="mx-1.5">/</span>
        <Link href="/articles" className="hover:text-teal">Articles</Link>
        <span className="mx-1.5">/</span>
        <span className="text-gray-600">{slug}</span>
      </nav>
      <div className="bg-teal-bg rounded-xl p-8 text-center">
        <div className="text-4xl mb-4">📝</div>
        <h1 className="font-serif font-bold text-2xl mb-2">Article Coming Soon</h1>
        <p className="text-gray-500 text-sm mb-4">
          This article will be published once the CMS is connected and content is created.
        </p>
        <Link href="/articles" className="text-teal font-semibold text-sm hover:underline">
          &larr; Back to Articles
        </Link>
      </div>
    </article>
  )
}
