import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = r'C:\ai-projects\skip-school\site\files\src'

# All articles with slugs and short display titles
articles = {
    '05-ai-curriculum-builder': 'How to Build a Custom AI Curriculum',
    '06-chatgpt-vs-claude-homeschool': 'ChatGPT vs Claude for Homeschooling',
    '07-socialization-myth': 'The Socialization Question',
    '08-morning-routine-ai': 'AI-Powered Homeschool Morning Routine',
    '09-first-week-ai-homeschool': 'Your First Week Using AI for Homeschool',
    '10-khan-academy-guide': 'Khan Academy for Homeschool: Setup Guide',
    '11-homeschool-on-budget': 'How to Homeschool for $0',
    '12-ai-reading-list-by-age': 'AI-Curated Reading Lists by Age',
    '13-teach-kids-use-ai': 'How to Teach Kids to Use AI Responsibly',
    '14-homeschool-field-trip-ideas': '25 Field Trip Ideas for Homeschoolers',
    '15-charlotte-mason-ai': 'Charlotte Mason + AI',
    '16-classical-education-ai': 'Classical Education Meets AI',
    '17-homeschool-writing-ai': 'How to Teach Writing With AI',
    '18-ai-science-experiments': '20 AI-Designed Science Experiments',
    '19-high-school-ai': 'Homeschooling High School With AI',
    '20-special-needs-ai': 'AI Tools for Special Needs Homeschooling',
    '21-ai-math-help': 'AI for Math Help',
    '22-screen-time-balance': 'AI Without the Screen Time Guilt',
    '23-state-homeschool-laws': 'Homeschool Laws by State (2026)',
    '24-homeschool-co-op-guide': 'How to Find a Homeschool Co-op',
    '25-ai-for-reluctant-learner': 'AI for the Reluctant Learner',
    '26-homeschool-assessment': 'How to Know If Your Kid Is Learning',
    '27-ai-history-alive': 'Making History Alive With AI',
    '28-best-free-resources': '15 Best Free Homeschool Resources',
    '29-ai-art-music-homeschool': 'Teaching Art and Music With AI',
    '30-summer-learning-ai': 'Summer Learning With AI',
    '31-college-admissions-homeschool': 'Homeschool to College Admissions',
    '32-ai-foreign-language': 'Teaching Foreign Languages With AI',
    '33-ai-financial-literacy-kids': 'Teaching Kids Financial Literacy With AI',
    '34-homeschool-burnout': 'Homeschool Burnout: How to Recover',
    '35-ai-coding-kids': 'Teaching Kids to Code With AI',
    '36-unschool-ai': 'Can You Unschool With AI?',
    '37-new-to-homeschool': 'New to Homeschool? Start Here',
    '38-ai-physical-education': 'PE at Home With AI',
    '39-dual-enrollment-guide': 'Dual Enrollment for Homeschoolers',
    '40-what-alpha-school-gets-right-wrong': 'What Alpha School Gets Right (and Wrong)',
    '41-ai-geography-lessons': 'Teaching Geography With AI',
    '42-ai-report-cards': 'How to Create Homeschool Report Cards',
    '43-weekly-newsletter-sample': 'This Week in AI Homeschooling',
    '44-ai-homeschool-myths': '7 AI Homeschool Myths Busted',
    '45-homeschool-schedule-templates': 'Homeschool Schedule Templates',
    '46-ai-homeschool-faq': 'AI Homeschooling FAQ',
    '47-ai-projects-by-age': '30 AI Projects by Age Group',
    '48-ai-homeschool-mistakes-first-year': '10 First-Year Homeschool Mistakes',
    '49-bible-study-ai': 'Using AI for Bible Study',
    '50-ai-prompts-homeschool': '50 AI Prompts for Homeschool',
    '50-eclectic-homeschool-ai': "The Eclectic Homeschooler's AI Toolkit",
    '51-montessori-ai': 'Montessori + AI',
    '52-ai-vocabulary-builder': 'Build Vocabulary 3x Faster With AI',
    '53-homeschool-record-keeping': 'Homeschool Record-Keeping Guide',
    '54-ai-handwriting-practice': 'AI Handwriting Practice',
    '55-ai-test-prep': 'AI-Powered Test Prep',
    '56-ai-debate-critical-thinking': 'Teaching Critical Thinking With AI',
    '57-ai-learning-disabilities-detection': 'Signs of a Learning Difference',
    '58-homeschool-with-toddlers': 'How to Homeschool With a Toddler',
    '59-world-history-ai-unit': 'Ancient Civilizations Unit (AI-Generated)',
    '60-ai-executive-function': 'Building Executive Function With AI',
    '61-ai-stem-girls': 'Encouraging Girls in STEM With AI',
    '62-ai-reading-comprehension': 'Boost Reading Comprehension With AI',
    '63-homeschool-dad-guide': 'The Homeschool Dad Guide',
    '64-ai-nature-journal': 'AI-Guided Nature Journal',
    '65-gifted-homeschool-ai': 'Homeschooling Gifted Kids With AI',
    '66-ai-grammar-painless': 'Painless Grammar With AI',
    'ai-homeschool-complete-guide': 'The Complete AI Homeschool Guide (2026)',
    'texas-esa-guide': 'Texas ESA Guide for Homeschoolers',
    'homeschool-kids-ai-five-years-ahead': 'Why AI Homeschool Kids Are 5 Years Ahead',
    'khan-academy-page': 'Khan Academy + Khanmigo Review',
}

# Topical clusters - each article maps to 4 related articles
clusters = {
    # Getting Started cluster
    '09-first-week-ai-homeschool': ['ai-homeschool-complete-guide', '37-new-to-homeschool', '05-ai-curriculum-builder', '08-morning-routine-ai'],
    '37-new-to-homeschool': ['09-first-week-ai-homeschool', 'ai-homeschool-complete-guide', '23-state-homeschool-laws', '48-ai-homeschool-mistakes-first-year'],
    'ai-homeschool-complete-guide': ['09-first-week-ai-homeschool', '05-ai-curriculum-builder', '50-ai-prompts-homeschool', 'homeschool-kids-ai-five-years-ahead'],
    '48-ai-homeschool-mistakes-first-year': ['37-new-to-homeschool', '09-first-week-ai-homeschool', '34-homeschool-burnout', '05-ai-curriculum-builder'],

    # Curriculum & Planning
    '05-ai-curriculum-builder': ['ai-homeschool-complete-guide', '08-morning-routine-ai', '45-homeschool-schedule-templates', '50-ai-prompts-homeschool'],
    '08-morning-routine-ai': ['05-ai-curriculum-builder', '45-homeschool-schedule-templates', '09-first-week-ai-homeschool', '22-screen-time-balance'],
    '45-homeschool-schedule-templates': ['08-morning-routine-ai', '05-ai-curriculum-builder', '58-homeschool-with-toddlers', '34-homeschool-burnout'],
    '50-ai-prompts-homeschool': ['ai-homeschool-complete-guide', '05-ai-curriculum-builder', '47-ai-projects-by-age', '09-first-week-ai-homeschool'],

    # Methods
    '15-charlotte-mason-ai': ['16-classical-education-ai', '51-montessori-ai', '36-unschool-ai', '50-eclectic-homeschool-ai'],
    '16-classical-education-ai': ['15-charlotte-mason-ai', '51-montessori-ai', '50-eclectic-homeschool-ai', '56-ai-debate-critical-thinking'],
    '51-montessori-ai': ['15-charlotte-mason-ai', '16-classical-education-ai', '36-unschool-ai', '64-ai-nature-journal'],
    '36-unschool-ai': ['51-montessori-ai', '50-eclectic-homeschool-ai', '15-charlotte-mason-ai', '22-screen-time-balance'],
    '50-eclectic-homeschool-ai': ['15-charlotte-mason-ai', '16-classical-education-ai', '36-unschool-ai', '05-ai-curriculum-builder'],

    # Subjects - ELA
    '17-homeschool-writing-ai': ['66-ai-grammar-painless', '62-ai-reading-comprehension', '52-ai-vocabulary-builder', '12-ai-reading-list-by-age'],
    '66-ai-grammar-painless': ['17-homeschool-writing-ai', '52-ai-vocabulary-builder', '62-ai-reading-comprehension', '54-ai-handwriting-practice'],
    '62-ai-reading-comprehension': ['12-ai-reading-list-by-age', '17-homeschool-writing-ai', '52-ai-vocabulary-builder', '66-ai-grammar-painless'],
    '52-ai-vocabulary-builder': ['62-ai-reading-comprehension', '17-homeschool-writing-ai', '66-ai-grammar-painless', '12-ai-reading-list-by-age'],
    '12-ai-reading-list-by-age': ['62-ai-reading-comprehension', '52-ai-vocabulary-builder', '17-homeschool-writing-ai', '47-ai-projects-by-age'],
    '54-ai-handwriting-practice': ['66-ai-grammar-painless', '17-homeschool-writing-ai', '52-ai-vocabulary-builder', '47-ai-projects-by-age'],

    # Subjects - Math & Science
    '21-ai-math-help': ['18-ai-science-experiments', '55-ai-test-prep', '10-khan-academy-guide', '35-ai-coding-kids'],
    '18-ai-science-experiments': ['21-ai-math-help', '64-ai-nature-journal', '47-ai-projects-by-age', '61-ai-stem-girls'],
    '35-ai-coding-kids': ['21-ai-math-help', '61-ai-stem-girls', '47-ai-projects-by-age', '13-teach-kids-use-ai'],
    '61-ai-stem-girls': ['35-ai-coding-kids', '18-ai-science-experiments', '21-ai-math-help', '47-ai-projects-by-age'],

    # Subjects - History & Social Studies
    '27-ai-history-alive': ['59-world-history-ai-unit', '41-ai-geography-lessons', '56-ai-debate-critical-thinking', '47-ai-projects-by-age'],
    '59-world-history-ai-unit': ['27-ai-history-alive', '41-ai-geography-lessons', '50-ai-prompts-homeschool', '47-ai-projects-by-age'],
    '41-ai-geography-lessons': ['27-ai-history-alive', '59-world-history-ai-unit', '14-homeschool-field-trip-ideas', '47-ai-projects-by-age'],

    # Subjects - Arts, Languages, Other
    '29-ai-art-music-homeschool': ['32-ai-foreign-language', '64-ai-nature-journal', '47-ai-projects-by-age', '38-ai-physical-education'],
    '32-ai-foreign-language': ['29-ai-art-music-homeschool', '52-ai-vocabulary-builder', '50-ai-prompts-homeschool', '47-ai-projects-by-age'],
    '33-ai-financial-literacy-kids': ['35-ai-coding-kids', '56-ai-debate-critical-thinking', '47-ai-projects-by-age', '13-teach-kids-use-ai'],
    '38-ai-physical-education': ['30-summer-learning-ai', '22-screen-time-balance', '45-homeschool-schedule-templates', '14-homeschool-field-trip-ideas'],
    '49-bible-study-ai': ['15-charlotte-mason-ai', '16-classical-education-ai', '50-ai-prompts-homeschool', '05-ai-curriculum-builder'],
    '64-ai-nature-journal': ['18-ai-science-experiments', '14-homeschool-field-trip-ideas', '51-montessori-ai', '29-ai-art-music-homeschool'],

    # Tools & Tech
    '10-khan-academy-guide': ['khan-academy-page', '06-chatgpt-vs-claude-homeschool', '28-best-free-resources', '21-ai-math-help'],
    'khan-academy-page': ['10-khan-academy-guide', '06-chatgpt-vs-claude-homeschool', '28-best-free-resources', '11-homeschool-on-budget'],
    '06-chatgpt-vs-claude-homeschool': ['10-khan-academy-guide', '28-best-free-resources', '13-teach-kids-use-ai', '50-ai-prompts-homeschool'],
    '28-best-free-resources': ['11-homeschool-on-budget', '10-khan-academy-guide', '06-chatgpt-vs-claude-homeschool', '50-ai-prompts-homeschool'],
    '11-homeschool-on-budget': ['28-best-free-resources', '10-khan-academy-guide', '53-homeschool-record-keeping', '05-ai-curriculum-builder'],
    '13-teach-kids-use-ai': ['22-screen-time-balance', '06-chatgpt-vs-claude-homeschool', '44-ai-homeschool-myths', '50-ai-prompts-homeschool'],
    '22-screen-time-balance': ['13-teach-kids-use-ai', '38-ai-physical-education', '44-ai-homeschool-myths', '08-morning-routine-ai'],
    '40-what-alpha-school-gets-right-wrong': ['06-chatgpt-vs-claude-homeschool', 'homeschool-kids-ai-five-years-ahead', '10-khan-academy-guide', '44-ai-homeschool-myths'],

    # Age-Specific
    '19-high-school-ai': ['39-dual-enrollment-guide', '31-college-admissions-homeschool', '55-ai-test-prep', '35-ai-coding-kids'],
    '39-dual-enrollment-guide': ['19-high-school-ai', '31-college-admissions-homeschool', '55-ai-test-prep', '23-state-homeschool-laws'],
    '31-college-admissions-homeschool': ['19-high-school-ai', '39-dual-enrollment-guide', '42-ai-report-cards', '53-homeschool-record-keeping'],
    '58-homeschool-with-toddlers': ['45-homeschool-schedule-templates', '34-homeschool-burnout', '08-morning-routine-ai', '37-new-to-homeschool'],
    '47-ai-projects-by-age': ['50-ai-prompts-homeschool', '18-ai-science-experiments', '35-ai-coding-kids', '30-summer-learning-ai'],
    '65-gifted-homeschool-ai': ['20-special-needs-ai', '47-ai-projects-by-age', '19-high-school-ai', '05-ai-curriculum-builder'],

    # Special Needs & Learning
    '20-special-needs-ai': ['57-ai-learning-disabilities-detection', '25-ai-for-reluctant-learner', '65-gifted-homeschool-ai', '60-ai-executive-function'],
    '57-ai-learning-disabilities-detection': ['20-special-needs-ai', '60-ai-executive-function', '25-ai-for-reluctant-learner', '26-homeschool-assessment'],
    '25-ai-for-reluctant-learner': ['20-special-needs-ai', '60-ai-executive-function', '22-screen-time-balance', '47-ai-projects-by-age'],
    '60-ai-executive-function': ['20-special-needs-ai', '57-ai-learning-disabilities-detection', '25-ai-for-reluctant-learner', '45-homeschool-schedule-templates'],

    # Assessment & Records
    '26-homeschool-assessment': ['42-ai-report-cards', '53-homeschool-record-keeping', '55-ai-test-prep', '05-ai-curriculum-builder'],
    '42-ai-report-cards': ['26-homeschool-assessment', '53-homeschool-record-keeping', '31-college-admissions-homeschool', '23-state-homeschool-laws'],
    '53-homeschool-record-keeping': ['42-ai-report-cards', '26-homeschool-assessment', '23-state-homeschool-laws', '31-college-admissions-homeschool'],
    '55-ai-test-prep': ['26-homeschool-assessment', '19-high-school-ai', '21-ai-math-help', '62-ai-reading-comprehension'],

    # Community & Lifestyle
    '07-socialization-myth': ['24-homeschool-co-op-guide', '14-homeschool-field-trip-ideas', '44-ai-homeschool-myths', '38-ai-physical-education'],
    '24-homeschool-co-op-guide': ['07-socialization-myth', '14-homeschool-field-trip-ideas', '23-state-homeschool-laws', '28-best-free-resources'],
    '14-homeschool-field-trip-ideas': ['07-socialization-myth', '24-homeschool-co-op-guide', '30-summer-learning-ai', '64-ai-nature-journal'],
    '34-homeschool-burnout': ['58-homeschool-with-toddlers', '48-ai-homeschool-mistakes-first-year', '45-homeschool-schedule-templates', '63-homeschool-dad-guide'],
    '63-homeschool-dad-guide': ['34-homeschool-burnout', '37-new-to-homeschool', '48-ai-homeschool-mistakes-first-year', '07-socialization-myth'],
    '30-summer-learning-ai': ['14-homeschool-field-trip-ideas', '47-ai-projects-by-age', '64-ai-nature-journal', '38-ai-physical-education'],

    # Legal & State
    '23-state-homeschool-laws': ['texas-esa-guide', '53-homeschool-record-keeping', '37-new-to-homeschool', '42-ai-report-cards'],
    'texas-esa-guide': ['23-state-homeschool-laws', '11-homeschool-on-budget', '37-new-to-homeschool', '28-best-free-resources'],

    # Meta / Overview
    '44-ai-homeschool-myths': ['46-ai-homeschool-faq', '13-teach-kids-use-ai', '07-socialization-myth', 'homeschool-kids-ai-five-years-ahead'],
    '46-ai-homeschool-faq': ['44-ai-homeschool-myths', 'ai-homeschool-complete-guide', '09-first-week-ai-homeschool', '37-new-to-homeschool'],
    '43-weekly-newsletter-sample': ['50-ai-prompts-homeschool', 'ai-homeschool-complete-guide', '47-ai-projects-by-age', '28-best-free-resources'],
    'homeschool-kids-ai-five-years-ahead': ['ai-homeschool-complete-guide', '44-ai-homeschool-myths', '13-teach-kids-use-ai', '06-chatgpt-vs-claude-homeschool'],

    # Critical thinking
    '56-ai-debate-critical-thinking': ['27-ai-history-alive', '17-homeschool-writing-ai', '13-teach-kids-use-ai', '16-classical-education-ai'],
}

# Related articles HTML block
RELATED_HTML_TEMPLATE = """
        <div class="related-articles" style="margin-top: 48px; padding: 32px; background: #f8f6f2; border-radius: 12px; border: 1px solid #e8e4de;">
            <h3 style="font-family: 'Fraunces', serif; font-size: 22px; color: #0d203b; margin-bottom: 20px;">Keep Reading</h3>
            <div style="display: grid; gap: 12px;">
{links}
            </div>
        </div>
"""

LINK_TEMPLATE = '                <a href="/{slug}" style="display: block; padding: 14px 18px; background: white; border-radius: 8px; border: 1px solid #e8e4de; color: #0d203b; font-weight: 500; font-size: 15px; text-decoration: none; transition: border-color 0.2s;">{title}</a>'

modified = 0
skipped = 0

for slug in articles:
    filepath = os.path.join(SRC, slug + '.html')
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {slug}")
        skipped += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has related articles
    if 'related-articles' in content:
        print(f"  SKIP (already has links): {slug}")
        skipped += 1
        continue

    # Get related articles for this slug
    related = clusters.get(slug)
    if not related:
        print(f"  SKIP (no cluster mapping): {slug}")
        skipped += 1
        continue

    # Build links HTML
    links = []
    for rel_slug in related:
        if rel_slug in articles:
            links.append(LINK_TEMPLATE.format(slug=rel_slug, title=articles[rel_slug]))

    if not links:
        continue

    links_html = '\n'.join(links)
    related_block = RELATED_HTML_TEMPLATE.format(links=links_html)

    # Insert before </article>
    if '</article>' in content:
        content = content.replace('</article>', related_block + '\n    </article>', 1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified += 1
        print(f"  OK: {slug} (+{len(links)} links)")
    else:
        print(f"  SKIP (no </article> tag): {slug}")
        skipped += 1

print(f"\nDone: {modified} modified, {skipped} skipped")
