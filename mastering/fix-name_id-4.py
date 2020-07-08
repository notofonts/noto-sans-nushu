"""
    Matches name ID 4 to name ID 1, which is expected in a single-style font.

    Run it from the directory above with the following command, including a font path:

    python mastering/fix-name_id-4.py fonts/NotoSansNushu-Regular.ttf
"""

import sys
from fontTools.ttLib import TTFont

# sets 'fontPath' variable to use the font path you pass in
fontPath = sys.argv[1]

print(fontPath)

# GET / SET NAME HELPER FUNCTIONS

def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font['name'].getName(ID, platformID, platEncID))
    return name

def setFontNameID(font, ID, newName):
    
    print(f"\n\t• name {ID}:")
    macIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}

    oldMacName = font['name'].getName(ID, *macIDs.values())

    if oldMacName != newName:
        print(f"\n\t\t Mac name was '{oldMacName}'")
        font['name'].setName(newName, ID, *macIDs.values())
        print(f"\n\t\t Mac name now '{newName}'")

# MAIN FUNCTION

def main(fontPath):
    # open font with TTFont
    font = TTFont(fontPath)

    # Font is a single weight only, so match name 4 to name 1
    name1 = getFontNameID(font, 1)
    setFontNameID(font, 4, name1)

    font.save(fontPath)


main(fontPath)
