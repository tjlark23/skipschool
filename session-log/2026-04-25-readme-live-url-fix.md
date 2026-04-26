# 2026-04-25 — Fix README live URL (skipschool.com → skipschool.ai)

Branch: main
Status: merged

## Summary
README.md line 2 said `Live: https://skipschool.com` but the production domain is skipschool.ai. The Projects registry auto-detector reads README.md to populate the production URL column, so the registry was resolving skipschool to the wrong domain. Fixed.

## Files touched
- `README.md` — `https://skipschool.com` → `https://skipschool.ai`.

## Why
Came up while locking the V1 site list for the Planet Express Portfolio SEO Dashboard build. GSC is verified on skipschool.ai, not skipschool.com.

## No deploy implications
The live site deploys via `vercel deploy --prod` from `site/files/src/`, not via git push. README change does not trigger a redeploy.
