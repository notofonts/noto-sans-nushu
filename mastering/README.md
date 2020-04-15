# Mastering Noto Nüshu

## How to: build output font

### Set up dependencies

1. Make a virtual environment & activate it

```
python3 -m venv venv && source venv/bin/activate
```

2. Install requirements

```
pip install -r requirements.freeze.**txt**
```

3. Give execute permissions to build script

```
chmod +x mastering/build.sh
```

### Run the build

```
mastering/build.sh
```

### Check the outputs


Noto fonts use FontBakery to check quality. For installation instructions, see https://font-bakery.readthedocs.io/en/stable/user/installation/index.html.

Due to a current issue, Noto checks must be run by directly calling the script from the installed package:

```bash
source venv/bin/activate # if venv is not already active
python venv/lib/python3.7/site-packages/fontbakery/commands/check_notofonts.py fonts/NotoSansNushu-Regular.ttf
```

## How to: update noto-source repo

1. Fork https://github.com/googlefonts/noto-source
2. `git clone` your fork to have a local copy (or `git pull` from the upstream master to update your local copy, if you already have one)
3. `git checkout -b noto-sans-nushu` to make a new branch and move to it
4. Move GlyphsApp source into `src/NotoSansNushu`
5. `git add src/NotoSansNushu` to stage the change
6. `git commit -m "Update Noto Sans Nushu source"` (change message as needed)
7. Check if `.DS_Store` files have been created. If they have been, use `git clean -f` to remove uncommitted files.
8. Push to your remote fork
9. Pull Request to the noto-source repo

## How to: update noto-fonts repo

Repeat the above steps, but moving the TTF in `fonts/` to the directory `unhinted/NotoSansNushu` of https://github.com/googlefonts/noto-fonts.

---

## Log: work done in Mastering

### Cleaning up font source

I've made `source/nushu-glyphsapp-scripts/set-metrics.glyphs.py` to set vertical metrics as required by the document [Noto Font Delivery Requirements](https://github.com/arrowtype/noto-source/blob/bdf616554fca1b4c0e29a8cd52fdf3731d1c22a6/FONT_CONTRIBUTION.md)

### Build troubleshooting

The build failed with a traceback ending like this:

```
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/fontTools/pens/basePen.py", line 360, in decomposeQuadraticSegment
    assert n > 0
AssertionError
```

This was because the Latin alphabet glyphs in the source were in quadratic curves, copied in from a TTF. These were present only as examples during design, but should not be built into the final fonts (based on other Noto fonts).

I deleted these from the Glyphs source, and that made the build run fine. If these Latin glyphs *are* needed in this source, they should be copied in from https://github.com/googlefonts/noto-source/blob/39f54503fdc61a146702497d349bf3ce9eb83695/src/NotoSans-MM.glyphs, in which they are cubic curves.

### FontBakery checks & fixes

 - [x] file issue (https://github.com/googlefonts/fontbakery/issues/2831) for irrelevant checks `mono-bad-post-isFixedPitch`, `mono-bad-panose-proportion` 
 - [x] FAIL: Whitespace glyphs missing for the following codepoints: 0x00A0 (added `nbspace` to source)
 - [x] `WARN: GPOS table lacks kerning information.` verify that font should not have kerning (it shouldn't)

I've made `source/nushu-glyphsapp-scripts/set-metrics.glyphs.py` to set vertical metrics as required by the document "Noto Font Delivery Requirements."

## Test webpage

I adapted a [script originally made for the Recursive project](https://github.com/arrowtype/recursive/blob/23bf5fdbf5938a5ac533c7d8bd969226d939e882/src/build-scripts/data-tables-for-website/build-html-unicode-grid-from-string.py) that builds a Unicode data table for the Recursive minisite, but cleaned it up and simplified it for this project.

This is available at `docs/index.html`.

If desired, this can be hosted on GitHub Pages or elsewhere.

### Pull requested to Noto repos

- [noto-fonts/pull/1710](https://github.com/googlefonts/noto-fonts/pull/1710)
- [noto-source/pull/188](https://github.com/googlefonts/noto-source/pull/188)

