# Oliver’s Lab — source

Personal site for Oliver. Static HTML and one stylesheet, served by GitHub Pages.
No framework, no build step. The only JavaScript is two analytics tags —
documented below, and on the site itself at `/about/#analytics`.

Live at <https://oliver804.github.io/>

## What this site is

A work record, not a blog. The home page is an index of things that shipped —
one downloadable application, one repository of this site — followed by a short
list of notes. There is no archive, no schedule and no "latest" rail, because
the site is updated a few times a year and should still look current six months
later.

The reading order is deliberate: **work first, notes second, person third.**
Page titles, section order and type sizes all follow that order.

`/projects/` holds three different kinds of claim, and keeps them physically
apart:

| Section | What it is | Evidence |
| --- | --- | --- |
| Public projects | code anyone can download or read | releases, source, checksums |
| Engineering experience | paid work, described as practice | none published — no employer, client or dataset named |
| What is public, exactly | a data table about the two repositories | each row checkable |

The middle section is the one to be careful with. It may describe the shape of
a problem and the part Oliver owned. It may not name an employer, a client, an
internal system, a dataset, a team size or a percentage.


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
2. Update the spec list, figures, links, page title and JSON-LD.
3. Add a `<li>` to `.work` in `projects/index.html` with the next number, then
   the same entry in `index.html`. Work is the only numbered list on the site,
   and the numbers have to match across the two pages. Use
   `work-item--compact` for anything that should not compete with the first.
4. Update the facts table on `projects/index.html` (releases, platforms, licence,
   repository count) and the section note on both pages.
5. Add the project to the `ItemList` in the JSON-LD on both pages.

## Release data

Every version, date and file size on the site has to match the published
release, and the only way to be sure is to read it from GitHub rather than from
memory:

```sh
curl -s "https://github.com/oliver804/ChatGPT-Proxy-Launcher/releases/expanded_assets/v1.2.0" \
  | grep -oE '(Local-[A-Za-z0-9.-]+|SHA256SUMS\.txt)'
```

Sizes on the launcher page are decimal megabytes, which is what the release
page shows: the DMG is 2.1 MB and the Windows installer 53.8 MB as of 1.2.0.
Do not convert them to MiB and do not round a 51.28 MiB file to "51 MB".

Changing the version means editing it in five places: the `mono` line and the
spec table on the project page, the two data lines on `/projects/` and `/`,
the JSON-LD `softwareVersion`, and any download links in the page head.

## Analytics

Two tags sit at the end of `<head>` on **every** page — the ten files listed in
*Structure*. Both are async; neither blocks rendering, and the pages stay
readable if they fail.

| Tag | ID | Loads from |
| --- | --- | --- |
| Google Analytics 4 | `G-472VKF5Y95` | `googletagmanager.com/gtag/js` |
| Microsoft Clarity | `z0l2ymgxa3` | `clarity.ms/tag/` |

Both set first-party cookies (`_ga`, `_ga_472VKF5Y95`, `_clck`, `_clsk`). There
is no advertising or remarketing configuration, and no other third-party script
on the site.

**The tags are not described anywhere on the public site.** That is a deliberate
decision, not an oversight: they measure traffic, they are not content, and a
page explaining them turned the colophon into a blog post about the colophon. What
the pages still say about the build — no framework, no build step, no script
needed to render — remains true and checkable.

The trade-off is that a visitor cannot find out from the site that it is
measured. If that ever needs to change, the smallest honest form is one line in
the footer colophon, not a section.

Adding a page means adding the same block: copy everything between the
`<!-- Analytics: … -->` comment and the closing `</script>` of the Clarity tag,
and put it immediately before `</head>`. A page without it is the only way this
setup silently under-reports.

To remove the analytics entirely, delete that block from the ten files. Nothing
else references them — no CSS, no markup, no sitemap entry.

## Design decisions

Four patterns only, all defined in `assets/css/style.css`, plus two supporting
rows that reuse the same grid:

| Pattern | Used for |
| --- | --- |
| `.work-item` | a numbered entry in the work list: number, name, data line, copy, links |
| `.spec` | two-column data tables (version, platforms, licence) |
| `.fig` | a screenshot with a numbered caption (`Fig. 1`) |
| `.notes` | one-line rows with a date on the right |
| `.caps` | capability rows: label in serif, paragraph in sans (`/projects/#experience`) |
| `.faq` | question in serif, answer in sans (launcher page) |

`.work-item--compact` is the same record at a smaller size, used for the site's
own repository so it does not compete with the application above it.

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
- A claim the site makes about itself — *no cookies*, *no build step*, *loads
  nothing from another domain* — is updated in the same commit as the change
  that breaks it. Those sentences are checkable, so they are not allowed to rot.

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
