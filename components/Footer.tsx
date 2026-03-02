import Link from 'next/link'

export function Footer() {
  return (
    <footer className="bg-white border-t border-gray-200">
      {/* Final CTA */}
      <section className="bg-gradient-to-br from-teal to-teal-dark py-12 px-7 text-center">
        <h2 className="font-serif font-extrabold text-2xl md:text-3xl text-white mb-2.5">
          Join 2,500+ families teaching smarter with AI
        </h2>
        <p className="text-sm text-white/75 mb-6">
          One email every Wednesday. Tools, prompts, reviews, and ESA updates. Free forever.
        </p>
        <form className="flex gap-2 max-w-md mx-auto flex-wrap justify-center">
          <input
            type="email"
            placeholder="your@email.com"
            className="flex-1 min-w-[200px] px-3.5 py-2.5 rounded-lg border-2 border-white/20 bg-white/10 text-white placeholder:text-white/40 text-sm outline-none focus:border-white/40"
          />
          <button className="px-5 py-2.5 rounded-lg bg-coral text-white text-sm font-bold hover:bg-coral/90 transition-colors">
            Subscribe Free
          </button>
        </form>
      </section>

      {/* Footer Grid */}
      <div className="px-7 py-10">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-7 mb-7">
          <div className="md:col-span-1">
            <div className="font-serif font-bold text-lg mb-1.5">Skip School</div>
            <p className="text-xs text-gray-400 leading-relaxed">
              The AI playbook for homeschool parents. Published weekly by Ashley and TJ Larkin from Williamson County, TX.
            </p>
          </div>
          <FooterCol title="Content" links={[
            { label: 'Articles', href: '/articles' },
            { label: 'Prompt Library', href: '/prompts' },
            { label: 'AI Tools Directory', href: '/directory' },
            { label: 'ESA Guides', href: '/esa-guides' },
            { label: 'Start Here', href: '/start-here' },
          ]} />
          <FooterCol title="Resources" links={[
            { label: 'Curriculum Reviews', href: '/articles?category=review' },
            { label: 'Tool Comparisons', href: '/articles?category=comparison' },
            { label: 'Co-op Finder', href: '/directory?category=co-ops' },
            { label: 'AI Readiness Quiz', href: '/quiz' },
          ]} />
          <FooterCol title="About" links={[
            { label: 'About Us', href: '/about' },
            { label: 'Advertise', href: '/advertise' },
            { label: 'Contact', href: '/contact' },
            { label: 'Privacy', href: '/privacy' },
            { label: 'Terms', href: '/terms' },
          ]} />
        </div>
        <div className="border-t border-gray-200 pt-4 flex justify-between flex-wrap gap-2 text-xs text-gray-400">
          <span>&copy; 2026 Skip School (SkipSchool.ai)</span>
          <span>Made with &#10084; and AI in Williamson County, TX</span>
        </div>
      </div>
    </footer>
  )
}

function FooterCol({ title, links }: { title: string; links: Array<{ label: string; href: string }> }) {
  return (
    <div>
      <div className="text-xs font-bold uppercase tracking-wider mb-3">{title}</div>
      {links.map((link) => (
        <Link key={link.href} href={link.href} className="block text-xs text-gray-400 py-0.5 hover:text-teal transition-colors">
          {link.label}
        </Link>
      ))}
    </div>
  )
}
