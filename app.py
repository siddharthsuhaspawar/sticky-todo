"""
Three Lists — standalone desktop app.

A clean native window (WebView2 on Windows) wrapping todo.html. Not a browser,
not an Edge PWA. Data (localStorage) persists in %LOCALAPPDATA%\\ThreeLists.

Dev run:   python app.py
Packaged:  build/build_exe.py  ->  dist/Three Lists.exe
"""
import os
import sys
import socket
import functools
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import webview

# A fixed port keeps the http origin stable across launches, so the app's
# localStorage data persists (WebView2 keys storage by origin).
PREFERRED_PORTS = [8731, 8732, 8733, 8734]
APP_NAME = "Three Lists"


def resource_dir() -> str:
    """Directory holding todo.html + assets, both frozen (PyInstaller) and not."""
    if getattr(sys, "frozen", False):
        return sys._MEIPASS  # type: ignore[attr-defined]
    return os.path.dirname(os.path.abspath(__file__))


def _port_free(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) != 0


def start_server(directory: str) -> int:
    handler = functools.partial(SimpleHTTPRequestHandler, directory=directory)
    for port in PREFERRED_PORTS:
        if not _port_free(port):
            continue
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
        except OSError:
            continue
        httpd.daemon_threads = True
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        return port
    raise RuntimeError("No free port for the local app server")


def main() -> None:
    base = resource_dir()
    port = start_server(base)

    storage = os.path.join(
        os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "ThreeLists"
    )
    os.makedirs(storage, exist_ok=True)

    webview.create_window(
        APP_NAME,
        f"http://127.0.0.1:{port}/todo.html",
        width=1240,
        height=860,
        min_size=(720, 600),
        background_color="#0c0c0e",
    )

    icon = os.path.join(base, "assets", "icon.ico")
    kwargs = dict(private_mode=False, storage_path=storage)  # persist localStorage
    if os.path.exists(icon):
        try:
            webview.start(icon=icon, **kwargs)
            return
        except TypeError:
            pass  # older pywebview without icon= in start()
    webview.start(**kwargs)


if __name__ == "__main__":
    main()
