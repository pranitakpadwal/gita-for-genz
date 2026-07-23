# One-time setup script: bakes a faint chakra watermark into every page of
# build/reference.docx via a floating, "behind text" picture in the header
# (the same mechanism Word's own Insert > Watermark feature uses). Already
# run once -- reference.docx has the watermark saved in it, so build.sh
# doesn't need to re-run this. Only re-run if you want to change the
# watermark image, size, or opacity; requires `pip install python-docx`.
#
# Note: this shows up when the docx is opened directly (Word, Google Docs,
# etc.) and may or may not survive KDP's conversion to the actual Kindle
# file -- Kindle's reflowable format has no fixed "page," and header-based
# content is often stripped during that conversion. Untested against a
# real KDP preview.

import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsmap

path = "/workspace/gita-for-genz/build/reference.docx"
image_path = "/workspace/gita-for-genz/assets/illustrations/motifs/chakra-watermark.png"

d = docx.Document(path)
section = d.sections[0]
header = section.header
header.is_linked_to_previous = False

rId, image = header.part.get_or_add_image(image_path)

EMU = 914400
size = int(4.2 * EMU)

xml = f'''
<w:p xmlns:w="{nsmap['w']}">
  <w:r>
    <w:drawing xmlns:wp="{nsmap['wp']}">
      <wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0"
                 relativeHeight="1" behindDoc="1" locked="0" layoutInCell="1" allowOverlap="1">
        <wp:simplePos x="0" y="0"/>
        <wp:positionH relativeFrom="page">
          <wp:align>center</wp:align>
        </wp:positionH>
        <wp:positionV relativeFrom="page">
          <wp:align>center</wp:align>
        </wp:positionV>
        <wp:extent cx="{size}" cy="{size}"/>
        <wp:wrapNone/>
        <wp:docPr id="1001" name="Watermark"/>
        <wp:cNvGraphicFramePr/>
        <a:graphic xmlns:a="{nsmap['a']}">
          <a:graphicData uri="{nsmap['pic']}">
            <pic:pic xmlns:pic="{nsmap['pic']}">
              <pic:nvPicPr>
                <pic:cNvPr id="0" name="watermark-chakra.png"/>
                <pic:cNvPicPr/>
              </pic:nvPicPr>
              <pic:blipFill>
                <a:blip xmlns:r="{nsmap['r']}" r:embed="{rId}"/>
                <a:stretch><a:fillRect/></a:stretch>
              </pic:blipFill>
              <pic:spPr>
                <a:xfrm>
                  <a:off x="0" y="0"/>
                  <a:ext cx="{size}" cy="{size}"/>
                </a:xfrm>
                <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              </pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:anchor>
    </w:drawing>
  </w:r>
</w:p>
'''

new_p = parse_xml(xml)
header._element.append(new_p)

d.save(path)
print("Watermark added to header, rId:", rId)
