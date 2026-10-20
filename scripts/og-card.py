#!/usr/bin/env python3
"""Render the 1200x630 link-preview card (assets/img/og-card.png).

Run only when the headline or the domain changes:

    python3 scripts/og-card.py

Requires Pillow. Fonts are taken from the macOS system collection, so this
script is a one-off authoring tool rather than part of the site build.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "og-card.png"

W, H = 1200, 630
PAPER = "#faf8f3"
INK = "#191b16"
INK_2 = "#5f6457"
INK_3 = "#8a8f80"
RULE = "#dad5c7"

SERIF = "/System/Library/Fonts/Supplemental/Charter.ttc"
SERIF_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=index)


def tracked(draw, xy, text, fnt, fill, tracking=0.0, anchor_right=None):
    """Draw text with letter-spacing; returns the x cursor after the run."""
    x, y = xy
    for ch in text:
        if anchor_right is not None and ch == text[0]:
            pass
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    left = 140
    right = W - 96

    # notebook corner: one vertical margin rule, one baseline rule
    d.line([(96, 88), (96, 520)], fill=RULE, width=1)
    d.line([(left - 44, 520), (right, 520)], fill=RULE, width=1)

    eyebrow = "SOFTWARE ENGINEERING · DATA · AI-ASSISTED DEVELOPMENT"
    tracked(d, (left, 104), eyebrow, font(MONO, 15, 0), INK_3, tracking=2.0)

    headline = font(SERIF, 76, 0)
    italic = font(SERIF_ITALIC, 76)
    d.text((left, 196), "Software that holds up", font=headline, fill=INK)

    x = left
    for text, fnt in (("after launch", italic), (".", headline)):
        d.text((x, 292), text, font=fnt, fill=INK)
        x += d.textlength(text, font=fnt)

    d.text((left, 420), "One open-source project, and notes on building tools "
                        "that stay maintainable.", font=font(SERIF, 26, 0), fill=INK_2)

    d.text((left, 540), "Oliver’s Lab", font=font(SERIF, 24, 0), fill=INK)

    site = "oliver804.github.io"
    site_font = font(MONO, 17, 0)
    d.text((right - d.textlength(site, font=site_font), 546), site,
           font=site_font, fill=INK_2)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
