# One-time setup script: applies all styling to build/reference.docx
# (fonts, page breaks, keep-with-next, shloka shading). Already run --
# reference.docx has these baked in, so build.sh doesn't re-run this.
#
# Only re-run this if reference.docx needs to be regenerated from a clean
# pandoc default (e.g. `pandoc --print-default-data-file reference.docx >
# build/reference.docx`) and restyled from scratch. Requires
# `pip install python-docx`.

import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

path = "/workspace/gita-for-genz/build/reference.docx"
d = docx.Document(path)


def get_style(name):
    for s in d.styles:
        if s.name == name:
            return s
    raise KeyError(name)


def set_page_break_before(style):
    pPr = style.element.get_or_add_pPr()
    pPr.append(OxmlElement("w:pageBreakBefore"))


def set_keep_next(style):
    pPr = style.element.get_or_add_pPr()
    pPr.append(OxmlElement("w:keepNext"))


def set_shading(style, hex_color):
    pPr = style.element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    pPr.append(shd)


def set_font(style, name, size=None, bold=None, color=None):
    style.font.name = name
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), name)
    if size:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if color:
        style.font.color.rgb = docx.shared.RGBColor.from_string(color)


# Body text: a widely available serif, close to a book feel.
normal = get_style("Normal")
set_font(normal, "Garamond", 11.5)
normal.paragraph_format.space_after = Pt(10)
normal.paragraph_format.line_spacing = 1.25

# Chapter titles ("Fight N: ...") -- new page each chapter, keep with
# the paragraph that follows so the heading can't get stranded alone at
# the bottom of a page.
h1 = get_style("Heading 1")
set_font(h1, "Georgia", 26, bold=True, color="241C12")
set_page_break_before(h1)
set_keep_next(h1)
h1.paragraph_format.space_before = Pt(0)
h1.paragraph_format.space_after = Pt(6)

# Section labels (Scene / Shloka / Real Talk / Takeaway).
h2 = get_style("Heading 2")
set_font(h2, "Georgia", 15, bold=True, color="A8471F")
set_keep_next(h2)
h2.paragraph_format.space_before = Pt(20)
h2.paragraph_format.space_after = Pt(8)

h3 = get_style("Heading 3")
set_keep_next(h3)

# The paragraph right after any heading should stay with it too.
first_para = get_style("First Paragraph")
set_keep_next(first_para)

# Title page.
title = get_style("Title")
set_font(title, "Georgia", 34, bold=True)
title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = get_style("Subtitle")
set_font(subtitle, "Georgia", 16, bold=False)
subtitle.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Shloka verse quotes get a highlighted background, same idea as the
# website's accent-soft blockquote treatment.
bq = get_style("Block Text")
set_font(bq, "Garamond", 11)
bq.paragraph_format.left_indent = Pt(24)
bq.paragraph_format.right_indent = Pt(24)
set_shading(bq, "F3E3D3")

d.save(path)
print("Styled reference.docx")
