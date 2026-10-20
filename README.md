# Oliver’s Lab — source

Personal site for Oliver. Static HTML and one stylesheet, served by GitHub Pages.
No framework, no build step, no JavaScript, no analytics.

Live at <https://oliver804.github.io/>

## What this site is

A work record, not a blog. The home page is an index of things that shipped —
two public repositories, each with what it does, what it costs and where to get
it — followed by a short list of notes. There is no archive, no schedule and no
"latest" rail, because the site is updated a few times a year and should still
look current six months later.

The reading order is deliberate: **work first, notes second, person third.**
Page titles, section order and type sizes all follow that order.

## Structure

```
.
├── index.html                              home
├── projects/
│   ├── index.html                          project index
│   └── local-route-launcher/index.html     project case notes
├── writing/
│   ├── index.html                          notes index
│   ├── why-the-launcher-drives-the-app/    Software engineering
│   ├── one-behaviour-two-builds/           Software engineering
│   ├── renaming-a-shipped-app/             Open source
│   └── a-version-number-is-a-build-output/ Developer tools
├── about/index.html                        about
├── 404.html
├── assets/
│   ├── css/style.css                       the whole design system
│   ├── fonts/                              Newsreader, self-hosted (OFL)
│   └── img/                                screenshots, favicon, link card
├── scripts/og-card.py                      one-off generator for the 1200×630 card
├── docs/
│   ├── research.md                         first-round research
│   ├── research-personal-sites.md          how project-first sites are built (2026)
│   └── design-plan.md                      design decisions, including the redesign
├── robots.txt  sitemap.xml  feed.xml
└── .nojekyll                               serve files as-is, no Jekyll
```

## Preview locally

```sh
python3 -m http.server 8000
# open http://localhost:8000
```

Root-absolute paths (`/assets/...`) mean the site must be served from a server
root, not opened as `file://`.

## Publishing

GitHub Pages serves `main` from the repository root of the user site
`oliver804.github.io`. Push to `main` and Pages rebuilds in about a minute.

The project site lives in a different repository
(`ChatGPT-Proxy-Launcher`, deployed from `site/**` by its own workflow) and is
not affected by this one.

## Add a note

1. Copy `writing/one-behaviour-two-builds/` to `writing/<slug>/`.
2. Change `<title>`, description, canonical, OG title/description/URL, the
   kicker (which project the note belongs to), the `<time datetime>` and the
   body.
3. Add one `<li>` to the top of the list in `writing/index.html`, *and* to the
   four-item list in `index.html` — the home page shows all notes, so the two
   lists must stay in step.
4. Add the entry to `feed.xml` and a `<url>` to `sitemap.xml`.
5. Set the *Read next* link at the bottom of the previous note to the new one,
   and give the new note its own *Read next* link.

There is no reading time and no topic taxonomy any more. A note is dated and
attributed to a project; that is the whole metadata.

## Add a project

1. Copy `projects/local-route-launcher/` to `projects/<slug>/`.
2. Update the spec list, figures, links and page title.
3. Add a `<li>` to `.work` in `projects/index.html` with the next number, then
   the same entry in `index.html`. Work is the only numbered list on the site,
   and the numbers have to match across the two pages.
4. Update the facts table on `projects/index.html` when the release, the
   licence or the repository count changes, and the "two public repositories"
   count in the home page section note.
5. Add the project to the `ItemList` in the JSON-LD on both pages.

## Design decisions

Four patterns only, all defined in `assets/css/style.css`:

| Pattern | Used for |
| --- | --- |
| `.work-item` | a numbered entry in the work list: number, name, data line, copy, links |
| `.spec` | two-column data tables (version, platforms, licence) |
| `.fig` | a screenshot with a numbered caption (`Fig. 1`) |
| `.notes` | one-line rows with a date on the right |

Palette: paper `#f2f0e9`, ink `#17181a`, one annotation red `#9b3a25`. No
radii, no shadows, no gradients, no animation beyond a 120 ms colour change.
Mono type is reserved for data cells — versions, dates, paths — and never used
as a decorative label above a heading.

Rationale, sources and the rejected alternatives are in
`docs/research-personal-sites.md` and section 11 of `docs/design-plan.md`.

## House rules

- Only publish facts that can be verified in the public repository.
- No metrics, user counts or testimonials that cannot be sourced.
- Every limitation goes next to the feature it limits, not in a footnote.
- Nothing personal beyond the name “Oliver”. No local paths, no employer, no
  location. The only public contact address is the one already listed in the
  launcher's README and LICENSE.
- An empty section stays empty. A plan is labelled as a plan.

## Fonts

`assets/fonts/newsreader-roman.woff2` and `newsreader-italic.woff2` are the
Latin subsets of Newsreader (Production Type), licensed under the SIL Open Font
License 1.1. Keep the licence notice if you replace the family.

## Regenerating the link card

```sh
pip install pillow
python scripts/og-card.py     # writes assets/img/og-card.png
```

Uses macOS system fonts, so it is an authoring tool rather than part of the
build.

## Search engines

The site is registered with both engines, and four files carry that state. Do
not delete them — each one is what keeps the property verified.

| File | What it is | Remove it and |
| --- | --- | --- |
| `index.html` → `google-site-verification` | Search Console ownership token for `https://oliver804.github.io/` | the Google property drops to unverified |
| `index.html` → `msvalidate.01` | Bing meta-tag route, kept alongside the file below | the fallback route stops working |
| `BingSiteAuth.xml` | Bing's file route, the one that actually verified | the Bing property drops to unverified |
| `<key>.txt` (`730d4866…`) | IndexNow key; the filename must equal its contents | IndexNow refuses submissions |

Registration state as of 20 Oct 2026:

- **Search Console** — property `https://oliver804.github.io/`, verified by meta
  tag. `sitemap.xml` submitted; Google reported *Couldn't fetch* on the first two
  attempts while the site and property were both minutes old. The file itself
  returns `200` with `content-type: application/xml` and parses to 9 URLs for
  both `curl` and a Googlebot user agent, so this is a queue state, not a
  broken sitemap. Re-check the Sitemaps report after a day.
- **Bing Webmaster Tools** — `oliver804.github.io/` verified via
  `BingSiteAuth.xml`, sitemap accepted (`Processing`), IndexNow accepted the
  nine URLs with `202`.

### After publishing a new page

1. Add it to `sitemap.xml`.
2. Push the nine-or-more URLs to IndexNow — Bing and Yandex pick it up in
   minutes instead of waiting for a crawl:

```sh
curl -s -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d '{"host":"oliver804.github.io","key":"'"$(cat 730d4866*.txt)"'",
       "keyLocation":"https://oliver804.github.io/'"$(basename 730d4866*.txt)"'",
       "urlList":["https://oliver804.github.io/writing/new-page/"]}'
```

3. In Search Console, run *URL Inspection* on the new URL and request indexing.
   There is a daily quota, so only do it for pages that matter.
