
# coding: utf-8

# In[ ]:

#!/usr/bin/python3
#+
# Demo of text and font support in Qahirah. For best results,
# your system should have a decent range of fonts installed.
#
# Copyright 2015 by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
# This script is licensed CC0
# <https://creativecommons.org/publicdomain/zero/1.0/>; do with it
# what you will.
#-

import sys
import os
import qahirah as qah
CAIRO = qah.CAIRO
Vector = qah.Vector

font_names =     ( # some popular names to try
        "courier")
font_size = 48
line_spacing = 1.5
shadow_offset = 1.5
shadow_thickness = 1.0

pix = qah.ImageSurface.create   (
    format = CAIRO.FORMAT_RGB24,
    dimensions = round(Vector(640, 420))
  )
g = qah.Context(pix)
g.set_source_rgb(.2, .5, .5)
g.paint()
g.set_source_rgb(.8, 1, .8)
g.set_font_size(font_size)

pos = Vector(80, font_size * line_spacing / 1)
for font_name in font_names :
    plain_face = qah.FontFace.create_for_pattern(font_name)
    g.font_face = plain_face
    g.move_to(pos)
    g.show_text('BroBeur')
    for name, suffix in         (
            ("cybercafe", ":slant=italic"),
            #("bold", ":weight=bold"),
            #("bold-italic", ":slant=italic:weight=bold"),
        ) \
    :
        g.font_face = qah.FontFace.create_for_pattern(font_name + suffix)
        g.show_text(" " + name)
    #end for
    g.font_face = plain_face


pix.flush()
pix.write_to_png("%s.png" % os.path.basename(sys.argv[0]))


# In[ ]:



