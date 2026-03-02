import type { CollectionConfig } from 'payload'

export const Media: CollectionConfig = {
  slug: 'media',
  admin: {
    group: 'Uploads',
  },
  access: { read: () => true },
  upload: {
    staticDir: 'public/media',
    mimeTypes: ['image/*'],
    imageSizes: [
      { name: 'thumbnail', width: 120, height: 120, position: 'centre' },
      { name: 'card', width: 400, height: 260, position: 'centre' },
      { name: 'hero', width: 1200, height: 630, position: 'centre' },
    ],
  },
  fields: [
    { name: 'alt', type: 'text', required: true },
  ],
}
