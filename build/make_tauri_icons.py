"""Generate the icon set Tauri needs (from assets/icon.png) into src-tauri/icons/."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "icon.png")
OUT = os.path.join(ROOT, "src-tauri", "icons")
os.makedirs(OUT, exist_ok=True)

base = Image.open(SRC).convert("RGBA")


def png(size, name):
    base.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name))


png(32, "32x32.png")
png(128, "128x128.png")
png(256, "128x128@2x.png")
png(256, "icon.png")

# multi-resolution .ico for the Windows exe + installer
base.resize((256, 256), Image.LANCZOS).save(
    os.path.join(OUT, "icon.ico"),
    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
print("wrote Tauri icons to", OUT)
