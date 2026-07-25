#!/usr/bin/env python3
"""Post-processing step: inserts a small tagline line under the subtitle
on the auto-generated title page, for both the epub and docx outputs.
Pandoc's built-in title-block only supports title/subtitle/author, so this
patches the already-built files rather than fighting pandoc's template.
"""
import sys
import zipfile
import shutil
import re

TAGLINE = "A Gita for Gen Z"


def patch_epub(path):
    tmp_path = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin:
        names = zin.namelist()
        title_page_name = next(n for n in names if n.endswith("title_page.xhtml"))
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == title_page_name:
                    text = data.decode("utf-8")
                    text = text.replace(
                        '<p class="author">',
                        f'<p class="tagline">{TAGLINE}</p>\n  <p class="author">',
                    )
                    data = text.encode("utf-8")
                # mimetype must stay stored, uncompressed, first entry
                compress_type = zipfile.ZIP_STORED if item.filename == "mimetype" else zipfile.ZIP_DEFLATED
                zout.writestr(item, data, compress_type=compress_type)
    shutil.move(tmp_path, path)
    print(f"Tagline added to epub title page -> {path}")


def patch_docx(path):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    import copy

    doc = Document(path)
    subtitle_idx = next(
        i for i, p in enumerate(doc.paragraphs) if p.style and p.style.name == "Subtitle"
    )
    subtitle_p = doc.paragraphs[subtitle_idx]
    new_p_elem = copy.deepcopy(subtitle_p._p)
    subtitle_p._p.addnext(new_p_elem)

    from docx.text.paragraph import Paragraph
    new_p = Paragraph(new_p_elem, subtitle_p._parent)
    for run in list(new_p.runs):
        run.text = ""
    if new_p.runs:
        new_p.runs[0].text = TAGLINE
    else:
        new_p.add_run(TAGLINE)
    for run in new_p.runs:
        run.font.size = subtitle_p.runs[0].font.size - 20000 if subtitle_p.runs and subtitle_p.runs[0].font.size else None
        run.italic = True

    doc.save(path)
    print(f"Tagline added to docx title page -> {path}")


if __name__ == "__main__":
    kind, path = sys.argv[1], sys.argv[2]
    if kind == "epub":
        patch_epub(path)
    elif kind == "docx":
        patch_docx(path)
    else:
        sys.exit(f"unknown kind {kind}")
