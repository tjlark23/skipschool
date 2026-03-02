import type { CollectionConfig } from 'payload'

export const Sponsors: CollectionConfig = {
  slug: 'sponsors',
  admin: {
    useAsTitle: 'name',
    group: 'Business',
  },
  access: { read: () => true },
  fields: [
    { name: 'name', type: 'text', required: true },
    { name: 'logo', type: 'upload', relationTo: 'media' },
    { name: 'tagline', type: 'text', maxLength: 100 },
    { name: 'url', type: 'text', required: true },
    {
      name: 'placement',
      type: 'select',
      required: true,
      options: [
        { label: 'Presenting Sponsor (top bar)', value: 'presenting' },
        { label: 'Newsletter Sponsor', value: 'newsletter' },
        { label: 'Directory Featured', value: 'directory-featured' },
      ],
    },
    {
      name: 'isActive',
      type: 'checkbox',
      defaultValue: true,
      admin: { position: 'sidebar' },
    },
    { name: 'startDate', type: 'date' },
    { name: 'endDate', type: 'date' },
  ],
}
