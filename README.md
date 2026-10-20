# Oliver’s Lab — source

Personal site for Oliver. Static HTML and one stylesheet, served by GitHub Pages.
No framework, no build step, no JavaScript, no analytics.

Live at <https://oliver804.github.io/>

## What this site is

Three parts, deliberately: a personal technical brand, a public record of the
open-source work, and the writing that comes out of building it. The home page
carries the project, the writing index carries the notes, and the project page
carries the evidence — release artefacts, checks and limits.

## Structure

```
.
├── index.html                              home
├── projects/
│   ├── index.html                          project index
│   └── local-route-launcher/index.html     project case notes
├── writing/
│   ├── index.html                          writing index, topics, plans
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
├── docs/                                   research + design decisions
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
   `<time datetime>`, the topic label, the reading time and the body.
3. Add one entry to the top of the list in `writing/index.html`, and to the
   three-entry list in `index.html` if it belongs on the home page.
4. Update the topic counts in `writing/index.html`, and move a topic out of the
   *Planned* section when its first note is published.
5. Add the entry to `feed.xml` and a `<url>` to `sitemap.xml`.
6. Set the *Read next* link at the bottom of the previous note to the new one,
   and give the new note its own *Read next* link.

Reading time is word count ÷ 200, rounded up.

## Add a project

1. Copy `projects/local-route-launcher/` to `projects/<slug>/`.
2. Update the spec list, figures and links.
3. Add the entry to `projects/index.html`, and to the selected-work block in
   `index.html` only if it deserves to be the first thing a visitor sees.
4. Update the facts table on `projects/index.html` when the release, the
   licence or the repository count changes.

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
