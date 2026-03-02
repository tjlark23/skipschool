'use client'

import { useState } from 'react'

interface NewsletterSignupProps {
  variant?: 'inline' | 'card' | 'hero'
  className?: string
}

export function NewsletterSignup({ variant = 'inline', className = '' }: NewsletterSignupProps) {
  const [email, setEmail] = useState('')
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle')

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (!email) return

    setStatus('loading')

    try {
      // TODO: Connect to Beehiiv API
      // const res = await fetch('/api/subscribe', { method: 'POST', body: JSON.stringify({ email }) })
      // For now, simulate success
      await new Promise((r) => setTimeout(r, 800))
      setStatus('success')
      setEmail('')
    } catch {
      setStatus('error')
    }
  }

  if (variant === 'inline') {
    return (
      <div className={`bg-teal rounded-xl p-4 flex items-center gap-5 flex-wrap ${className}`}>
        <div className="flex-1 min-w-[180px]">
          <h3 className="font-serif font-bold text-[15px] text-white mb-0.5">
            Get this in your inbox every Wednesday
          </h3>
          <p className="text-[11px] text-white/65">
            AI tools, prompts, curriculum picks, ESA updates. Free forever.
          </p>
        </div>
        {status === 'success' ? (
          <p className="text-sm font-semibold text-white">Welcome aboard! Check your inbox.</p>
        ) : (
          <form onSubmit={handleSubmit} className="flex gap-1.5 flex-1 min-w-[280px]">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="your@email.com"
              className="flex-1 px-3 py-2.5 rounded-lg text-sm outline-none min-w-0 placeholder:text-gray-400"
              required
            />
            <button
              type="submit"
              disabled={status === 'loading'}
              className="px-4 py-2.5 rounded-lg bg-coral text-white text-sm font-bold whitespace-nowrap hover:bg-coral/90 transition-colors disabled:opacity-50"
            >
              {status === 'loading' ? 'Joining...' : 'Subscribe Free →'}
            </button>
          </form>
        )}
      </div>
    )
  }

  return null
}
