# Mastering Noto Nüshu

## How to: build output font

### Set up dependencies

1. Make a virtual environment & activate it

```
python3 -m venv venv && source venv/bin/activate
```

2. Install requirements

```
pip install -r requirements.freeze.txt
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

I also ran the `check-googlefonts` FontBakery checks to see whether any suggested fixes from there would be useful. For this, I added several steps to the build script:
- `gftools fix-dsig`
- `gftools fix-gasp`
- `gftools fix-nonhinting` for "Font enables smart dropout control in "prep" table instructions?"

## Metadata fixes

Zachary Quinn Scheuren (@punchcutter) helpfully provided a file with Font Info fixes in a comment at https://github.com/googlefonts/noto-source/pull/188. I have copied these updates into the Glyphs source. 

Zachary also mentioned that there were unecessary layers, and I found that these were only in whitespace characters (probably copied in from another Noto source). So, I made a simple Glyphs script to remove all non-active layers, `source/nushu-glyphsapp-scripts/delete-unused-layers.glyphs.py` (this is a blunt tool – only use it if you are sure that non-active layers don't hold design versions, supporting content, etc).

To add this font info into a Glyphs file, you can simply copy and paste the following JSON into the `Custom Parameter` section of a Glyphs Font Info window:

<details>
<summary><b>Font Info added to Glyphs Source</b> (Click to expand JSON)</summary>


```json
(
        {
        vendorID = GOOG;
    },
        {
        unicodeRanges =         (
            0,
            1,
            31,
            45,
            57
        );
    },
        {
        "Use Typo Metrics" = 1;
    },
        {
        glyphOrder =         (
            ".notdef",
            NULL,
            CR,
            space,
            nbspace,
            u16FE1,
            u1B170,
            u1B171,
            u1B172,
            u1B173,
            u1B174,
            u1B175,
            u1B176,
            u1B177,
            u1B178,
            u1B179,
            u1B17A,
            u1B17B,
            u1B17C,
            u1B17D,
            u1B17E,
            u1B17F,
            u1B180,
            u1B181,
            u1B182,
            u1B183,
            u1B184,
            u1B185,
            u1B186,
            u1B187,
            u1B188,
            u1B189,
            u1B18A,
            u1B18B,
            u1B18C,
            u1B18D,
            u1B18E,
            u1B18F,
            u1B190,
            u1B191,
            u1B192,
            u1B193,
            u1B194,
            u1B195,
            u1B196,
            u1B197,
            u1B198,
            u1B199,
            u1B19A,
            u1B19B,
            u1B19C,
            u1B19D,
            u1B19E,
            u1B19F,
            u1B1A0,
            u1B1A1,
            u1B1A2,
            u1B1A3,
            u1B1A4,
            u1B1A5,
            u1B1A6,
            u1B1A7,
            u1B1A8,
            u1B1A9,
            u1B1AA,
            u1B1AB,
            u1B1AC,
            u1B1AD,
            u1B1AE,
            u1B1AF,
            u1B1B0,
            u1B1B1,
            u1B1B2,
            u1B1B3,
            u1B1B4,
            u1B1B5,
            u1B1B6,
            u1B1B7,
            u1B1B8,
            u1B1B9,
            u1B1BA,
            u1B1BB,
            u1B1BC,
            u1B1BD,
            u1B1BE,
            u1B1BF,
            u1B1C0,
            u1B1C1,
            u1B1C2,
            u1B1C3,
            u1B1C4,
            u1B1C5,
            u1B1C6,
            u1B1C7,
            u1B1C8,
            u1B1C9,
            u1B1CA,
            u1B1CB,
            u1B1CC,
            u1B1CD,
            u1B1CE,
            u1B1CF,
            u1B1D0,
            u1B1D1,
            u1B1D2,
            u1B1D3,
            u1B1D4,
            u1B1D5,
            u1B1D6,
            u1B1D7,
            u1B1D8,
            u1B1D9,
            u1B1DA,
            u1B1DB,
            u1B1DC,
            u1B1DD,
            u1B1DE,
            u1B1DF,
            u1B1E0,
            u1B1E1,
            u1B1E2,
            u1B1E3,
            u1B1E4,
            u1B1E5,
            u1B1E6,
            u1B1E7,
            u1B1E8,
            u1B1E9,
            u1B1EA,
            u1B1EB,
            u1B1EC,
            u1B1ED,
            u1B1EE,
            u1B1EF,
            u1B1F0,
            u1B1F1,
            u1B1F2,
            u1B1F3,
            u1B1F4,
            u1B1F5,
            u1B1F6,
            u1B1F7,
            u1B1F8,
            u1B1F9,
            u1B1FA,
            u1B1FB,
            u1B1FC,
            u1B1FD,
            u1B1FE,
            u1B1FF,
            u1B200,
            u1B201,
            u1B202,
            u1B203,
            u1B204,
            u1B205,
            u1B206,
            u1B207,
            u1B208,
            u1B209,
            u1B20A,
            u1B20B,
            u1B20C,
            u1B20D,
            u1B20E,
            u1B20F,
            u1B210,
            u1B211,
            u1B212,
            u1B213,
            u1B214,
            u1B215,
            u1B216,
            u1B217,
            u1B218,
            u1B219,
            u1B21A,
            u1B21B,
            u1B21C,
            u1B21D,
            u1B21E,
            u1B21F,
            u1B220,
            u1B221,
            u1B222,
            u1B223,
            u1B224,
            u1B225,
            u1B226,
            u1B227,
            u1B228,
            u1B229,
            u1B22A,
            u1B22B,
            u1B22C,
            u1B22D,
            u1B22E,
            u1B22F,
            u1B230,
            u1B231,
            u1B232,
            u1B233,
            u1B234,
            u1B235,
            u1B236,
            u1B237,
            u1B238,
            u1B239,
            u1B23A,
            u1B23B,
            u1B23C,
            u1B23D,
            u1B23E,
            u1B23F,
            u1B240,
            u1B241,
            u1B242,
            u1B243,
            u1B244,
            u1B245,
            u1B246,
            u1B247,
            u1B248,
            u1B249,
            u1B24A,
            u1B24B,
            u1B24C,
            u1B24D,
            u1B24E,
            u1B24F,
            u1B250,
            u1B251,
            u1B252,
            u1B253,
            u1B254,
            u1B255,
            u1B256,
            u1B257,
            u1B258,
            u1B259,
            u1B25A,
            u1B25B,
            u1B25C,
            u1B25D,
            u1B25E,
            u1B25F,
            u1B260,
            u1B261,
            u1B262,
            u1B263,
            u1B264,
            u1B265,
            u1B266,
            u1B267,
            u1B268,
            u1B269,
            u1B26A,
            u1B26B,
            u1B26C,
            u1B26D,
            u1B26E,
            u1B26F,
            u1B270,
            u1B271,
            u1B272,
            u1B273,
            u1B274,
            u1B275,
            u1B276,
            u1B277,
            u1B278,
            u1B279,
            u1B27A,
            u1B27B,
            u1B27C,
            u1B27D,
            u1B27E,
            u1B27F,
            u1B280,
            u1B281,
            u1B282,
            u1B283,
            u1B284,
            u1B285,
            u1B286,
            u1B287,
            u1B288,
            u1B289,
            u1B28A,
            u1B28B,
            u1B28C,
            u1B28D,
            u1B28E,
            u1B28F,
            u1B290,
            u1B291,
            u1B292,
            u1B293,
            u1B294,
            u1B295,
            u1B296,
            u1B297,
            u1B298,
            u1B299,
            u1B29A,
            u1B29B,
            u1B29C,
            u1B29D,
            u1B29E,
            u1B29F,
            u1B2A0,
            u1B2A1,
            u1B2A2,
            u1B2A3,
            u1B2A4,
            u1B2A5,
            u1B2A6,
            u1B2A7,
            u1B2A8,
            u1B2A9,
            u1B2AA,
            u1B2AB,
            u1B2AC,
            u1B2AD,
            u1B2AE,
            u1B2AF,
            u1B2B0,
            u1B2B1,
            u1B2B2,
            u1B2B3,
            u1B2B4,
            u1B2B5,
            u1B2B6,
            u1B2B7,
            u1B2B8,
            u1B2B9,
            u1B2BA,
            u1B2BB,
            u1B2BC,
            u1B2BD,
            u1B2BE,
            u1B2BF,
            u1B2C0,
            u1B2C1,
            u1B2C2,
            u1B2C3,
            u1B2C4,
            u1B2C5,
            u1B2C6,
            u1B2C7,
            u1B2C8,
            u1B2C9,
            u1B2CA,
            u1B2CB,
            u1B2CC,
            u1B2CD,
            u1B2CE,
            u1B2CF,
            u1B2D0,
            u1B2D1,
            u1B2D2,
            u1B2D3,
            u1B2D4,
            u1B2D5,
            u1B2D6,
            u1B2D7,
            u1B2D8,
            u1B2D9,
            u1B2DA,
            u1B2DB,
            u1B2DC,
            u1B2DD,
            u1B2DE,
            u1B2DF,
            u1B2E0,
            u1B2E1,
            u1B2E2,
            u1B2E3,
            u1B2E4,
            u1B2E5,
            u1B2E6,
            u1B2E7,
            u1B2E8,
            u1B2E9,
            u1B2EA,
            u1B2EB,
            u1B2EC,
            u1B2ED,
            u1B2EE,
            u1B2EF,
            u1B2F0,
            u1B2F1,
            u1B2F2,
            u1B2F3,
            u1B2F4,
            u1B2F5,
            u1B2F6,
            u1B2F7,
            u1B2F8,
            u1B2F9,
            u1B2FA,
            u1B2FB
        );
    },
        {
        description = "Designed by Lisa Huang";
    },
        {
        license = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software.";
    },
        {
        licenseURL = "http://scripts.sil.org/OFL";
    },
        {
        trademark = "Noto is a trademark of Google Inc.";
    },
        {
        versionString = "Version 2.000";
    },
        {
        fsType =         (
        );
    },
        {
        codePageRanges =         (
            1252
        );
    },
        {
        Axes =         (
                        {
                Name = Weight;
                Tag = wght;
            }
        );
    },
        {
        "Has WWS Names" = 1;
    },
        {
        "Don't use Production Names" = 1;
    }
)
```

</details>

Additionally, the following Panose values were added into the Master Custom Parameter:

<details>
<summary><b>Panose added to Master</b> (Click to expand JSON)</summary>

```json
(
        {
        panose =         (
            2,
            11,
            2,
            2,
            4,
            5,
            4,
            2,
            2,
            4
        );
    }
)
```

</details>

And, the following parameters were also added into the Regular instance Custom Parameter (mostly, matching the custom params of the Master):

<details>
<summary><b>Custom Parameters added to instance</b> (Click to expand JSON)</summary>

```json
(
        {
        weightClass = 400;
    },
        {
        panose =         (
            2,
            11,
            5,
            2,
            4,
            5,
            4,
            2,
            2,
            4
        );
    },
        {
        xHeight = 536;
    },
        {
        typoAscender = 1069;
    },
        {
        typoDescender = "-321";
    },
        {
        typoLineGap = 0;
    },
        {
        winAscent = 1069;
    },
        {
        winDescent = 321;
    },
        {
        hheaAscender = 1069;
    },
        {
        hheaDescender = "-321";
    },
        {
        hheaLineGap = 0;
    },
        {
        underlinePosition = "-100";
    },
        {
        underlineThickness = 50;
    }
)
```

</details>

In the Features, the prefix `Languagesystems` was added with a value of `languagesystem nshu dflt;`.

## Test webpage

I adapted a [script originally made for the Recursive project](https://github.com/arrowtype/recursive/blob/23bf5fdbf5938a5ac533c7d8bd969226d939e882/src/build-scripts/data-tables-for-website/build-html-unicode-grid-from-string.py) that builds a Unicode data table for the Recursive minisite, but cleaned it up and simplified it for this project.

This is available at `docs/index.html`.

If desired, this can be hosted on GitHub Pages or elsewhere.

### Pull requested to Noto repos

- [noto-fonts/pull/1710](https://github.com/googlefonts/noto-fonts/pull/1710)
- [noto-source/pull/188](https://github.com/googlefonts/noto-source/pull/188)

