# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=12,<13"]
# ///
"""Build the organization dust bumper: uv run scripts/build_dust_cover.py.

No remote assets or installed system fonts are needed. The bundled Montserrat
variable font is unchanged and distributed under the adjacent OFL license.
"""
from pathlib import Path
from math import sin, cos, pi
import random
import tempfile
import subprocess
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "profile/assets"
WIDTH, HEIGHT, FPS, SECONDS = 1920, 640, 25, 12
FONT = ROOT / "scripts/fonts/Montserrat-wght.ttf"

def smooth(value):
    value = max(0.0, min(1.0, value))
    return value * value * (3 - 2 * value)

def fade(t, start, end):
    return smooth((t - start) / (end - start))

def font(size, weight):
    face = ImageFont.truetype(str(FONT), size)
    face.set_variation_by_axes([weight])
    return face

def text_card(primary, secondary, primary_size, secondary_size, secondary_y=432):
    canvas = Image.new("L", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(canvas)
    draw.text((WIDTH / 2, 296), primary, font=font(primary_size, 700), fill=255, anchor="mm")
    draw.text((WIDTH / 2, secondary_y), secondary, font=font(secondary_size, 500), fill=235, anchor="mm")
    return canvas

TITLE = text_card("yaqyn.", "dev", 224, 48, secondary_y=470)
CONTACT = text_card("contact@yaqyn.dev", "let's work", 88, 44)
rng = random.Random(1729)
# Every mote has a periodic trajectory, so the last and first frames meet.
# Layered focus, irregular sizes and slow advection suggest dust, not stars.
MOTES = []
for depth, count in enumerate((150, 140, 70)):
    layer = []
    for _ in range(count):
        layer.append((rng.uniform(-80, WIDTH + 80), rng.uniform(-40, HEIGHT + 40),
                      rng.uniform(.65, 1.8) * (1 + depth * .8),
                      rng.uniform(22, 78) / (1 + depth * .5),
                      rng.uniform(0, 2 * pi), rng.uniform(0, 2 * pi),
                      rng.uniform(.65, 1.4)))
    MOTES.append(layer)

PALETTE = [component for index in range(128) for component in [round(index * 255 / 127)] * 3]
PALETTE += [0] * (768 - len(PALETTE))
QUANTIZE = [round(index * 127 / 255) for index in range(256)]

def dust(t, opacity):
    result = Image.new("L", (WIDTH, HEIGHT))
    if opacity < .001:
        return result
    angle = 2 * pi * t / SECONDS
    for depth, motes in enumerate(MOTES):
        layer = Image.new("L", result.size)
        draw = ImageDraw.Draw(layer)
        for x, y, radius, bright, phase, phase2, aspect in motes:
            px = x + (22 + depth * 13) * sin(angle + phase) + 5 * sin(2 * angle + phase2)
            py = y + (9 + depth * 7) * cos(angle + phase2) + 4 * sin(2 * angle + phase)
            strength = bright * opacity * (.8 + .2 * sin(angle + phase2))
            draw.ellipse((px-radius, py-radius*aspect, px+radius, py+radius*aspect), fill=round(strength))
        layer = layer.filter(ImageFilter.GaussianBlur((.45, 1.2, 2.8)[depth]))
        result = ImageChops.add(result, layer)
    return result

def render(t):
    dust_opacity = max(1 - fade(t, 0, 1.6), fade(t, 9.2, 10.8))
    title_opacity = fade(t, 1.6, 2.2) * (1 - fade(t, 4.3, 5.1))
    contact_opacity = fade(t, 5.4, 6.2) * (1 - fade(t, 9, 10.5))
    frame = dust(t, dust_opacity)
    if title_opacity:
        frame = ImageChops.lighter(frame, TITLE.point([round(i * title_opacity) for i in range(256)]))
    if contact_opacity:
        frame = ImageChops.lighter(frame, CONTACT.point([round(i * contact_opacity) for i in range(256)]))
    return frame

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    frames = []
    reviews = Path(tempfile.mkdtemp(prefix="yaqyn-dust-review-"))
    review_times = {0, 1, 3, 5, 7, 10, 11}
    for n in range(FPS * SECONDS):
        t = n / FPS
        frame = render(t)
        if n % FPS == 0 and n // FPS in review_times:
            frame.convert("RGB").save(reviews / f"frame-{n//FPS:02d}.png")
        indexed = frame.point(QUANTIZE).convert("P")
        indexed.putpalette(PALETTE)
        frames.append(indexed)
    output = OUT / "yaqyn-dust-intro.gif"
    frames[0].save(output, save_all=True, append_images=frames[1:], duration=1000//FPS,
                   loop=0, disposal=2, optimize=True)
    # Static fallback uses the same exact typography and full HD resolution.
    poster_source = reviews / "poster.png"
    TITLE.convert("RGB").save(poster_source)
    poster = OUT / "yaqyn-dust-poster.webp"
    subprocess.run(["magick", str(poster_source), "-strip", "-define", "webp:lossless=true", str(poster)], check=True)
    subprocess.run([os.environ.get("EXIFTOOL_BIN", "exiftool"), "-overwrite_original", "-all=",
                    "-XMP-dc:Creator=Abdulrahman M. Yaqyn",
                    "-XMP-dc:Rights=Copyright Abdulrahman M. Yaqyn",
                    "-XMP-x:XMPToolkit=", str(poster)], check=True)
    print(f"Built {WIDTH}×{HEIGHT}, {FPS}fps, {SECONDS}s; {output.stat().st_size:,} bytes")
    print(f"Review frames: {reviews}")

if __name__ == "__main__":
    main()
