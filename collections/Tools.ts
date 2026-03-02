import type { CollectionConfig } from 'payload'

export const Tools: CollectionConfig = {
  slug: 'tools',
  admin: {
    useAsTitle: 'name',
    defaultColumns: ['name', 'category', 'rating', 'isFeatured'],
    group: 'Directory',
  },
  access: {
    read: () => true,
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
    },
    {
      name: 'logo',
      type: 'upload',
      relationTo: 'media',
    },
    {
      name: 'description',
      type: 'textarea',
      required: true,
      maxLength: 500,
      admin: {
        description: 'Short description for directory cards (1-2 sentences)',
      },
    },
    {
      name: 'fullDescription',
      type: 'richText',
      admin: {
        description: 'Full description for the tool detail page',
      },
    },
    {
      name: 'category',
      type: 'select',
      required: true,
      options: [
        { label: 'AI Tutoring', value: 'ai-tutoring' },
        { label: 'AI Assistant', value: 'ai-assistant' },
        { label: 'Curriculum', value: 'curriculum' },
        { label: 'Enrichment', value: 'enrichment' },
        { label: 'Testing & Assessment', value: 'testing' },
        { label: 'Co-ops & Community', value: 'co-ops' },
        { label: 'ESA-Approved', value: 'esa-approved' },
        { label: 'Books & Resources', value: 'books' },
        { label: 'K-8 Platform', value: 'k8-platform' },
        { label: 'Math', value: 'math' },
        { label: 'Reading & Writing', value: 'reading-writing' },
        { label: 'Science', value: 'science' },
        { label: 'College Prep', value: 'college-prep' },
      ],
    },
    {
      name: 'pricing',
      type: 'group',
      fields: [
        {
          name: 'model',
          type: 'select',
          options: [
            { label: 'Free', value: 'free' },
            { label: 'Freemium', value: 'freemium' },
            { label: 'Paid', value: 'paid' },
            { label: 'Contact for Pricing', value: 'contact' },
          ],
        },
        {
          name: 'price',
          type: 'text',
          admin: { description: 'Display price, e.g. "$44/mo" or "$199/year"' },
        },
        {
          name: 'priceNumeric',
          type: 'number',
          admin: { description: 'Monthly price in dollars for sorting/filtering' },
        },
      ],
    },
    {
      name: 'ageRange',
      type: 'group',
      fields: [
        { name: 'min', type: 'number', admin: { description: 'Minimum age' } },
        { name: 'max', type: 'number', admin: { description: 'Maximum age' } },
        { name: 'display', type: 'text', admin: { description: 'e.g. "Ages 5-14" or "All ages"' } },
      ],
    },
    {
      name: 'rating',
      type: 'number',
      min: 0,
      max: 5,
      admin: {
        description: 'Ashley\'s rating out of 5',
        step: 0.1,
      },
    },
    {
      name: 'ashleyTake',
      type: 'textarea',
      maxLength: 300,
      admin: {
        description: 'Ashley\'s one-line take for directory cards',
      },
    },
    {
      name: 'pros',
      type: 'array',
      fields: [{ name: 'item', type: 'text' }],
    },
    {
      name: 'cons',
      type: 'array',
      fields: [{ name: 'item', type: 'text' }],
    },
    {
      name: 'url',
      type: 'text',
      admin: { description: 'Official website URL' },
    },
    {
      name: 'affiliateUrl',
      type: 'text',
      admin: { description: 'Affiliate link (if available)' },
    },
    {
      name: 'badge',
      type: 'select',
      admin: { description: 'Homepage badge for featured tools' },
      options: [
        { label: 'We Use This Daily', value: 'daily-use' },
        { label: 'Free 30-Day Trial', value: 'free-trial' },
        { label: 'New', value: 'new' },
        { label: 'Best for Math', value: 'best-math' },
        { label: 'Best for Reading', value: 'best-reading' },
        { label: 'Skip School Recommended', value: 'recommended' },
        { label: 'ESA Approved', value: 'esa-approved' },
      ],
    },
    {
      name: 'isEsaApproved',
      type: 'checkbox',
      defaultValue: false,
      admin: { position: 'sidebar' },
    },
    {
      name: 'esaStates',
      type: 'select',
      hasMany: true,
      admin: {
        position: 'sidebar',
        description: 'States where this tool is ESA-approved',
        condition: (data) => data?.isEsaApproved,
      },
      options: [
        { label: 'Texas', value: 'TX' },
        { label: 'Arizona', value: 'AZ' },
        { label: 'Florida', value: 'FL' },
        { label: 'West Virginia', value: 'WV' },
        { label: 'Indiana', value: 'IN' },
        { label: 'Iowa', value: 'IA' },
        { label: 'Utah', value: 'UT' },
        { label: 'North Carolina', value: 'NC' },
      ],
    },
    {
      name: 'isFeatured',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        position: 'sidebar',
        description: 'Show on homepage "What We\'re Using" section',
      },
    },
    {
      name: 'subjects',
      type: 'select',
      hasMany: true,
      options: [
        { label: 'Math', value: 'math' },
        { label: 'Reading', value: 'reading' },
        { label: 'Writing', value: 'writing' },
        { label: 'Science', value: 'science' },
        { label: 'History', value: 'history' },
        { label: 'Art', value: 'art' },
        { label: 'Music', value: 'music' },
        { label: 'Foreign Language', value: 'language' },
        { label: 'Coding', value: 'coding' },
        { label: 'All Subjects', value: 'all' },
      ],
    },
    {
      name: 'seo',
      type: 'group',
      fields: [
        { name: 'metaTitle', type: 'text', maxLength: 60 },
        { name: 'metaDescription', type: 'textarea', maxLength: 160 },
      ],
    },
    {
      name: 'faq',
      type: 'array',
      admin: { description: 'FAQ for this tool\'s detail page' },
      fields: [
        { name: 'question', type: 'text', required: true },
        { name: 'answer', type: 'textarea', required: true },
      ],
    },
  ],
}
