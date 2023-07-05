@echo off
color a
echo.
set /p url="Paste your path and press Enter: "
python fast_DirTreeGenerator.py "%url%"
