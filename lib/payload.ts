import { getPayload as getPayloadClient } from 'payload'
import config from '@payload-config'

export async function getPayloadInstance() {
  return getPayloadClient({ config })
}

export async function getPublishedArticles(limit = 20) {
  const payload = await getPayloadInstance()
  return payload.find({
    collection: 'articles',
    where: { status: { equals: 'published' } },
    sort: '-publishedAt',
    limit,
    depth: 2,
  })
}

export async function getFeaturedArticle() {
  const payload = await getPayloadInstance()
  const result = await payload.find({
    collection: 'articles',
    where: {
      status: { equals: 'published' },
      isFeatured: { equals: true },
    },
    sort: '-publishedAt',
    limit: 1,
    depth: 2,
  })
  return result.docs[0] || null
}

export async function getArticleBySlug(slug: string) {
  const payload = await getPayloadInstance()
  const result = await payload.find({
    collection: 'articles',
    where: { slug: { equals: slug } },
    limit: 1,
    depth: 2,
  })
  return result.docs[0] || null
}

export async function getFeaturedTools(limit = 4) {
  const payload = await getPayloadInstance()
  return payload.find({
    collection: 'tools',
    where: { isFeatured: { equals: true } },
    limit,
    depth: 1,
  })
}

export async function getTools(category?: string, limit = 20) {
  const payload = await getPayloadInstance()
  const where: any = {}
  if (category) where.category = { equals: category }
  return payload.find({
    collection: 'tools',
    where,
    sort: '-rating',
    limit,
    depth: 1,
  })
}

export async function getToolBySlug(slug: string) {
  const payload = await getPayloadInstance()
  const result = await payload.find({
    collection: 'tools',
    where: { slug: { equals: slug } },
    limit: 1,
    depth: 1,
  })
  return result.docs[0] || null
}

export async function getFeaturedPrompt() {
  const payload = await getPayloadInstance()
  const result = await payload.find({
    collection: 'prompts',
    where: { isFeatured: { equals: true } },
    limit: 1,
  })
  return result.docs[0] || null
}

export async function getActiveSponsor(placement: string) {
  const payload = await getPayloadInstance()
  const result = await payload.find({
    collection: 'sponsors',
    where: {
      isActive: { equals: true },
      placement: { equals: placement },
    },
    limit: 1,
    depth: 1,
  })
  return result.docs[0] || null
}
