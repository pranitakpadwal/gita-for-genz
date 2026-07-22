# Gita for Gen Z

The Bhagavad Gita's 18 chapters, retold through the situations we actually
live in — a group chat spiraling, a boundary you're scared to set, burnout
you're pretending isn't burnout, a decision your parents won't understand.
Same teaching. Less gyaan, more "oh, this is literally me right now."

## Vision

- **Format**: Kindle ebook first (reflowable, ships fast, easy to revise),
  paperback / print-on-demand second once the content is locked.
- **Structure per chapter**: **Scene → Shloka → Takeaway.**
  1. *Scene* — a real, specific Gen Z moment (named character, present
     tense) that puts the reader inside the same emotional problem Arjuna
     or Krishna is dealing with in that chapter — no explanation yet, just
     the situation.
  2. *Shloka* — the actual chapter content: what happens/is taught in that
     chapter of the Gita, referenced by verse, explained plainly.
  3. *Takeaway* — one tight, quotable line (or a short paragraph, max) that
     the reader could screenshot. Not a moral lecture — the point already
     landed in the scene.
- **Graphics**: one chapter-opener illustration per chapter (title-page
  style). Interior stays text-only — keeps it reflow-friendly for Kindle
  and keeps production manageable. Art direction briefs live in
  `assets/illustrations/briefs/`.
- **Tone**: direct, a little funny where it's earned, never mocking the
  source material and never mocking the reader either. The goal is
  *faster understanding*, not a meme version of scripture.

## Repo structure

```
manuscript/
  front-matter/     title page, intro/how-to-read-this-book
  chapters/         01-....md through 18-....md, one file per chapter
assets/
  illustrations/
    briefs/          text art-direction briefs, one per chapter
  cover/             front cover assets (added once content is locked)
build/               md -> docx/pdf export pipeline (added once format is approved)
```

## Status

Chapter 1 is a **format sample** — draft it, react to it, and we lock the
template before doing the rest. See `manuscript/chapters/01-the-freeze.md`.
