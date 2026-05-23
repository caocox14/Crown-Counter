import os
import psycopg2


def get_connection():
    """
    Conexión a la base de datos usando variable de entorno (Supabase / Vercel)
    """
    try:
        database_url = os.environ.get("DATABASE_URL")

        if not database_url:
            raise Exception("❌ DATABASE_URL no está definida en las variables de entorno")

        conexion = psycopg2.connect(database_url)
        return conexion

    except Exception as e:
        print("❌ Error al conectar a la base de datos:", e)
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