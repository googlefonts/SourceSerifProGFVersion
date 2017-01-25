# Source Serif Pro v2.000 for Google Fonts
by Frank Grießhammer

This repository hot fixes the binary sources for [Source Serif Pro v2.000](https://github.com/adobe-fonts/source-serif-pro/releases/tag/2.000R)


## Changes from source
1. Change font names to fit within Google Font's api. We can only have weights from Thin to Black.


## Building fonts
```
$ cd build
$ sh build.sh
```

## Dependencies
[FontTools](https://github.com/fonttools/fonttools)
[Font Bakery](https://github.com/googlefonts/fontbakery)
[ttfautohint](https://www.freetype.org/ttfautohint/)
[fontforge](https://fontforge.github.io/en-US/)