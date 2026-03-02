import type { Metadata } from 'next'
import Link from 'next/link'
import { getToolBySlug } from '@/lib/payload'
import { toolSchema, faqSchema, breadcrumbSchema } from '@/lib/seo'
import { NewsletterSignup } from '@/components/NewsletterSignup'

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'

interface PageProps {
  params: Promise<{ slug: string }>
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params
  let tool: any = null
  try { tool = await getToolBySlug(slug) } catch {}

  if (!tool) return { title: 'Tool Not Found' }

  return {
    title: tool.seo?.metaTitle || `${tool.name} Review | AI Homeschool Directory`,
    description: tool.seo?.metaDescription || tool.description,
    openGraph: {
      title: `${tool.name} Review | Skip School Directory`,
      description: tool.description,
      type: 'website',
    },
  }
}

export default async function ToolDetailPage({ params }: PageProps) {
  const { slug } = await params
  let tool: any = null
  try { tool = await getToolBySlug(slug) } catch {}

  if (!tool) return <PlaceholderTool slug={slug} />

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(toolSchema(tool)) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema([
        { name: 'Home', url: SITE_URL },
        { name: 'Directory', url: `${SITE_URL}/directory` },
        { name: tool.name, url: `${SITE_URL}/directory/${slug}` },
      ])) }} />
      {tool.faq?.length > 0 && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema(tool.faq)) }} />
      )}

      <div className="max-w-4xl mx-auto px-7 py-8">
        <nav className="text-xs text-gray-400 mb-6">
          <Link href="/" className="hover:text-teal">Home</Link>
          <span className="mx-1.5">/</span>
          <Link href="/directory" className="hover:text-teal">Directory</Link>
          <span className="mx-1.5">/</span>
          <span className="text-gray-600">{tool.name}</span>
        </nav>

        <div className="grid grid-cols-1 lg:grid-cols-[2fr_1fr] gap-8">
          <div>
            <h1 className="font-serif font-bold text-3xl mb-2">{tool.name}</h1>
            <p className="text-gray-500 text-base leading-relaxed mb-4">{tool.description}</p>

            {tool.ashleyTake && (
              <div className="bg-teal-bg border border-teal/20 rounded-xl p-4 mb-6">
                <div className="text-xs font-bold text-teal mb-1">Ashley&apos;s Take</div>
                <p className="text-sm text-charcoal italic">&ldquo;{tool.ashleyTake}&rdquo;</p>
              </div>
            )}

            {tool.pros?.length > 0 && (
              <div className="mb-4">
                <h2 className="font-semibold text-sm mb-2">What Works</h2>
                {tool.pros.map((p: any, i: number) => (
                  <div key={i} className="flex items-start gap-2 text-sm text-gray-600 mb-1">
                    <span className="text-emerald-500 mt-0.5">✓</span> {p.item}
                  </div>
                ))}
              </div>
            )}

            {tool.cons?.length > 0 && (
              <div className="mb-6">
                <h2 className="font-semibold text-sm mb-2">What Doesn&apos;t</h2>
                {tool.cons.map((c: any, i: number) => (
                  <div key={i} className="flex items-start gap-2 text-sm text-gray-600 mb-1">
                    <span className="text-coral mt-0.5">✕</span> {c.item}
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="space-y-4">
            <div className="bg-white border border-gray-200 rounded-xl p-5">
              {tool.rating && (
                <div className="text-center mb-3">
                  <div className="text-3xl font-bold text-teal">{tool.rating}</div>
                  <div className="text-xs text-gray-400">out of 5</div>
                </div>
              )}
              <div className="space-y-2 text-sm">
                <div className="flex justify-between"><span className="text-gray-500">Price</span><span className="font-semibold">{tool.pricing?.price || 'Free'}</span></div>
                {tool.ageRange?.display && <div className="flex justify-between"><span className="text-gray-500">Ages</span><span className="font-semibold">{tool.ageRange.display}</span></div>}
                <div className="flex justify-between"><span className="text-gray-500">Category</span><span className="font-semibold capitalize">{tool.category?.replace(/-/g, ' ')}</span></div>
                {tool.isEsaApproved && <div className="flex justify-between"><span className="text-gray-500">ESA</span><span className="font-semibold text-emerald-600">Approved ✓</span></div>}
              </div>
              {tool.url && (
                <a href={tool.affiliateUrl || tool.url} target="_blank" rel="noopener noreferrer" className="block w-full mt-4 bg-teal text-white text-center py-2.5 rounded-lg font-semibold text-sm hover:bg-teal-dark transition-colors">
                  Visit {tool.name} &rarr;
                </a>
              )}
            </div>
          </div>
        </div>

        <div className="my-10"><NewsletterSignup variant="inline" /></div>

        {tool.faq?.length > 0 && (
          <section className="mt-10 border-t border-gray-200 pt-8">
            <h2 className="font-serif font-bold text-xl mb-4">Frequently Asked Questions</h2>
            {tool.faq.map((faq: any, i: number) => (
              <div key={i} className="border-b border-gray-100 py-4">
                <h3 className="font-semibold text-sm mb-2">{faq.question}</h3>
                <p className="text-sm text-gray-500 leading-relaxed">{faq.answer}</p>
              </div>
            ))}
          </section>
        )}
      </div>
    </>
  )
}

function PlaceholderTool({ slug }: { slug: string }) {
  return (
    <div className="max-w-4xl mx-auto px-7 py-8">
      <nav className="text-xs text-gray-400 mb-6">
        <Link href="/" className="hover:text-teal">Home</Link>
        <span className="mx-1.5">/</span>
        <Link href="/directory" className="hover:text-teal">Directory</Link>
        <span className="mx-1.5">/</span>
        <span className="text-gray-600">{slug}</span>
      </nav>
      <div className="bg-teal-bg rounded-xl p-8 text-center">
        <div className="text-4xl mb-4">🔧</div>
        <h1 className="font-serif font-bold text-2xl mb-2">Tool Listing Coming Soon</h1>
        <p className="text-gray-500 text-sm mb-4">This tool will be added once the directory is populated.</p>
        <Link href="/directory" className="text-teal font-semibold text-sm hover:underline">&larr; Back to Directory</Link>
      </div>
    </div>
  )
}
