# !/bin/bash

# A script to build Noto Sans Nushu
# See mastering/README.md for setup instructions

# ------------------------------------------------------
# CONFIGURATION - update these paths if needed

source="source/NotoSansNushu.glyphs"
output="fonts/NotoSansNushu-Regular.ttf"

# ------------------------------------------------------
# sets up script to run properly

source venv/bin/activate
set -e

# ------------------------------------------------------
# builds static TTF

fontmake -o ttf -g $source --output-dir fonts

# ------------------------------------------------------
# fixes for fontbakery

# add empty dsig table
gftools fix-dsig $output --autofix

# fix gasp
gftools fix-gasp $output --autofix
mv ${output/".ttf"/".ttf.fix"} $output

# fix prep dropout - args for fontfile_in, fontfile_out
gftools fix-nonhinting $output $output
rm ${output/".ttf"/"-backup-fonttools-prep-gasp.ttf"}

# ------------------------------------------------------
# copy font to web test

cp $output mastering/test-webpage/fonts/NotoSansNushu-Regular.ttf
