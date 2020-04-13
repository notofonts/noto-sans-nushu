"""
    Set vertical metrics to follow Google Noto standards.

    Meant for use within GlyphApp.
    
    Some code borrowed from https://github.com/googlefonts/gf-glyphs-scripts/blob/master/Google%20Fonts/initial_vertmetrics.py
"""

font = Glyphs.font

font.customParameters["Use Typo Metrics"] = True

tallestGlyph = ""
lowestGlyph = ""
yMax = 0
yMin = 0

def verticalBBox(glyph):
    
    _max = None
    _min = None
    
    for layer in glyph.layers:
        
        top = layer.bounds.origin.y + layer.bounds.size.height
        bottom = layer.bounds.origin.y
        
        if not _max:
            _max = top
        else:
            _max = max(_max, top)
        if not _min:
            _min = bottom
        else:
            _min = min(_min, bottom)

    return _min, _max       
    
for g in f.glyphs:  
	if g.export:
	    bbox = verticalBBox(g)
	    _min, _max = bbox
	    
	    if _min < yMin:
	        yMin = _min
	        lowestGlyph = g.name

	    if _max > yMax:
	        yMax = _max
	        tallestGlyph = g.name
	        
print "tallest glyph is ", tallestGlyph, " at ", yMax
print "\nlowest glyph is ", lowestGlyph, " at ", yMin

if yMax <= 1069 and yMin >= -293:
	for master in font.masters:
		
		master.customParameters["hheaAscender"] = 1069
		master.customParameters["hheaDescender"] = -293
		master.customParameters["hheaLineGap"] = 0		
		master.customParameters["winAscent"] = 1069
		master.customParameters["winDescent"] = -293
		master.customParameters["typoAscender"] = 1069
		master.customParameters["typoDescender"] = -293
		master.customParameters["typoLineGap"] = 0

else:
	print "refer to docs and update this script as needed"
