#!/bin/bash

cd "C:/Users/Aaron/Documents/Crown-Counter/Crown-Counter" || cd "/c/Users/Aaron/Documents/Crown-Counter/Crown-Counter"

echo "========================================================================"
echo "   🚀 SUBIENDO CAMBIOS A GITHUB - CROWN-COUNTER"
echo "========================================================================"
echo ""

echo "📋 Paso 1: Preparar archivos"
git add .
echo "✅ Archivos preparados"
echo ""

echo "📋 Paso 2: Ver cambios preparados"
git status --short
echo ""

echo "📋 Paso 3: Resumen de cambios"
git diff --cached --stat
echo ""

echo "📋 Paso 4: Crear commit"
git commit -m "Fix: Arreglar timeout en Vercel con reintentos y timeouts" \
  -m "- Agregado vercel.json con configuración Python" \
  -m "- Mejorada conexion_base.py con reintentos automáticos (3x) y timeouts" \
  -m "- Optimizado app.py con signal/alarm de 55 segundos" \
  -m "- Agregados handlers para errores 504 y 500" \
  -m "- Mejorado logging con emojis para debugging" \
  -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

if [ $? -ne 0 ]; then
    echo "❌ Error al crear commit"
    exit 1
fi
echo "✅ Commit creado"
echo ""

echo "📋 Paso 5: Ver commit"
git log --oneline -1
echo ""

echo "📋 Paso 6: Subir a GitHub"
git push

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================================================"
    echo "   ✅ ¡CAMBIOS SUBIDOS EXITOSAMENTE!"
    echo "========================================================================"
    echo ""
    echo "📌 PRÓXIMOS PASOS:"
    echo ""
    echo "1. Vercel detectará los cambios automáticamente"
    echo "2. Redesplegará tu app en 1-2 minutos"
    echo "3. Puedes monitorear el deployment en:"
    echo "   https://vercel.com/dashboard"
    echo ""
    echo "4. Tu app debería cargar sin timeouts en:"
    echo "   https://crown-counter-gfjl.vercel.app/"
    echo ""
    echo "¡Listo! 🚀"
else
    echo "❌ Error al subir a GitHub"
    exit 1
fi
