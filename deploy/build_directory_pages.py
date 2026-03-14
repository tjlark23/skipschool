#!/usr/bin/env python3
"""Build brand/directory pages for Skip School tool directory."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

SRC = os.path.join(os.path.dirname(__file__), '..', 'site', 'files', 'src')
DEPLOY = os.path.dirname(__file__)

# Load nav and footer snippets (with base64 logos)
with open(os.path.join(DEPLOY, 'nav_snippet.txt'), 'r', encoding='utf-8') as f:
    NAV_HTML = f.read()
with open(os.path.join(DEPLOY, 'footer_snippet.txt'), 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read()

# CSS from khan-academy-page (the <style> block)
CSS = """:root { --navy: #0d203b; --yellow: #fbc926; --cream: #fdf8ef; --warm-white: #faf9f7; --sand: #f0ebe3; --text: #1a1a1a; --text-mid: #444; --text-light: #777; --border: #d8d3cb; --border-light: #e8e4de; --max: 1280px; --green: #16a34a; --coral: #ef4444; }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family: 'DM Sans', -apple-system, sans-serif; background: var(--warm-white); color: var(--text); -webkit-font-smoothing: antialiased; }
        a { color: inherit; text-decoration: none; }
        .wrap { max-width: var(--max); margin: 0 auto; padding: 0 20px; }
        .nav { background: #fff; border-bottom: 3px solid var(--navy); position: sticky; top: 0; z-index: 100; }
        .nav .wrap { display: flex; align-items: center; justify-content: space-between; padding-top: 8px; padding-bottom: 8px; }
        .nav-left { display: flex; align-items: center; gap: 14px; }
        .nav-logo img { height: 28px; }
        .nav-tagline { font-size: 12px; color: var(--text-light); padding-left: 14px; border-left: 1.5px solid var(--border); }
        .nav-right { display: flex; align-items: center; gap: 20px; }
        .nav-right a { font-size: 13px; font-weight: 600; color: var(--text-mid); }
        .nav-sub { background: var(--navy) !important; color: #fff !important; padding: 7px 16px; border-radius: 5px; }
        .sponsor-bar { background: var(--yellow); color: var(--navy); padding: 9px 20px; font-size: 13px; text-align: center; }
        .sponsor-tag { background: var(--navy); color: var(--yellow); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 2px 7px; border-radius: 2px; margin-right: 6px; }
        .sponsor-bar a { color: var(--navy); font-weight: 700; text-decoration: underline; }
        .brand-header { background: var(--navy); padding: 28px 0 32px; }
        .brand-crumb { font-size: 12px; color: rgba(255,255,255,0.4); margin-bottom: 14px; }
        .brand-crumb a { color: var(--yellow); }
        .brand-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 32px; }
        .brand-title-area h1 { font-family: 'Fraunces', serif; font-size: 32px; font-weight: 900; color: #fff; margin-bottom: 6px; }
        .brand-subtitle { font-size: 15px; color: rgba(255,255,255,0.65); max-width: 500px; line-height: 1.5; }
        .brand-rating { display: flex; align-items: center; gap: 8px; margin-top: 10px; }
        .brand-score { font-family: 'Fraunces', serif; font-size: 28px; font-weight: 900; color: var(--yellow); }
        .brand-score-label { font-size: 12px; color: rgba(255,255,255,0.5); }
        .brand-cta-area { flex-shrink: 0; text-align: right; }
        .brand-visit { display: inline-block; padding: 11px 24px; background: var(--yellow); color: var(--navy); border-radius: 6px; font-weight: 700; font-size: 14px; margin-bottom: 6px; }
        .brand-visit:hover { transform: translateY(-1px); }
        .brand-free { font-size: 12px; color: rgba(255,255,255,0.45); }
        .product-layout { display: grid; grid-template-columns: 1fr 340px; gap: 32px; padding: 28px 0; }
        .sidebar { position: sticky; top: 60px; align-self: start; }
        .quick-card { background: #fff; border: 1.5px solid var(--border-light); border-radius: 10px; overflow: hidden; }
        .quick-card-head { background: var(--navy); padding: 14px 18px; }
        .quick-card-head h3 { font-family: 'Fraunces', serif; font-size: 15px; font-weight: 800; color: #fff; }
        .quick-card-body { padding: 16px 18px; }
        .qf-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid var(--border-light); font-size: 13px; }
        .qf-row:last-child { border-bottom: none; }
        .qf-label { color: var(--text-light); }
        .qf-value { font-weight: 600; color: var(--navy); text-align: right; }
        .qf-value.free { color: var(--green); }
        .sidebar-cta { display: block; width: 100%; padding: 12px; background: var(--navy); color: #fff; border: none; border-radius: 6px; font-weight: 700; font-size: 14px; text-align: center; margin-top: 12px; font-family: inherit; cursor: pointer; text-decoration: none; }
        .sidebar-link { display: block; text-align: center; font-size: 12px; color: var(--text-light); margin-top: 8px; }
        .sidebar-link a { color: var(--navy); font-weight: 600; border-bottom: 1px solid var(--yellow); }
        .main { }
        .main h2 { font-family: 'Fraunces', serif; font-size: 22px; font-weight: 800; color: var(--navy); margin: 28px 0 12px; }
        .main h2:first-child { margin-top: 0; }
        .main p { font-size: 15px; line-height: 1.7; color: var(--text-mid); margin-bottom: 14px; }
        .feat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0 24px; }
        .feat-block { background: var(--cream); border-radius: 8px; padding: 14px 16px; }
        .feat-block h4 { font-size: 14px; font-weight: 700; color: var(--navy); margin-bottom: 3px; }
        .feat-block p { font-size: 13px; color: var(--text-mid); line-height: 1.45; margin-bottom: 0; }
        .pc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0 24px; }
        .pc-col { background: #fff; border: 1.5px solid var(--border-light); border-radius: 8px; padding: 16px; }
        .pc-col h4 { font-size: 13px; font-weight: 700; margin-bottom: 10px; }
        .pc-col h4.pro { color: var(--green); }
        .pc-col h4.con { color: var(--coral); }
        .pc-item { font-size: 13px; color: var(--text-mid); line-height: 1.5; padding: 4px 0 4px 16px; position: relative; }
        .pc-item::before { content: ''; position: absolute; left: 0; top: 10px; width: 6px; height: 6px; border-radius: 50%; }
        .pc-col .pc-item::before { background: var(--green); }
        .pc-col:last-child .pc-item::before { background: var(--coral); }
        .callout { background: var(--cream); border-left: 4px solid var(--yellow); border-radius: 0 8px 8px 0; padding: 18px 20px; margin: 20px 0; }
        .callout h4 { font-size: 14px; font-weight: 700; color: var(--navy); margin-bottom: 6px; }
        .callout p { font-size: 14px; color: var(--text-mid); line-height: 1.6; margin-bottom: 0; }
        .footer { background: #0a1828; color: rgba(255,255,255,0.55); padding: 32px 0; }
        .footer .wrap { display: flex; justify-content: space-between; gap: 32px; }
        .footer-brand img { height: 28px; margin-bottom: 8px; }
        .footer-brand p { font-size: 12.5px; max-width: 260px; line-height: 1.5; }
        .footer-col h4 { color: var(--yellow); font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
        .footer-col a { display: block; font-size: 12.5px; margin-bottom: 5px; opacity: 0.6; }
        .footer-bottom { margin-top: 20px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 11px; opacity: 0.35; }
        .similar-section { background: #fff; padding: 36px 0; }
        .similar-header { display:flex;align-items:center;gap:12px;margin-bottom:18px; }
        .similar-title { font-family:'Fraunces',serif;font-size:14px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.07em; }
        .similar-line { flex:1;height:1.5px;background:var(--border); }
        .similar-grid { display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px; }
        .sim-card { background:#fff;border:1.5px solid var(--border-light);border-radius:8px;overflow:hidden;transition:border-color 0.2s,transform 0.15s;text-decoration:none;color:inherit; }
        .sim-card:hover { border-color:var(--navy);transform:translateY(-2px); }
        .sim-img { height:120px;position:relative;display:flex;align-items:center;justify-content:center; }
        .sim-tag { position:absolute;top:10px;left:10px;font-size:10px;font-weight:700;color:#fff;text-transform:uppercase;padding:2px 7px;border-radius:3px;background:rgba(0,0,0,0.35); }
        .sim-body { padding:12px 14px; }
        .sim-body h3 { font-family:'Fraunces',serif;font-size:15px;font-weight:700;color:var(--navy);margin-bottom:2px; }
        .sim-price { font-size:12px;color:var(--green);font-weight:600;margin-bottom:4px; }
        .sim-body p { font-size:12px;color:var(--text-mid);line-height:1.4; }
        .faq-section { padding: 28px 0; }
        .faq-section h2 { font-family:'Fraunces',serif; font-size:22px; font-weight:800; color:var(--navy); margin-bottom:16px; }
        .faq-item { background:#fff; border:1.5px solid var(--border-light); border-radius:8px; padding:16px 20px; margin-bottom:10px; }
        .faq-item h3 { font-size:15px; font-weight:700; color:var(--navy); margin-bottom:6px; }
        .faq-item p { font-size:14px; color:var(--text-mid); line-height:1.6; margin:0; }
        @media (max-width: 900px) {
            .product-layout { grid-template-columns: 1fr; }
            .brand-top { flex-direction: column; }
            .feat-grid, .pc-grid { grid-template-columns: 1fr; }
            .similar-grid { grid-template-columns: 1fr; }
        }"""

# ---- BRAND DATA ----
BRANDS = [
    {
        "slug": "ixl-page",
        "title": "IXL for Homeschool",
        "meta_title": "IXL for Homeschool | Skip School Directory",
        "meta_desc": "Honest review of IXL for homeschool families. Adaptive math and ELA practice, diagnostic assessments, and parent reporting. See pricing, pros, cons, and our rating.",
        "h1": "IXL Learning",
        "subtitle": "Adaptive math and ELA practice with real-time diagnostics. Covers K-12 across multiple subjects with detailed parent reporting.",
        "rating": "4.3",
        "url": "https://www.ixl.com",
        "cta_text": "Try IXL Free",
        "cta_note": "Free trial available",
        "category": "Adaptive Practice",
        "features": [
            ("Adaptive Math Practice", "K-12 math with questions that adjust to your child's level in real time."),
            ("Diagnostic Assessments", "Pinpoints exactly where your child is grade-level in each skill area."),
            ("Parent Reporting", "Weekly email reports and a dashboard showing skill mastery across subjects."),
            ("ELA + More Subjects", "Covers language arts, science, and social studies in addition to math."),
        ],
        "best_for_p1": "<strong>Filling specific skill gaps.</strong> The diagnostic tool identifies exactly where your child needs work, then serves targeted practice. Great for kids who are strong overall but have pockets of weakness.",
        "best_for_p2": "<strong>Structured daily practice.</strong> IXL works best as a 15-20 minute daily drill supplement, not a full curriculum. The adaptive difficulty keeps kids in their zone of proximal development.",
        "pros": ["Excellent diagnostic tool", "Covers K-12 math and ELA", "Adaptive difficulty works well", "Detailed parent reports", "Aligned to state standards"],
        "cons": ["Can feel repetitive", "Not a full curriculum", "Subscription cost adds up", "Gamification is minimal"],
        "callout": "We use IXL as a gap-filler, not a primary curriculum. After Khan Academy math, our daughter does 15 minutes of IXL practice targeting the skills the diagnostic flagged. It is one of the best tools for pinpointing and closing specific gaps.",
        "quick_facts": [
            ("Price", "$9.95/mo per subject", ""),
            ("Family Plan", "$19.95/mo all subjects", ""),
            ("Ages", "K-12", ""),
            ("Best For", "Math + ELA Practice", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "Yes", ""),
            ("ESA Eligible", "Yes, in most states", ""),
        ],
        "sidebar_cta_text": "Start IXL Free Trial",
        "sidebar_link_text": "Read our math tools guide",
        "sidebar_link_url": "21-ai-math-help",
        "similar": [("khan-academy-page", "Khan Academy", "Free / $44 yr", "Complete K-12 math + AI tutor.", "AI Platform"),
                     ("mathway-page", "Mathway", "Free / $9.99 mo", "Step-by-step math problem solver.", "Math Tool"),
                     ("prodigy-page", "Prodigy Math", "Free / $8.95 mo", "Game-based math practice for K-8.", "Math Game")],
        "faqs": [
            ("Is IXL worth it for homeschool?", "IXL is a strong supplement for targeted math and ELA practice, especially when used alongside a primary curriculum. The diagnostic tool alone justifies the cost for many families because it identifies exact skill gaps."),
            ("Can IXL replace a full math curriculum?", "IXL works best as a practice tool, not a standalone curriculum. It does not teach new concepts through lessons. Pair it with a teaching curriculum like Khan Academy, Math-U-See, or Saxon for the best results."),
            ("How much does IXL cost for homeschool families?", "IXL costs $9.95 per month for a single subject or $19.95 per month for all subjects. Annual plans offer a discount. There is no separate homeschool pricing, but the family plan covers all subjects for one child."),
        ],
    },
    {
        "slug": "duolingo-page",
        "title": "Duolingo for Homeschool",
        "meta_title": "Duolingo for Homeschool | Skip School Directory",
        "meta_desc": "Review of Duolingo for homeschool language learning. Free gamified lessons in 40+ languages, AI-powered practice, and family features. Our honest rating and tips.",
        "h1": "Duolingo",
        "subtitle": "Free gamified language learning in 40+ languages. Short daily lessons, AI conversation practice, and streak-based motivation that kids actually stick with.",
        "rating": "4.5",
        "url": "https://www.duolingo.com",
        "cta_text": "Start Duolingo Free",
        "cta_note": "Free forever. No credit card.",
        "category": "Language Learning",
        "features": [
            ("40+ Languages", "From Spanish to Korean to Latin. Far more options than any textbook curriculum."),
            ("Gamified Lessons", "XP, streaks, leagues, and characters keep kids engaged and coming back daily."),
            ("AI Conversation", "Duolingo Max includes AI roleplay practice for realistic speaking scenarios."),
            ("Duolingo for Schools", "Free teacher/parent dashboard to assign lessons and track progress."),
        ],
        "best_for_p1": "<strong>Daily language maintenance.</strong> Duolingo excels at building vocabulary and basic grammar through consistent short practice. The streak system creates a habit loop that works especially well for elementary and middle schoolers.",
        "best_for_p2": "<strong>Introduction to a new language.</strong> Great for kids who want to explore a language before committing to a full curriculum. The low-pressure, game-like format removes anxiety about making mistakes.",
        "pros": ["Completely free core app", "40+ language options", "Streak system builds habits", "Duolingo for Schools dashboard", "AI conversation practice (Max)"],
        "cons": ["Not deep enough alone for fluency", "Limited grammar explanations", "Ads on free tier", "Repetitive at higher levels"],
        "callout": "Both our kids do Duolingo Spanish every morning before formal lessons start. It takes 5-10 minutes and gets their brains warmed up. We pair it with Spanish podcasts and conversation practice for a fuller language experience.",
        "quick_facts": [
            ("Price", "Free", "free"),
            ("Super Duolingo", "$6.99/mo", ""),
            ("Ages", "5+", ""),
            ("Best For", "Language Practice", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "Yes (paid)", ""),
            ("Parent Tools", "Yes (Schools)", ""),
            ("ESA Eligible", "No (free app)", ""),
        ],
        "sidebar_cta_text": "Try Duolingo Free",
        "sidebar_link_text": "Read our language guide",
        "sidebar_link_url": "32-ai-foreign-language",
        "similar": [("rosetta-stone-page", "Rosetta Stone", "$11.99/mo", "Immersive language learning.", "Language"),
                     ("babbel-page", "Babbel", "$6.95/mo", "Conversation-focused language lessons.", "Language"),
                     ("khan-academy-page", "Khan Academy", "Free / $44 yr", "Complete K-12 learning platform.", "AI Platform")],
        "faqs": [
            ("Is Duolingo enough for homeschool language credit?", "Duolingo alone is unlikely to satisfy a full high school language credit. However, combined with conversation practice, reading, and writing exercises, it can serve as the daily practice component of a well-rounded language program."),
            ("What age can kids start Duolingo?", "Duolingo works for kids as young as 5-6 with parent help. The Duolingo ABC app is designed specifically for younger learners. Most kids can use the main app independently by age 8-9."),
            ("Is Duolingo Super worth the cost for homeschoolers?", "Super Duolingo removes ads and adds offline access, which is helpful for homeschool families who do lessons in the car or without reliable internet. The free version is fully functional for learning, though."),
        ],
    },
    {
        "slug": "outschool-page",
        "title": "Outschool for Homeschool",
        "meta_title": "Outschool for Homeschool | Skip School Directory",
        "meta_desc": "Honest review of Outschool for homeschool families. Live online classes in every subject, taught by independent teachers. Pricing, pros, cons, and our rating.",
        "h1": "Outschool",
        "subtitle": "Live online classes taught by independent teachers across every subject. One-time sessions, multi-week courses, and ongoing clubs for ages 3-18.",
        "rating": "4.4",
        "url": "https://outschool.com",
        "cta_text": "Browse Outschool Classes",
        "cta_note": "Pay per class. No subscription.",
        "category": "Live Classes",
        "features": [
            ("Live Video Classes", "Real teachers on Zoom-style video. Small groups typically 3-12 students."),
            ("Huge Course Catalog", "200,000+ classes covering every subject, hobby, and interest imaginable."),
            ("Flexible Scheduling", "One-time sessions, multi-week courses, or ongoing weekly clubs."),
            ("Social Connection", "Kids interact with peers, building friendships beyond the homeschool bubble."),
        ],
        "best_for_p1": "<strong>Socialization and peer learning.</strong> Outschool solves the \"but what about socialization?\" question better than almost anything else. Kids interact with same-age peers who share their interests in structured, teacher-led settings.",
        "best_for_p2": "<strong>Subjects you cannot teach yourself.</strong> Advanced math, foreign languages, coding, art techniques, and niche interests like marine biology or creative writing. Outschool lets your child learn from specialists.",
        "pros": ["Massive course variety", "No subscription required", "Great for socialization", "ESA-eligible in many states", "Quality varies but reviews help"],
        "cons": ["Per-class costs add up fast", "Teacher quality varies widely", "Scheduling can be tricky", "No integrated curriculum path"],
        "callout": "We use Outschool for two things: a weekly creative writing club (socialization + writing practice) and a monthly science experiment class. Total cost runs about $80-100/month, but both kids look forward to it all week.",
        "quick_facts": [
            ("Price", "$10-40 per class", ""),
            ("Subscription", "None required", ""),
            ("Ages", "3-18", ""),
            ("Best For", "Electives + Social", ""),
            ("Platform", "Web (Zoom-based)", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "Basic dashboard", ""),
            ("ESA Eligible", "Yes, widely accepted", ""),
        ],
        "sidebar_cta_text": "Browse Classes on Outschool",
        "sidebar_link_text": "Read our co-op guide",
        "sidebar_link_url": "24-homeschool-co-op-guide",
        "similar": [("khan-academy-page", "Khan Academy", "Free / $44 yr", "Self-paced K-12 learning.", "AI Platform"),
                     ("ixl-page", "IXL", "$9.95/mo", "Adaptive practice platform.", "Practice"),
                     ("duolingo-page", "Duolingo", "Free / $6.99 mo", "Gamified language learning.", "Language")],
        "faqs": [
            ("Is Outschool worth it for homeschool?", "Outschool is worth it for specific needs: socialization, subjects you cannot teach, and enrichment. It is not cost-effective as a primary curriculum for all subjects. Most families use it selectively for 1-3 classes per week."),
            ("Can you use ESA funds on Outschool?", "Yes, Outschool is approved for ESA spending in most states that offer education savings accounts, including Arizona, Florida, and others. Check your specific state's approved vendor list."),
            ("How do you find good Outschool teachers?", "Filter by reviews and number of students taught. Look for teachers with 100+ reviews and 4.8+ ratings. Read recent reviews specifically, and try a one-time class before committing to multi-week courses."),
        ],
    },
    {
        "slug": "chatgpt-homeschool-page",
        "title": "ChatGPT for Homeschool",
        "meta_title": "ChatGPT for Homeschool | Skip School Directory",
        "meta_desc": "How to use ChatGPT for homeschooling. Lesson planning, custom worksheets, tutoring, and curriculum design. Our honest review with pricing and best practices.",
        "h1": "ChatGPT (OpenAI)",
        "subtitle": "The most widely used AI assistant for homeschool lesson planning, custom worksheet generation, tutoring support, and curriculum design.",
        "rating": "4.6",
        "url": "https://chat.openai.com",
        "cta_text": "Try ChatGPT Free",
        "cta_note": "Free tier available. Plus is $20/mo.",
        "category": "AI Assistant",
        "features": [
            ("Lesson Planning", "Generate full lesson plans for any subject, grade level, and teaching style in seconds."),
            ("Custom Worksheets", "Create printable worksheets, quizzes, and activities tailored to your child's level."),
            ("Tutoring Support", "Explain concepts step-by-step in ways your child understands. Patient and endlessly available."),
            ("Curriculum Design", "Build full semester or year plans aligned to standards or your preferred method."),
        ],
        "best_for_p1": "<strong>Parents who want a teaching assistant.</strong> ChatGPT acts like having a knowledgeable co-teacher available 24/7. Ask it to explain fractions five different ways, generate a week of history discussion questions, or create a reading list for your reluctant reader.",
        "best_for_p2": "<strong>Customizing materials to your child.</strong> Instead of using one-size-fits-all worksheets, ChatGPT lets you create resources that match your child's exact interests, reading level, and learning style.",
        "pros": ["Free tier is powerful enough", "Incredible versatility", "Creates custom materials instantly", "Works for all subjects and ages", "Constantly improving"],
        "cons": ["Can produce inaccurate info", "No built-in curriculum structure", "Requires parent skill to prompt well", "No parent dashboard or tracking"],
        "callout": "ChatGPT is our most-used homeschool tool after Khan Academy. We use it to generate weekly spelling lists based on our daughter's reading book, create math word problems about topics she loves (horses), and plan our history unit studies. The key is learning to write good prompts.",
        "quick_facts": [
            ("Price", "Free", "free"),
            ("ChatGPT Plus", "$20/mo", ""),
            ("Ages", "All (parent-guided)", ""),
            ("Best For", "Lesson Planning", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "No", ""),
            ("ESA Eligible", "No", ""),
        ],
        "sidebar_cta_text": "Try ChatGPT Free",
        "sidebar_link_text": "Read our AI prompts guide",
        "sidebar_link_url": "50-ai-prompts-homeschool",
        "similar": [("claude-homeschool-page", "Claude", "Free / $20 mo", "Thoughtful AI for long-form planning.", "AI Assistant"),
                     ("khan-academy-page", "Khan Academy", "Free / $44 yr", "K-12 learning with AI tutor.", "AI Platform"),
                     ("ixl-page", "IXL", "$9.95/mo", "Adaptive math and ELA practice.", "Practice")],
        "faqs": [
            ("Is ChatGPT safe for kids to use directly?", "ChatGPT is designed for users 13+ and younger children should use it with parent supervision. For homeschool, we recommend parents use ChatGPT to create materials rather than having young children interact with it directly."),
            ("What is the best ChatGPT model for homeschool?", "The free GPT-4o model handles most homeschool tasks well. ChatGPT Plus ($20/mo) gives you faster responses and longer conversations, which helps when planning full curriculum units or generating lots of materials."),
            ("How do I write good homeschool prompts for ChatGPT?", "Be specific about grade level, subject, teaching method, and output format. Instead of 'teach fractions,' try 'Create 10 fraction word problems for a 4th grader who loves animals, with answer key.' Our 50 AI Prompts guide has ready-to-use templates."),
        ],
    },
    {
        "slug": "claude-homeschool-page",
        "title": "Claude for Homeschool",
        "meta_title": "Claude AI for Homeschool | Skip School Directory",
        "meta_desc": "How to use Claude AI for homeschooling. Long-form lesson plans, curriculum design, and nuanced tutoring. Our honest review comparing Claude to ChatGPT for homeschool.",
        "h1": "Claude (Anthropic)",
        "subtitle": "A thoughtful AI assistant that excels at long-form curriculum planning, nuanced subject explanations, and creating structured educational materials.",
        "rating": "4.7",
        "url": "https://claude.ai",
        "cta_text": "Try Claude Free",
        "cta_note": "Free tier available. Pro is $20/mo.",
        "category": "AI Assistant",
        "features": [
            ("Long-Form Planning", "Generates detailed, multi-week curriculum plans without losing coherence or quality."),
            ("Nuanced Explanations", "Explains complex topics with age-appropriate depth and multiple perspectives."),
            ("Structured Materials", "Creates well-organized lesson plans, rubrics, and assessment frameworks."),
            ("Research Synthesis", "Summarizes educational approaches and helps you choose the right method for your family."),
        ],
        "best_for_p1": "<strong>Detailed curriculum design.</strong> Claude's longer context window and thoughtful responses make it ideal for building out full semester plans, unit studies, and scope-and-sequence documents. It handles complex planning tasks without losing track of details.",
        "best_for_p2": "<strong>Nuanced subject tutoring.</strong> When your child asks \"why\" questions that go deeper than surface level, Claude provides thoughtful, balanced explanations. It is particularly strong for writing instruction, history analysis, and philosophical discussions.",
        "pros": ["Excellent for long-form planning", "More thoughtful and nuanced answers", "Strong writing and humanities support", "Free tier is generous", "Less likely to hallucinate facts"],
        "cons": ["Smaller ecosystem than ChatGPT", "No image generation built in", "No mobile app (web only)", "Less well-known"],
        "callout": "Claude is our go-to for building out full unit studies and semester plans. When we planned our American history unit, Claude created a 12-week scope and sequence with book lists, discussion questions, primary source suggestions, and weekly project ideas. The depth of planning it produces is genuinely impressive.",
        "quick_facts": [
            ("Price", "Free", "free"),
            ("Claude Pro", "$20/mo", ""),
            ("Ages", "All (parent-guided)", ""),
            ("Best For", "Curriculum Planning", ""),
            ("Platform", "Web", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "No", ""),
            ("ESA Eligible", "No", ""),
        ],
        "sidebar_cta_text": "Try Claude Free",
        "sidebar_link_text": "ChatGPT vs Claude comparison",
        "sidebar_link_url": "06-chatgpt-vs-claude-homeschool",
        "similar": [("chatgpt-homeschool-page", "ChatGPT", "Free / $20 mo", "Versatile AI for lesson planning.", "AI Assistant"),
                     ("khan-academy-page", "Khan Academy", "Free / $44 yr", "K-12 learning with AI tutor.", "AI Platform"),
                     ("outschool-page", "Outschool", "$10-40/class", "Live online classes.", "Live Classes")],
        "faqs": [
            ("Is Claude better than ChatGPT for homeschool?", "Claude tends to be better for long-form curriculum planning and nuanced writing tasks. ChatGPT is more versatile with its plugin ecosystem and image generation. Many homeschool parents use both. Our comparison guide breaks down the differences."),
            ("Can Claude create a full homeschool curriculum?", "Claude can generate detailed curriculum plans including scope and sequence, weekly lesson plans, book lists, and assessment ideas. It works best when you give it context about your child's age, learning style, and your preferred homeschool method."),
            ("Is Claude safe for children?", "Claude is designed for users 13+ with younger children supervised by parents. For homeschool, we recommend parents use Claude to create materials and plans rather than having young children chat with it directly."),
        ],
    },
    {
        "slug": "prodigy-page",
        "title": "Prodigy Math for Homeschool",
        "meta_title": "Prodigy Math for Homeschool | Skip School Directory",
        "meta_desc": "Review of Prodigy Math Game for homeschool. Free game-based math practice for K-8. See how it works, pricing for premium, and whether it's worth it for your family.",
        "h1": "Prodigy Math Game",
        "subtitle": "A free game-based math platform where kids practice grade-level skills by battling monsters and exploring a fantasy world. Covers K-8 math standards.",
        "rating": "3.9",
        "url": "https://www.prodigygame.com",
        "cta_text": "Play Prodigy Free",
        "cta_note": "Free to play. Premium optional.",
        "category": "Math Game",
        "features": [
            ("RPG Math Game", "Kids answer math questions to battle monsters and progress through a fantasy adventure."),
            ("Adaptive Difficulty", "Questions adjust based on your child's performance and grade level."),
            ("Curriculum Aligned", "Covers 1,500+ skills aligned to Common Core and state standards for grades 1-8."),
            ("Parent Dashboard", "Free reports showing which skills your child practiced and where they struggled."),
        ],
        "best_for_p1": "<strong>Reluctant math learners.</strong> If your child resists math practice, Prodigy's game format gets them doing problems without feeling like \"school.\" The RPG wrapper makes repetitive practice feel like play.",
        "best_for_p2": "<strong>Supplemental practice for elementary.</strong> Prodigy works best as a reward or free-choice activity, not a core math curriculum. Let kids play it after finishing their primary math lesson for the day.",
        "pros": ["Free core game", "Kids genuinely enjoy it", "Adaptive difficulty", "Good for reluctant learners", "Covers K-8 math skills"],
        "cons": ["Heavy monetization pressure on kids", "Game elements distract from math", "Premium membership is expensive", "Not deep enough for primary curriculum"],
        "callout": "Our kids play Prodigy as a reward after completing their Khan Academy math. It is not our primary math tool, but it keeps them practicing without complaints. We do not pay for premium because the free version covers the educational content.",
        "quick_facts": [
            ("Price", "Free", "free"),
            ("Premium", "$8.95/mo", ""),
            ("Ages", "K-8 (ages 5-14)", ""),
            ("Best For", "Math Practice", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "Yes (free)", ""),
            ("ESA Eligible", "Varies", ""),
        ],
        "sidebar_cta_text": "Start Prodigy Free",
        "sidebar_link_text": "Read our math guide",
        "sidebar_link_url": "21-ai-math-help",
        "similar": [("khan-academy-page", "Khan Academy", "Free / $44 yr", "Complete K-12 math curriculum.", "AI Platform"),
                     ("ixl-page", "IXL", "$9.95/mo", "Adaptive math and ELA.", "Practice"),
                     ("mathway-page", "Mathway", "Free / $9.99 mo", "Step-by-step math solver.", "Math Tool")],
        "faqs": [
            ("Is Prodigy Math free for homeschool?", "The core math game is completely free with no time limits. Premium membership ($8.95/mo) unlocks cosmetic items and extra game features but does not add educational content. The free version covers all the math practice."),
            ("Can Prodigy replace a math curriculum?", "No. Prodigy is a practice tool, not a teaching tool. It does not introduce new concepts through lessons. Use it alongside a structured math curriculum like Khan Academy, Math-U-See, or Saxon Math."),
            ("Is Prodigy appropriate for homeschool kids?", "Prodigy is appropriate for K-8, but be aware that premium membership marketing is aggressive. Set expectations with your child about in-game purchases before they start playing."),
        ],
    },
    {
        "slug": "mathway-page",
        "title": "Mathway for Homeschool",
        "meta_title": "Mathway for Homeschool | Skip School Directory",
        "meta_desc": "Review of Mathway for homeschool math help. Free step-by-step problem solver from basic math through calculus. Pricing, how to use it, and our honest rating.",
        "h1": "Mathway",
        "subtitle": "A step-by-step math problem solver covering basic math through calculus. Type or photograph any math problem and get an instant solution with work shown.",
        "rating": "4.1",
        "url": "https://www.mathway.com",
        "cta_text": "Try Mathway Free",
        "cta_note": "Free answers. Step-by-step is $9.99/mo.",
        "category": "Math Tool",
        "features": [
            ("Step-by-Step Solutions", "Shows complete work for every problem, not just the answer. Great for learning process."),
            ("Photo Input", "Snap a picture of any math problem and Mathway reads and solves it instantly."),
            ("All Math Levels", "Covers basic math, algebra, geometry, trig, calculus, statistics, and more."),
            ("Graph Plotting", "Visualize equations and functions with built-in graphing tools."),
        ],
        "best_for_p1": "<strong>Homeschool parents who need a math lifeline.</strong> When your child is stuck on a problem and you cannot remember how to solve it, Mathway shows you the step-by-step process so you can teach it.",
        "best_for_p2": "<strong>High school math support.</strong> Once math gets to algebra II and beyond, many homeschool parents need help. Mathway acts as an on-demand tutor that shows its work for every problem type.",
        "pros": ["Solves any math problem", "Shows complete work", "Photo input is convenient", "Covers all math levels", "Useful for parent learning too"],
        "cons": ["Step-by-step requires paid plan", "Free version only shows answers", "Can become a crutch", "No practice or drill features"],
        "callout": "We use Mathway as a parent resource more than a student tool. When our daughter brings me a pre-algebra problem I have not seen in 20 years, I type it into Mathway to see the steps, then teach her using those steps. It is a teacher's aide, not a replacement for learning.",
        "quick_facts": [
            ("Price", "Free (answers only)", "free"),
            ("Premium", "$9.99/mo", ""),
            ("Ages", "Middle school+", ""),
            ("Best For", "Problem Solving", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "No", ""),
            ("ESA Eligible", "No", ""),
        ],
        "sidebar_cta_text": "Try Mathway Free",
        "sidebar_link_text": "Read our math guide",
        "sidebar_link_url": "21-ai-math-help",
        "similar": [("khan-academy-page", "Khan Academy", "Free / $44 yr", "Full math curriculum with videos.", "AI Platform"),
                     ("ixl-page", "IXL", "$9.95/mo", "Adaptive math practice.", "Practice"),
                     ("prodigy-page", "Prodigy Math", "Free / $8.95 mo", "Game-based math for K-8.", "Math Game")],
        "faqs": [
            ("Is Mathway cheating for homeschool?", "Mathway is a tool, not a shortcut. Used correctly, the step-by-step feature teaches problem-solving methods. The key is using it to understand the process, not just copy answers. We recommend parents control access and use it as a teaching aid."),
            ("Is Mathway Premium worth it for homeschool?", "If your child is in algebra or above, Premium is worth it for the step-by-step explanations. Without Premium, you only get final answers, which limits the learning value. At $9.99/mo, it costs less than a math tutor."),
            ("What math levels does Mathway cover?", "Mathway covers basic math, pre-algebra, algebra, trigonometry, precalculus, calculus, statistics, finite math, linear algebra, and chemistry. It handles virtually any math problem a K-12 homeschool student would encounter."),
        ],
    },
    {
        "slug": "epic-books-page",
        "title": "Epic! Books for Homeschool",
        "meta_title": "Epic! Books for Homeschool | Skip School Directory",
        "meta_desc": "Review of Epic! digital library for homeschool readers. 40,000+ books for kids 12 and under. Free for educators. Pricing, pros, cons, and our rating.",
        "h1": "Epic! Digital Library",
        "subtitle": "A digital reading platform with 40,000+ books, audiobooks, and educational videos for kids 12 and under. Free for educators including homeschool parents.",
        "rating": "4.4",
        "url": "https://www.getepic.com",
        "cta_text": "Get Epic! Free",
        "cta_note": "Free for educators. Family plan available.",
        "category": "Reading Platform",
        "features": [
            ("40,000+ Books", "Massive library of children's books, from picture books to middle-grade chapter books."),
            ("Read-to-Me", "Audio narration for younger readers building independence."),
            ("Educator Free Access", "Homeschool parents qualify for free educator accounts with unlimited reading."),
            ("Reading Tracking", "Badges, reading streaks, and time-spent reports for parents."),
        ],
        "best_for_p1": "<strong>Building a reading habit.</strong> Epic's library is deep enough that every child finds something they love. The \"read-to-me\" feature helps struggling readers, while the variety keeps voracious readers engaged.",
        "best_for_p2": "<strong>Supplementing your home library.</strong> Instead of buying dozens of books your child might read once, Epic gives unlimited access to a rotating selection. Great for research projects and topic deep-dives too.",
        "pros": ["Free for homeschool educators", "Huge book selection", "Read-to-me audio feature", "Works on tablets", "Reading tracking for parents"],
        "cons": ["Limited to age 12 and under", "Some popular titles missing", "Free educator limits after 2024 changes", "Screen-based reading only"],
        "callout": "Epic replaced our weekly library trips for everyday reading. Our kids still visit the library for special books, but Epic handles the \"I finished my book, what next?\" problem. The educator account gives us unlimited access at no cost.",
        "quick_facts": [
            ("Price", "Free (educators)", "free"),
            ("Family Plan", "$9.99/mo", ""),
            ("Ages", "12 and under", ""),
            ("Best For", "Daily Reading", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "Yes (paid)", ""),
            ("Parent Tools", "Yes", ""),
            ("ESA Eligible", "Varies", ""),
        ],
        "sidebar_cta_text": "Get Epic! Educator Access",
        "sidebar_link_text": "Read our reading guide",
        "sidebar_link_url": "12-ai-reading-list-by-age",
        "similar": [("khan-academy-page", "Khan Academy", "Free / $44 yr", "K-12 learning platform.", "AI Platform"),
                     ("duolingo-page", "Duolingo", "Free / $6.99 mo", "Language learning app.", "Language"),
                     ("outschool-page", "Outschool", "$10-40/class", "Live online classes.", "Live Classes")],
        "faqs": [
            ("Is Epic! really free for homeschool?", "Epic offers free educator accounts for homeschool parents, though access terms have changed over time. Sign up with your homeschool information and you should qualify for free unlimited reading during school hours."),
            ("What age range does Epic! cover?", "Epic is designed for kids 12 and under, roughly preschool through 6th grade. The selection is strongest for elementary-age readers. For older kids, consider your local library's digital options or Kindle Unlimited."),
            ("Can Epic! replace the library for homeschool?", "Epic supplements but does not fully replace a library. It is great for everyday reading and quick access, but physical libraries offer a wider selection, community programs, and the experience of choosing physical books."),
        ],
    },
    {
        "slug": "brainly-page",
        "title": "Brainly for Homeschool",
        "meta_title": "Brainly for Homeschool | Skip School Directory",
        "meta_desc": "Review of Brainly for homeschool homework help. AI-powered answers and community-verified solutions for K-12. Pricing, safety tips, and our honest rating.",
        "h1": "Brainly",
        "subtitle": "AI-powered homework help with community-verified answers. Students ask questions and get step-by-step explanations from AI and human experts across all subjects.",
        "rating": "3.7",
        "url": "https://brainly.com",
        "cta_text": "Try Brainly Free",
        "cta_note": "Free tier. Plus is $24/year.",
        "category": "Homework Help",
        "features": [
            ("AI Answer Engine", "Instant step-by-step explanations for questions across all K-12 subjects."),
            ("Community Answers", "Millions of verified Q&A pairs from students and teachers worldwide."),
            ("Photo Search", "Snap a photo of a textbook problem and Brainly finds or generates the answer."),
            ("Math Solver", "Dedicated math solver with detailed work shown for every step."),
        ],
        "best_for_p1": "<strong>Quick answers when you are stuck.</strong> When your child hits a roadblock and you need a clear explanation fast, Brainly's AI provides step-by-step breakdowns that help both of you understand the solution.",
        "best_for_p2": "<strong>Supplement for independent learners.</strong> Older homeschool students working independently can use Brainly to check their understanding without waiting for a parent to be available.",
        "pros": ["Fast answers to specific questions", "Covers all K-12 subjects", "Step-by-step explanations", "Photo input for textbooks", "Affordable Plus plan"],
        "cons": ["Can become answer-copying tool", "Community answers vary in quality", "Ads on free tier", "Not structured for learning"],
        "callout": "We allow our older daughter to use Brainly after she has attempted a problem herself. The rule is: try it first, check with Brainly second, and understand why the answer works before moving on. Used this way, it is a helpful learning tool rather than a shortcut.",
        "quick_facts": [
            ("Price", "Free (limited)", "free"),
            ("Brainly Plus", "$24/year", ""),
            ("Ages", "10+ (with guidance)", ""),
            ("Best For", "Homework Help", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "No", ""),
            ("ESA Eligible", "No", ""),
        ],
        "sidebar_cta_text": "Try Brainly Free",
        "sidebar_link_text": "Read our AI tools guide",
        "sidebar_link_url": "13-teach-kids-use-ai",
        "similar": [("chatgpt-homeschool-page", "ChatGPT", "Free / $20 mo", "AI assistant for any subject.", "AI Assistant"),
                     ("mathway-page", "Mathway", "Free / $9.99 mo", "Step-by-step math solver.", "Math Tool"),
                     ("khan-academy-page", "Khan Academy", "Free / $44 yr", "Full K-12 curriculum.", "AI Platform")],
        "faqs": [
            ("Is Brainly safe for homeschool kids?", "Brainly is generally safe but includes community content that is not always accurate. We recommend parents review answers with younger children and teach older kids to verify information. The AI answers tend to be more reliable than community answers."),
            ("Is Brainly considered cheating?", "In a homeschool context, Brainly is a tool. The difference between cheating and learning depends on how it is used. If your child copies answers without understanding, it is counterproductive. If they use it to check work and understand mistakes, it is helpful."),
            ("Is Brainly Plus worth it?", "At $24/year, Brainly Plus removes ads and provides unlimited AI answers. If your child uses it regularly for homework help, the ad-free experience alone justifies the cost. It is one of the cheapest educational subscriptions available."),
        ],
    },
    {
        "slug": "rosetta-stone-page",
        "title": "Rosetta Stone for Homeschool",
        "meta_title": "Rosetta Stone for Homeschool | Skip School Directory",
        "meta_desc": "Review of Rosetta Stone for homeschool language learning. Immersive method, speech recognition, and structured curriculum. Pricing, pros, cons, and our rating.",
        "h1": "Rosetta Stone",
        "subtitle": "The gold standard in structured language learning. Immersive method with speech recognition, structured lessons, and a complete curriculum path from beginner to advanced.",
        "rating": "4.2",
        "url": "https://www.rosettastone.com",
        "cta_text": "Try Rosetta Stone",
        "cta_note": "3-day free trial. Plans from $11.99/mo.",
        "category": "Language Learning",
        "features": [
            ("Immersive Method", "Learn like a child learns their first language. No translation, just context and immersion."),
            ("Speech Recognition", "TruAccent technology provides real-time pronunciation feedback."),
            ("Structured Curriculum", "Clear lesson path from beginner through advanced with measurable milestones."),
            ("25 Languages", "Major world languages with complete curricula for each."),
        ],
        "best_for_p1": "<strong>Earning homeschool language credit.</strong> Rosetta Stone's structured, sequential curriculum makes it easy to document progress for transcripts. Many homeschool families use it to satisfy high school foreign language requirements.",
        "best_for_p2": "<strong>Independent language study.</strong> Unlike Duolingo's gamified approach, Rosetta Stone provides a traditional curriculum path that older students can follow independently with minimal parent involvement.",
        "pros": ["Structured curriculum path", "Excellent pronunciation tools", "Good for transcript documentation", "ESA-eligible in most states", "No translation crutch"],
        "cons": ["Expensive compared to alternatives", "Method can feel slow", "Less engaging for young kids", "Grammar is not explicitly taught"],
        "callout": "We use Rosetta Stone for our high schooler's Spanish requirement specifically because it provides a clear, documentable curriculum path. For our younger child, Duolingo is more engaging. Different tools for different ages and goals.",
        "quick_facts": [
            ("Price", "$11.99/mo", ""),
            ("Annual Plan", "$7.99/mo billed yearly", ""),
            ("Ages", "10+ recommended", ""),
            ("Best For", "Language Credit", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "Yes", ""),
            ("Parent Tools", "Basic progress", ""),
            ("ESA Eligible", "Yes", ""),
        ],
        "sidebar_cta_text": "Start Rosetta Stone Trial",
        "sidebar_link_text": "Read our language guide",
        "sidebar_link_url": "32-ai-foreign-language",
        "similar": [("duolingo-page", "Duolingo", "Free / $6.99 mo", "Gamified language learning.", "Language"),
                     ("babbel-page", "Babbel", "$6.95/mo", "Conversation-focused lessons.", "Language"),
                     ("outschool-page", "Outschool", "$10-40/class", "Live language classes.", "Live Classes")],
        "faqs": [
            ("Is Rosetta Stone worth the cost for homeschool?", "If you need documented foreign language credits for a high school transcript, Rosetta Stone's structured curriculum and progress tracking justify the cost. For casual language exploration, free options like Duolingo may be sufficient."),
            ("Can Rosetta Stone count as a high school language credit?", "Yes. Many homeschool families use Rosetta Stone to satisfy foreign language requirements. One full level typically equals one semester of study. Document completion with screenshots of progress reports for your transcript."),
            ("Rosetta Stone vs Duolingo for homeschool?", "Rosetta Stone offers more structure, better pronunciation tools, and clearer curriculum progression. Duolingo is free, more engaging for younger kids, and offers more languages. Many families use Duolingo for daily practice and Rosetta Stone for formal credit."),
        ],
    },
    {
        "slug": "babbel-page",
        "title": "Babbel for Homeschool",
        "meta_title": "Babbel for Homeschool | Skip School Directory",
        "meta_desc": "Review of Babbel for homeschool language learning. Conversation-focused lessons, grammar explanations, and practical vocabulary. Pricing and our honest rating.",
        "h1": "Babbel",
        "subtitle": "Conversation-focused language learning with explicit grammar instruction. Practical vocabulary, real-world dialogues, and lessons designed by linguists.",
        "rating": "4.0",
        "url": "https://www.babbel.com",
        "cta_text": "Try Babbel Free",
        "cta_note": "First lesson free. Plans from $6.95/mo.",
        "category": "Language Learning",
        "features": [
            ("Conversation Focus", "Lessons built around real-world dialogues and practical speaking scenarios."),
            ("Grammar Explanations", "Unlike immersion-only apps, Babbel explicitly teaches grammar rules."),
            ("Speech Recognition", "Pronunciation practice with instant feedback on your accent."),
            ("14 Languages", "Major languages with complete structured courses."),
        ],
        "best_for_p1": "<strong>Teens who want to actually speak a language.</strong> Babbel's focus on conversational skills and practical vocabulary produces faster real-world speaking ability than flashcard-heavy alternatives.",
        "best_for_p2": "<strong>Families who want grammar explained.</strong> If your homeschool approach values understanding the \"why\" behind language rules, Babbel's explicit grammar instruction fills a gap that Duolingo and Rosetta Stone leave open.",
        "pros": ["Conversation-focused approach", "Explicit grammar teaching", "Affordable pricing", "Practical vocabulary", "Good for teens"],
        "cons": ["Only 14 languages", "Less engaging for young kids", "No free tier beyond first lesson", "No parent dashboard"],
        "callout": "Babbel is our recommendation for homeschool teens who want to develop real conversational ability. The lessons are more mature in tone than Duolingo, and the grammar explanations help analytical learners understand patterns rather than just memorize phrases.",
        "quick_facts": [
            ("Price", "$6.95/mo (annual)", ""),
            ("Monthly Plan", "$13.95/mo", ""),
            ("Ages", "12+ recommended", ""),
            ("Best For", "Conversation Skills", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "Yes (paid)", ""),
            ("Parent Tools", "No", ""),
            ("ESA Eligible", "Varies", ""),
        ],
        "sidebar_cta_text": "Start Babbel Free Lesson",
        "sidebar_link_text": "Read our language guide",
        "sidebar_link_url": "32-ai-foreign-language",
        "similar": [("duolingo-page", "Duolingo", "Free / $6.99 mo", "Gamified language practice.", "Language"),
                     ("rosetta-stone-page", "Rosetta Stone", "$11.99/mo", "Immersive language curriculum.", "Language"),
                     ("outschool-page", "Outschool", "$10-40/class", "Live language classes.", "Live Classes")],
        "faqs": [
            ("Is Babbel good for homeschool language learning?", "Babbel is a strong choice for teens and older students who want practical conversation skills with grammar understanding. It is not ideal for young children due to its more mature teaching style. Pair it with speaking practice for best results."),
            ("Babbel vs Duolingo for homeschool?", "Babbel teaches more practical conversation and explains grammar rules explicitly. Duolingo is free, more gamified, and better for younger kids. For serious language study, many families start with Duolingo for basics and switch to Babbel for deeper learning."),
            ("Can Babbel count as homeschool language credit?", "Babbel can contribute to a language credit when combined with other resources. Its structured lessons provide documentable progress, but most families supplement with conversation practice, reading, and writing exercises for a complete credit."),
        ],
    },
    {
        "slug": "splashlearn-page",
        "title": "SplashLearn for Homeschool",
        "meta_title": "SplashLearn for Homeschool | Skip School Directory",
        "meta_desc": "Review of SplashLearn for homeschool. Game-based math and reading for PreK-5. Free for teachers, adaptive learning, and detailed parent reports. Our honest rating.",
        "h1": "SplashLearn",
        "subtitle": "Game-based math and reading practice for PreK through Grade 5. Adaptive learning, curriculum-aligned content, and free access for homeschool educators.",
        "rating": "4.3",
        "url": "https://www.splashlearn.com",
        "cta_text": "Try SplashLearn Free",
        "cta_note": "Free for educators. Family plan available.",
        "category": "Early Learning",
        "features": [
            ("Game-Based Learning", "Math and ELA games that feel like play while covering real curriculum standards."),
            ("Adaptive Practice", "Adjusts difficulty based on your child's performance in real time."),
            ("PreK-5 Coverage", "Focused specifically on younger learners with age-appropriate design."),
            ("Educator Free Access", "Homeschool parents can access the full platform free with an educator account."),
        ],
        "best_for_p1": "<strong>Young learners (PreK-2).</strong> SplashLearn's colorful, game-based approach is perfectly designed for the youngest homeschoolers. The activities feel like play but cover real math and reading skills.",
        "best_for_p2": "<strong>Daily math practice supplement.</strong> Use SplashLearn as the fun practice component alongside your primary math curriculum. 15-20 minutes of game-based practice reinforces concepts without worksheet fatigue.",
        "pros": ["Free for homeschool educators", "Excellent for young learners", "Genuinely fun games", "Adaptive difficulty", "Covers math and reading"],
        "cons": ["Limited to grade 5 and below", "Premium upselling", "Some games more fun than educational", "Web-based only for full features"],
        "callout": "SplashLearn is our favorite tool for our kindergartner. He thinks he is playing games, but he is actually practicing number sense, counting, and early reading skills. The educator account gives us full access at no cost.",
        "quick_facts": [
            ("Price", "Free (educators)", "free"),
            ("Family Plan", "$7.99/mo", ""),
            ("Ages", "PreK-Grade 5", ""),
            ("Best For", "Early Math + Reading", ""),
            ("Platform", "Web, iOS, Android", ""),
            ("Offline", "No", ""),
            ("Parent Tools", "Yes", ""),
            ("ESA Eligible", "Varies", ""),
        ],
        "sidebar_cta_text": "Get SplashLearn Free",
        "sidebar_link_text": "Read our age-based guide",
        "sidebar_link_url": "47-ai-projects-by-age",
        "similar": [("prodigy-page", "Prodigy Math", "Free / $8.95 mo", "Math game for K-8.", "Math Game"),
                     ("khan-academy-page", "Khan Academy", "Free / $44 yr", "K-12 learning platform.", "AI Platform"),
                     ("epic-books-page", "Epic! Books", "Free (educators)", "Digital reading library.", "Reading")],
        "faqs": [
            ("Is SplashLearn free for homeschool?", "Yes, homeschool parents can sign up for a free educator account that provides full access to SplashLearn's math and reading content. Family plans with additional features are available for $7.99/month."),
            ("What ages is SplashLearn best for?", "SplashLearn is designed for PreK through Grade 5 (ages 3-11). It is strongest for PreK-2 where the game-based approach matches developmental needs. Older elementary students may prefer more challenging platforms like Khan Academy or IXL."),
            ("SplashLearn vs Prodigy for homeschool?", "SplashLearn is better for younger children (PreK-2) with its simpler, more colorful interface. Prodigy is better for older elementary students (grades 1-8) with its RPG-style game. SplashLearn also covers reading, while Prodigy is math-only."),
        ],
    },
]

# Color palette for gallery placeholders (brand-appropriate gradients)
COLORS = [
    ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
    ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#f093fb"),
    ("linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)", "#4facfe"),
    ("linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)", "#43e97b"),
]

def build_similar_cards(similar_list):
    cards = []
    for slug, name, price, desc, tag in similar_list:
        color_idx = hash(slug) % len(COLORS)
        grad, _ = COLORS[color_idx]
        cards.append(f'''                <a href="{slug}" class="sim-card">
                    <div class="sim-img" style="background:{grad};">
                        <span class="sim-tag">{tag}</span>
                    </div>
                    <div class="sim-body">
                        <h3>{name}</h3>
                        <div class="sim-price">{price}</div>
                        <p>{desc}</p>
                    </div>
                </a>''')
    return '\n'.join(cards)

def build_quick_facts(facts):
    rows = []
    for label, value, extra in facts:
        cls = ' class="qf-value free"' if extra == "free" else ' class="qf-value"'
        rows.append(f'                    <div class="qf-row"><span class="qf-label">{label}</span><span{cls}>{value}</span></div>')
    return '\n'.join(rows)

def build_faq_html(faqs):
    items = []
    for q, a in faqs:
        items.append(f'''        <div class="faq-item">
            <h3>{q}</h3>
            <p>{a}</p>
        </div>''')
    return '\n'.join(items)

def build_faq_schema(brand_name, slug, faqs):
    entries = []
    for q, a in faqs:
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"')
        entries.append(f'''{{"@type":"Question","name":"{q_esc}","acceptedAnswer":{{"@type":"Answer","text":"{a_esc}"}}}}''')
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{','.join(entries)}]}}
</script>'''

def build_page(brand):
    features_html = '\n'.join([
        f'                <div class="feat-block"><h4>{title}</h4><p>{desc}</p></div>'
        for title, desc in brand["features"]
    ])

    pros_html = '\n'.join([f'                    <div class="pc-item">{p}</div>' for p in brand["pros"]])
    cons_html = '\n'.join([f'                    <div class="pc-item">{c}</div>' for c in brand["cons"]])

    similar_cards = build_similar_cards(brand["similar"])
    quick_facts = build_quick_facts(brand["quick_facts"])
    faq_items = build_faq_html(brand["faqs"])
    faq_schema = build_faq_schema(brand["h1"], brand["slug"], brand["faqs"])

    # Gallery placeholder using gradients
    gallery_html = ''
    for i in range(4):
        grad, _ = COLORS[i]
        gallery_html += f'                <div class="gallery-img" style="background:{grad};display:flex;align-items:center;justify-content:center;color:#fff;font-family:Fraunces,serif;font-size:14px;font-weight:700;opacity:0.7;"></div>\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{brand["meta_title"]}</title>
    <meta name="description" content="{brand["meta_desc"]}">
    <link rel="canonical" href="https://skipschool.ai/{brand["slug"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&display=swap" rel="stylesheet">
    <style>
        {CSS}
        .gallery {{ display: flex; gap: 10px; overflow-x: auto; padding: 4px 0 12px; margin: 0 0 20px; }}
        .gallery-img {{ width: 220px; height: 150px; border-radius: 8px; flex-shrink: 0; border: 1.5px solid var(--border-light); }}
    </style>
    {faq_schema}
</head>
<body>

    {NAV_HTML}

    <div class="brand-header"><div class="wrap">
        <div class="brand-crumb"><a href="/directory-index">Directory</a> &nbsp;/&nbsp; {brand["category"]}</div>
        <div class="brand-top">
            <div class="brand-title-area">
                <h1>{brand["h1"]}</h1>
                <p class="brand-subtitle">{brand["subtitle"]}</p>
                <div class="brand-rating"><span class="brand-score">{brand["rating"]}</span><span class="brand-score-label">/5 Our Rating</span></div>
            </div>
            <div class="brand-cta-area">
                <a href="{brand["url"]}" target="_blank" rel="noopener" class="brand-visit">{brand["cta_text"]} &rarr;</a>
                <div class="brand-free">{brand["cta_note"]}</div>
            </div>
        </div>
    </div></div>

    <div class="wrap"><div class="product-layout">
        <div class="main">

            <div class="gallery">
{gallery_html}            </div>

            <h2>What It Does</h2>
            <div class="feat-grid">
{features_html}
            </div>

            <h2>What It's Best For</h2>
            <p>{brand["best_for_p1"]}</p>
            <p>{brand["best_for_p2"]}</p>

            <h2>Pros &amp; Cons</h2>
            <div class="pc-grid">
                <div class="pc-col">
                    <h4 class="pro">What we love</h4>
{pros_html}
                </div>
                <div class="pc-col">
                    <h4 class="con">What could be better</h4>
{cons_html}
                </div>
            </div>

            <div class="callout">
                <h4>How We Use It</h4>
                <p>{brand["callout"]}</p>
            </div>

        </div>

        <div class="sidebar">
            <div class="quick-card">
                <div class="quick-card-head"><h3>Quick Facts</h3></div>
                <div class="quick-card-body">
{quick_facts}
                    <div class="qf-row"><span class="qf-label">Our Rating</span><span class="qf-value" style="color:var(--yellow);font-size:16px;">{brand["rating"]}/5</span></div>
                    <a href="{brand["url"]}" target="_blank" rel="noopener" class="sidebar-cta">{brand["sidebar_cta_text"]} &rarr;</a>
                    <div class="sidebar-link"><a href="/{brand["sidebar_link_url"]}">{brand["sidebar_link_text"]} &rarr;</a></div>
                </div>
            </div>
        </div>
    </div></div>

    <!-- FAQ Section -->
    <section class="faq-section"><div class="wrap">
        <h2>Frequently Asked Questions</h2>
{faq_items}
    </div></section>

    <!-- Similar Tools -->
    <section class="similar-section">
        <div class="wrap">
            <div class="similar-header">
                <span class="similar-title">Similar Tools</span>
                <span class="similar-line"></span>
                <a href="/directory-index" style="font-size:12px;font-weight:600;color:var(--text-light);">Browse all &rarr;</a>
            </div>
            <div class="similar-grid">
{similar_cards}
            </div>
        </div>
    </section>

    {FOOTER_HTML}

</body></html>'''


# Generate all pages
count = 0
for brand in BRANDS:
    html = build_page(brand)
    filepath = os.path.join(SRC, f'{brand["slug"]}.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f'  Created: {brand["slug"]}.html')

print(f'\nDone! Created {count} directory pages.')
