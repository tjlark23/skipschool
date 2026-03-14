#!/usr/bin/env python3
"""Generate the Ashley Larkin author / about page."""
import os

DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DEPLOY_DIR)
SRC = os.path.join(ROOT, "site", "files", "src")

nav = open(os.path.join(DEPLOY_DIR, "nav_snippet.txt"), "r", encoding="utf-8").read()
footer = open(os.path.join(DEPLOY_DIR, "footer_snippet.txt"), "r", encoding="utf-8").read()

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Ashley Larkin | Skip School - AI Homeschool Expert</title>
  <meta name="description" content="Meet Ashley Larkin, founder of Skip School. Former educator turned homeschool parent, helping families across all 50 states use AI tools to build personalized learning plans.">
  <link rel="canonical" href="https://skipschool.ai/about-ashley-larkin">
  <meta property="og:title" content="About Ashley Larkin | Skip School">
  <meta property="og:description" content="Meet Ashley Larkin, founder of Skip School. Former educator turned homeschool parent, helping families use AI to personalize education.">
  <meta property="og:url" content="https://skipschool.ai/about-ashley-larkin">
  <meta property="og:type" content="profile">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Ashley Larkin",
    "jobTitle": "Founder",
    "worksFor": {{
      "@type": "Organization",
      "name": "Skip School",
      "url": "https://skipschool.ai"
    }},
    "description": "Former educator turned homeschool parent. Founder of Skip School, helping families across all 50 states use AI tools to build personalized learning plans.",
    "url": "https://skipschool.ai/about-ashley-larkin",
    "sameAs": []
  }}
  </script>
  <style>
    :root {{
      --navy: #0d203b;
      --yellow: #fbc926;
      --cream: #fdf8ef;
      --text: #1a1a1a;
      --muted: #5a5a5a;
      --border: #e5e5e5;
      --radius: 12px;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: "DM Sans", sans-serif; color: var(--text); background: var(--cream); line-height: 1.7; }}
    h1, h2, h3 {{ font-family: "Fraunces", serif; }}

    .author-hero {{
      background: var(--navy);
      color: #fff;
      padding: 80px 20px 60px;
      text-align: center;
    }}
    .author-hero .container {{ max-width: 800px; margin: 0 auto; }}
    .author-avatar {{
      width: 140px; height: 140px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--yellow), #f0a800);
      margin: 0 auto 24px;
      display: flex; align-items: center; justify-content: center;
      font-size: 56px; font-family: "Fraunces", serif; color: var(--navy); font-weight: 700;
    }}
    .author-hero h1 {{ font-size: 2.4rem; margin-bottom: 8px; }}
    .author-hero .role {{ color: var(--yellow); font-size: 1.1rem; font-weight: 500; margin-bottom: 16px; }}
    .author-hero .tagline {{ font-size: 1.15rem; opacity: 0.9; max-width: 600px; margin: 0 auto; }}

    .author-body {{ max-width: 800px; margin: 0 auto; padding: 48px 20px 60px; }}

    .bio-section {{ margin-bottom: 40px; }}
    .bio-section h2 {{ font-size: 1.6rem; color: var(--navy); margin-bottom: 16px; }}
    .bio-section p {{ margin-bottom: 16px; color: var(--text); font-size: 1.05rem; }}

    .credentials-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px; margin: 32px 0 40px;
    }}
    .credential-card {{
      background: #fff; border: 1px solid var(--border); border-radius: var(--radius);
      padding: 24px; text-align: center;
    }}
    .credential-card .icon {{ font-size: 2rem; margin-bottom: 8px; }}
    .credential-card h3 {{ font-size: 1rem; color: var(--navy); margin-bottom: 4px; }}
    .credential-card p {{ font-size: 0.9rem; color: var(--muted); }}

    .topics-list {{ list-style: none; display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0 40px; }}
    .topics-list li {{
      background: var(--navy); color: #fff; padding: 8px 16px;
      border-radius: 20px; font-size: 0.9rem; font-weight: 500;
    }}

    .articles-section {{ margin-bottom: 40px; }}
    .articles-section h2 {{ font-size: 1.6rem; color: var(--navy); margin-bottom: 20px; }}
    .article-list {{ list-style: none; }}
    .article-list li {{ margin-bottom: 12px; }}
    .article-list a {{
      color: var(--navy); font-weight: 500; font-size: 1.05rem;
      text-decoration: none; border-bottom: 2px solid var(--yellow);
      transition: color 0.2s;
    }}
    .article-list a:hover {{ color: #1a3a6a; }}

    .cta-box {{
      background: var(--navy); color: #fff; border-radius: var(--radius);
      padding: 40px; text-align: center; margin-top: 48px;
    }}
    .cta-box h2 {{ font-size: 1.5rem; margin-bottom: 12px; color: #fff; }}
    .cta-box p {{ margin-bottom: 20px; opacity: 0.9; }}
    .cta-box a {{
      display: inline-block; background: var(--yellow); color: var(--navy);
      padding: 14px 32px; border-radius: 8px; font-weight: 700;
      text-decoration: none; font-size: 1rem;
    }}

    @media (max-width: 600px) {{
      .author-hero h1 {{ font-size: 1.8rem; }}
      .credentials-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
{nav}

  <section class="author-hero">
    <div class="container">
      <div class="author-avatar">AL</div>
      <h1>Ashley Larkin</h1>
      <p class="role">Founder, Skip School</p>
      <p class="tagline">Former educator turned homeschool parent, helping families across all 50 states use AI tools to build personalized learning plans for their kids.</p>
    </div>
  </section>

  <div class="author-body">

    <div class="bio-section">
      <h2>My Story</h2>
      <p>I spent six years teaching in public schools before becoming a homeschool parent. When my oldest started struggling with the one-size-fits-all approach, I knew there had to be a better way. I pulled my kids out, built our own curriculum, and discovered that AI tools could do what no single textbook or teacher ever could: adapt to each child in real time.</p>
      <p>Skip School started as a blog where I shared the prompts and workflows I was using with ChatGPT and Claude to plan our weeks. Within months, thousands of parents were reading along. Today, Skip School is a national resource serving homeschool families in every state, with practical guides, tool reviews, and curriculum templates that make AI-powered homeschooling accessible to everyone.</p>
      <p>I believe every parent can give their child a world-class education from home. You do not need a teaching degree. You do not need an expensive curriculum. You need curiosity, consistency, and the right tools. That is what Skip School is here to help with.</p>
    </div>

    <div class="credentials-grid">
      <div class="credential-card">
        <div class="icon">&#127979;</div>
        <h3>6 Years Teaching</h3>
        <p>Public school classroom experience before homeschooling</p>
      </div>
      <div class="credential-card">
        <div class="icon">&#127968;</div>
        <h3>Homeschool Parent</h3>
        <p>Teaching my own kids with AI-powered methods daily</p>
      </div>
      <div class="credential-card">
        <div class="icon">&#128218;</div>
        <h3>60+ Guides Published</h3>
        <p>Practical articles on AI homeschooling for every age</p>
      </div>
      <div class="credential-card">
        <div class="icon">&#127758;</div>
        <h3>50-State Coverage</h3>
        <p>Homeschool law guides and ESA info nationwide</p>
      </div>
    </div>

    <div class="bio-section">
      <h2>What I Write About</h2>
      <p>Every article on Skip School comes from real experience. I test the tools, try the prompts, and refine the workflows with my own kids before recommending them to you.</p>
      <ul class="topics-list">
        <li>AI Curriculum Design</li>
        <li>ChatGPT &amp; Claude for Parents</li>
        <li>Homeschool Methods</li>
        <li>State Laws &amp; ESAs</li>
        <li>Math &amp; STEM</li>
        <li>Reading &amp; Writing</li>
        <li>Special Needs</li>
        <li>College Prep</li>
        <li>Tool Reviews</li>
        <li>Scheduling &amp; Record-Keeping</li>
      </ul>
    </div>

    <div class="articles-section">
      <h2>Featured Guides</h2>
      <ul class="article-list">
        <li><a href="/ai-homeschool-complete-guide">The Complete Guide to AI-Powered Homeschooling</a></li>
        <li><a href="/50-ai-prompts-homeschool">50 AI Prompts Every Homeschool Parent Needs</a></li>
        <li><a href="/texas-esa-guide">Texas ESA Guide for Homeschool Families</a></li>
        <li><a href="/homeschool-kids-ai-five-years-ahead">Why Homeschool Kids Using AI Are 5 Years Ahead</a></li>
        <li><a href="/06-chatgpt-vs-claude-homeschool">ChatGPT vs Claude: Which AI Is Better for Homeschool?</a></li>
        <li><a href="/09-first-week-ai-homeschool">Your First Week of AI Homeschooling</a></li>
        <li><a href="/37-new-to-homeschool">Brand New to Homeschool? Start Here</a></li>
        <li><a href="/23-state-homeschool-laws">Homeschool Laws by State: What You Need to Know</a></li>
      </ul>
    </div>

    <div class="articles-section">
      <h2>Browse All Content</h2>
      <ul class="article-list">
        <li><a href="/articles-index">All Articles</a></li>
        <li><a href="/guides-index">All Guides</a></li>
        <li><a href="/tools-index">Tool Reviews</a></li>
        <li><a href="/directory-index">Tool Directory</a></li>
      </ul>
    </div>

    <div class="cta-box">
      <h2>Get Weekly AI Homeschool Tips</h2>
      <p>Join thousands of parents getting practical prompts, tool recommendations, and curriculum ideas every week.</p>
      <a href="/subscribe">Subscribe Free</a>
    </div>

  </div>

{footer}
</body>
</html>'''

outpath = os.path.join(SRC, "about-ashley-larkin.html")
with open(outpath, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Created {outpath} ({len(html):,} chars)")
