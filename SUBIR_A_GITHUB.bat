rem ============================================
rem SCRIPT PARA SUBIR CAMBIOS A GITHUB
rem ============================================
rem
rem Ejecuta este archivo en CMD o PowerShell desde la carpeta del proyecto
rem
rem PASOS AUTOMÁTICOS:
rem 1. Prepara todos los cambios
rem 2. Crea un commit con mensaje descriptivo
rem 3. Sube a GitHub
rem

@echo off
setlocal enabledelayedexpansion

echo.
echo ════════════════════════════════════════════════
echo   🚀 SUBIENDO CAMBIOS A GITHUB
echo ════════════════════════════════════════════════
echo.

cd /d "C:\Users\Aaron\Documents\Crown-Counter\Crown-Counter"

echo 📍 Ubicación actual:
cd

echo.
echo 📋 Estado actual:
git status --short

echo.
echo 📝 Preparando archivos...
git add .

echo.
echo ✅ Archivos preparados. Creando commit...
git commit -m "Fix: Arreglar timeout en Vercel con reintentos y timeouts en BD" ^
    -m "- Agregado vercel.json con configuración para Python" ^
    -m "- Mejorada conexion_base.py con reintentos automáticos (3x) y timeouts" ^
    -m "- Optimizado app.py con signal/alarm de 55 segundos máximo" ^
    -m "- Agregados handlers para errores 504 y 500" ^
    -m "- Mejorado logging con emojis para debugging" ^
    -m "- Fallback automático a imagen de respaldo si falla la BD"

echo.
echo 🔍 Verificando commit:
git log --oneline -1

echo.
echo 📤 Subiendo a GitHub...
git push

echo.
echo ════════════════════════════════════════════════
echo   ✅ ¡CAMBIOS SUBIDOS EXITOSAMENTE!
echo ════════════════════════════════════════════════
echo.
echo 📌 Vercel detectará los cambios automáticamente
echo    en los próximos 1-2 minutos y redesplegará.
echo.
echo 🔗 Puedes monitorear el deployment en:
echo    https://vercel.com/dashboard
echo.
pause
