#!/usr/bin/env python3
"""
Script para ejecutar git commands y subir cambios a GitHub
"""

import os
import subprocess
import sys

def run_command(cmd, description=""):
    """Ejecuta un comando y muestra el resultado"""
    if description:
        print(f"\n{'='*70}")
        print(f"📋 {description}")
        print(f"{'='*70}")
    
    print(f"💻 Ejecutando: {cmd}\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd="C:\\Users\\Aaron\\Documents\\Crown-Counter\\Crown-Counter"
        )
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("⚠️  STDERR:", result.stderr)
        
        if result.returncode != 0:
            print(f"❌ Error (código {result.returncode})")
            return False
        else:
            print("✅ Comando exitoso")
            return True
            
    except Exception as e:
        print(f"❌ Error ejecutando comando: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("   🚀 SUBIENDO CAMBIOS A GITHUB - CROWN-COUNTER")
    print("="*70)
    
    # Paso 1: Agregar todos los archivos
    if not run_command("git add .", "Paso 1: Preparar archivos"):
        print("❌ Error al preparar archivos")
        return False
    
    # Paso 2: Ver estado
    run_command("git status --short", "Paso 2: Verificar archivos preparados")
    
    # Paso 3: Ver diff
    run_command("git diff --cached --stat", "Paso 3: Resumen de cambios")
    
    # Paso 4: Crear commit
    commit_cmd = (
        'git commit -m "Fix: Arreglar timeout en Vercel con reintentos y timeouts" '
        '-m "- Agregado vercel.json con configuración Python" '
        '-m "- Mejorada conexion_base.py con reintentos automáticos (3x) y timeouts" '
        '-m "- Optimizado app.py con signal/alarm de 55 segundos" '
        '-m "- Agregados handlers para errores 504 y 500" '
        '-m "- Mejorado logging con emojis para debugging" '
        '-m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"'
    )
    
    if not run_command(commit_cmd, "Paso 4: Crear commit"):
        print("❌ Error al crear commit")
        return False
    
    # Paso 5: Ver el commit
    run_command("git log --oneline -1", "Paso 5: Verificar commit creado")
    
    # Paso 6: Push a GitHub
    if not run_command("git push", "Paso 6: Subir a GitHub"):
        print("❌ Error al subir a GitHub")
        print("\n⚠️  POSIBLES SOLUCIONES:")
        print("  1. Verifica que tengas credenciales de GitHub configuradas")
        print("  2. Si usas SSH, asegúrate de que tu clave está agregada")
        print("  3. Si usas HTTPS, revisa que tengas un token de GitHub válido")
        return False
    
    # Paso 7: Confirmación final
    print("\n" + "="*70)
    print("   ✅ ¡CAMBIOS SUBIDOS EXITOSAMENTE!")
    print("="*70)
    print("""
📌 PRÓXIMOS PASOS:

1. Vercel detectará los cambios automáticamente
2. Redesplegará tu app en 1-2 minutos
3. Puedes monitorear el deployment en:
   https://vercel.com/dashboard

4. Tu app debería cargar sin timeouts en:
   https://crown-counter-gfjl.vercel.app/

¡Listo! 🚀
""")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
