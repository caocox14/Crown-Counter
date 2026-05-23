@echo off
cd /d "C:\Users\Aaron\Documents\Crown-Counter\Crown-Counter"
echo === COMMITS RECIENTES ===
git log --oneline -20
echo.
echo === ESTADO DEL REPOSITORIO ===
git status --short
echo.
echo === DIFF PREPARADO PARA COMMIT ===
git diff --cached --stat
