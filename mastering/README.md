# Mastering Noto Nüshu

Goal: mastering & PR Noto Nüshu to meet [Noto Font Submission Requirements](https://github.com/arrowtype/noto-source/blob/bdf616554fca1b4c0e29a8cd52fdf3731d1c22a6/FONT_CONTRIBUTION.md).

## Build instructions

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

## Update noto-source repo

1. Fork https://github.com/googlefonts/noto-source
2. `git clone` your fork to have a local copy (or `git pull` from the upstream master to update your local copy, if you already have one)
3. `git checkout -b noto-sans-nushu` to make a new branch and move to it
4. Move GlyphsApp source into `src/NotoSansNushu`
5. `git add src/NotoSansNushu` to stage the change
6. `git commit -m "Update Noto Sans Nushu source"` (change message as needed)
7. Check if `.DS_Store` files have been created. If they have been, use `git clean -f` to remove uncommitted files.
8. Push to your remote fork
9. Pull Request to the noto-source repo

## Update noto-fonts repo

Repeat the above steps, but moving the TTF in `fonts/` to the directory `unhinted/NotoSansNushu` of https://github.com/googlefonts/noto-fonts.

## Troubleshooting

The build may fail with a traceback ending like this:

```
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/fontTools/pens/basePen.py", line 360, in decomposeQuadraticSegment
    assert n > 0
AssertionError
```

In this case, it may be due to the Latin alphabet glyphs in the source, which are already cubic curves. These are present only as examples during design, but should not be built into the final fonts.

These should be deleted from the Glyphs source, and the build should be run again.

## FontBakery checks

 - [x] file issue (https://github.com/googlefonts/fontbakery/issues/2831) for irrelevant checks `mono-bad-post-isFixedPitch`, `mono-bad-panose-proportion` 
 - [x] FAIL: Whitespace glyphs missing for the following codepoints: 0x00A0 (added `nbspace` to source)
 - [ ] `WARN: GPOS table lacks kerning information.` verify that font should not have kerning

## Questions for Lisa


- Is it useful to have the Latin alphabet in the Nushü source? (If so, I may try to add that back in as OTF outlines, but subset it from the outputs).

## Tasks
- [x] set vertical metrics to spec
- [x] build otf & ttf
- [x] merge previous `mastering` branch with this one (I made two due to a temporary computer issue)
- [ ] PR to https://github.com/googlefonts/noto-fonts


I've made `mastering/set-metrics.glyphs.py` to set vertical metrics as required by the document "Noto Font Delivery Requirements."

