"""Generate a clean app icon for Three Lists (dark rounded square + three list rows)."""
import os
from PIL import Image, ImageDraw

OUT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(OUT), "assets")
os.makedirs(ASSETS, exist_ok=True)

S = 256
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# rounded background (deep near-black, like the app)
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=58, fill=(22, 22, 26, 255))

# three rows: a ring (checkbox) + a rounded bar, decreasing width = To-Do / Watch / Later
rows = [
    (128, (245, 245, 247, 255)),   # To-Do
    (104, (245, 245, 247, 225)),   # Watch
    (78,  (245, 245, 247, 195)),   # Later
]
bar_h = 22
gap = 40
total = bar_h * len(rows) + gap * (len(rows) - 1)
y = (S - total) // 2
cx = 66
for w, color in rows:
    cyc = y + bar_h // 2
    # checkbox ring
    rr = 12
    d.ellipse([cx - rr, cyc - rr, cx + rr, cyc + rr], outline=(255, 255, 255, 170), width=4)
    # bar
    bx = cx + rr + 20
    d.rounded_rectangle([bx, y, bx + w, y + bar_h], radius=bar_h // 2, fill=color)
    y += bar_h + gap

# blue accent dot on the first checkbox (the single accent)
rr = 12
cyc0 = (S - total) // 2 + bar_h // 2
d.ellipse([cx - 6, cyc0 - 6, cx + 6, cyc0 + 6], fill=(10, 132, 255, 255))

img.save(os.path.join(ASSETS, "icon.png"))
img.save(
    os.path.join(ASSETS, "icon.ico"),
    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
print("wrote", os.path.join(ASSETS, "icon.png"), "and icon.ico")
