import os
import psycopg2
from psycopg2 import OperationalError
import time


def get_connection(reintentos=3, timeout=5):
    """
    Conexión a la base de datos usando variable de entorno (Supabase / Vercel)
    con reintentos y timeout para evitar cuelgues.
    """
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        print("❌ DATABASE_URL no está definida en las variables de entorno")
        return None

    for intento in range(reintentos):
        try:
            conexion = psycopg2.connect(
                database_url,
                connect_timeout=timeout,
                options="-c statement_timeout=10000"
            )
            print(f"✅ Conexión a DB establecida exitosamente")
            return conexion

        except (OperationalError, psycopg2.Error) as e:
            print(f"⚠️ Intento {intento + 1}/{reintentos} - Error conexión DB: {e}")
            if intento < reintentos - 1:
                time.sleep(1)
            else:
                print("❌ No se pudo conectar a la base de datos después de reintentos")
                return None

    return None


def verificar_tabla():
    """
    Verifica si la tabla 'plantas' existe (solo informativo)
    """
    try:
        conexion = get_connection()
        if conexion is None:
            return False

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'plantas'
            );
        """)

        existe_tabla = cursor.fetchone()[0]

        if existe_tabla:
            print("✅ La tabla 'plantas' existe.")
        else:
            print("⚠️ La tabla 'plantas' NO existe. Debes crearla en Supabase.")

        cursor.close()
        conexion.close()

        return existe_tabla

    except Exception as e:
        print("❌ Error verificando la tabla:", e)
        return False