import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Skip School — The AI Playbook for Homeschool Parents',
  description:
    'Skip the classroom. Use AI to personalize how your kids learn. Give them a five-year head start.',
  metadataBase: new URL(
    process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai',
  ),
}

export default function StandaloneLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
