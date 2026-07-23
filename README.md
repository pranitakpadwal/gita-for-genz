# Krishna Texts Back

### 18 Fights You're Already In

The Bhagavad Gita's 18 chapters, retold through the situations we actually
live in — a group chat spiraling, a boundary you're scared to set, burnout
you're pretending isn't burnout, a decision your parents won't understand.
Same teaching. Less gyaan, more "oh, this is literally me right now."

> **Naming note**: the working title used to be "Gita for Gen Z." That's
> now a real, Penguin-published book (*The Gita for Gen Z: Clarity in
> Chaos* by Rania Sen, Dec 2024) plus at least two other self-published
> titles using near-identical names. We're not competing on a crowded,
> already-owned title — hence *Krishna Texts Back*.

## Vision

- **Format**: Kindle ebook first (reflowable, ships fast, easy to revise),
  paperback / print-on-demand second once the content is locked.
- **Structure per chapter, labeled "Fight 1" through "Fight 18"** — locked,
  final: **Scene → Shloka → Why It Lands → Takeaway.**
  1. *Scene* — a real, specific Gen Z moment (named character, present
     tense) that puts the reader inside the same emotional problem Arjuna
     or Krishna is dealing with in that chapter — no explanation yet, just
     the situation.
  2. *Shloka* — the actual chapter content: what happens/is taught in that
     chapter of the Gita, referenced by verse, explained plainly. This is
     information — what the text says — not yet what it means for the
     reader. For the philosophically dense chapters (2, 6, 12, 13, 15,
     18 — the ones carrying real argument, not just a moment), this
     section runs longer and can move through 2–3 sub-scenes instead of
     one.
  3. *Why It Lands* — the bridge. Connects the textual explanation back to
     the reader directly: this is you, right now, in that scene. Makes
     the meta-point explicit (why the Gita handles it this way) and
     universalizes it. This is the section that does the actual arguing —
     Shloka informs, Why It Lands persuades.
  4. *Takeaway* — one tight, quotable line (or a short paragraph, max)
     that compresses Why It Lands into something screenshot-able. It's
     meant to overlap with Why It Lands on purpose — this is the
     retention line for skimmers, not new content.
  The 4-part shape stays consistent across all 18 chapters; only the
  length of Shloka and Why It Lands flexes to match how much the source
  chapter is actually carrying.
- **Graphics**: one chapter-opener illustration per chapter (title-page
  style). Interior stays text-only — keeps it reflow-friendly for Kindle
  and keeps production manageable. Art direction briefs live in
  `assets/illustrations/briefs/`.
- **Tone**: direct, a little funny where it's earned, never mocking the
  source material and never mocking the reader either. The goal is
  *faster understanding*, not a meme version of scripture.

## Editorial guardrails

- **Don't flatten the philosophy.** This genre gets fairly criticized for
  reducing the Gita to feel-good one-liners that fall apart under any
  real scrutiny. The dense chapters (see above) are allowed to be longer
  and harder — resist the urge to force every chapter into a single
  Instagram-quote takeaway just for consistency's sake.
- **Swadharma / duty (chapters 3, 4, 18).** Frame it throughout as *your
  authentic individual calling* — that's the standard, defensible modern
  reading, not a dodge. But somewhere in Chapter 18 (the synthesis
  chapter), include one direct, honest paragraph acknowledging that this
  teaching was historically used to justify caste hierarchy (Ambedkar's
  well-known critique), and why this book reads it differently. One
  paragraph, not a detour into caste politics — but not silence either.

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

Fight 1 is a **format sample**, drafted and approved. Title and editorial
guardrails are locked (see above). Next: outline all 18 chapters, then
draft the rest. See `manuscript/chapters/01-the-freeze.md`.
