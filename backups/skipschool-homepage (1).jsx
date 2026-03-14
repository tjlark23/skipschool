import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import {
  Search, Menu, X, Play, Terminal, ArrowRight, ClipboardCheck,
  Zap, Mail, GraduationCap, MessageSquare, BookOpen, Calculator,
  Star, ExternalLink, Check, Crown, Palette, BadgeCheck,
  ClipboardList, Users, Twitter, Instagram, Youtube
} from "lucide-react";

/* ─── Design Tokens ─── */
const T = {
  navy: "#1a2332",
  navyLight: "#243044",
  navyBorder: "#2d3d52",
  forest: "#2d5a3d",
  amber: "#E8B830",
  coral: "#e8735a",
  cream: "#faf7f2",
  white: "#ffffff",
  text: "#1a1a1a",
  muted: "#6b7280",
  border: "#e8e2d9",
  lightAmber: "#fdf6e9",
  lightForest: "#f0f7f2",
  lightCoral: "#fdf0ed",
};

const font = {
  serif: "'Fraunces', Georgia, serif",
  sans: "'Inter', system-ui, sans-serif",
};

const shadow = {
  warm: "0 10px 40px -10px rgba(26,35,50,0.08), 0 0 4px rgba(26,35,50,0.03)",
  warmLg: "0 20px 40px -10px rgba(26,35,50,0.12), 0 0 4px rgba(26,35,50,0.03)",
  warmSm: "0 4px 12px -4px rgba(26,35,50,0.06), 0 0 2px rgba(26,35,50,0.02)",
};

/* ─── Global Styles ─── */
function GlobalStyles() {
  return (
    <style>{`
      @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600;9..144,700;9..144,800&family=Inter:wght@300;400;500;600;700&display=swap');
      *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
      body { background: ${T.cream}; color: ${T.text}; font-family: ${font.sans}; -webkit-font-smoothing: antialiased; }
      ::selection { background: ${T.amber}; color: ${T.navy}; }
      ::-webkit-scrollbar { width: 10px; }
      ::-webkit-scrollbar-track { background: ${T.cream}; }
      ::-webkit-scrollbar-thumb { background: ${T.border}; border-radius: 5px; }
      ::-webkit-scrollbar-thumb:hover { background: ${T.muted}; }
      .line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    `}</style>
  );
}

/* ─── Shared Logo (SVG fallback since CDN images may expire) ─── */
function LogoMark({ inverted = false, height = 36 }) {
  const fill = inverted ? T.white : T.navy;
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height }}>
      <div style={{
        width: height, height, borderRadius: 8,
        background: inverted ? "rgba(255,255,255,0.15)" : T.navy,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontFamily: font.serif, fontWeight: 800, fontSize: height * 0.5,
        color: inverted ? T.amber : T.white,
      }}>S</div>
      <span style={{ fontFamily: font.serif, fontWeight: 700, fontSize: height * 0.55, color: fill, letterSpacing: "-0.02em" }}>
        Skip School
      </span>
    </div>
  );
}

/* ═══════════════════════════════════════════════
   1. NAVIGATION
   ═══════════════════════════════════════════════ */
function Navigation() {
  const [open, setOpen] = useState(false);
  const links = ["Home", "Articles", "Directory", "Prompts", "ESA Guides", "Start Here"];

  return (
    <header style={{
      position: "sticky", top: 0, zIndex: 50, width: "100%",
      background: `${T.cream}ee`, backdropFilter: "blur(12px)",
      borderBottom: `1px solid ${T.border}`,
    }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px", display: "flex", justifyContent: "space-between", alignItems: "center", height: 64 }}>
        <LogoMark height={32} />

        {/* Desktop Nav */}
        <nav style={{ display: "flex", alignItems: "center", gap: 32 }} className="hidden-mobile">
          <ul style={{ display: "flex", gap: 24, listStyle: "none" }}>
            {links.map(l => (
              <li key={l}>
                <a href="#" style={{
                  fontSize: 14, fontWeight: l === "Start Here" ? 600 : 500,
                  color: l === "Start Here" ? T.forest : T.muted,
                  textDecoration: "none",
                }}>{l}</a>
              </li>
            ))}
          </ul>
          <div style={{ display: "flex", alignItems: "center", gap: 16, paddingLeft: 24, borderLeft: `1px solid ${T.border}` }}>
            <Search style={{ width: 20, height: 20, color: T.muted, cursor: "pointer" }} />
            <a href="#subscribe" style={{
              background: T.amber, color: T.navy, padding: "10px 20px",
              borderRadius: 8, fontSize: 14, fontWeight: 600, textDecoration: "none",
            }}>Subscribe Free</a>
          </div>
        </nav>

        {/* Mobile Toggle */}
        <button onClick={() => setOpen(!open)} style={{ background: "none", border: "none", cursor: "pointer", padding: 8 }} className="show-mobile-only">
          {open ? <X style={{ width: 24, height: 24, color: T.navy }} /> : <Menu style={{ width: 24, height: 24, color: T.navy }} />}
        </button>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            style={{ overflow: "hidden", background: T.cream, borderBottom: `1px solid ${T.border}` }}
            className="show-mobile-only"
          >
            <div style={{ padding: "24px 16px", display: "flex", flexDirection: "column", gap: 16 }}>
              {links.map(l => (
                <a key={l} href="#" style={{ fontSize: 18, fontWeight: 500, color: l === "Start Here" ? T.forest : T.navy, textDecoration: "none" }}>{l}</a>
              ))}
              <div style={{ borderTop: `1px solid ${T.border}`, paddingTop: 16 }}>
                <a href="#subscribe" style={{
                  display: "block", textAlign: "center", background: T.amber, color: T.navy,
                  padding: "12px 20px", borderRadius: 8, fontWeight: 600, textDecoration: "none",
                }}>Subscribe Free</a>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <style>{`
        @media (max-width: 768px) { .hidden-mobile { display: none !important; } }
        @media (min-width: 769px) { .show-mobile-only { display: none !important; } }
      `}</style>
    </header>
  );
}

/* ═══════════════════════════════════════════════
   2. SPONSOR BAR
   ═══════════════════════════════════════════════ */
function SponsorBar() {
  return (
    <div style={{ width: "100%", background: T.navy, color: T.white, padding: "10px 0", borderBottom: `1px solid ${T.navyBorder}` }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px", display: "flex", alignItems: "center", justifyContent: "center", gap: 12, fontSize: 13, flexWrap: "wrap" }}>
        <span style={{ fontWeight: 700, letterSpacing: "0.1em", color: "rgba(255,255,255,0.5)", fontSize: 10, textTransform: "uppercase" }}>Presented By</span>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ fontWeight: 700, background: T.navyLight, padding: "2px 8px", borderRadius: 4 }}>K</span>
          <span style={{ fontWeight: 600 }}>Khanmigo</span>
          <span style={{ color: "rgba(255,255,255,0.7)" }} className="hidden-mobile-inline"> — AI tutoring for every subject. Try free for 30 days.</span>
        </div>
        <a href="#" style={{ color: T.amber, fontWeight: 600, textDecoration: "none" }}>Learn More →</a>
      </div>
      <style>{`@media (max-width: 640px) { .hidden-mobile-inline { display: none !important; } }`}</style>
    </div>
  );
}

/* ═══════════════════════════════════════════════
   3. HERO GRID
   ═══════════════════════════════════════════════ */
function HeroGrid() {
  const sidebarItems = [
    { id: "1", cat: "VIDEO", catColor: T.coral, title: "Setting Up Claude Projects for Your Homeschool", grad: `linear-gradient(135deg, ${T.navy}, ${T.forest})`, isVideo: true },
    { id: "2", cat: "ESA GUIDE", catColor: T.coral, title: "Texas ESA: Getting $10,474 for Your Kids", grad: `linear-gradient(135deg, ${T.coral}, ${T.amber})` },
    { id: "3", cat: "AI FOR PARENTS", catColor: T.forest, title: "5 AI Tools My Kids Actually Use", grad: `linear-gradient(135deg, ${T.forest}, ${T.forest}aa)` },
    { id: "4", cat: "DATA", catColor: T.forest, title: "Homeschool Families Spent $2.3B on AI Tools", grad: `linear-gradient(135deg, ${T.forest}, ${T.navy})` },
    { id: "5", cat: "THE DOWNLOAD", catColor: T.navy, title: "Three New AI Ed Tools This Week", grad: `linear-gradient(135deg, ${T.muted}, ${T.navy})` },
  ];

  const productCards = [
    { href: "#quiz", bg: T.lightCoral, border: `${T.coral}33`, icon: <ClipboardCheck style={{ width: 20, height: 20, color: T.coral }} />, title: "AI Readiness Quiz", desc: "2-min quiz · Get your personalized plan", cta: "Take the Quiz →", ctaColor: T.coral },
    { href: "#directory", bg: T.lightForest, border: `${T.forest}33`, icon: <Search style={{ width: 20, height: 20, color: T.forest }} />, title: "AI Tool Directory", desc: "47 tools reviewed & compared", cta: "Browse Tools →", ctaColor: T.forest },
    { href: "#membership", bg: T.lightAmber, border: `${T.amber}4d`, icon: <Zap style={{ width: 20, height: 20, color: T.amber }} />, title: "Skip School Pro", desc: "Prompts, guides & live sessions", cta: "From $29/mo →", ctaColor: T.amber },
  ];

  return (
    <section style={{ paddingTop: 24, paddingBottom: 8 }}>
      <div style={{ maxWidth: 1400, margin: "0 auto", padding: "0 24px" }}>
        {/* Main Grid */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr", gap: 28 }} className="hero-grid">
          {/* Left Sidebar */}
          <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4, delay: 0.1 }} className="hero-sidebar">
            {sidebarItems.map((item, i) => (
              <a key={item.id} href="#" style={{ display: "flex", alignItems: "flex-start", gap: 12, padding: "12px 0", borderTop: i > 0 ? `1px solid ${T.border}66` : "none", textDecoration: "none" }}>
                <div style={{ width: 64, height: 64, flexShrink: 0, borderRadius: 8, background: item.grad, position: "relative", overflow: "hidden" }}>
                  {item.isVideo && (
                    <div style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center" }}>
                      <div style={{ width: 24, height: 24, borderRadius: "50%", background: "rgba(255,255,255,0.3)", display: "flex", alignItems: "center", justifyContent: "center" }}>
                        <Play style={{ width: 12, height: 12, color: "white", fill: "white", marginLeft: 2 }} />
                      </div>
                    </div>
                  )}
                </div>
                <div style={{ minWidth: 0, paddingTop: 2 }}>
                  <span style={{ display: "inline-flex", padding: "2px 8px", borderRadius: 4, fontSize: 10, fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase", color: "white", background: item.catColor, lineHeight: 1.4 }}>{item.cat}</span>
                  <h3 style={{ fontFamily: font.serif, fontSize: 15, fontWeight: 700, color: T.navy, lineHeight: 1.3, marginTop: 6 }} className="line-clamp-2">{item.title}</h3>
                </div>
              </a>
            ))}
          </motion.div>

          {/* Center Featured */}
          <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }} className="hero-featured">
            <a href="#" style={{ display: "block", textDecoration: "none" }}>
              <div style={{ position: "relative", aspectRatio: "4/3", width: "100%", borderRadius: 12, overflow: "hidden", marginBottom: 16, boxShadow: shadow.warm }}>
                <div style={{ width: "100%", height: "100%", background: `linear-gradient(135deg, ${T.forest}22, ${T.navy}22), linear-gradient(45deg, ${T.lightForest}, ${T.cream})`, display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <div style={{ textAlign: "center", padding: 32 }}>
                    <div style={{ fontSize: 48, marginBottom: 8 }}>🎓</div>
                    <p style={{ fontFamily: font.serif, fontSize: 18, color: T.navy, fontWeight: 600 }}>Featured Article</p>
                  </div>
                </div>
                <div style={{ position: "absolute", bottom: 12, left: 12 }}>
                  <span style={{ display: "inline-flex", padding: "4px 10px", borderRadius: 4, background: T.forest, color: "white", fontSize: 11, fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase" }}>AI For Parents</span>
                </div>
              </div>
              <h1 style={{ fontFamily: font.serif, fontSize: "clamp(20px, 2.5vw, 26px)", fontWeight: 700, color: T.navy, lineHeight: 1.25, marginBottom: 8 }}>
                How I Plan Our Entire Homeschool Week in 15 Minutes with Claude
              </h1>
              <div style={{ display: "flex", alignItems: "center", fontSize: 12, color: T.muted, fontWeight: 500 }}>
                <span style={{ color: T.navy, fontWeight: 600 }}>Ashley Larkin</span>
                <span style={{ margin: "0 6px" }}>·</span>
                <span>2 days ago</span>
                <span style={{ margin: "0 6px" }}>·</span>
                <span>6 min read</span>
              </div>
            </a>
          </motion.div>

          {/* Right: Prompt Card */}
          <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4, delay: 0.05 }} className="hero-prompt">
            <div style={{ background: T.navy, borderRadius: 12, padding: 24, height: "100%", display: "flex", flexDirection: "column", boxShadow: shadow.warmLg }}>
              <div style={{ display: "inline-flex", alignItems: "center", gap: 6, marginBottom: 16 }}>
                <Terminal style={{ width: 14, height: 14, color: T.amber }} />
                <span style={{ color: T.amber, fontSize: 11, fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase" }}>Prompt of the Week</span>
              </div>
              <h3 style={{ fontFamily: font.serif, fontSize: 18, fontWeight: 700, color: "white", lineHeight: 1.3, marginBottom: 16 }}>
                Turn Any Obsession Into a Full Week of Learning
              </h3>
              <div style={{ background: T.navyLight, border: `1px solid ${T.navyBorder}`, borderRadius: 8, padding: 16, marginBottom: 20, flexGrow: 1 }}>
                <div style={{ display: "flex", gap: 6, marginBottom: 12 }}>
                  <div style={{ width: 8, height: 8, borderRadius: "50%", background: T.coral }} />
                  <div style={{ width: 8, height: 8, borderRadius: "50%", background: T.amber }} />
                  <div style={{ width: 8, height: 8, borderRadius: "50%", background: T.forest }} />
                </div>
                <div style={{ fontFamily: "monospace", fontSize: 12, color: "white", lineHeight: 1.6 }}>
                  <p><span style={{ color: T.amber }}>You are a creative homeschool curriculum designer.</span> My child is [AGE] and is obsessed with [INTEREST].</p>
                  <p style={{ color: "rgba(255,255,255,0.6)", marginTop: 8 }}>Create a one-week unit study connecting their interest to math, science, reading, writing, and history...</p>
                </div>
              </div>
              <p style={{ color: "rgba(255,255,255,0.6)", fontSize: 14, lineHeight: 1.5, marginBottom: 20 }}>
                My 7-year-old spent three days talking about volcanoes. Instead of fighting it, I turned it into our whole week.
              </p>
              <a href="#" style={{ display: "inline-flex", alignItems: "center", gap: 8, color: T.amber, fontWeight: 700, fontSize: 14, textDecoration: "none", marginTop: "auto" }}>
                Browse 100+ prompts <ArrowRight style={{ width: 16, height: 16 }} />
              </a>
            </div>
          </motion.div>
        </div>

        {/* Product Cards Row */}
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4, delay: 0.2 }}
          style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16, marginTop: 40 }}>
          {productCards.map(c => (
            <a key={c.title} href={c.href} style={{
              display: "flex", alignItems: "center", gap: 16, padding: 20,
              background: c.bg, border: `1px solid ${c.border}`, borderRadius: 12,
              textDecoration: "none",
            }}>
              <div style={{ background: "white", padding: 10, borderRadius: 8, boxShadow: shadow.warmSm, flexShrink: 0 }}>{c.icon}</div>
              <div>
                <h3 style={{ fontFamily: font.serif, fontWeight: 700, color: T.navy, fontSize: 16, marginBottom: 2 }}>{c.title}</h3>
                <p style={{ fontSize: 14, color: `${T.navy}b3`, marginBottom: 6, lineHeight: 1.3 }}>{c.desc}</p>
                <span style={{ color: c.ctaColor, fontWeight: 700, fontSize: 14 }}>{c.cta}</span>
              </div>
            </a>
          ))}
        </motion.div>

        {/* Confidence Bar */}
        <div style={{ width: "100%", borderTop: `1px solid ${T.border}66`, padding: "12px 0", textAlign: "center", marginTop: 24 }}>
          <p style={{ fontSize: 12, color: T.muted, fontWeight: 500, letterSpacing: "0.02em" }}>
            The AI Playbook for Homeschool Parents <span style={{ margin: "0 6px", color: T.border }}>•</span> Updated daily <span style={{ margin: "0 6px", color: T.border }}>•</span> Read by 5,000+ families
          </p>
        </div>
      </div>

      <style>{`
        @media (min-width: 1024px) {
          .hero-grid { grid-template-columns: 3fr 5fr 4fr !important; }
        }
        @media (min-width: 768px) and (max-width: 1023px) {
          .hero-grid { grid-template-columns: 1fr 1fr !important; }
          .hero-sidebar { grid-column: 1 / -1; display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; }
        }
      `}</style>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   4. LATEST ARTICLES
   ═══════════════════════════════════════════════ */
function LatestArticles() {
  const articles = [
    { id: "6", title: "Three New AI Ed Tools That Launched This Week", cat: "THE DOWNLOAD", catBg: `${T.navy}b3`, catColor: "white", author: "TJ Larkin", date: "Yesterday", read: "3 min read" },
    { id: "7", title: "The Case for Letting AI Grade Your Kid's Writing", cat: "AI FOR PARENTS", catBg: T.forest, catColor: "white", author: "Ashley Larkin", date: "3 days ago", read: "5 min read" },
    { id: "2", title: "Khanmigo After 30 Days: The Good, the Frustrating, and What I'd Pay For", cat: "THE REVIEW", catBg: T.navy, catColor: "white", author: "Ashley Larkin", date: "Monday", read: "8 min read" },
    { id: "3", title: "Arizona Just Expanded Its ESA — Here's What Changed", cat: "ESA GUIDE", catBg: T.coral, catColor: "white", author: "TJ Larkin", date: "Last week", read: "4 min read" },
    { id: "4", title: "Beast Academy vs. Saxon Math: Which One Is Actually Better?", cat: "COMPARISON", catBg: T.amber, catColor: T.navy, author: "TJ Larkin", date: "2 weeks ago", read: "7 min read" },
    { id: "5", title: "What Our Homeschool Schedule Actually Looks Like (Messy Version)", cat: "BEHIND THE SCENES", catBg: `${T.navy}b3`, catColor: "white", author: "Ashley Larkin", date: "2 weeks ago", read: "6 min read" },
  ];

  return (
    <section style={{ padding: "56px 0 80px" }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 40 }}>
          <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy }}>More from Skip School</h2>
          <a href="#" style={{ color: T.forest, fontWeight: 600, textDecoration: "none" }}>All Articles →</a>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))", gap: 24 }}>
          {articles.map((a, i) => (
            <motion.a key={a.id} href="#" style={{
              display: "flex", flexDirection: "column", background: "white", borderRadius: 12,
              boxShadow: shadow.warm, border: `1px solid ${T.border}80`, textDecoration: "none", overflow: "hidden",
            }}
              initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.4, delay: i * 0.08 }}
            >
              <div style={{ padding: "24px 32px", display: "flex", flexDirection: "column", height: "100%" }}>
                <div style={{ marginBottom: 16 }}>
                  <span style={{ display: "inline-flex", padding: "4px 10px", borderRadius: 4, fontSize: 11, fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase", background: a.catBg, color: a.catColor }}>{a.cat}</span>
                </div>
                <h3 style={{ fontFamily: font.serif, fontWeight: 700, color: T.navy, lineHeight: 1.25, marginBottom: 16, fontSize: 20 }}>{a.title}</h3>
                <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", fontSize: 12, color: T.muted, fontWeight: 500, marginTop: "auto", paddingTop: 16, borderTop: `1px solid ${T.border}` }}>
                  <span style={{ color: T.navy, fontWeight: 600 }}>{a.author}</span>
                  <span style={{ margin: "0 6px" }}>·</span>
                  <span>{a.date}</span>
                  <span style={{ margin: "0 6px" }}>·</span>
                  <span>{a.read}</span>
                </div>
              </div>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   5. NEWSLETTER CTA
   ═══════════════════════════════════════════════ */
function NewsletterCTA() {
  const [focused, setFocused] = useState(false);

  return (
    <section style={{ padding: "56px 0 80px" }} id="subscribe">
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <motion.div style={{
          background: T.navy, borderRadius: 16, padding: "clamp(32px, 5vw, 64px)",
          position: "relative", overflow: "hidden", boxShadow: shadow.warmLg,
          display: "flex", flexWrap: "wrap", gap: 48, alignItems: "center",
        }}
          initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }} transition={{ duration: 0.6 }}
        >
          {/* Left: Preview */}
          <div style={{ flex: "1 1 400px", position: "relative", zIndex: 10 }}>
            <div style={{ background: T.navyLight, borderRadius: 12, padding: "clamp(24px, 3vw, 32px)", border: `1px solid ${T.navyBorder}` }}>
              <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: T.amber, color: T.navy, fontSize: 12, fontWeight: 700, padding: "4px 12px", borderRadius: 4, textTransform: "uppercase", letterSpacing: "0.05em", marginBottom: 20 }}>
                <Mail style={{ width: 14, height: 14 }} /> This Week's Issue: #47
              </div>
              <h3 style={{ fontFamily: font.serif, fontSize: "clamp(22px, 2.5vw, 28px)", fontWeight: 700, color: "white", marginBottom: 24 }}>
                Five Claude Tricks for Reluctant Writers
              </h3>
              <ul style={{ listStyle: "none", display: "flex", flexDirection: "column", gap: 12 }}>
                {[
                  'The "Interactive Fiction" prompt that got our 10yo writing for an hour',
                  "How to use AI for gentle grammar correction (without tears)",
                  "A parent's 5-minute writing warm-up routine",
                  "Tool spotlight: LittleLit's new writing module",
                ].map((item, i) => (
                  <li key={i} style={{ display: "flex", alignItems: "flex-start", gap: 12, color: "white" }}>
                    <span style={{ color: T.amber, fontWeight: 700, flexShrink: 0, marginTop: 2 }}>—</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
              <div style={{ marginTop: 24, paddingTop: 24, borderTop: `1px solid ${T.navyBorder}` }}>
                <a href="#" style={{ color: T.amber, fontWeight: 700, textDecoration: "none", fontSize: 14 }}>Read this issue →</a>
              </div>
            </div>
          </div>

          {/* Right: Signup */}
          <div style={{ flex: "1 1 400px", position: "relative", zIndex: 10 }}>
            <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 4vw, 44px)", fontWeight: 700, color: "white", marginBottom: 24, lineHeight: 1.15 }}>
              Get smarter about AI every Wednesday
            </h2>
            <p style={{ fontSize: 18, color: "rgba(255,255,255,0.75)", marginBottom: 32, lineHeight: 1.5 }}>
              Join thousands of homeschool parents. Tools, prompts, curriculum picks, ESA updates. Free forever.
            </p>
            <div style={{
              display: "flex", flexWrap: "wrap", gap: 12, padding: 6, borderRadius: 12,
              background: "white", boxShadow: focused ? `0 0 0 4px ${T.amber}80, 0 4px 24px rgba(0,0,0,0.1)` : "0 4px 12px rgba(0,0,0,0.1)",
              transition: "all 0.3s",
            }}>
              <input type="email" placeholder="your@email.com"
                onFocus={() => setFocused(true)} onBlur={() => setFocused(false)}
                style={{ flex: "1 1 200px", padding: "12px 16px", background: "transparent", border: "none", outline: "none", color: T.navy, fontSize: 16 }}
              />
              <button style={{
                background: T.amber, color: T.navy, padding: "12px 24px", borderRadius: 8,
                fontWeight: 700, fontSize: 16, border: "none", cursor: "pointer", whiteSpace: "nowrap",
              }}>Subscribe Free →</button>
            </div>
            <p style={{ fontSize: 13, color: "rgba(255,255,255,0.5)", marginTop: 24, fontWeight: 500 }}>
              No spam. Unsubscribe anytime. Read by 5,000+ families.
            </p>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   6. TOOL PICKS
   ═══════════════════════════════════════════════ */
function ToolPicks() {
  const tools = [
    { name: "Khanmigo", price: "$44/mo", rating: "4.2", cat: "AI Tutor", desc: "AI tutor from Khan Academy. Guided practice for math, science, humanities.", badge: "Free 30-Day Trial", icon: <GraduationCap style={{ width: 24, height: 24, color: T.forest }} />, iconBg: T.lightForest },
    { name: "Claude", price: "$20/mo", rating: "4.5", cat: "AI Assistant", desc: "AI assistant for lesson planning, curriculum design, and custom prompts.", badge: "We Use This Daily", icon: <MessageSquare style={{ width: 24, height: 24, color: T.navy }} />, iconBg: `${T.navy}1a` },
    { name: "LittleLit", price: "$15/mo", rating: "4.0", cat: "K-8 Platform", desc: "Full K-8 AI platform. Adaptive reading, writing, and comprehension.", badge: "New", icon: <BookOpen style={{ width: 24, height: 24, color: T.coral }} />, iconBg: T.lightCoral },
    { name: "Beast Academy", price: "$13/mo", rating: "4.6", cat: "Math", desc: "Rigorous math curriculum disguised as a comic book.", badge: "Best for Math", icon: <Calculator style={{ width: 24, height: 24, color: T.amber }} />, iconBg: T.lightAmber },
  ];

  return (
    <section style={{ padding: "56px 0 80px" }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 48, gap: 24 }}>
          <div style={{ maxWidth: 560 }}>
            <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy, marginBottom: 16 }}>What We're Using Right Now</h2>
            <p style={{ fontSize: 18, color: T.muted }}>The AI tools our family actually relies on, reviewed and tested by real homeschool parents.</p>
          </div>
          <a href="#" style={{ color: T.forest, fontWeight: 600, textDecoration: "none", flexShrink: 0 }}>Full Directory →</a>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))", gap: 24 }}>
          {tools.map((t, i) => (
            <motion.div key={t.name} style={{
              background: "white", borderRadius: 12, padding: 24, boxShadow: shadow.warm,
              border: `1px solid ${T.border}80`, display: "flex", flexDirection: "column", position: "relative",
            }}
              initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.4, delay: i * 0.1 }}
            >
              <div style={{ position: "absolute", top: 16, right: 16 }}>
                <span style={{ display: "inline-block", background: T.amber, color: T.navy, fontSize: 10, fontWeight: 700, padding: "2px 8px", borderRadius: 6, textTransform: "uppercase", letterSpacing: "0.05em" }}>{t.badge}</span>
              </div>
              <div style={{ width: 48, height: 48, borderRadius: 12, display: "flex", alignItems: "center", justifyContent: "center", background: t.iconBg, marginBottom: 24 }}>{t.icon}</div>
              <h3 style={{ fontFamily: font.serif, fontSize: 20, fontWeight: 700, color: T.navy, marginBottom: 8 }}>{t.name}</h3>
              <p style={{ color: T.muted, fontSize: 14, lineHeight: 1.5, marginBottom: 24, flexGrow: 1 }}>{t.desc}</p>
              <div style={{ paddingTop: 16, borderTop: `1px solid ${T.border}`, display: "flex", flexDirection: "column", gap: 16 }}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 14, fontWeight: 500 }}>
                  <span style={{ color: T.navy, fontWeight: 700 }}>{t.price}</span>
                  <div style={{ display: "flex", alignItems: "center", gap: 4, color: T.muted }}>
                    <Star style={{ width: 16, height: 16, fill: T.amber, color: T.amber }} />
                    <span>{t.rating}</span>
                    <span style={{ margin: "0 4px" }}>·</span>
                    <span>{t.cat}</span>
                  </div>
                </div>
                <a href="#" style={{ color: T.forest, fontWeight: 600, fontSize: 14, textDecoration: "none" }}>Read Our Review →</a>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   7. PROMPT OF THE WEEK
   ═══════════════════════════════════════════════ */
function PromptOfTheWeek() {
  return (
    <section style={{ padding: "56px 0 80px", background: T.lightForest, borderTop: `1px solid ${T.forest}1a`, borderBottom: `1px solid ${T.forest}1a` }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px", display: "flex", flexWrap: "wrap", gap: "48px 80px", alignItems: "center" }}>
        {/* Left */}
        <motion.div style={{ flex: "1 1 360px" }}
          initial={{ opacity: 0, x: -20 }} whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }} transition={{ duration: 0.6 }}
        >
          <div style={{ display: "inline-flex", alignItems: "center", gap: 8, padding: "4px 12px", borderRadius: 6, background: `${T.forest}1a`, color: T.forest, fontWeight: 700, fontSize: 12, letterSpacing: "0.05em", textTransform: "uppercase", marginBottom: 24 }}>
            <Terminal style={{ width: 16, height: 16 }} /> Prompt of the Week
          </div>
          <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy, marginBottom: 24 }}>
            Turn Any Obsession Into a Full Week of Learning
          </h2>
          <div style={{ color: T.muted, fontSize: 18, lineHeight: 1.6, marginBottom: 32 }}>
            <p style={{ marginBottom: 16 }}>My 7-year-old spent three days talking about volcanoes. Instead of fighting it, I turned it into our whole week.</p>
            <p>This prompt acts as your personal curriculum designer, taking any hyper-fixation and spinning it into a balanced, multi-subject unit study that feels like play.</p>
          </div>
          <a href="#" style={{ color: T.forest, fontWeight: 600, textDecoration: "none", fontSize: 18 }}>Browse 100+ prompts in the library →</a>
        </motion.div>

        {/* Right: Code block */}
        <motion.div style={{ flex: "1 1 420px" }}
          initial={{ opacity: 0, scale: 0.95 }} whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.2 }}
        >
          <div style={{ background: T.navy, borderRadius: 12, padding: "clamp(24px, 3vw, 32px)", boxShadow: shadow.warmLg, position: "relative" }}>
            <div style={{ display: "flex", gap: 8, marginBottom: 24 }}>
              <div style={{ width: 12, height: 12, borderRadius: "50%", background: T.coral }} />
              <div style={{ width: 12, height: 12, borderRadius: "50%", background: T.amber }} />
              <div style={{ width: 12, height: 12, borderRadius: "50%", background: T.forest }} />
            </div>
            <div style={{ fontFamily: "monospace", fontSize: "clamp(13px, 1.2vw, 16px)", color: "white", lineHeight: 1.6 }}>
              <p><span style={{ color: T.amber }}>You are a creative homeschool curriculum designer.</span> My child is [AGE] years old and is obsessed with [INTEREST].</p>
              <p style={{ marginTop: 16 }}>Create a one-week unit study connecting their interest to:</p>
              <ul style={{ listStyle: "none", paddingLeft: 16, marginTop: 8 }}>
                {["Math (real-world problems)", "Science (experiments or concepts)", "Reading (book recs at their level)", "Writing (one fun project)", "History or Geography connection"].map(item => (
                  <li key={item} style={{ display: "flex", alignItems: "flex-start", gap: 8, marginBottom: 6 }}>
                    <span style={{ color: T.amber, flexShrink: 0 }}>•</span> {item}
                  </li>
                ))}
              </ul>
              <p style={{ marginTop: 16 }}>Make it feel like play, not school. Include one field trip idea and one hands-on project.</p>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   8. THE FEED
   ═══════════════════════════════════════════════ */
function TheFeed() {
  const items = [
    { source: "WASHINGTON POST", title: "Grade Inflation Hits 30-Year High While Test Scores Keep Falling", comment: "File this under: reasons we homeschool" },
    { source: "ANTHROPIC BLOG", title: "Teach For All Partners with Anthropic to Bring AI to 100K+ Teachers", comment: "If schools are adopting it, imagine what you can do at home" },
    { source: "EDWEEK RESEARCH", title: "44% of Homeschool Families Now Use AI Tools Regularly, Up From 12% in 2023", comment: "We're ahead of the curve on this one" },
  ];

  return (
    <section style={{ padding: "56px 0 80px" }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <div style={{ marginBottom: 48, maxWidth: 560 }}>
          <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy, marginBottom: 16 }}>What We're Reading</h2>
          <p style={{ fontSize: 18, color: T.muted }}>The latest AI + education news from around the web, curated for homeschool families.</p>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: 24 }}>
          {items.map((item, i) => (
            <motion.a key={item.source} href="#" style={{
              display: "flex", flexDirection: "column", background: "white", borderRadius: 12,
              padding: "clamp(24px, 3vw, 32px)", boxShadow: shadow.warm, border: `1px solid ${T.border}80`,
              textDecoration: "none", height: "100%",
            }}
              initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.4, delay: i * 0.1 }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 16 }}>
                <span style={{ fontSize: 12, fontWeight: 700, letterSpacing: "0.05em", color: T.muted, textTransform: "uppercase" }}>{item.source}</span>
                <ExternalLink style={{ width: 16, height: 16, color: T.muted }} />
              </div>
              <h3 style={{ fontFamily: font.serif, fontSize: 20, fontWeight: 700, color: T.navy, lineHeight: 1.3, marginBottom: 24, flexGrow: 1 }}>{item.title}</h3>
              <div style={{ paddingTop: 16, borderTop: `1px solid ${T.border}`, marginTop: "auto" }}>
                <p style={{ fontSize: 14, color: T.forest, fontStyle: "italic", fontWeight: 500 }}>"{item.comment}"</p>
              </div>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   9. COMMUNITY MEMBERSHIP
   ═══════════════════════════════════════════════ */
function CommunityMembership() {
  const proFeatures = [
    "100+ ready-to-use AI prompts for every subject",
    "Step-by-step Claude & ChatGPT setup guides",
    "Member-only articles & deep dives",
    "New resources added every week",
    "Community discussion board access",
  ];
  const circleFeatures = [
    "Everything in Pro",
    "Weekly live calls with TJ & Ashley",
    "Private community chat (Circle)",
    "Direct access for questions & feedback",
    "Connect with other homeschool families",
    "Priority support & early access to new tools",
  ];

  return (
    <section style={{ padding: "56px 0 80px", background: T.lightForest, borderTop: `1px solid ${T.forest}1a`, borderBottom: `1px solid ${T.forest}1a` }} id="membership">
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <motion.div style={{ textAlign: "center", marginBottom: 48, maxWidth: 560, margin: "0 auto 48px" }}
          initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }} transition={{ duration: 0.5 }}
        >
          <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy, marginBottom: 16 }}>Go Deeper with Skip School</h2>
          <p style={{ fontSize: 18, color: `${T.navy}cc`, lineHeight: 1.5 }}>Free articles get you started. Our membership tiers give you everything you need to confidently run an AI-powered homeschool.</p>
        </motion.div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: 32, alignItems: "start" }}>
          {/* Pro Tier */}
          <motion.div style={{ background: "white", borderRadius: 12, padding: 32, boxShadow: shadow.warm, border: `1px solid ${T.border}80`, display: "flex", flexDirection: "column" }}
            initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }} transition={{ duration: 0.5 }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 24 }}>
              <div style={{ background: T.lightAmber, padding: 8, borderRadius: 12 }}><Zap style={{ width: 20, height: 20, color: T.amber }} /></div>
              <div>
                <h3 style={{ fontFamily: font.serif, fontSize: 24, fontWeight: 700, color: T.navy }}>Skip School Pro</h3>
                <p style={{ fontSize: 13, color: T.muted, fontWeight: 500 }}>For self-starters</p>
              </div>
            </div>
            <div style={{ marginBottom: 24 }}>
              <div style={{ display: "flex", alignItems: "baseline", gap: 4 }}>
                <span style={{ fontSize: 36, fontWeight: 700, color: T.navy, fontFamily: font.serif }}>$29</span>
                <span style={{ color: T.muted, fontWeight: 500 }}>/month</span>
              </div>
              <p style={{ fontSize: 13, color: T.forest, fontWeight: 600, marginTop: 4 }}>or $249/year (save 28%)</p>
            </div>
            <ul style={{ listStyle: "none", display: "flex", flexDirection: "column", gap: 12, marginBottom: 32, flexGrow: 1 }}>
              {proFeatures.map(f => (
                <li key={f} style={{ display: "flex", alignItems: "flex-start", gap: 12 }}>
                  <Check style={{ width: 20, height: 20, color: T.forest, flexShrink: 0, marginTop: 2 }} />
                  <span style={{ color: T.navy, fontWeight: 500, fontSize: 14 }}>{f}</span>
                </li>
              ))}
            </ul>
            <a href="#" style={{ display: "block", width: "100%", background: T.amber, color: T.navy, padding: "14px 0", borderRadius: 8, fontWeight: 700, textAlign: "center", textDecoration: "none" }}>Start 7-Day Free Trial →</a>
            <p style={{ fontSize: 12, color: T.muted, textAlign: "center", marginTop: 12, fontWeight: 500 }}>Cancel anytime. No questions asked.</p>
          </motion.div>

          {/* Inner Circle */}
          <motion.div style={{ background: T.navy, borderRadius: 12, padding: 32, boxShadow: shadow.warmLg, display: "flex", flexDirection: "column", position: "relative", overflow: "hidden" }}
            initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }} transition={{ duration: 0.5, delay: 0.1 }}
          >
            <div style={{ position: "absolute", top: 16, right: 16 }}>
              <span style={{ background: T.amber, color: T.navy, fontSize: 11, fontWeight: 700, padding: "4px 12px", borderRadius: 4, textTransform: "uppercase", letterSpacing: "0.05em" }}>Most Popular</span>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 24 }}>
              <div style={{ background: T.navyLight, padding: 8, borderRadius: 12 }}><Crown style={{ width: 20, height: 20, color: T.amber }} /></div>
              <div>
                <h3 style={{ fontFamily: font.serif, fontSize: 24, fontWeight: 700, color: "white" }}>Inner Circle</h3>
                <p style={{ fontSize: 13, color: "rgba(255,255,255,0.6)", fontWeight: 500 }}>For families who want it all</p>
              </div>
            </div>
            <div style={{ marginBottom: 24 }}>
              <div style={{ display: "flex", alignItems: "baseline", gap: 4 }}>
                <span style={{ fontSize: 36, fontWeight: 700, color: "white", fontFamily: font.serif }}>$99</span>
                <span style={{ color: "rgba(255,255,255,0.6)", fontWeight: 500 }}>/month</span>
              </div>
              <p style={{ fontSize: 13, color: T.amber, fontWeight: 600, marginTop: 4 }}>or $899/year (save 24%)</p>
            </div>
            <ul style={{ listStyle: "none", display: "flex", flexDirection: "column", gap: 12, marginBottom: 32, flexGrow: 1 }}>
              {circleFeatures.map(f => (
                <li key={f} style={{ display: "flex", alignItems: "flex-start", gap: 12 }}>
                  <Check style={{ width: 20, height: 20, color: T.amber, flexShrink: 0, marginTop: 2 }} />
                  <span style={{ color: "white", fontWeight: 500, fontSize: 14 }}>{f}</span>
                </li>
              ))}
            </ul>
            <a href="#" style={{ display: "block", width: "100%", background: T.amber, color: T.navy, padding: "14px 0", borderRadius: 8, fontWeight: 700, textAlign: "center", textDecoration: "none" }}>Join Inner Circle →</a>
            <p style={{ fontSize: 12, color: "rgba(255,255,255,0.5)", textAlign: "center", marginTop: 12, fontWeight: 500 }}>Limited spots. 7-day free trial.</p>
          </motion.div>

          {/* Testimonials */}
          <motion.div style={{ display: "flex", flexDirection: "column", gap: 24 }}
            initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }} transition={{ duration: 0.5, delay: 0.2 }}
          >
            {[
              { quote: "I was completely overwhelmed by AI until I found Skip School. The prompt library alone saved me hours every week. And the community? These are MY people.", name: "Jessica M.", detail: "3 kids in Florida · Inner Circle member", color: T.coral },
              { quote: "The live calls are worth 10x the price. Last week TJ walked me through setting up Claude for our entire science curriculum in 20 minutes.", name: "David R.", detail: "2 kids in Texas · Inner Circle member", color: T.forest },
            ].map(t => (
              <div key={t.name} style={{ background: "white", borderRadius: 12, padding: 32, boxShadow: shadow.warm, border: `1px solid ${T.border}80`, position: "relative" }}>
                <div style={{ color: T.amber, fontSize: 48, fontFamily: font.serif, position: "absolute", top: 16, left: 20, opacity: 0.2, lineHeight: 1 }}>"</div>
                <p style={{ fontSize: 18, color: T.navy, fontWeight: 500, fontStyle: "italic", lineHeight: 1.5, marginBottom: 24, position: "relative", zIndex: 1 }}>{t.quote}</p>
                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                  <div style={{ width: 40, height: 40, borderRadius: "50%", background: t.color, color: "white", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 700, fontSize: 14 }}>
                    {t.name.split(" ").map(n => n[0]).join("")}
                  </div>
                  <div>
                    <div style={{ fontWeight: 700, color: T.navy }}>{t.name}</div>
                    <div style={{ fontSize: 12, color: T.muted, fontWeight: 500 }}>{t.detail}</div>
                  </div>
                </div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   10. AI READINESS QUIZ CTA
   ═══════════════════════════════════════════════ */
function AIReadinessQuiz() {
  return (
    <section style={{ padding: "32px 24px", maxWidth: 1280, margin: "0 auto", width: "100%" }} id="quiz">
      <motion.div style={{
        background: T.lightCoral, borderRadius: 12, padding: "clamp(24px, 4vw, 40px)",
        border: `1px solid ${T.coral}33`, boxShadow: shadow.warm,
        display: "flex", flexWrap: "wrap", alignItems: "center", justifyContent: "space-between", gap: 32,
        position: "relative", overflow: "hidden",
      }}
        initial={{ opacity: 0, scale: 0.98 }} whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true }} transition={{ duration: 0.5 }}
      >
        <div style={{ position: "absolute", right: 0, top: 0, width: 256, height: 256, background: `${T.coral}1a`, borderRadius: "50%", filter: "blur(48px)", transform: "translate(25%, -50%)" }} />
        <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 24, position: "relative", zIndex: 1 }}>
          <div style={{ background: "white", padding: 16, borderRadius: 12, boxShadow: shadow.warmSm, flexShrink: 0 }}>
            <ClipboardCheck style={{ width: 32, height: 32, color: T.coral }} />
          </div>
          <div>
            <h2 style={{ fontFamily: font.serif, fontSize: "clamp(22px, 2.5vw, 28px)", fontWeight: 700, color: T.navy, marginBottom: 8 }}>What's Your AI Readiness Score?</h2>
            <p style={{ color: `${T.navy}cc`, fontSize: 18, maxWidth: 560 }}>2-minute quiz. Find out which AI tools match your family's needs and get a personalized setup plan.</p>
          </div>
        </div>
        <a href="#" style={{
          display: "inline-flex", alignItems: "center", gap: 8, background: T.coral,
          color: "white", padding: "16px 32px", borderRadius: 8, fontWeight: 700, fontSize: 18,
          textDecoration: "none", position: "relative", zIndex: 1, flexShrink: 0,
        }}>
          Take the Quiz <ArrowRight style={{ width: 20, height: 20 }} />
        </a>
      </motion.div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   11. DIRECTORY BROWSE
   ═══════════════════════════════════════════════ */
function DirectoryBrowse() {
  const cats = [
    { name: "AI Tutoring", count: "24 listings", icon: <GraduationCap style={{ width: 24, height: 24, color: "white" }} />, bg: T.forest },
    { name: "Curriculum", count: "47 listings", icon: <BookOpen style={{ width: 24, height: 24, color: "white" }} />, bg: T.navy },
    { name: "Enrichment", count: "83 listings", icon: <Palette style={{ width: 24, height: 24, color: "white" }} />, bg: T.coral },
    { name: "ESA-Approved", count: "31 listings", icon: <BadgeCheck style={{ width: 24, height: 24, color: T.navy }} />, bg: T.amber },
    { name: "Testing", count: "16 listings", icon: <ClipboardList style={{ width: 24, height: 24, color: "white" }} />, bg: T.muted },
    { name: "Co-ops", count: "26 listings", icon: <Users style={{ width: 24, height: 24, color: "white" }} />, bg: T.forest },
  ];

  return (
    <section style={{ padding: "56px 0 80px" }} id="directory">
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 40, gap: 16 }}>
          <h2 style={{ fontFamily: font.serif, fontSize: "clamp(28px, 3vw, 36px)", fontWeight: 700, color: T.navy }}>Browse the Directory</h2>
          <a href="#" style={{ color: T.forest, fontWeight: 600, textDecoration: "none" }}>Full Directory →</a>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(160px, 1fr))", gap: 20 }}>
          {cats.map((c, i) => (
            <motion.a key={c.name} href="#" style={{
              display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center",
              background: "white", borderRadius: 12, padding: 24, boxShadow: shadow.warm,
              border: `1px solid ${T.border}80`, textDecoration: "none",
            }}
              initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.4, delay: i * 0.05 }}
            >
              <div style={{ width: 56, height: 56, borderRadius: 12, display: "flex", alignItems: "center", justifyContent: "center", background: c.bg, marginBottom: 16, boxShadow: shadow.warmSm }}>{c.icon}</div>
              <h3 style={{ fontFamily: font.serif, fontWeight: 700, color: T.navy, marginBottom: 4 }}>{c.name}</h3>
              <p style={{ fontSize: 14, color: T.muted, fontWeight: 500 }}>{c.count}</p>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════
   12. FOOTER
   ═══════════════════════════════════════════════ */
function Footer() {
  const cols = [
    { title: "Articles", links: ["AI For Parents", "Tool Reviews", "ESA Guides", "Curriculum"] },
    { title: "Tools & Community", links: ["AI Directory", "Prompt Library", "Join Community", "AI Readiness Quiz"] },
    { title: "Company", links: ["About Us", "Newsletter", "Contact", "Sponsor"] },
  ];

  return (
    <footer style={{ background: T.navy, color: "white", paddingTop: 80, paddingBottom: 40, borderTop: `4px solid ${T.amber}` }}>
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 48, marginBottom: 64 }}>
          {/* Brand */}
          <div style={{ gridColumn: "span 1" }} className="footer-brand">
            <div style={{ marginBottom: 24 }}><LogoMark inverted height={32} /></div>
            <p style={{ color: "rgba(255,255,255,0.6)", fontSize: 18, maxWidth: 320, marginBottom: 32, fontFamily: font.serif, fontStyle: "italic" }}>
              The AI Playbook for Homeschool Parents
            </p>
            <div style={{ display: "flex", gap: 12 }}>
              {[Twitter, Instagram, Youtube].map((Icon, i) => (
                <a key={i} href="#" style={{ width: 40, height: 40, borderRadius: 8, background: "rgba(255,255,255,0.1)", display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <Icon style={{ width: 20, height: 20, color: "white" }} />
                </a>
              ))}
            </div>
          </div>

          {cols.map(col => (
            <div key={col.title}>
              <h4 style={{ fontWeight: 700, marginBottom: 24, textTransform: "uppercase", letterSpacing: "0.1em", fontSize: 13 }}>{col.title}</h4>
              <ul style={{ listStyle: "none", display: "flex", flexDirection: "column", gap: 16 }}>
                {col.links.map(l => (
                  <li key={l}><a href="#" style={{ color: "rgba(255,255,255,0.6)", textDecoration: "none" }}>{l}</a></li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div style={{ paddingTop: 32, borderTop: "1px solid rgba(255,255,255,0.1)", display: "flex", flexWrap: "wrap", justifyContent: "space-between", alignItems: "center", gap: 16, fontSize: 14, color: "rgba(255,255,255,0.4)" }}>
          <p>© {new Date().getFullYear()} Skip School. All rights reserved.</p>
          <div style={{ display: "flex", gap: 24 }}>
            <a href="#" style={{ color: "rgba(255,255,255,0.4)", textDecoration: "none" }}>Privacy Policy</a>
            <a href="#" style={{ color: "rgba(255,255,255,0.4)", textDecoration: "none" }}>Terms of Service</a>
          </div>
        </div>
      </div>

      <style>{`
        @media (min-width: 1024px) { .footer-brand { grid-column: span 2 !important; } }
      `}</style>
    </footer>
  );
}

/* ═══════════════════════════════════════════════
   APP ROOT
   ═══════════════════════════════════════════════ */
export default function App() {
  return (
    <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column", width: "100%", background: T.cream, color: T.text, fontFamily: font.sans }}>
      <GlobalStyles />
      <Navigation />
      <SponsorBar />
      <main style={{ flexGrow: 1, display: "flex", flexDirection: "column" }}>
        <HeroGrid />
        <LatestArticles />
        <NewsletterCTA />
        <ToolPicks />
        <PromptOfTheWeek />
        <TheFeed />
        <CommunityMembership />
        <AIReadinessQuiz />
        <DirectoryBrowse />
      </main>
      <Footer />
    </div>
  );
}
