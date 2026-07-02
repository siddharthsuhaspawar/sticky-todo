@echo off
REM Initialize the MSVC (VS2017 BuildTools) environment, then run the passed command.
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
%*
