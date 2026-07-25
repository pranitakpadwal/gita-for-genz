#!/usr/bin/env bash
# Builds the manuscript (manuscript/front-matter + manuscript/chapters) into
# a Kindle-ready .docx and a .epub. Requires pandoc (https://pandoc.org).
#
# Usage: ./build/build.sh

set -euo pipefail

# Force a UTF-8 locale: under POSIX/C locale, bash mangles multi-byte
# characters (like the curly apostrophe in BOOK_SUBTITLE below) when they
# pass through shell variables/arguments, producing mojibake in pandoc's
# output even though this file itself is valid UTF-8.
export LC_ALL=C.utf8

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/build/output"
BOOK_TITLE="Krishna Texts Back"
BOOK_SUBTITLE="18 Fights You’re Already In"
BOOK_AUTHOR="Rudra Prasad Kasturi"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is required but not installed. See https://pandoc.org/installing.html" >&2
  exit 1
fi

# Chapter/front-matter files reference images with paths relative to the repo
# root (e.g. "assets/illustrations/final/01-the-freeze.png") -- run pandoc
# from there so those resolve correctly regardless of where build.sh is
# invoked from.
cd "$ROOT_DIR"

mkdir -p "$OUT_DIR"
COMBINED="$OUT_DIR/manuscript.md"

{
  shopt -s nullglob
  for f in $(ls "$ROOT_DIR"/manuscript/front-matter/*.md 2>/dev/null | sort); do
    cat "$f"
    printf '\n\n'
  done
  for f in $(ls "$ROOT_DIR"/manuscript/chapters/*.md | sort); do
    cat "$f"
    printf '\n\n'
  done
  for f in $(ls "$ROOT_DIR"/manuscript/back-matter/*.md 2>/dev/null | sort); do
    cat "$f"
    printf '\n\n'
  done
} > "$COMBINED"

echo "Combined manuscript -> $COMBINED"

# Section-icon version: prepend the matching icon image to each section
# heading (Scene / Shloka / Real Talk / Takeaway), so the ebook has the
# same little icons the website shows. Only the epub uses this; the docx
# uses the plain combined file.
#
# PNG, not SVG: pandoc's epub writer mislabels embedded SVGs with a
# .svgz extension (implying gzip compression) while leaving the content
# uncompressed, which Amazon's KDP converter chokes on ("couldn't
# convert your HTML file to Kindle format"). Kindle's renderer also has
# unreliable SVG support in general, so PNG icons sidestep both problems.
COMBINED_ICONS="$OUT_DIR/manuscript-icons.md"
sed \
  -e 's|^## Scene$|## ![](assets/illustrations/icons/scene.png){width=18px} Scene|' \
  -e 's|^## Shloka$|## ![](assets/illustrations/icons/shloka.png){width=18px} Shloka|' \
  -e 's|^## Real Talk$|## ![](assets/illustrations/icons/why-it-lands.png){width=18px} Real Talk|' \
  -e 's|^## Takeaway$|## ![](assets/illustrations/icons/takeaway.png){width=18px} Takeaway|' \
  -e 's|^## Krishna Texts Back$|## ![](assets/illustrations/icons/krishna.png){width=18px} Krishna Texts Back|' \
  "$COMBINED" > "$COMBINED_ICONS"

pandoc "$COMBINED" \
  --from=markdown+smart \
  --to=docx \
  --reference-doc="$ROOT_DIR/build/reference.docx" \
  --metadata title="$BOOK_TITLE" \
  --metadata subtitle="$BOOK_SUBTITLE" \
  --metadata author="$BOOK_AUTHOR" \
  -o "$OUT_DIR/krishna-texts-back.docx"

python3 "$ROOT_DIR/build/scripts/add-tagline.py" docx "$OUT_DIR/krishna-texts-back.docx"

echo "Kindle-ready docx -> $OUT_DIR/krishna-texts-back.docx"

pandoc "$COMBINED_ICONS" \
  --from=markdown+smart \
  --to=epub3 \
  --css="$ROOT_DIR/build/epub.css" \
  --metadata title="$BOOK_TITLE" \
  --metadata subtitle="$BOOK_SUBTITLE" \
  --metadata author="$BOOK_AUTHOR" \
  --epub-cover-image="$ROOT_DIR/assets/cover/cover.png" \
  -o "$OUT_DIR/krishna-texts-back.epub"

python3 "$ROOT_DIR/build/scripts/add-tagline.py" epub "$OUT_DIR/krishna-texts-back.epub"

echo "EPUB -> $OUT_DIR/krishna-texts-back.epub"
