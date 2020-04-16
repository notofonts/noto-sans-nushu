"""
    Remove all non-active layers (for Noto Nushu, this just cleans up unused layers in whitespace glyphs)

    To be run in GlyphsApp
"""

font = Glyphs.font

layers = []

for g in font.glyphs:
    if len(g.layers) > 1:
        activeLayer = g.layers[0].layerId
        print(activeLayer)
        layersToDelete = []
        for layer in g.layers:
            if layer.layerId is not activeLayer:
                layersToDelete.append(layer.layerId)
        for id in layersToDelete:
            del(g.layers[id])
