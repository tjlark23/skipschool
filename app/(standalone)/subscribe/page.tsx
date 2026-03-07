import fs from 'fs'
import path from 'path'

export default function SubscribePage() {
  const html = fs.readFileSync(
    path.join(process.cwd(), 'public', 'subscribe.html'),
    'utf-8',
  )
  return <div dangerouslySetInnerHTML={{ __html: html }} />
}
