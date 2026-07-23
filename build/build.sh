#!/usr/bin/env bash
# Builds the manuscript (manuscript/front-matter + manuscript/chapters) into
# a Kindle-ready .docx and a .epub. Requires pandoc (https://pandoc.org).
#
# Usage: ./build/build.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/build/output"
BOOK_TITLE="Krishna Texts Back"
BOOK_SUBTITLE="18 Fights You're Already In"
BOOK_AUTHOR="Rudra Prasad Kasturi"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is required but not installed. See https://pandoc.org/installing.html" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
COMBINED="$OUT_DIR/manuscript.md"

{
  shopt -s nullglob
  for f in "$ROOT_DIR"/manuscript/front-matter/*.md; do
    cat "$f"
    printf '\n\n'
  done
  for f in $(ls "$ROOT_DIR"/manuscript/chapters/*.md | sort); do
    cat "$f"
    printf '\n\n'
  done
} > "$COMBINED"

echo "Combined manuscript -> $COMBINED"

pandoc "$COMBINED" \
  --from=markdown+smart \
  --to=docx \
  --reference-doc="$ROOT_DIR/build/reference.docx" \
  --metadata title="$BOOK_TITLE" \
  --metadata subtitle="$BOOK_SUBTITLE" \
  --metadata author="$BOOK_AUTHOR" \
  --toc --toc-depth=1 \
  -o "$OUT_DIR/krishna-texts-back.docx"

echo "Kindle-ready docx -> $OUT_DIR/krishna-texts-back.docx"

pandoc "$COMBINED" \
  --from=markdown+smart \
  --to=epub3 \
  --metadata title="$BOOK_TITLE" \
  --metadata subtitle="$BOOK_SUBTITLE" \
  --metadata author="$BOOK_AUTHOR" \
  --toc --toc-depth=1 \
  -o "$OUT_DIR/krishna-texts-back.epub"

echo "EPUB -> $OUT_DIR/krishna-texts-back.epub"
