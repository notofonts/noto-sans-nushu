# !/bin/bash

# A script to build Noto Sans Nushu
# See mastering/README.md for setup instructions

source venv/bin/activate

set -e

fontmake -o ttf -g source/NotoSansNushu.glyphs --output-dir fonts

# add empty dsig table

gftools fix-dsig "fonts/NotoSansNushu-Regular.ttf" --autofix