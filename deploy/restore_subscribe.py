#!/usr/bin/env python3
"""Restore subscribe page from backup with Beehiiv API integration."""
import os, re

DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DEPLOY_DIR)
BACKUP = os.path.join(ROOT, "backups", "subscribe (10).html")
REPO = os.path.join(os.path.dirname(ROOT), "skipschool-repo")

content = open(BACKUP, "r", encoding="utf-8").read()

# Fix the title
content = content.replace(
    "Skip School \u2014 The AI Playbook for Homeschool Parents</title>",
    "Subscribe to Skip School | The AI Playbook for Homeschool Parents</title>"
)

# Add meta description + canonical after </title>
meta_inject = """
    <meta name="description" content="Get one email a week with AI tools, tested prompts, and honest advice for homeschool parents. Free forever.">
    <link rel="canonical" href="https://skipschool.ai/subscribe">
    <meta property="og:title" content="Subscribe to Skip School | The AI Playbook for Homeschool Parents">
    <meta property="og:description" content="One email a week with AI tools, tested prompts, and honest advice for homeschool parents.">
    <meta property="og:url" content="https://skipschool.ai/subscribe">
    <meta property="og:type" content="website">"""

# Insert after </title>
content = content.replace("</title>", "</title>" + meta_inject, 1)

# Add the form submission JS before </body>
js_block = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var emailInput = document.querySelector('.email-input');
    var ctaBtn = document.querySelector('.cta-btn');
    var formRow = document.querySelector('.form-row');

    function handleSubscribe() {
        var email = emailInput.value.trim();
        if (!email || email.indexOf('@') === -1) {
            emailInput.style.borderColor = '#c0392b';
            emailInput.setAttribute('placeholder', 'Please enter a valid email');
            return;
        }

        ctaBtn.textContent = 'Subscribing...';
        ctaBtn.disabled = true;

        fetch('/api/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, source: 'subscribe-page' })
        })
        .then(function(res) { return res.json().then(function(d) { return { ok: res.ok, data: d }; }); })
        .then(function(result) {
            if (result.ok) {
                formRow.innerHTML = '<div style="background:#1a6b4a;color:#fff;padding:16px 24px;border-radius:8px;font-weight:600;font-size:16px;text-align:center;">You are in! Check your inbox for a welcome email.</div>';
            } else {
                ctaBtn.textContent = 'Try Again';
                ctaBtn.disabled = false;
                emailInput.style.borderColor = '#c0392b';
            }
        })
        .catch(function() {
            ctaBtn.textContent = 'Try Again';
            ctaBtn.disabled = false;
        });
    }

    ctaBtn.addEventListener('click', handleSubscribe);
    emailInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') handleSubscribe();
    });
});
</script>
"""

content = content.replace("</body>", js_block + "</body>")

outpath = os.path.join(REPO, "subscribe.html")
with open(outpath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Restored subscribe.html ({len(content):,} chars)")
print("  - Original phone mockup design from backup")
print("  - Added /api/subscribe form submission JS")
print("  - Fixed title, meta description, canonical, OG tags")
