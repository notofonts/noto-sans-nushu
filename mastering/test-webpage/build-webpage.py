"""
    A script to generate a basic HTML page with a unicode table from an OpenType font.

    USAGE:

    python docs/build-webpage.py docs/fonts/NotoSansNushu-Regular.ttf mastering/test-webpage/index.html
"""

from fontTools.ttLib import TTFont
import unicodedata

def getUnicodeName(c):
    try:
        return unicodedata.name(c).lower()
    except:
        print("unicode issue")


def main():

    html ="""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nushu Test Page</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <style>
    @font-face {
        font-family: "Nushu";
        src: url('./fonts/NotoSansNushu-Regular.ttf');
    }
    html {
        font-family: "Nushu", monospace;
    }
    .unicode-table {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(5rem, 1fr) );
    }
    .unicode-table>div {
        border: 1px solid #eee;
        text-align: center;
        padding: 0.5rem;
    }
    .letter-lg {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .label {
        font-size: 0.75rem;
    }
    </style>
    <body>        
        <!-- BEGIN CHARSET GRID -->
        <div class="unicode-table">
    """

    args = parser.parse_args()
    font = TTFont(args.fontpath)

    # fontGlyphs = {}
    fontC = ""
    print(font)

    for item in font['cmap'].getBestCmap():
        c = chr(item)
        print(c)

        html += f"""\
        <div class="detail">
            <div class="letter-lg">
                {c}          
            </div>
            <div class="label">
                <!-- {getUnicodeName(c)}  -->
                {'%04x' % ord(c)}
            </div>
        </div>
"""

    html += """\
            </div>
            <!-- END CHARSET GRID -->
        </body>
    </html>
    """

    path = args.indexHtmlPath
    with open(path, 'w') as file:
        file.write(html)
        print('saved to ', str(path)) 


if __name__ == "__main__":

    import argparse
    description = "Builds a unicode data table webpage for a font."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("fontpath",
                        help="The path to a font to build a unicode data table for")
    parser.add_argument("indexHtmlPath",
                        help="The path for an html file to build")


    main()