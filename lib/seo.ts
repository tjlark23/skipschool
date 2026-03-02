const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://skipschool.ai'

export function organizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Skip School',
    url: SITE_URL,
    description: 'Skip School is a media brand for homeschool families who use AI. Founded by Ashley and TJ Larkin.',
    founder: [
      {
        '@type': 'Person',
        name: 'Ashley Larkin',
        jobTitle: 'Editor',
        knowsAbout: ['Homeschooling', 'AI in Education', 'Curriculum Design'],
      },
      {
        '@type': 'Person',
        name: 'TJ Larkin',
        jobTitle: 'AI & Technology',
        knowsAbout: ['Artificial Intelligence', 'Education Technology', 'AI Prompting'],
      },
    ],
    sameAs: [
      'https://instagram.com/skipschool.ai',
    ],
  }
}

export function articleSchema(article: any) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: article.title,
    description: article.excerpt,
    url: `${SITE_URL}/articles/${article.slug}`,
    datePublished: article.publishedAt,
    dateModified: article.updatedAt,
    author: {
      '@type': 'Person',
      name: article.author?.name || 'Ashley Larkin',
      url: SITE_URL,
    },
    publisher: {
      '@type': 'Organization',
      name: 'Skip School',
      url: SITE_URL,
    },
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': `${SITE_URL}/articles/${article.slug}`,
    },
  }
}

export function toolSchema(tool: any) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: tool.name,
    description: tool.description,
    url: `${SITE_URL}/directory/${tool.slug}`,
    brand: { '@type': 'Brand', name: tool.name },
    ...(tool.rating && {
      aggregateRating: {
        '@type': 'AggregateRating',
        ratingValue: tool.rating,
        bestRating: 5,
        ratingCount: 1,
      },
    }),
    ...(tool.pricing?.price && {
      offers: {
        '@type': 'Offer',
        price: tool.pricing.priceNumeric || 0,
        priceCurrency: 'USD',
        description: tool.pricing.price,
      },
    }),
    ...(tool.category && {
      category: tool.category,
    }),
  }
}

export function faqSchema(faqs: Array<{ question: string; answer: string }>) {
  if (!faqs || faqs.length === 0) return null
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  }
}

export function breadcrumbSchema(items: Array<{ name: string; url: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: item.url,
    })),
  }
}
