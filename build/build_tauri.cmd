@echo off
REM Self-contained Tauri build: proxy (Clash) + MSVC env + tauri CLI.
set "HTTPS_PROXY=http://127.0.0.1:7897"
set "HTTP_PROXY=http://127.0.0.1:7897"
set "ALL_PROXY=http://127.0.0.1:7897"
set "CARGO_HTTP_CHECK_REVOKE=false"
set "CARGO_NET_RETRY=5"
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
cd /d "D:\codes\todo"
echo === syncing ui/ from todo.html ===
if not exist "ui\assets" mkdir "ui\assets"
copy /Y "todo.html" "ui\index.html" >nul
copy /Y "todo.html" "index.html" >nul
copy /Y "assets\icon.ico" "ui\assets\icon.ico" >nul
copy /Y "assets\scene.jpg" "ui\assets\scene.jpg" >nul
echo === running tauri build ===
call "%APPDATA%\npm\tauri.cmd" build
echo === tauri build exit code: %ERRORLEVEL% ===
