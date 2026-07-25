#!/usr/bin/env python3
"""Post-processing step: inserts a small eyebrow tagline line above the
title on the auto-generated title page, for both the epub and docx
outputs. Pandoc's built-in title-block only supports title/subtitle/
author, so this patches the already-built files rather than fighting
pandoc's template.
"""
import sys
import zipfile
import shutil

TAGLINE = "A Gita for Gen Z"


def patch_epub(path):
    tmp_path = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin:
        names = zin.namelist()
        title_page_name = next(n for n in names if n.endswith("title_page.xhtml"))
        nav_name = next(n for n in names if n.endswith("nav.xhtml"))
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == title_page_name:
                    text = data.decode("utf-8")
                    text = text.replace(
                        '<h1 class="title">',
                        f'<p class="tagline">{TAGLINE}</p>\n  <h1 class="title">',
                    )
                    data = text.encode("utf-8")
                if item.filename == nav_name:
                    # Without --toc, pandoc places nav.xhtml at the EPUB
                    # root but still emits "../media/..." paths meant for
                    # files one level down (text/*.xhtml), which resolve
                    # outside the EPUB entirely. nav.xhtml is at the same
                    # level as media/, so the "../" needs to go.
                    text = data.decode("utf-8").replace("../media/", "media/")
                    data = text.encode("utf-8")
                # mimetype must stay stored, uncompressed, first entry
                compress_type = zipfile.ZIP_STORED if item.filename == "mimetype" else zipfile.ZIP_DEFLATED
                zout.writestr(item, data, compress_type=compress_type)
    shutil.move(tmp_path, path)
    print(f"Tagline added + nav.xhtml media paths fixed -> {path}")


def patch_docx(path):
    from docx import Document
    import copy
    from docx.text.paragraph import Paragraph

    doc = Document(path)
    title_idx = next(
        i for i, p in enumerate(doc.paragraphs) if p.style and p.style.name == "Title"
    )
    title_p = doc.paragraphs[title_idx]
    new_p_elem = copy.deepcopy(title_p._p)
    title_p._p.addprevious(new_p_elem)

    new_p = Paragraph(new_p_elem, title_p._parent)
    new_p.style = doc.styles["Subtitle"]
    for run in list(new_p.runs):
        run.text = ""
    if new_p.runs:
        new_p.runs[0].text = TAGLINE
    else:
        new_p.add_run(TAGLINE)
    for run in new_p.runs:
        run.italic = True
        if run.font.size:
            run.font.size = int(run.font.size * 0.7)

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
