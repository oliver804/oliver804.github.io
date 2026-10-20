#!/usr/bin/env python3
"""Render the 1200x630 link-preview card (assets/img/og-card.png).

Run only when the headline, the palette or the domain changes:

    python3 scripts/og-card.py

Requires Pillow. Fonts are taken from the macOS system collection, so this
script is a one-off authoring tool rather than part of the site build.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "og-card.png"

W, H = 1200, 630
PAPER = "#f2f0e9"
INK = "#17181a"
INK_2 = "#4e5154"
INK_3 = "#63666a"
RULE = "#d5d1c3"
MARK = "#9b3a25"

SERIF = "/System/Library/Fonts/Supplemental/Charter.ttc"
MONO = "/System/Library/Fonts/Menlo.ttc"


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=index)


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    left = 100
    right = W - 100

    # drawing-sheet marks: one red margin line, one baseline rule
    d.line([(56, 90), (56, 512)], fill=MARK, width=1)
    d.line([(left, 512), (right, 512)], fill=RULE, width=1)

    head = font(SERIF, 74, 0)
    for i, line in enumerate(("I build small tools,", "then write down", "what they cost.")):
        d.text((left, 150 + i * 88), line, font=head, fill=INK)

    d.text((left, 72), "Oliver’s Lab", font=font(SERIF, 24, 0), fill=INK)
    site = "oliver804.github.io"
    site_font = font(MONO, 16, 0)
    d.text((right - d.textlength(site, font=site_font), 76), site,
           font=site_font, fill=INK_3)

    d.text((left, 540), "Local Route Launcher 1.2.0 — macOS and Windows, MIT",
           font=font(MONO, 17, 0), fill=INK_2)

    year = "2026"
    d.text((right - d.textlength(year, font=font(MONO, 17, 0)), 540), year,
           font=font(MONO, 17, 0), fill=INK_2)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
