export default async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', 'https://skipschool.ai');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }
  
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, source } = req.body || {};
  
  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Valid email required' });
  }

  try {
    const response = await fetch(
      'https://api.beehiiv.com/v2/publications/pub_5c9a95b1-9b7d-4809-a24f-e7dd6fb96512/subscriptions',
      {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer kRII45B7ClwC4RST00PgrNSMTeMDn7ssbX5Bgt0LDTiy67Jk3iXPRNPzLKaXjotF',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          reactivate_existing: true,
          send_welcome_email: true,
          utm_source: source || 'website',
          utm_medium: 'organic',
        }),
      }
    );

    const data = await response.json();

    if (response.ok) {
      return res.status(200).json({ success: true, message: 'Subscribed!' });
    } else {
      return res.status(400).json({ error: data.message || 'Subscription failed' });
    }
  } catch (err) {
    return res.status(500).json({ error: 'Server error' });
  }
}
