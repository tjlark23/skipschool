#!/usr/bin/env python3
"""Generate llms.txt for skipschool.ai from actual HTML files in the repo."""
import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

REPO = os.path.normpath('C:/ai-projects/skipschool-repo')
os.chdir(REPO)

base = 'https://skipschool.ai'
files = sorted([f for f in os.listdir('.') if f.endswith('.html') and f != '404.html'])

def get_title(filename):
    html = open(filename, encoding='utf-8').read()
    m = re.search(r'<title>([^<]+)</title>', html)
    if m:
        return m.group(1).split('|')[0].strip()
    return filename.replace('.html', '')

lines = [
    '# Skip School - skipschool.ai',
    '# The AI Playbook for Homeschool Parents',
    '',
    '## About',
    "Skip School helps homeschool parents use AI tools to personalize their kids' education. Weekly newsletter with tested prompts, honest tool reviews, and practical advice.",
    '',
    '## Key Pages',
    f'- Homepage: {base}/',
    f'- Subscribe: {base}/subscribe',
    f'- Complete Guide: {base}/ai-homeschool-complete-guide',
    f'- About the Author: {base}/about-ashley-larkin',
    '',
    '## Articles',
]

articles = [f for f in files if re.match(r'\d+-', f) or f in ('homeschool-kids-ai-five-years-ahead.html', 'ai-homeschool-complete-guide.html')]
for f in articles:
    slug = f.replace('.html', '')
    lines.append(f'- {get_title(f)}: {base}/{slug}')

lines.append('')
lines.append('## Tool Reviews')
for f in sorted(f for f in files if f.startswith('review-')):
    slug = f.replace('.html', '')
    lines.append(f'- {get_title(f)}: {base}/{slug}')

lines.append('')
lines.append('## Comparison Guides')
for f in sorted(f for f in files if '-vs-' in f):
    slug = f.replace('.html', '')
    lines.append(f'- {get_title(f)}: {base}/{slug}')

lines.append('')
lines.append('## State ESA Guides')
for f in sorted(f for f in files if f.endswith('-esa-guide.html')):
    slug = f.replace('.html', '')
    lines.append(f'- {get_title(f)}: {base}/{slug}')

lines.append('')
lines.append('## Directory')
for f in sorted(f for f in files if f.endswith('-page.html')):
    slug = f.replace('.html', '')
    lines.append(f'- {get_title(f)}: {base}/{slug}')

content = '\n'.join(lines) + '\n'
with open('llms.txt', 'w', encoding='utf-8') as fh:
    fh.write(content)

print(f'Generated llms.txt with {len(lines)} lines')
