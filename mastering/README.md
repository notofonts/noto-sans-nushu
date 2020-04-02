# Mastering Noto Nüshu

## Build instructions

### Set up dependencies

1. Make a virtual environment & activate it

```
python3 -m venv venv && source venv/bin/activate
```

2. Install requirements

```
pip install -r requirements.txt
```

3. Give execute permissions to build script

```
chmod +x mastering/build.sh
```

### Run the build

```
mastering/build.sh
```

## Troubleshooting

The build may fail with a traceback ending like this:

```
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/fontTools/pens/basePen.py", line 360, in decomposeQuadraticSegment
    assert n > 0
AssertionError
```

In this case, it may be due to the Latin alphabet glyphs in the source, which are already cubic curves. These are present only as examples during design, but should not be built into the final fonts.

These should be deleted from the Glyphs source, and the build should be run again.

## Questions for Lisa

- Is there a link on github somewhere for “Noto Font Delivery Requirements”? If so, I’ll add it to my notes
- Is it useful to have the Latin alphabet in the Nushü source? (If so, I may try to add that back in as OTF outlines, but subset it from the outputs).

## Tasks
- [x] set vertical metrics to spec
- [x] build otf & ttf
- [x] merge previous `mastering` branch with this one (I made two due to a temporary computer issue)
- [ ] PR to https://github.com/googlefonts/noto-fonts


I've made `mastering/set-metrics.glyphs.py` to set vertical metrics as required by the document "Noto Font Delivery Requirements."

