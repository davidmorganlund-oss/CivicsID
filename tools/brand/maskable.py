"""Make the maskable app icon (site/icon-maskable-512.png) from site/icon-512.png.

Android crops app icons to a circle or rounded square, which would cut off
"Civics" and the edges of the state badge on the regular icon. This shrinks
the artwork into the safe zone (a circle 80% of the icon's width), keeps the
background and the full-width bar along the bottom, and saves the result.
Run from the repo root after tools/brand/render.js: python3 tools/brand/maskable.py
"""
from pathlib import Path
from PIL import Image

SRC, OUT = Path("site/icon-512.png"), Path("site/icon-maskable-512.png")
icon = Image.open(SRC).convert("RGB")
W = icon.width
bg = icon.getpixel((W // 2, 2))
# The bar is the solid strip along the bottom edge that isn't the background.
bar_top = W
while bar_top > 0 and icon.getpixel((W // 2, bar_top - 1)) != bg and icon.getpixel((2, bar_top - 1)) != bg:
    bar_top -= 1
art = icon.crop((0, 0, W, bar_top))
# Bounding box of everything that isn't background.
mask = Image.eval(art.convert("L"), lambda v: 0)
px, ap = mask.load(), art.load()
for y in range(art.height):
    for x in range(art.width):
        if sum(abs(a - b) for a, b in zip(ap[x, y], bg)) > 24:
            px[x, y] = 255
l, t, r, b = mask.getbbox()
box = art.crop((l, t, r, b))
# Fit the box's corners inside a circle of radius 0.38 W (a little inside the 0.40 safe zone).
half_diag = ((box.width / 2) ** 2 + (box.height / 2) ** 2) ** 0.5
scale = min(1.0, 0.38 * W / half_diag)
box = box.resize((round(box.width * scale), round(box.height * scale)), Image.LANCZOS)
out = Image.new("RGB", (W, W), bg)
out.paste(box, ((W - box.width) // 2, (W - box.height) // 2))
out.paste(icon.crop((0, bar_top, W, W)), (0, bar_top))
out.save(OUT, optimize=True)
print(f"{OUT}: artwork scaled to {scale:.0%}, bar from y={bar_top}")
