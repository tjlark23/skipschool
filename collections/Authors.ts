import type { CollectionConfig } from 'payload'

export const Authors: CollectionConfig = {
  slug: 'authors',
  admin: {
    useAsTitle: 'name',
    group: 'Content',
  },
  access: { read: () => true },
  fields: [
    { name: 'name', type: 'text', required: true },
    { name: 'slug', type: 'text', required: true, unique: true },
    { name: 'role', type: 'text', admin: { description: 'e.g. "Editor" or "AI & Technology"' } },
    { name: 'bio', type: 'textarea', maxLength: 300 },
    { name: 'photo', type: 'upload', relationTo: 'media' },
    {
      name: 'socialLinks',
      type: 'group',
      fields: [
        { name: 'instagram', type: 'text' },
        { name: 'twitter', type: 'text' },
        { name: 'linkedin', type: 'text' },
      ],
    },
  ],
}
