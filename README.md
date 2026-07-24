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
  final: **Scene → Shloka → Real Talk → Takeaway.** (Section 3 was
  originally called "Why It Lands" — renamed after reader feedback that
  the label itself was confusing. Same job, clearer name.)
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
  3. *Real Talk* — the bridge. Connects the textual explanation back to
     the reader directly: this is you, right now, in that scene. Makes
     the meta-point explicit (why the Gita handles it this way) and
     universalizes it. This is the section that does the actual arguing —
     Shloka informs, Real Talk persuades.
  4. *Takeaway* — one tight, quotable line (or a short paragraph, max)
     that compresses Real Talk into something screenshot-able. It's
     meant to overlap with Real Talk on purpose — this is the retention
     line for skimmers, not new content.
  5. *Krishna Texts Back* — the signature closing beat, added in the v2
     editorial pass. A short (~110-130 word) direct message from Krishna
     to the reader, in his own timeless, calm voice (deliberately NOT
     motivational-influencer speak), echoing that chapter's teaching as
     if he were texting back. Reinforces the title and gives each fight a
     distinct final note. Rendered as an italic reply block with the
     conch (shankha) icon, visually distinct from the verse quotes.
  The 5-part shape stays consistent across all 18 chapters; only the
  length of Shloka and Real Talk flexes to match how much the source
  chapter is actually carrying.
- **Graphics**: one chapter-opener illustration per chapter (title-page
  style). Interior stays text-only — keeps it reflow-friendly for Kindle
  and keeps production manageable. Art direction briefs live in
  `assets/illustrations/briefs/`.
- **Tone**: direct, a little funny where it's earned, never mocking the
  source material and never mocking the reader either. The goal is
  *faster understanding*, not a meme version of scripture.

## Editorial guardrails

- **No em dashes.** Zero, in any chapter. Reader feedback on Fight 1 was
  that the prose read as AI-written, and the em dash is one of the more
  recognizable tells. Use a period, comma, colon, or parentheses instead,
  or just restructure the sentence. (En dashes in verse citations like
  `BG 1.28–30` are fine, that's a normal number-range convention, not the
  same thing.)
- **Don't overuse "it's not X, it's Y."** That reversal construction
  ("Arjuna doesn't hesitate because he's a coward, he hesitates because
  ...") is a natural move, but Fight 1's first draft leaned on it 8-9
  times in one chapter and it started reading as a tic, not a voice. One,
  maybe two per chapter, and vary how it's built (fragments, direct
  statement, a question) instead of repeating the same two-sentence
  shape.
- **Lead with the feeling, not the analysis.** Reader feedback also
  flagged "emotions missing" — the risk of this format is that Shloka and
  Real Talk read as explainers instead of something felt. Put physical,
  specific sensation in the Scene (stomach hurting, throat tight, feet
  heavy) rather than naming the emotion abstractly, and let Real Talk
  stay a little rough around the edges rather than fully resolved and
  tidy.
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
build/
  build.sh           manuscript -> docx (Kindle) + epub, see build/README.md
  reference.docx     Word style template build.sh uses (fonts, page breaks)
```

## Status

Fight 1 is a **format sample**, drafted, revised, and approved. Title and
editorial guardrails are locked (see above). The manuscript → ebook build
pipeline works (see `build/README.md` for how to run it and upload to
KDP) — currently a one-chapter test of the pipeline, not the finished
book. Next: outline all 18 chapters, then draft the rest. See
`manuscript/chapters/01-the-freeze.md`.
