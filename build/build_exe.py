"""Package Three Lists into a single standalone Windows .exe (PyInstaller)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

args = [
    sys.executable, "-m", "PyInstaller",
    "--noconfirm", "--clean",
    "--onefile", "--windowed",
    "--name", "Three Lists",
    "--icon", os.path.join(ROOT, "assets", "icon.ico"),
    "--add-data", f"{os.path.join(ROOT, 'todo.html')}{os.pathsep}.",
    "--add-data", f"{os.path.join(ROOT, 'assets', 'icon.ico')}{os.pathsep}assets",
    "--collect-all", "webview",
    "--collect-all", "clr_loader",
    "--distpath", os.path.join(ROOT, "dist"),
    "--workpath", os.path.join(ROOT, "build", "_work"),
    "--specpath", os.path.join(ROOT, "build"),
    os.path.join(ROOT, "app.py"),
]

print(">>", " ".join(args))
sys.exit(subprocess.call(args, cwd=ROOT))
