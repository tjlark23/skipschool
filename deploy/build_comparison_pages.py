#!/usr/bin/env python3
"""Build comparison (vs) pages for Skip School."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

SRC = os.path.join(os.path.dirname(__file__), '..', 'site', 'files', 'src')
DEPLOY = os.path.dirname(__file__)

with open(os.path.join(DEPLOY, 'nav_snippet.txt'), 'r', encoding='utf-8') as f:
    NAV_HTML = f.read()
with open(os.path.join(DEPLOY, 'footer_snippet.txt'), 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read()

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
        .vs-hero { background: var(--navy); padding: 36px 0 40px; text-align: center; }
        .vs-hero h1 { font-family: 'Fraunces', serif; font-size: 34px; font-weight: 900; color: #fff; margin-bottom: 8px; }
        .vs-hero h1 span { color: var(--yellow); }
        .vs-hero p { font-size: 15px; color: rgba(255,255,255,0.6); max-width: 600px; margin: 0 auto; line-height: 1.55; }
        .vs-content { max-width: 860px; margin: 0 auto; padding: 32px 20px; }
        .vs-content h2 { font-family: 'Fraunces', serif; font-size: 22px; font-weight: 800; color: var(--navy); margin: 32px 0 12px; }
        .vs-content h2:first-child { margin-top: 0; }
        .vs-content p { font-size: 15px; line-height: 1.7; color: var(--text-mid); margin-bottom: 14px; }
        .vs-content strong { color: var(--text); }
        .compare-table { width: 100%; border-collapse: collapse; margin: 20px 0 28px; background: #fff; border-radius: 10px; overflow: hidden; border: 1.5px solid var(--border-light); }
        .compare-table th { background: var(--navy); color: #fff; font-size: 14px; font-weight: 700; padding: 12px 16px; text-align: left; }
        .compare-table th:first-child { color: rgba(255,255,255,0.5); font-weight: 500; }
        .compare-table td { padding: 10px 16px; font-size: 13px; border-bottom: 1px solid var(--border-light); color: var(--text-mid); }
        .compare-table tr:last-child td { border-bottom: none; }
        .compare-table td:first-child { font-weight: 600; color: var(--text-light); font-size: 12px; }
        .compare-table .winner { background: rgba(251,201,38,0.08); font-weight: 600; color: var(--navy); }
        .verdict-box { background: var(--cream); border-left: 4px solid var(--yellow); border-radius: 0 10px 10px 0; padding: 20px 24px; margin: 24px 0; }
        .verdict-box h3 { font-family: 'Fraunces', serif; font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px; }
        .verdict-box p { font-size: 14px; color: var(--text-mid); line-height: 1.6; margin-bottom: 0; }
        .cta-row { display: flex; gap: 12px; margin: 24px 0; }
        .cta-btn { display: inline-block; padding: 12px 24px; border-radius: 6px; font-weight: 700; font-size: 14px; text-align: center; flex: 1; }
        .cta-btn.primary { background: var(--navy); color: #fff; }
        .cta-btn.secondary { background: #fff; color: var(--navy); border: 1.5px solid var(--border); }
        .faq-section { padding: 28px 0; max-width: 860px; margin: 0 auto; }
        .faq-section h2 { font-family:'Fraunces',serif; font-size:22px; font-weight:800; color:var(--navy); margin-bottom:16px; }
        .faq-item { background:#fff; border:1.5px solid var(--border-light); border-radius:8px; padding:16px 20px; margin-bottom:10px; }
        .faq-item h3 { font-size:15px; font-weight:700; color:var(--navy); margin-bottom:6px; }
        .faq-item p { font-size:14px; color:var(--text-mid); line-height:1.6; margin:0; }
        .footer { background: #0a1828; color: rgba(255,255,255,0.55); padding: 32px 0; }
        .footer .wrap { display: flex; justify-content: space-between; gap: 32px; }
        .footer-brand img { height: 28px; margin-bottom: 8px; }
        .footer-brand p { font-size: 12.5px; max-width: 260px; line-height: 1.5; }
        .footer-col h4 { color: var(--yellow); font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
        .footer-col a { display: block; font-size: 12.5px; margin-bottom: 5px; opacity: 0.6; }
        .footer-bottom { margin-top: 20px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 11px; opacity: 0.35; }
        @media (max-width: 700px) {
            .cta-row { flex-direction: column; }
            .compare-table { font-size: 12px; }
        }"""

COMPARISONS = [
    {
        "slug": "ixl-vs-khan-academy",
        "meta_title": "IXL vs Khan Academy for Homeschool (2025) | Skip School",
        "meta_desc": "IXL vs Khan Academy: which is better for homeschool? We compare pricing, features, math coverage, and parent tools. See our side-by-side breakdown and verdict.",
        "h1_a": "IXL", "h1_b": "Khan Academy",
        "subtitle": "Two of the most popular homeschool platforms compared head-to-head. One costs money, one is free. Here is which one your family actually needs.",
        "table_rows": [
            ("Price", "$9.95-19.95/mo", "Free (Khanmigo $44/yr)", "b"),
            ("Best For", "Skill practice + diagnostics", "Full math curriculum", "b"),
            ("Math Coverage", "K-12 (practice only)", "K-12 (lessons + practice)", "b"),
            ("ELA Coverage", "K-12", "Limited", "a"),
            ("Teaching Method", "Adaptive drill", "Video lessons + practice", "b"),
            ("AI Tutor", "No", "Yes (Khanmigo)", "b"),
            ("Parent Dashboard", "Yes (detailed)", "Yes (good)", "a"),
            ("Diagnostic Tool", "Yes (excellent)", "No", "a"),
            ("ESA Eligible", "Yes", "Varies", "a"),
            ("Offline Access", "No", "No", ""),
        ],
        "intro": "IXL and Khan Academy are the two platforms homeschool families ask about most for math and academics. They serve different purposes, and many families end up using both.",
        "sections": [
            ("When to Choose Khan Academy", "<p><strong>Khan Academy is the better choice when you need a primary math curriculum.</strong> It teaches concepts through video lessons, then provides practice to reinforce them. The learning path from counting through calculus is complete and well-structured.</p><p>If budget is a factor, Khan Academy wins by default. The core platform is entirely free, and even the Khanmigo AI tutor is only $44/year. For a family trying to homeschool without breaking the bank, Khan Academy should be your first stop.</p>"),
            ("When to Choose IXL", "<p><strong>IXL is the better choice when you need targeted skill practice and diagnostics.</strong> Its diagnostic tool pinpoints exactly where your child is in each skill area, then serves adaptive practice to close those gaps.</p><p>IXL works best as a supplement alongside a teaching curriculum. If your child is using Saxon Math or Math-U-See for instruction, IXL provides the adaptive practice that fills gaps and builds fluency.</p>"),
            ("Can You Use Both?", "<p><strong>Yes, and many homeschool families do.</strong> The best combination is Khan Academy for primary instruction (video lessons + structured practice) plus IXL for targeted gap-filling (diagnostics + adaptive drill). Khan Academy teaches the concepts; IXL ensures nothing falls through the cracks.</p><p>A typical daily schedule might look like 30 minutes of Khan Academy math followed by 15 minutes of IXL practice targeting flagged skill areas.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Start with Khan Academy. It is free, it teaches concepts (not just drills them), and the Khanmigo AI tutor adds genuine value. Add IXL later if you need diagnostics to identify specific skill gaps or want more structured practice in ELA. Most families do not need both from day one.",
        "cta_a": ("Try IXL Free", "https://www.ixl.com", "secondary"),
        "cta_b": ("Start Khan Academy Free", "https://www.khanacademy.org", "primary"),
        "page_a": "ixl-page",
        "page_b": "khan-academy-page",
        "faqs": [
            ("Is IXL or Khan Academy better for homeschool math?", "Khan Academy is better as a primary math curriculum because it teaches concepts through video lessons. IXL is better as a practice supplement with its diagnostic tool. Many families use Khan Academy for instruction and IXL for targeted practice."),
            ("Is Khan Academy really free?", "Yes, the core Khan Academy platform is completely free with no limits. The optional Khanmigo AI tutor costs $44/year. There are no ads, no freemium restrictions, and no hidden costs for the main learning content."),
            ("Can IXL replace Khan Academy for homeschool?", "IXL is a practice tool, not a teaching tool. It does not include video lessons or concept explanations. You would need a separate teaching curriculum alongside IXL, whereas Khan Academy can serve as a standalone math curriculum."),
        ],
    },
    {
        "slug": "chatgpt-vs-claude-homeschool",
        "meta_title": "ChatGPT vs Claude for Homeschool (2025) | Skip School",
        "meta_desc": "ChatGPT vs Claude for homeschool: which AI is better for lesson planning, tutoring, and curriculum design? Side-by-side comparison with our honest recommendation.",
        "h1_a": "ChatGPT", "h1_b": "Claude",
        "subtitle": "The two leading AI assistants compared for homeschool use. Both are powerful, but they have different strengths that matter for education.",
        "table_rows": [
            ("Price (Free)", "GPT-4o", "Claude 3.5 Sonnet", ""),
            ("Price (Paid)", "$20/mo (Plus)", "$20/mo (Pro)", ""),
            ("Best For", "Versatile tasks + images", "Long-form planning", ""),
            ("Lesson Planning", "Excellent", "Excellent", ""),
            ("Curriculum Design", "Good", "Excellent", "b"),
            ("Writing Help", "Good", "Excellent", "b"),
            ("Math Tutoring", "Very good", "Good", "a"),
            ("Image Generation", "Yes (DALL-E)", "No", "a"),
            ("Context Length", "128K tokens", "200K tokens", "b"),
            ("Mobile App", "Yes", "No", "a"),
        ],
        "intro": "ChatGPT and Claude are both excellent AI tools for homeschool parents. The question is not which one is better overall, but which one is better for your specific needs.",
        "sections": [
            ("When to Choose ChatGPT", "<p><strong>ChatGPT is the better choice for versatility and quick tasks.</strong> It handles a wider range of requests, generates images with DALL-E, has a polished mobile app, and connects to a massive plugin ecosystem. For day-to-day homeschool tasks like generating a quick worksheet, creating a quiz, or brainstorming field trip ideas, ChatGPT is fast and reliable.</p><p>ChatGPT also tends to be stronger for math tutoring, producing more accurate step-by-step solutions and clearer mathematical explanations.</p>"),
            ("When to Choose Claude", "<p><strong>Claude is the better choice for detailed planning and writing.</strong> Its longer context window and more thoughtful response style make it ideal for building full curriculum plans, writing detailed unit studies, and creating nuanced assessment rubrics. When you need depth and coherence over a long document, Claude consistently outperforms.</p><p>Claude is also our pick for writing instruction support. Its feedback on student writing is more nuanced, and it provides better suggestions for improvement without being overly prescriptive.</p>"),
            ("Using Both Together", "<p><strong>The best approach is using both for their strengths.</strong> Use ChatGPT for daily quick tasks: worksheets, quiz generation, brainstorming, and image creation. Use Claude for bigger planning projects: semester plans, unit studies, curriculum design, and writing feedback.</p><p>Both have generous free tiers, so you can use both without paying for either. If you upgrade one, choose based on which tasks you do more often.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Start with ChatGPT for everyday homeschool tasks because of its versatility and mobile app. Add Claude when you need to do deeper curriculum planning or writing work. Both free tiers are powerful enough for most homeschool families. If you only pay for one, choose ChatGPT Plus for its broader feature set, or Claude Pro if you primarily need long-form planning.",
        "cta_a": ("Try ChatGPT Free", "https://chat.openai.com", "primary"),
        "cta_b": ("Try Claude Free", "https://claude.ai", "secondary"),
        "page_a": "chatgpt-homeschool-page",
        "page_b": "claude-homeschool-page",
        "faqs": [
            ("Is ChatGPT or Claude better for homeschool?", "Both are excellent for homeschool. ChatGPT is more versatile for daily tasks and has a mobile app. Claude is better for long-form curriculum planning and writing instruction. Many homeschool parents use both for their respective strengths."),
            ("Can AI replace a homeschool curriculum?", "AI tools like ChatGPT and Claude are powerful assistants but work best alongside structured curricula. Use them to customize materials, fill gaps, and create supplemental content. They should enhance your curriculum, not replace it entirely."),
            ("Are ChatGPT and Claude safe for kids?", "Both are designed for users 13+ and younger children should use them with parent supervision. For homeschool, we recommend parents use these AI tools to create materials rather than having young children interact with them directly."),
        ],
    },
    {
        "slug": "duolingo-vs-rosetta-stone",
        "meta_title": "Duolingo vs Rosetta Stone for Homeschool (2025) | Skip School",
        "meta_desc": "Duolingo vs Rosetta Stone for homeschool language learning. Free vs paid, gamified vs structured. Our comparison helps you choose the right language tool.",
        "h1_a": "Duolingo", "h1_b": "Rosetta Stone",
        "subtitle": "Free and gamified versus paid and structured. Two very different approaches to language learning, and your choice depends on your child's age and goals.",
        "table_rows": [
            ("Price", "Free (Super $6.99/mo)", "$11.99/mo", "a"),
            ("Languages", "40+", "25", "a"),
            ("Method", "Gamified + AI", "Immersive (no translation)", ""),
            ("Best Ages", "5-14", "10+", "a"),
            ("Grammar Teaching", "Minimal", "Implicit (immersion)", ""),
            ("Pronunciation", "Basic", "Excellent (TruAccent)", "b"),
            ("Curriculum Structure", "Loose (skill tree)", "Structured (sequential)", "b"),
            ("For HS Credit", "Difficult to document", "Yes, commonly accepted", "b"),
            ("Offline Access", "Paid only", "Yes", "b"),
            ("Engagement", "Very high (streaks/XP)", "Moderate", "a"),
        ],
        "intro": "Duolingo and Rosetta Stone represent opposite ends of the language learning spectrum. Your choice comes down to your child's age, your budget, and whether you need documentable credit.",
        "sections": [
            ("When to Choose Duolingo", "<p><strong>Duolingo wins for younger learners and budget-conscious families.</strong> It is free, incredibly engaging, and offers more language options than any competitor. The streak system builds daily habits, and kids genuinely enjoy using it.</p><p>For elementary and middle school homeschoolers, Duolingo provides an excellent introduction to a new language without any financial commitment. The gamified approach removes the anxiety of making mistakes and keeps kids coming back.</p>"),
            ("When to Choose Rosetta Stone", "<p><strong>Rosetta Stone wins for high school credit and serious study.</strong> Its structured curriculum path makes it easy to document progress for transcripts. The pronunciation technology is genuinely superior, and the immersive method builds deeper comprehension.</p><p>If your homeschool teen needs a foreign language credit for college applications, Rosetta Stone's sequential curriculum and progress tracking make documentation straightforward. Many colleges recognize Rosetta Stone completion as evidence of language study.</p>"),
            ("The Best of Both Worlds", "<p><strong>Start with Duolingo, graduate to Rosetta Stone.</strong> Use Duolingo in elementary and middle school to build basic vocabulary, develop a daily language habit, and explore which languages interest your child. When they reach high school and need formal credit, switch to Rosetta Stone for structured curriculum with documentable progress.</p><p>Some families run both simultaneously: Duolingo for daily maintenance (5-10 minutes) and Rosetta Stone for formal study (20-30 minutes).</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Use Duolingo if your child is under 12 or you want free language exploration. Use Rosetta Stone if you need documentable high school credit or want structured curriculum with excellent pronunciation tools. Both are good tools serving different needs at different price points.",
        "cta_a": ("Start Duolingo Free", "https://www.duolingo.com", "primary"),
        "cta_b": ("Try Rosetta Stone", "https://www.rosettastone.com", "secondary"),
        "page_a": "duolingo-page",
        "page_b": "rosetta-stone-page",
        "faqs": [
            ("Is Duolingo or Rosetta Stone better for homeschool?", "Duolingo is better for younger kids and casual language exploration (free and engaging). Rosetta Stone is better for teens who need documentable high school language credit (structured curriculum with progress tracking)."),
            ("Can Duolingo count as homeschool language credit?", "Duolingo alone is difficult to document as a formal language credit. It works better as a daily practice supplement. For credit, pair it with conversation practice, writing, and reading, or use a structured program like Rosetta Stone."),
            ("Is Rosetta Stone worth the money compared to free Duolingo?", "For casual language exploration, no. For structured language study with pronunciation feedback and transcript-ready documentation, yes. Rosetta Stone's value increases with your child's age and the formality of your language requirements."),
        ],
    },
    {
        "slug": "outschool-vs-khan-academy",
        "meta_title": "Outschool vs Khan Academy for Homeschool (2025) | Skip School",
        "meta_desc": "Outschool vs Khan Academy: live classes vs self-paced learning. Compare pricing, teaching styles, and features to find the best fit for your homeschool.",
        "h1_a": "Outschool", "h1_b": "Khan Academy",
        "subtitle": "Live teacher-led classes versus self-paced video learning. Two fundamentally different approaches that many homeschool families combine.",
        "table_rows": [
            ("Price", "$10-40/class", "Free", "b"),
            ("Format", "Live video classes", "Self-paced videos", ""),
            ("Teacher", "Independent educators", "Pre-recorded + AI", ""),
            ("Socialization", "Excellent (live peers)", "None", "a"),
            ("Subject Range", "Massive (200K+ classes)", "Math-focused + some", "a"),
            ("Flexibility", "Must attend live", "Anytime", "b"),
            ("Parent Involvement", "Low (teacher-led)", "Medium", "a"),
            ("ESA Eligible", "Yes, widely", "Varies", "a"),
            ("Age Range", "3-18", "K-12", "a"),
            ("Math Curriculum", "Varies by teacher", "Complete K-12", "b"),
        ],
        "intro": "Outschool and Khan Academy serve completely different needs. Understanding what each does well helps you build a well-rounded homeschool program using both.",
        "sections": [
            ("When to Choose Khan Academy", "<p><strong>Khan Academy is the right choice for core academic instruction, especially math.</strong> Its complete K-12 math curriculum with video lessons, adaptive practice, and the Khanmigo AI tutor provides a solid foundation for daily learning. It is self-paced, free, and available whenever your family is ready to learn.</p><p>For families on a tight budget or those who need flexible scheduling, Khan Academy delivers college-level educational content at zero cost.</p>"),
            ("When to Choose Outschool", "<p><strong>Outschool is the right choice for socialization, enrichment, and specialized subjects.</strong> Live classes with real teachers and peer interaction solve the \"what about socialization?\" question. Your child gets to interact with same-age kids who share their interests.</p><p>Outschool also fills gaps in subjects that are hard to teach at home: foreign languages, advanced science labs, art techniques, creative writing workshops, and niche interests like marine biology or game design.</p>"),
            ("The Ideal Combination", "<p><strong>Most successful homeschool families use both.</strong> Khan Academy handles core math instruction daily (free, self-paced, thorough). Outschool fills in with weekly live classes for socialization, electives, and subjects where a specialist teacher adds value.</p><p>A typical week might include Khan Academy math 4-5 days plus 2-3 Outschool classes for writing, science, and a social club. Total Outschool cost: $60-120/month for the live class component.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Start with Khan Academy for free, self-paced core instruction. Add Outschool selectively for socialization and subjects that benefit from a live teacher. Do not try to replace Khan Academy with Outschool for math, and do not expect Khan Academy to provide the social interaction that Outschool delivers.",
        "cta_a": ("Browse Outschool Classes", "https://outschool.com", "secondary"),
        "cta_b": ("Start Khan Academy Free", "https://www.khanacademy.org", "primary"),
        "page_a": "outschool-page",
        "page_b": "khan-academy-page",
        "faqs": [
            ("Should I use Outschool or Khan Academy for homeschool?", "Use both for different purposes. Khan Academy is best for self-paced core instruction (especially math). Outschool is best for live classes, socialization, and specialized subjects. They complement each other well."),
            ("Is Outschool worth the cost when Khan Academy is free?", "Outschool provides something Khan Academy cannot: live teacher interaction and peer socialization. If your child needs social connection and specialist instruction in certain subjects, Outschool's per-class cost is a worthwhile investment."),
            ("Can Outschool replace Khan Academy for math?", "You could find math classes on Outschool, but Khan Academy's complete, free, self-paced math curriculum is generally more effective and cost-efficient for daily math instruction. Use Outschool for enrichment, not to replace free core tools."),
        ],
    },
    {
        "slug": "prodigy-vs-khan-academy",
        "meta_title": "Prodigy vs Khan Academy Math for Homeschool (2025) | Skip School",
        "meta_desc": "Prodigy vs Khan Academy for homeschool math. Game-based practice vs structured curriculum. Our comparison helps you pick the right math tool for your child.",
        "h1_a": "Prodigy Math", "h1_b": "Khan Academy",
        "subtitle": "Game-based math practice versus structured video curriculum. Both are free, but they serve very different roles in your homeschool math program.",
        "table_rows": [
            ("Price", "Free (Premium $8.95/mo)", "Free (Khanmigo $44/yr)", ""),
            ("Format", "RPG math game", "Video lessons + practice", ""),
            ("Grade Range", "K-8", "K-12+", "b"),
            ("Teaches Concepts", "No (practice only)", "Yes (full lessons)", "b"),
            ("Engagement", "Very high (game)", "Moderate (videos)", "a"),
            ("Math Depth", "Standard skills", "Through AP Calculus", "b"),
            ("AI Tutor", "No", "Yes (Khanmigo)", "b"),
            ("Parent Dashboard", "Yes (free)", "Yes", ""),
            ("SAT/ACT Prep", "No", "Yes (official)", "b"),
            ("Reluctant Learner", "Excellent", "Moderate", "a"),
        ],
        "intro": "Prodigy and Khan Academy are both free math platforms, but they have fundamentally different purposes. One teaches math; the other makes practicing math feel like playing a video game.",
        "sections": [
            ("When to Choose Khan Academy", "<p><strong>Khan Academy is a math curriculum. Prodigy is not.</strong> Khan Academy teaches new concepts through video lessons with Sal Khan (or AI-powered Khanmigo), then provides practice to reinforce them. It is a complete math education from counting through AP Calculus.</p><p>If you need one tool to handle your child's math education, Khan Academy is the only choice between these two. It is structured, sequential, and thorough.</p>"),
            ("When to Choose Prodigy", "<p><strong>Prodigy shines as a reward and practice supplement.</strong> After your child does their \"real\" math lesson, Prodigy provides gamified practice that reinforces skills without feeling like more school. The RPG format motivates reluctant math learners.</p><p>Prodigy is also useful for review during breaks. Summer slide is real, and a child who plays Prodigy for 20 minutes a day during summer maintains skills without formal instruction.</p>"),
            ("The Smart Combination", "<p><strong>Khan Academy for instruction, Prodigy for fun practice.</strong> This is the combination we use and recommend. Khan Academy handles the teaching and structured practice (30 minutes daily). Prodigy serves as a reward activity or free-choice option (15-20 minutes as earned time).</p><p>Do not rely on Prodigy alone for math. It does not teach concepts or provide the sequential instruction your child needs to progress.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Khan Academy is your math curriculum. Prodigy is your math reward. Use Khan Academy daily for structured learning, and let your child earn Prodigy time as a bonus. Both are free, so there is no reason not to use both in their proper roles.",
        "cta_a": ("Play Prodigy Free", "https://www.prodigygame.com", "secondary"),
        "cta_b": ("Start Khan Academy Free", "https://www.khanacademy.org", "primary"),
        "page_a": "prodigy-page",
        "page_b": "khan-academy-page",
        "faqs": [
            ("Is Prodigy or Khan Academy better for homeschool math?", "Khan Academy is better as a math curriculum because it teaches concepts through lessons. Prodigy is better as a fun practice supplement because of its game format. They serve different purposes and work well together."),
            ("Can Prodigy Math replace Khan Academy?", "No. Prodigy is a practice tool that reinforces skills through gameplay. It does not teach new concepts or provide structured math instruction. Khan Academy provides complete math curriculum from K through AP Calculus."),
            ("Is Prodigy Math Premium worth it for homeschool?", "Premium unlocks cosmetic game items but no additional educational content. The free version includes all the math practice. Most homeschool families find the free version sufficient."),
        ],
    },
    {
        "slug": "ixl-vs-prodigy",
        "meta_title": "IXL vs Prodigy Math for Homeschool (2025) | Skip School",
        "meta_desc": "IXL vs Prodigy for homeschool math practice. Adaptive diagnostics vs game-based learning. Pricing, features, and which one is right for your child.",
        "h1_a": "IXL", "h1_b": "Prodigy Math",
        "subtitle": "Structured adaptive practice versus game-based math. Two popular math supplements compared for homeschool families deciding where to spend time and money.",
        "table_rows": [
            ("Price", "$9.95-19.95/mo", "Free (Premium $8.95/mo)", "b"),
            ("Format", "Adaptive drill", "RPG math game", ""),
            ("Grade Range", "K-12", "K-8", "a"),
            ("Diagnostic Tool", "Yes (excellent)", "No", "a"),
            ("Engagement", "Low-moderate", "Very high", "b"),
            ("ELA Coverage", "Yes", "No", "a"),
            ("Skill Tracking", "Detailed per-skill", "Basic progress", "a"),
            ("Standards Aligned", "Yes (detailed)", "Yes (basic)", "a"),
            ("Reluctant Learner", "Poor fit", "Excellent fit", "b"),
            ("Motivated Learner", "Excellent fit", "Good fit", "a"),
        ],
        "intro": "IXL and Prodigy both supplement your primary math curriculum, but they take completely different approaches. Your child's personality and your goals determine which fits better.",
        "sections": [
            ("When to Choose IXL", "<p><strong>IXL is the better choice for serious, targeted practice.</strong> Its diagnostic tool identifies exact skill gaps, and the adaptive practice systematically closes them. Parent reports show precisely which skills are mastered and which need work.</p><p>IXL works best for self-motivated learners who do not need gamification to stay engaged. If your child will sit down and do focused practice without complaint, IXL delivers more educational value per minute than Prodigy.</p>"),
            ("When to Choose Prodigy", "<p><strong>Prodigy is the better choice for reluctant math learners.</strong> If getting your child to practice math is a daily battle, Prodigy transforms that fight into enthusiastic play. The RPG format wraps math practice in a game that kids actually want to play.</p><p>Prodigy also wins on price. The core game is completely free with all math content included. IXL requires a paid subscription for full access. If budget is tight, Prodigy provides free math practice that your child will willingly do.</p>"),
            ("Choosing by Age and Stage", "<p><strong>For K-3: Prodigy usually wins.</strong> Young learners respond better to game-based practice, and the math concepts at this level do not require IXL's sophisticated diagnostics.</p><p><strong>For grades 4-8: it depends on your child.</strong> Motivated learners benefit more from IXL's targeted approach. Reluctant learners engage better with Prodigy's game format.</p><p><strong>For grades 9-12: IXL wins.</strong> Prodigy only covers K-8, and older students need the diagnostic precision and standards alignment that IXL provides.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Choose Prodigy for reluctant learners and young kids who need math practice to feel like play. Choose IXL for motivated learners and older students who benefit from diagnostic precision and detailed skill tracking. If budget matters, Prodigy's free tier beats IXL's paid subscription for basic math practice.",
        "cta_a": ("Start IXL Free Trial", "https://www.ixl.com", "secondary"),
        "cta_b": ("Play Prodigy Free", "https://www.prodigygame.com", "primary"),
        "page_a": "ixl-page",
        "page_b": "prodigy-page",
        "faqs": [
            ("Is IXL or Prodigy better for homeschool?", "IXL is better for targeted skill practice with diagnostics. Prodigy is better for reluctant learners who need math to feel like a game. Neither is a standalone curriculum. Choose based on your child's motivation level and your budget."),
            ("Is Prodigy free and IXL paid?", "Prodigy's core math game is free with all educational content. IXL requires a subscription ($9.95-19.95/mo) for full access. Prodigy's premium ($8.95/mo) only unlocks cosmetic game items, not educational features."),
            ("Can I use both IXL and Prodigy?", "Yes, some families use IXL for structured skill-gap practice and Prodigy as a fun reward activity. This combines diagnostic precision with engagement. However, this may be more screen time than most families want for math alone."),
        ],
    },
    {
        "slug": "epic-vs-kindle-kids",
        "meta_title": "Epic! vs Kindle Kids for Homeschool Reading (2025) | Skip School",
        "meta_desc": "Epic! vs Kindle for homeschool reading. Compare digital libraries, pricing, age ranges, and features. Find the best reading platform for your homeschool child.",
        "h1_a": "Epic!", "h1_b": "Kindle Kids",
        "subtitle": "Two popular digital reading options for homeschool families. One is an app-based library, the other is a dedicated reading device with curated content.",
        "table_rows": [
            ("Price", "Free (educators) / $9.99 mo", "$99-149 device + $4.99/mo", "a"),
            ("Book Count", "40,000+", "Thousands + Kindle Unlimited", "a"),
            ("Age Range", "12 and under", "3-12+", "b"),
            ("Read-to-Me", "Yes", "Yes (Audible)", ""),
            ("Device", "Any tablet/computer", "Dedicated e-reader", ""),
            ("Screen Type", "LCD (backlit)", "E-ink (paper-like)", "b"),
            ("Eye Strain", "Higher (LCD)", "Lower (e-ink)", "b"),
            ("Offline Access", "Paid only", "Yes", "b"),
            ("Parent Controls", "Basic", "Excellent", "b"),
            ("For Educators", "Free account", "No special pricing", "a"),
        ],
        "intro": "Digital reading is a core part of most homeschool programs. Epic! and Kindle Kids take different approaches to getting books into your child's hands.",
        "sections": [
            ("When to Choose Epic!", "<p><strong>Epic! is the better choice for breadth and budget.</strong> With 40,000+ titles and free educator access for homeschool parents, Epic! provides an enormous library at zero cost. The app-based format works on any tablet or computer your family already owns.</p><p>Epic! excels at exploration. When your child finishes a book and wants something similar, or when you are doing a unit study and need books on ancient Egypt, Epic!'s library usually has what you need immediately.</p>"),
            ("When to Choose Kindle Kids", "<p><strong>Kindle Kids is the better choice for eye health and deep reading.</strong> The e-ink display eliminates the eye strain of backlit screens, which matters when your child reads for extended periods. A dedicated reading device also removes the distraction of games and apps.</p><p>Kindle's parental controls are more robust, and the device-only format means your child is reading, not switching to YouTube. For families concerned about screen time quality, a Kindle is a screen that only does one thing: read.</p>"),
            ("Which Format Builds Better Readers?", "<p><strong>The best reading platform is the one your child uses.</strong> If your child happily reads on a Kindle for 30 minutes a day, the Kindle is the right choice. If they prefer the interactive, colorful Epic! interface, go with that.</p><p>Many families use both: Epic! on a shared tablet for browsing and discovery, and a Kindle for dedicated reading time. The key is consistent daily reading, regardless of the platform.</p>"),
        ],
        "verdict_title": "Our Verdict",
        "verdict": "Start with Epic! because it is free for educators and works on devices you already own. If your child reads heavily (30+ minutes daily) and you want to reduce eye strain, invest in a Kindle Kids device. The e-ink screen is genuinely better for extended reading, but the upfront cost only makes sense for committed readers.",
        "cta_a": ("Get Epic! Free", "https://www.getepic.com", "primary"),
        "cta_b": ("See Kindle Kids", "https://www.amazon.com/kindle-kids", "secondary"),
        "page_a": "epic-books-page",
        "page_b": "",
        "faqs": [
            ("Is Epic! or Kindle better for homeschool reading?", "Epic! is better for variety and cost (free for educators, 40,000+ books). Kindle Kids is better for eye health and focused reading (e-ink display, no app distractions). Many families use Epic! for browsing and Kindle for dedicated reading time."),
            ("Is Epic! really free for homeschool families?", "Epic! offers free educator accounts for homeschool parents with unlimited reading during school hours. The terms have changed over time, so check current availability when you sign up."),
            ("Does reading on screens hurt my child's eyes?", "Backlit LCD screens (tablets, Epic!) can contribute to eye strain with extended use. E-ink screens (Kindle) are designed to mimic paper and produce significantly less eye strain. For heavy readers, e-ink is the healthier choice."),
        ],
    },
]

def build_table(rows, name_a, name_b):
    html = f'''        <table class="compare-table">
            <tr><th>Feature</th><th>{name_a}</th><th>{name_b}</th></tr>\n'''
    for label, val_a, val_b, winner in rows:
        cls_a = ' class="winner"' if winner == "a" else ''
        cls_b = ' class="winner"' if winner == "b" else ''
        html += f'            <tr><td>{label}</td><td{cls_a}>{val_a}</td><td{cls_b}>{val_b}</td></tr>\n'
    html += '        </table>'
    return html

def build_faq_schema(faqs):
    entries = []
    for q, a in faqs:
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"')
        entries.append(f'{{"@type":"Question","name":"{q_esc}","acceptedAnswer":{{"@type":"Answer","text":"{a_esc}"}}}}')
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(entries)}]}}
</script>'''

def build_page(comp):
    table_html = build_table(comp["table_rows"], comp["h1_a"], comp["h1_b"])
    faq_schema = build_faq_schema(comp["faqs"])

    sections_html = ""
    for title, body in comp["sections"]:
        sections_html += f'\n            <h2>{title}</h2>\n            {body}\n'

    faq_html = ""
    for q, a in comp["faqs"]:
        faq_html += f'''        <div class="faq-item">
            <h3>{q}</h3>
            <p>{a}</p>
        </div>\n'''

    cta_a_text, cta_a_url, cta_a_cls = comp["cta_a"]
    cta_b_text, cta_b_url, cta_b_cls = comp["cta_b"]

    page_links = ""
    if comp["page_a"]:
        page_links += f'            <p style="font-size:13px;color:var(--text-light);margin-top:8px;">Read our full review: <a href="/{comp["page_a"]}" style="color:var(--navy);font-weight:600;border-bottom:1px solid var(--yellow);">{comp["h1_a"]}</a>'
    if comp["page_b"]:
        page_links += f' | <a href="/{comp["page_b"]}" style="color:var(--navy);font-weight:600;border-bottom:1px solid var(--yellow);">{comp["h1_b"]}</a>'
    if page_links:
        page_links += '</p>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp["meta_title"]}</title>
    <meta name="description" content="{comp["meta_desc"]}">
    <link rel="canonical" href="https://skipschool.ai/{comp["slug"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&display=swap" rel="stylesheet">
    <style>
        {CSS}
    </style>
    {faq_schema}
</head>
<body>

    {NAV_HTML}

    <div class="vs-hero"><div class="wrap">
        <h1>{comp["h1_a"]} <span>vs</span> {comp["h1_b"]}</h1>
        <p>{comp["subtitle"]}</p>
    </div></div>

    <div class="vs-content">
        <p>{comp["intro"]}</p>

        <h2>Side-by-Side Comparison</h2>
{table_html}
{sections_html}
        <div class="verdict-box">
            <h3>{comp["verdict_title"]}</h3>
            <p>{comp["verdict"]}</p>
        </div>

        <div class="cta-row">
            <a href="{cta_a_url}" target="_blank" rel="noopener" class="cta-btn {cta_a_cls}">{cta_a_text} &rarr;</a>
            <a href="{cta_b_url}" target="_blank" rel="noopener" class="cta-btn {cta_b_cls}">{cta_b_text} &rarr;</a>
        </div>

{page_links}
    </div>

    <section class="faq-section" style="padding: 0 20px 28px;">
        <h2>Frequently Asked Questions</h2>
{faq_html}    </section>

    {FOOTER_HTML}

</body></html>'''


count = 0
for comp in COMPARISONS:
    html = build_page(comp)
    filepath = os.path.join(SRC, f'{comp["slug"]}.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f'  Created: {comp["slug"]}.html')

print(f'\nDone! Created {count} comparison pages.')
