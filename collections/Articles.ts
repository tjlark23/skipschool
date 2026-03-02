import type { CollectionConfig } from 'payload'

export const Articles: CollectionConfig = {
  slug: 'articles',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'category', 'status', 'publishedAt'],
    group: 'Content',
  },
  access: {
    read: () => true,
  },
  fields: [
    {
      name: 'title',
      type: 'text',
      required: true,
      maxLength: 120,
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
      admin: {
        position: 'sidebar',
        description: 'URL-friendly version of the title. Auto-generated if left blank.',
      },
    },
    {
      name: 'excerpt',
      type: 'textarea',
      maxLength: 300,
      admin: {
        description: 'Short summary shown in article cards and meta description. 1-2 sentences.',
      },
    },
    {
      name: 'featuredImage',
      type: 'upload',
      relationTo: 'media',
    },
    {
      name: 'category',
      type: 'select',
      required: true,
      options: [
        { label: 'AI for Parents', value: 'ai-for-parents' },
        { label: 'AI for Kids', value: 'ai-for-kids' },
        { label: 'The Review', value: 'review' },
        { label: 'ESA Guide', value: 'esa-guide' },
        { label: 'Comparison', value: 'comparison' },
        { label: 'Our Week', value: 'our-week' },
        { label: 'The Download', value: 'the-download' },
        { label: 'Tutorial', value: 'tutorial' },
        { label: 'Community', value: 'community' },
        { label: 'Data', value: 'data' },
      ],
    },
    {
      name: 'pillar',
      type: 'select',
      admin: {
        position: 'sidebar',
        description: 'Content pillar this belongs to (for internal tracking)',
      },
      options: [
        { label: 'AI Tools (40%)', value: 'ai-tools' },
        { label: 'Curriculum & Resources (25%)', value: 'curriculum' },
        { label: 'ESA / School Choice (15%)', value: 'esa' },
        { label: 'Community & Lifestyle (20%)', value: 'community' },
      ],
    },
    {
      name: 'content',
      type: 'richText',
      required: true,
    },
    {
      name: 'author',
      type: 'relationship',
      relationTo: 'authors',
      required: true,
    },
    {
      name: 'tags',
      type: 'relationship',
      relationTo: 'tags',
      hasMany: true,
    },
    {
      name: 'relatedTools',
      type: 'relationship',
      relationTo: 'tools',
      hasMany: true,
      admin: {
        description: 'Tools mentioned or reviewed in this article (shows tool cards)',
      },
    },
    {
      name: 'readTime',
      type: 'number',
      admin: {
        position: 'sidebar',
        description: 'Estimated reading time in minutes',
      },
    },
    {
      name: 'status',
      type: 'select',
      required: true,
      defaultValue: 'draft',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'In Review (Ashley Edit)', value: 'review' },
        { label: 'Published', value: 'published' },
        { label: 'Archived', value: 'archived' },
      ],
      admin: {
        position: 'sidebar',
      },
    },
    {
      name: 'publishedAt',
      type: 'date',
      admin: {
        position: 'sidebar',
        date: {
          pickerAppearance: 'dayAndTime',
        },
      },
    },
    {
      name: 'isFeatured',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        position: 'sidebar',
        description: 'Show on homepage hero',
      },
    },
    {
      name: 'isGated',
      type: 'checkbox',
      defaultValue: true,
      admin: {
        position: 'sidebar',
        description: 'Require newsletter signup to read full article',
      },
    },
    {
      name: 'seo',
      type: 'group',
      fields: [
        { name: 'metaTitle', type: 'text', maxLength: 60 },
        { name: 'metaDescription', type: 'textarea', maxLength: 160 },
        { name: 'ogImage', type: 'upload', relationTo: 'media' },
      ],
    },
    {
      name: 'faq',
      type: 'array',
      admin: {
        description: 'FAQ items that appear at bottom of article and in FAQPage schema',
      },
      fields: [
        { name: 'question', type: 'text', required: true },
        { name: 'answer', type: 'textarea', required: true },
      ],
    },
  ],
}
