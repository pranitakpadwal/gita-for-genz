# Build: manuscript → ebook

Turns everything in `manuscript/front-matter/` + `manuscript/chapters/`
into a single manuscript and exports it to the file formats Amazon KDP
actually accepts.

## Requirements

- [pandoc](https://pandoc.org/installing.html) (the conversion engine —
  `apt install pandoc` / `brew install pandoc`)

## Run it

```
./build/build.sh
```

Outputs to `build/output/` (gitignored — regenerate anytime, don't
commit these):

- `krishna-texts-back.docx` — the **Kindle-ready manuscript**. This is
  what gets uploaded to KDP; their converter turns it into the actual
  reflowable Kindle ebook.
- `krishna-texts-back.epub` — an EPUB, for previewing in an e-reader app
  or submitting anywhere that wants EPUB instead of docx (e.g. Apple
  Books, Kobo, direct-to-reader sales later).

## How the styling works

`build/reference.docx` is a Word style template pandoc uses to format the
output — it defines what "Heading 1" (chapter titles), "Heading 2"
(Scene/Shloka/Real Talk/Takeaway), "Normal" (body text), and "Block Text"
(the Sanskrit verse quotes) look like. Several things are already set up
in it:

- Every chapter (`# Fight N: ...`, a Heading 1) starts on a fresh page
  automatically.
- Fonts are set to Georgia (headings) and Garamond (body) — not the
  Lora/Fraunces used on the preview site, because those are Google Fonts
  Word/KDP's converter can't use; Georgia/Garamond are universally
  available serifs that read as "book," not "webpage."
- Headings have "keep with next" set, so a heading can't get stranded
  alone at the bottom of a page with its content pushed to the next one.
- Shloka verse quotes (Block Text style) have a light shaded background,
  matching the highlighted look on the preview site.
- A faint chakra symbol is anchored in the header, centered and behind
  the text, so it repeats on every page — see "Page watermark" below.

To change fonts, spacing, or heading style further: open
`build/reference.docx` in Word or Google Docs, edit the styles (not the
placeholder text), save, and re-run the build. Pandoc reads the style
definitions, not the content, from this file.

### Page watermark

`build/scripts/add-header-watermark.py` is what generated the chakra
watermark already baked into `reference.docx` — it's a one-time setup
script, already run, not part of the normal `build.sh` flow. Only run it
again if you want to swap the image, resize it, or change its opacity
(edit `assets/illustrations/motifs/chakra-watermark.png`, or point the
script at a different motif from that folder, then re-run the script).

This is confirmed structurally correct (a real "behind text" floating
image in the header, the same mechanism as Word's own Insert > Watermark)
but not visually verified in this environment — LibreOffice's headless
PDF conversion doesn't work in this sandbox, unrelated to this file
specifically. Open the docx directly in Word to check it. It's also
untested whether this survives KDP's conversion to the actual Kindle
file — Kindle's reflowable format has no fixed "page" and often strips
header content, so don't be surprised if it doesn't carry through to a
real device even though it shows in Word.

## Getting it onto Amazon

1. **Run the build**, get `krishna-texts-back.docx`.
2. **Create a KDP account** at kdp.amazon.com (free) if you don't have
   one yet.
3. **"Create a new title" → Kindle eBook.** Upload the `.docx` directly
   — KDP's converter (Kindle Create, run automatically on upload) turns
   it into the actual Kindle format. It preserves headings, page breaks,
   and styles from the docx.
4. **Preview before publishing.** KDP shows an in-browser previewer
   after upload — check that chapter breaks, the Sanskrit verse
   formatting, and the table of contents all look right on a simulated
   device. (Amazon also has a free desktop app, Kindle Previewer, for a
   more thorough check across device sizes, if you want that before
   final upload.)
5. **Paperback is a separate, later step** — KDP Print needs a
   fixed-layout PDF (trim size, margins, bleed, gutter) generated
   differently from the reflowable ebook. Not part of this script yet;
   revisit once all 18 chapters are locked and Kindle is live.

## Current status

Only Fight 1 is in `manuscript/chapters/` right now, so the generated
docx/epub are a **one-chapter test of the pipeline**, not the book. As
chapters get added to that folder, re-running `build.sh` picks them up
automatically — no changes to this script needed.

`manuscript/front-matter/` is empty so far (title page, dedication,
"how to read this book" intro, author bio). Those get written and
dropped in later; the build already includes anything placed there
automatically, sorted before the chapters.
