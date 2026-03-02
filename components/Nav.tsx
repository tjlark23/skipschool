import Link from 'next/link'

export function Nav() {
  return (
    <>
      {/* Main Nav */}
      <nav className="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm px-7 h-14 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-teal flex items-center justify-center text-white font-serif font-extrabold text-base">
            S
          </div>
          <span className="font-serif font-bold text-xl text-charcoal">
            Skip <span className="text-teal">School</span>
          </span>
        </Link>

        <div className="hidden lg:flex items-center gap-1 h-full">
          <NavLink href="/" active>Home</NavLink>
          <NavLink href="/articles">Articles</NavLink>
          <NavLink href="/directory">Directory</NavLink>
          <NavLink href="/prompts">Prompts</NavLink>
          <NavLink href="/esa-guides">ESA Guides</NavLink>
          <NavLink href="/start-here">Start Here</NavLink>
        </div>

        <div className="flex items-center gap-3">
          <button className="w-9 h-9 rounded-lg border border-gray-200 flex items-center justify-center text-gray-400 hover:text-charcoal transition-colors">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <circle cx="11" cy="11" r="8" />
              <line x1="21" y1="21" x2="16.65" y2="16.65" />
            </svg>
          </button>
          <button className="bg-teal text-white px-5 py-2 rounded-lg text-sm font-semibold hover:bg-teal-dark transition-colors">
            Subscribe Free
          </button>
        </div>
      </nav>

      {/* Tagline Bar */}
      <div className="bg-teal-light border-b border-teal/20 py-3.5 px-7 text-center">
        <p className="font-serif font-bold text-lg text-teal-dark tracking-wide">
          The AI Playbook for Homeschool Parents
        </p>
      </div>
    </>
  )
}

function NavLink({ href, children, active }: { href: string; children: React.ReactNode; active?: boolean }) {
  return (
    <Link
      href={href}
      className={`px-4 h-full flex items-center text-sm font-medium relative transition-colors ${
        active
          ? 'text-teal font-semibold after:absolute after:bottom-0 after:left-4 after:right-4 after:h-0.5 after:bg-teal after:rounded-t'
          : 'text-gray-500 hover:text-charcoal'
      }`}
    >
      {children}
    </Link>
  )
}
