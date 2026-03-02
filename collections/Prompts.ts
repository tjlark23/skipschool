import type { CollectionConfig } from 'payload'

export const Prompts: CollectionConfig = {
  slug: 'prompts',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'subject', 'ageRange', 'isFeatured'],
    group: 'Content',
  },
  access: { read: () => true },
  fields: [
    { name: 'title', type: 'text', required: true },
    { name: 'slug', type: 'text', required: true, unique: true },
    {
      name: 'description',
      type: 'textarea',
      maxLength: 300,
      admin: { description: 'What this prompt does and when to use it' },
    },
    {
      name: 'prompt',
      type: 'textarea',
      required: true,
      admin: { description: 'The actual copy-paste-ready prompt text' },
    },
    {
      name: 'subject',
      type: 'select',
      required: true,
      options: [
        { label: 'Math', value: 'math' },
        { label: 'Reading', value: 'reading' },
        { label: 'Writing', value: 'writing' },
        { label: 'Science', value: 'science' },
        { label: 'History', value: 'history' },
        { label: 'Art', value: 'art' },
        { label: 'General / Multi-Subject', value: 'general' },
        { label: 'Planning & Organization', value: 'planning' },
        { label: 'Assessment', value: 'assessment' },
      ],
    },
    {
      name: 'ageRange',
      type: 'text',
      admin: { description: 'e.g. "Ages 5-8" or "All ages"' },
    },
    {
      name: 'bestWith',
      type: 'select',
      hasMany: true,
      admin: { description: 'Which AI tools work best with this prompt' },
      options: [
        { label: 'Claude', value: 'claude' },
        { label: 'ChatGPT', value: 'chatgpt' },
        { label: 'Gemini', value: 'gemini' },
        { label: 'Any AI', value: 'any' },
      ],
    },
    {
      name: 'isFeatured',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        position: 'sidebar',
        description: 'This week\'s featured prompt on homepage',
      },
    },
    {
      name: 'isPremium',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        position: 'sidebar',
        description: 'Paid tier only',
      },
    },
    {
      name: 'seo',
      type: 'group',
      fields: [
        { name: 'metaTitle', type: 'text', maxLength: 60 },
        { name: 'metaDescription', type: 'textarea', maxLength: 160 },
      ],
    },
  ],
}
