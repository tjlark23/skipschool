import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './app/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        teal: {
          DEFAULT: '#0D7377',
          dark: '#0A5C5F',
          light: '#E8F4F4',
          bg: '#f0f9f9',
        },
        coral: {
          DEFAULT: '#E8724A',
          light: '#FFF0EB',
          bg: '#fef3ed',
        },
        charcoal: {
          DEFAULT: '#1a1a2e',
          mid: '#2d2d44',
        },
        gold: {
          DEFAULT: '#D4A843',
          light: '#FBF5E8',
          bg: '#fef9ee',
        },
        cream: '#FAF7F2',
      },
      fontFamily: {
        serif: ['Fraunces', 'Georgia', 'serif'],
        sans: ['DM Sans', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
}

export default config
