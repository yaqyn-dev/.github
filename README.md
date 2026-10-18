# Yaqyn Development organization profile

Source for the public [yaqyn-dev organization profile](https://github.com/yaqyn-dev).

Edit `profile/README.md` for the organization introduction. Its active masthead is `profile/assets/yaqyn-dust-intro.gif`, with a reduced-motion poster. The organization profile uses an absolute image URL so it resolves independently of the repository view.

Project application repositories remain private. Link to approved public showcases and retain the distinction between prototypes and operational products.

## Rebuild the masthead

Requires uv, ImageMagick, and ExifTool. Montserrat and its license are bundled in `scripts/fonts/`; visitors do not fetch fonts. From this repository:

```sh
uv run --locked scripts/build_dust_cover.py
```

Set `EXIFTOOL_BIN` if ExifTool is outside `PATH`. The renderer produces the 1920 × 640, 12-second dust/title/contact loop and a lossless still poster. It uses a fixed seed and periodic motion for reproducibility. Only the masthead assets and profile references need publication; application repositories are unaffected.
