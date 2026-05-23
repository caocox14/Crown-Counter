# 🌿 GUÍA PARA ARREGLAR TIMEOUT EN VERCEL - Crown-Counter

## ✅ Lo que se ha hecho

Se han realizado los siguientes cambios para arreglar el problema de timeout (504) en Vercel:

### 1. ✅ `vercel.json` - Configuración de Vercel (CREADO)
- Especifica que Vercel debe usar Python
- Configura timeout máximo de 60 segundos
- Mapea rutas correctamente (/ → app.py)
- Asigna 1024MB de memoria

### 2. ✅ `conexion_base.py` - Conexión a BD mejorada (ACTUALIZADO)
- ✨ **Reintentos automáticos**: Si la BD falla, reinten ta hasta 2 veces más
- ✨ **Timeout en conexión**: Máximo 3-5 segundos esperando conexión a Supabase
- ✨ **Statement timeout**: Las queries tienen límite de 10 segundos
- ✨ **Manejo de errores**: Captura timeouts de operación

### 3. ✅ `app.py` - Lógica optimizada (ACTUALIZADO)
- ✨ **Timeout de solicitud**: 55 segundos de límite (Vercel máximo es 60)
- ✨ **Mejor manejo de errores**: Captura y reporta todos los fallos
- ✨ **Fallback automático**: Si algo falla, usa imagen de respaldo
- ✨ **Logging mejorado**: Emojis y mensajes claros para debugging
- ✨ **Limpieza de archivos**: Borra archivos temporales incluso si hay error
- ✨ **Error handlers**: Respuestas 504/500 personalizadas

### 4. ✅ `requirements.txt` - Dependencias (SIN CAMBIOS NECESARIOS)
- Ya tiene todas las dependencias correctas

---

## 📋 PASOS PARA ACTUALIZAR EN VERCEL

### Opción 1: Con Git (RECOMENDADO - Automático)
```bash
# Desde la carpeta del proyecto
git add .
git commit -m "Fix: Arreglar timeout en Vercel con reintentos y timeouts en BD"
git push
```
**Vercel detectará los cambios automáticamente y redesplegará en 1-2 minutos**

### Opción 2: Manual en Dashboard de Vercel
1. Ve a https://vercel.com/dashboard
2. Selecciona proyecto "crown-counter-gfjl"
3. Click en "Deployments"
4. Click en "Redeploy" en el último deployment

---

## 🔍 VERIFICACIÓN

Después de desplegar, prueba en:
- **Inicio**: https://crown-counter-gfjl.vercel.app/ (debería cargar rápido)
- **Upload**: Sube una imagen para verificar que responde en <10 segundos

Si aún hay problemas:
1. Abre DevTools (F12) → Console y busca errores
2. Revisa logs en Vercel Dashboard → tu proyecto → Deployments → Logs
3. Verifica que DATABASE_URL esté configurado en Vercel Settings → Environment Variables

---

## 🚀 OPTIMIZACIONES APLICADAS

| Problema | Solución |
|----------|----------|
| **No hay configuración Vercel** | Agregado `vercel.json` |
| **BD se cuelga en timeout** | Timeouts en conexión (3s) y queries (10s) |
| **Reintentos faltan** | Ahora reinten ta 2 veces si falla |
| **Sin manejo de error 504** | Agregado handler especial + logging |
| **Archivos temporales no se borran** | Agregado try/except en cleanup |
| **Logs poco claros** | Agregados emojis y mensajes descriptivos |

---

## ⚠️ SI SIGUE SIN FUNCIONAR

Revisa estos puntos en orden:

1. **¿El DATABASE_URL está correcto?**
   - Vercel Settings → Environment Variables → DATABASE_URL
   - Debe ser la URL de conexión de Supabase completa

2. **¿Supabase está disponible?**
   - Entra a https://supabase.com y verifica estado
   - Intenta conectarte localmente: `psql <tu-database-url>`

3. **¿Hay errores de importación?**
   - Mira los logs en Vercel
   - Los módulos (plantapi, consulta_img) deben estar en el mismo nivel que app.py

4. **¿Necesitas caché?**
   - Si identificar plantas es lento, considera guardar resultados en memoria

---

## 📞 SOPORTE

Si después de esto sigue fallando:
1. Copia el mensaje de error exacto de Vercel logs
2. Verifica que todos los archivos .py estén correctamente en GitHub
3. Confirma que no hay secretos (API keys) hardcodeados en el código

