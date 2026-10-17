# Public discovery: SEO and GEO, R10

## Implemented

| Area | Concrete change |
| --- | --- |
| Content discovery | 94 self-contained FR/EN public pages, with linked catalogues and previous/next lesson links. |
| Rendering | Complete readable HTML without JavaScript. Identical content for browsers and crawlers; no user-agent branch. |
| Metadata | Unique titles/descriptions, canonical production URLs, Open Graph tags and Twitter summary cards. |
| Languages | Reciprocal French/English `hreflang`, `x-default` English references and HTML language attributes. |
| Structured data | WebSite, publisher Organization, BreadcrumbList and WebPage / Article / LearningResource consistent with visible copy. No fabricated reviews, accreditation or pass-rate claims. |
| Discovery files | `robots.txt` allowing crawl; `sitemap.xml` containing 95 canonical URLs including the application and 94 public pages, with language alternates. |
| Reader intent | Guides explaining CMMI, Practitioner preparation, comparison with Scrum/SAFe, and a practical study pathway. |
| Attribution | Visible dated sources, per-PA quick-guide page references, publisher/method/scope page, explicit fictional cases and original exercises. |
| Performance | Public pages have no runtime API, JavaScript dependency, third-party fonts, trackers or blocking external requests. The interactive app keeps its standalone data payload. |
| Handoff | Public lessons open the correct app lesson/workshop with explicit validated language and code parameters. |
| Deployment | Only generated `dist/` is deployed. Source scripts and test outputs do not become public routes. |
| Regression coverage | HTML/internal-link audit plus no-JavaScript browser checks for all 95 routes; interactive workshop coverage across both languages and two screen sizes. |

GEO here means making useful, sourced material available for retrieval and citation. It is not an independent ranking guarantee. Google states that its AI search features use the same foundational SEO requirements and require no special AI file or schema:
<https://developers.google.com/search/docs/appearance/ai-features>.

## Measurement still requiring external account data

No Google Search Console property or analytics account was connected in this work. Do not treat generated sitemap entries as proof of actual indexing.

Once the owner has access to the property:

1. Verify the production property in Search Console and submit `/sitemap.xml`.
2. Inspect a French lesson, its English counterpart and a guide; compare discovered URL, selected canonical and indexed HTML.
3. Establish a baseline for indexed pages, impressions, clicks and relevant queries; review after recrawling rather than inventing immediate traffic gains.
4. Measure useful transitions to study/lesson/workshop without collecting narrative drafts. No tracker is enabled by this release.
5. Check citations manually on a small stable set of CMMI questions across chosen answer engines. Record date, query and source page; absence/presence on one query is not an overall GEO score.

No credential was requested, no search-console ownership was claimed and no unrelated account changes were made. A custom domain, if introduced later, requires changing the canonical base, redirects and property tracking together.
