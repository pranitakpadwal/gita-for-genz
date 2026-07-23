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
(Scene/Shloka/Why It Lands/Takeaway), "Normal" (body text), and "Block
Text" (the Sanskrit verse quotes) look like. Two things are already set
up in it:

- Every chapter (`# Fight N: ...`, a Heading 1) starts on a fresh page
  automatically.
- Fonts are set to Georgia (headings) and Garamond (body) — not the
  Lora/Fraunces used on the preview site, because those are Google Fonts
  Word/KDP's converter can't use; Georgia/Garamond are universally
  available serifs that read as "book," not "webpage."

To change fonts, spacing, or heading style further: open
`build/reference.docx` in Word or Google Docs, edit the styles (not the
placeholder text), save, and re-run the build. Pandoc reads the style
definitions, not the content, from this file.

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
