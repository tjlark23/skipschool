import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const { email, utm_source, utm_medium, utm_campaign } = await request.json()

    if (!email) {
      return NextResponse.json(
        { success: false, error: 'Email is required' },
        { status: 400 },
      )
    }

    const publicationId = process.env.BEEHIIV_PUBLICATION_ID
    const apiKey = process.env.BEEHIIV_API_KEY

    if (!publicationId || !apiKey) {
      console.error('Missing BEEHIIV_PUBLICATION_ID or BEEHIIV_API_KEY')
      return NextResponse.json(
        { success: false, error: 'Server configuration error' },
        { status: 500 },
      )
    }

    const response = await fetch(
      `https://api.beehiiv.com/v2/publications/${publicationId}/subscriptions`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          email,
          reactivate_existing: true,
          send_welcome_email: true,
          utm_source: utm_source || undefined,
          utm_medium: utm_medium || undefined,
          utm_campaign: utm_campaign || undefined,
          referring_site: 'https://skipschool.ai/subscribe',
        }),
      },
    )

    if (!response.ok) {
      const errorData = await response.text()
      console.error('Beehiiv API error:', response.status, errorData)
      return NextResponse.json(
        { success: false, error: 'Subscription failed' },
        { status: response.status },
      )
    }

    return NextResponse.json({
      success: true,
      redirect: process.env.SURVEY_REDIRECT_URL || '/thank-you',
    })
  } catch (error) {
    console.error('Subscribe API error:', error)
    return NextResponse.json(
      { success: false, error: 'Internal server error' },
      { status: 500 },
    )
  }
}
