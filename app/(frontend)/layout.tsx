import type { Metadata } from 'next'
import '../../styles/globals.css'
import { Nav } from '@/components/Nav'
import { Footer } from '@/components/Footer'
import { organizationSchema, faqSchema } from '@/lib/seo'

export const metadata: Metadata = {
  title: {
    default: 'Skip School | The AI Playbook for Homeschool Parents',
    template: '%s | Skip School',
  },
  description: 'Skip School helps homeschool parents use AI, find the right resources, and connect with other families doing the same thing. Free weekly newsletter, tool directory, prompt library.',
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'),
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: '/',
    siteName: 'Skip School',
    title: 'Skip School | The AI Playbook for Homeschool Parents',
    description: 'AI tools, prompts, and resources for homeschool families. Written by a real homeschool family.',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Skip School | The AI Playbook for Homeschool Parents',
    description: 'AI tools, prompts, and resources for homeschool families.',
  },
  other: {
    'geo.region': 'US-TX',
    'geo.placename': 'Williamson County, Texas',
  },
}

export default function FrontendLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(organizationSchema()) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(
              faqSchema([
                {
                  question: 'What is Skip School?',
                  answer: 'Skip School is a media brand for homeschool families who use AI. Founded by Ashley and TJ Larkin, Skip School publishes a free weekly newsletter, tool reviews, a prompt library, ESA guides, and a directory of 200+ AI education resources.',
                },
                {
                  question: 'How can AI help with homeschooling?',
                  answer: 'AI tools like Claude, ChatGPT, and Khanmigo help parents plan lessons in minutes, generate custom curriculum, and tutor kids one-on-one. Skip School shows you exactly how to use them.',
                },
                {
                  question: 'What are the best AI tools for homeschool parents?',
                  answer: 'Top tools in 2026 include Khanmigo for tutoring, Claude for lesson planning, LittleLit for K-8, and Beast Academy for math. Skip School\'s directory has 200+ reviewed tools with ratings and pricing.',
                },
                {
                  question: 'What is an Education Savings Account (ESA)?',
                  answer: 'An ESA is a state program giving homeschool families money for education. Texas offers up to $10,474 per child per year for curriculum, tutoring, enrichment, and approved services.',
                },
                {
                  question: 'Who writes Skip School?',
                  answer: 'Ashley Larkin, a homeschool mom in Texas, and TJ Larkin, who handles AI and technology. Ashley tests every tool with her own kids before recommending it.',
                },
              ])
            ),
          }}
        />
      </head>
      <body>
        <Nav />
        {/* Tagline Bar */}
        <div className="bg-teal-light border-b border-teal/20 py-3 px-7 text-center">
          <p className="font-serif font-bold text-teal-dark text-lg tracking-wide">
            The AI Playbook for Homeschool Parents
          </p>
        </div>
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  )
}
