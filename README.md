# Oliver’s Lab — source

Personal site for Oliver. Static HTML and one stylesheet, served by GitHub Pages.
No framework, no build step, no JavaScript, no analytics.

Live at <https://oliver804.github.io/>

## Structure

```
.
├── index.html                              home
├── projects/
│   ├── index.html                           project index
│   └── local-route-launcher/index.html      project case notes
├── notes/
│   ├── index.html                           note index
│   └── why-the-launcher-drives-the-app/     published note
├── about/index.html                         about
├── 404.html
├── assets/
│   ├── css/style.css                        the whole design system
│   ├── fonts/                               Newsreader, self-hosted (OFL)
│   └── img/                                 screenshots, favicon, link card
├── scripts/og-card.py                       one-off generator for the 1200×630 card
├── docs/                                    research + design decisions
├── robots.txt  sitemap.xml  feed.xml
└── .nojekyll                                serve files as-is, no Jekyll
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

1. Copy `notes/why-the-launcher-drives-the-app/` to `notes/<slug>/`.
2. Change `<title>`, description, canonical, OG URL, the `<time datetime>`, and the body.
3. Add the entry to the top of the list in `notes/index.html`.
4. Add the entry to `feed.xml` and a `<url>` to `sitemap.xml`.

## Add a project

1. Copy `projects/local-route-launcher/` to `projects/<slug>/`.
2. Update the spec list, figures and links.
3. Add the entry to `projects/index.html`, and to the selected-work block in
   `index.html` only if it deserves to be the first thing a visitor sees.

## House rules

- Only publish facts that can be verified in the public repository.
- No metrics, user counts or testimonials that cannot be sourced.
- Every limitation goes next to the feature it limits, not in a footnote.
- Nothing personal beyond the name “Oliver”. No local paths, no private email,
  no employer, no location.

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
