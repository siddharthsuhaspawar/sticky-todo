@echo off
REM Self-contained Tauri build: proxy (Clash) + MSVC env + tauri CLI.
REM Portable across machines: finds vcvars64.bat via vswhere, falls back to
REM known install paths, and puts cargo on PATH if it isn't already.
setlocal enabledelayedexpansion

set "HTTPS_PROXY=http://127.0.0.1:7897"
set "HTTP_PROXY=http://127.0.0.1:7897"
set "ALL_PROXY=http://127.0.0.1:7897"
set "CARGO_HTTP_CHECK_REVOKE=false"
set "CARGO_NET_RETRY=5"

REM --- cargo on PATH ---
if exist "%USERPROFILE%\.cargo\bin\cargo.exe" set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"

REM --- locate the MSVC environment ---
set "VCVARS="
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "%VSWHERE%" (
  for /f "usebackq tokens=*" %%i in (`"%VSWHERE%" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath 2^>nul`) do (
    if exist "%%i\VC\Auxiliary\Build\vcvars64.bat" set "VCVARS=%%i\VC\Auxiliary\Build\vcvars64.bat"
  )
)
if not defined VCVARS (
  for %%p in (
    "%ProgramFiles%\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
    "%ProgramFiles%\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
    "%ProgramFiles(x86)%\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
    "%ProgramFiles(x86)%\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
    "%ProgramFiles(x86)%\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
  ) do if not defined VCVARS if exist %%p set "VCVARS=%%~p"
)
if not defined VCVARS (
  echo === ERROR: MSVC build tools not found. Install VS Build Tools with the
  echo ===        "Desktop development with C++" workload, then re-run.
  exit /b 9009
)
echo === MSVC env: %VCVARS%
call "%VCVARS%" >nul 2>&1

cd /d "D:\codes\todo"
echo === syncing ui/ from todo.html ===
if not exist "ui\assets" mkdir "ui\assets"
copy /Y "todo.html" "ui\index.html" >nul
copy /Y "todo.html" "index.html" >nul
copy /Y "assets\icon.ico" "ui\assets\icon.ico" >nul

REM --- tauri CLI: global npm install, else npx ---
set "TAURI=%APPDATA%\npm\tauri.cmd"
echo === running tauri build ===
if exist "%TAURI%" (
  call "%TAURI%" build
) else (
  call npx --yes @tauri-apps/cli build
)
echo === tauri build exit code: %ERRORLEVEL% ===
endlocal
