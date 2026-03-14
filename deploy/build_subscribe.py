import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Read logo
with open('logo_horizontal.txt', 'r') as f:
    logo = f.read().strip()
with open('nl_logo.txt', 'r') as f:
    nl_logo = f.read().strip()

# Read avatars
avatars = []
for i in range(5):
    with open(f'avatar_{i}.txt', 'r') as f:
        avatars.append(f.read().strip())

# Build subscribe page HTML
head = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to Skip School: The AI Playbook for Homeschool Parents</title>
    <meta name="description" content="Get the exact AI tools, prompts, and strategies real homeschool parents use every week. Free newsletter, one email per week, five minutes to read.">
    <meta name="keywords" content="AI homeschooling newsletter, homeschool AI tools, ChatGPT homeschool, Claude homeschool, AI education newsletter">
    <link rel="canonical" href="https://skipschool.ai/subscribe">

    <meta property="og:title" content="Subscribe to Skip School: The AI Playbook for Homeschool Parents">
    <meta property="og:description" content="Free weekly newsletter with AI tools, prompts, and strategies for homeschool parents. Five minutes to read.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://skipschool.ai/subscribe">
    <meta property="og:site_name" content="Skip School">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Subscribe to Skip School: AI Homeschool Playbook">
    <meta name="twitter:description" content="Free weekly newsletter with AI tools, prompts, and strategies for homeschool parents.">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&display=swap" rel="stylesheet">
    <style>
        :root {
            --yellow: #fbc926;
            --yellow-hover: #e5b820;
            --navy: #0d203b;
            --navy-light: #1a3358;
            --bg: #f0f4f8;
            --white: #ffffff;
            --gray-200: #e2e8f0;
            --gray-400: #94a3b8;
            --gray-600: #64748b;
            --gray-800: #1e293b;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { height: 100%; }
        body {
            font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--navy);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        .page {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 24px;
        }
        .container {
            max-width: 1120px;
            width: 100%;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }
        .content { max-width: 520px; }
        .logo { margin-bottom: 32px; }
        .logo a { display: block; }
        .logo-img {
            height: auto;
            width: 300px;
            max-width: 100%;
            display: block;
        }
        .nl-logo-img {
            height: auto;
            width: 140px;
            display: block;
            margin: 0 auto;
        }
        .stars {
            display: flex;
            gap: 3px;
            margin-bottom: 16px;
        }
        .star {
            color: var(--yellow);
            font-size: 20px;
        }
        h1 {
            font-family: 'Fraunces', serif;
            font-size: clamp(32px, 4vw, 46px);
            line-height: 1.12;
            color: var(--navy);
            margin-bottom: 20px;
            letter-spacing: -0.5px;
            font-weight: 700;
        }
        h1 .highlight {
            color: var(--yellow);
            position: relative;
            text-decoration: underline;
            text-decoration-color: var(--yellow);
            text-underline-offset: 4px;
            text-decoration-thickness: 3px;
        }
        .description {
            font-size: 17px;
            line-height: 1.65;
            color: var(--gray-600);
            margin-bottom: 12px;
        }
        .description strong { color: var(--navy); font-weight: 600; }
        .description u {
            text-decoration-color: var(--yellow);
            text-underline-offset: 3px;
            text-decoration-thickness: 2px;
        }
        .frequency {
            font-size: 16px;
            line-height: 1.6;
            color: var(--gray-600);
            margin-bottom: 28px;
        }
        .frequency strong { color: var(--navy); font-weight: 700; }
        .form-row {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }
        .email-input {
            flex: 1;
            padding: 14px 18px;
            border: 2px solid var(--gray-200);
            border-radius: 10px;
            font-size: 16px;
            font-family: 'DM Sans', sans-serif;
            color: var(--navy);
            background: var(--white);
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
            outline: none;
        }
        .email-input::placeholder { color: var(--gray-400); }
        .email-input:focus {
            border-color: var(--yellow);
            box-shadow: 0 0 0 3px rgba(251, 201, 38, 0.15);
        }
        .cta-btn {
            padding: 14px 28px;
            background: var(--yellow);
            color: var(--navy);
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 700;
            font-family: 'DM Sans', sans-serif;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
            letter-spacing: 0.2px;
        }
        .cta-btn:hover {
            background: var(--yellow-hover);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(251, 201, 38, 0.35);
        }
        .cta-btn:active { transform: translateY(0); }
        .cta-btn:disabled {
            opacity: 0.7;
            cursor: not-allowed;
            transform: none;
        }
        .social-proof {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .avatars { display: flex; }
        .avatar {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 2.5px solid var(--bg);
            margin-left: -10px;
            object-fit: cover;
        }
        .avatar:first-child { margin-left: 0; }
        .social-proof-text {
            font-size: 14px;
            color: var(--gray-600);
        }
        .social-proof-text strong {
            color: var(--navy);
            font-weight: 700;
        }
        .phone-col {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .phone-frame {
            width: 320px;
            background: var(--white);
            border-radius: 40px;
            padding: 14px;
            box-shadow:
                0 25px 60px rgba(13, 32, 59, 0.15),
                0 8px 20px rgba(13, 32, 59, 0.08);
            position: relative;
        }
        .phone-notch {
            width: 120px;
            height: 28px;
            background: var(--white);
            border-radius: 0 0 18px 18px;
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            z-index: 2;
        }
        .phone-screen {
            background: var(--white);
            border-radius: 28px;
            overflow: hidden;
            border: 1px solid var(--gray-200);
        }
        .nl-preview { padding: 24px 20px 20px; }
        .nl-header {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 16px;
            padding-bottom: 14px;
            border-bottom: 2px solid var(--gray-200);
        }
        .nl-greeting {
            font-size: 14px;
            color: var(--navy);
            margin-bottom: 14px;
            line-height: 1.5;
        }
        .nl-greeting strong { font-weight: 700; }
        .nl-article {
            background: linear-gradient(135deg, #f8fafc, #f0f4f8);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 14px;
            border-left: 3px solid var(--yellow);
        }
        .nl-article-label {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--yellow);
            margin-bottom: 6px;
        }
        .nl-article-title {
            font-family: 'Fraunces', serif;
            font-size: 15px;
            color: var(--navy);
            line-height: 1.3;
            margin-bottom: 6px;
            font-weight: 600;
        }
        .nl-article-desc {
            font-size: 12px;
            color: var(--gray-600);
            line-height: 1.5;
        }
        .nl-prompt-box {
            background: var(--navy);
            border-radius: 10px;
            padding: 14px;
            margin-bottom: 14px;
        }
        .nl-prompt-label {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--yellow);
            margin-bottom: 6px;
        }
        .nl-prompt-text {
            font-size: 12px;
            color: rgba(255,255,255,0.85);
            line-height: 1.5;
            font-style: italic;
        }
        .nl-quick-hits {
            display: flex;
            gap: 8px;
        }
        .nl-quick-hit {
            flex: 1;
            background: #f8fafc;
            border-radius: 8px;
            padding: 10px 8px;
            text-align: center;
        }
        .nl-qh-emoji { font-size: 18px; margin-bottom: 4px; }
        .nl-qh-text {
            font-size: 10px;
            font-weight: 600;
            color: var(--navy);
        }
        .success-message {
            display: none;
            text-align: center;
            padding: 20px 0;
        }
        .success-message h2 {
            font-family: 'Fraunces', serif;
            font-size: 28px;
            color: var(--navy);
            margin-bottom: 12px;
            font-weight: 700;
        }
        .success-message p {
            font-size: 16px;
            color: var(--gray-600);
            line-height: 1.6;
        }
        .error-text {
            color: #dc2626;
            font-size: 14px;
            margin-top: -12px;
            margin-bottom: 16px;
            display: none;
        }
        @media (max-width: 900px) {
            .container {
                grid-template-columns: 1fr;
                gap: 40px;
                max-width: 520px;
                margin: 0 auto;
            }
            .phone-col { order: -1; }
            .phone-frame { width: 280px; }
            h1 { font-size: clamp(28px, 5vw, 38px); }
        }
        @media (max-width: 480px) {
            .page { padding: 24px 16px; }
            .form-row { flex-direction: column; }
            .cta-btn { width: 100%; text-align: center; }
            .phone-frame { width: 260px; }
        }
    </style>
</head>
<body>
'''

body = '''
<div class="page">
    <div class="container">

        <div class="content">
            <div class="logo">
                <a href="https://skipschool.ai">
                    <img src="LOGO_PLACEHOLDER" alt="Skip School" class="logo-img">
                </a>
            </div>

            <div id="subscribe-form">
                <div class="stars">
                    <span class="star">&#9733;</span>
                    <span class="star">&#9733;</span>
                    <span class="star">&#9733;</span>
                    <span class="star">&#9733;</span>
                    <span class="star">&#9733;</span>
                </div>

                <h1>The Free Weekly Newsletter That Teaches You to <span class="highlight">Homeschool Smarter with AI</span></h1>

                <p class="description">
                    Every week, get the exact AI tools, prompts, and strategies real homeschool parents are using right now. No jargon. No fluff. Just <u>practical stuff</u> you can try with your kids <strong>this week</strong>.
                </p>

                <p class="frequency">
                    <strong>One email per week.</strong> Five minutes to read. Written by parents who actually use this stuff every day.
                </p>

                <div class="form-row">
                    <input type="email" id="email-input" class="email-input" placeholder="Enter your email" aria-label="Email address">
                    <button id="subscribe-btn" class="cta-btn">Subscribe Free</button>
                </div>
                <p id="error-text" class="error-text"></p>

                <div class="social-proof">
                    <div class="avatars">
                        <img class="avatar" src="AVATAR_0" alt="">
                        <img class="avatar" src="AVATAR_1" alt="">
                        <img class="avatar" src="AVATAR_2" alt="">
                        <img class="avatar" src="AVATAR_3" alt="">
                        <img class="avatar" src="AVATAR_4" alt="">
                    </div>
                    <span class="social-proof-text">Join <strong>500+</strong> homeschool parents already reading</span>
                </div>
            </div>

            <div id="success-message" class="success-message">
                <h2>You're in! &#127881;</h2>
                <p>Check your inbox for a welcome email from Skip School. If you don't see it, check your spam folder.</p>
                <p style="margin-top: 16px;"><a href="https://skipschool.ai" style="color: var(--yellow); font-weight: 700; text-decoration: underline;">Browse the site while you wait &rarr;</a></p>
            </div>
        </div>

        <div class="phone-col">
            <div class="phone-frame">
                <div class="phone-notch"></div>
                <div class="phone-screen">
                    <div class="nl-preview">
                        <div class="nl-header">
                            <img src="NL_LOGO_PLACEHOLDER" alt="Skip School" class="nl-logo-img">
                        </div>

                        <p class="nl-greeting">Hey friend &#128075;<br>This week I let <strong>Claude build my 7-year-old's entire spelling curriculum.</strong> Here's what happened.</p>

                        <div class="nl-article">
                            <div class="nl-article-label">This Week's Deep Dive</div>
                            <div class="nl-article-title">I Replaced Our $200 Spelling Program with One AI Prompt</div>
                            <div class="nl-article-desc">The exact prompt I used, what Claude gave me, and the one thing I had to fix before my kid could use it.</div>
                        </div>

                        <div class="nl-prompt-box">
                            <div class="nl-prompt-label">&#10024; Prompt of the Week</div>
                            <div class="nl-prompt-text">"Create a 20-word spelling list for a 2nd grader based on the Magic Tree House books we're reading..."</div>
                        </div>

                        <div class="nl-quick-hits">
                            <div class="nl-quick-hit">
                                <div class="nl-qh-emoji">&#128295;</div>
                                <div class="nl-qh-text">3 New AI Tools</div>
                            </div>
                            <div class="nl-quick-hit">
                                <div class="nl-qh-emoji">&#128176;</div>
                                <div class="nl-qh-text">ESA Update</div>
                            </div>
                            <div class="nl-quick-hit">
                                <div class="nl-qh-emoji">&#128218;</div>
                                <div class="nl-qh-text">Free Resources</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>
'''

script = '''
<script>
(function() {
    var btn = document.getElementById('subscribe-btn');
    var input = document.getElementById('email-input');
    var errorEl = document.getElementById('error-text');
    var formEl = document.getElementById('subscribe-form');
    var successEl = document.getElementById('success-message');

    function getUTMParams() {
        var params = new URLSearchParams(window.location.search);
        return {
            utm_source: params.get('utm_source') || 'skipschool_subscribe',
            utm_medium: params.get('utm_medium') || 'web',
            utm_campaign: params.get('utm_campaign') || '',
            utm_content: params.get('utm_content') || '',
            utm_term: params.get('utm_term') || ''
        };
    }

    function validateEmail(email) {
        return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email);
    }

    btn.addEventListener('click', function(e) {
        e.preventDefault();
        errorEl.style.display = 'none';

        var email = input.value.trim();
        if (!email) {
            errorEl.textContent = 'Please enter your email address.';
            errorEl.style.display = 'block';
            input.focus();
            return;
        }
        if (!validateEmail(email)) {
            errorEl.textContent = 'Please enter a valid email address.';
            errorEl.style.display = 'block';
            input.focus();
            return;
        }

        var originalText = btn.textContent;
        btn.textContent = 'Subscribing...';
        btn.disabled = true;

        var utm = getUTMParams();

        fetch('https://api.beehiiv.com/v2/publications/pub_5c9a95b1-9b7d-4809-a24f-e7dd6fb96512/subscriptions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer kRII45B7ClwC4RST00PgrNSMTeMDn7ssbX5Bgt0LDTiy67Jk3iXPRNPzLKaXjotF'
            },
            body: JSON.stringify({
                email: email,
                reactivate_existing: true,
                send_welcome_email: true,
                utm_source: utm.utm_source,
                utm_medium: utm.utm_medium,
                utm_campaign: utm.utm_campaign,
                referring_site: 'https://skipschool.ai/subscribe'
            })
        })
        .then(function(r) { return r.json(); })
        .then(function(data) {
            if (data.data && data.data.id) {
                formEl.style.display = 'none';
                successEl.style.display = 'block';
            } else {
                btn.textContent = originalText;
                btn.disabled = false;
                errorEl.textContent = 'Something went wrong. Please try again.';
                errorEl.style.display = 'block';
            }
        })
        .catch(function() {
            btn.textContent = originalText;
            btn.disabled = false;
            errorEl.textContent = 'Network error. Please try again.';
            errorEl.style.display = 'block';
        });
    });

    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            btn.click();
        }
    });
})();
</script>

</body>
</html>
'''

# Replace placeholders with actual base64 data
body = body.replace('LOGO_PLACEHOLDER', logo)
body = body.replace('NL_LOGO_PLACEHOLDER', nl_logo)
for i in range(5):
    body = body.replace(f'AVATAR_{i}', avatars[i])

html = head + body + script

with open('subscribe/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Subscribe page created: {len(html)} bytes')
