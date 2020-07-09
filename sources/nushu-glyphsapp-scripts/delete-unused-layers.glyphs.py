"""
    Remove all non-active layers (for Noto Nushu, this just cleans up unused layers in whitespace glyphs)

    To be run in GlyphsApp
"""

font = Glyphs.font

for g in font.glyphs:
    for layer in list(g.layers):
        if not layer.isMasterLayer:
            del(g.layers[layer.layerId])