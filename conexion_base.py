import os
import psycopg2
from psycopg2 import sql


def inicializar_base():
    print("🔎 Verificando base de datos...")

    database = "plantas_db"
    host = "localhost"
    user = "postgres"
    password = "plantas_db1234567890_*"
    port = "5432"

    try:
        # 1. Conexión inicial para verificar/crear la base de datos
        conexion_admin = psycopg2.connect(
            host=host, database="postgres", user=user, password=password, port=port
        )
        conexion_admin.autocommit = True
        cursor_admin = conexion_admin.cursor()

        cursor_admin.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s", (database,)
        )
        existe_db = cursor_admin.fetchone()

        if not existe_db:
            print("⚠️ Base no existe, creando...")
            cursor_admin.execute(
                sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database))
            )
            print("✅ Base de datos creada con éxito.")
        else:
            print("ℹ️ La base de datos ya existe.")

        cursor_admin.close()
        conexion_admin.close()

        # ========================================================
        # 2. CONEXIÓN DIRECTA A PLANTAS_DB PARA VERIFICAR LA TABLA
        # ========================================================
        conexion_app = psycopg2.connect(
            host=host, database=database, user=user, password=password, port=port
        )
        conexion_app.autocommit = True
        cursor_app = conexion_app.cursor()

        # Verificamos si la tabla 'plantas' existe en el esquema público
        cursor_app.execute(
            """
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'plantas'
            );
        """
        )
        existe_tabla = cursor_app.fetchone()[0]

        if not existe_tabla:
            print("⏳ Tabla 'plantas' no encontrada. Inyectando estructura SQL...")

            # Leemos el archivo plantas_db.sql de forma nativa con Python
            ruta_sql = os.path.join(os.getcwd(), "plantas_db.sql")

            if os.path.exists(ruta_sql):
                with open(ruta_sql, "r", encoding="utf-8") as f:
                    contenido_sql = f.read()

                # Ejecutamos el script completo directamente en el cursor
                cursor_app.execute(contenido_sql)
                print("✅ ¡Tabla 'plantas' e información inicializadas desde el código!")
            else:
                print(
                    f"❌ Error: No se encontró el archivo plantas_db.sql en: {ruta_sql}"
                )
        else:
            print("✅ La tabla 'plantas' ya existe y está lista para operar.")

        cursor_app.close()
        conexion_app.close()

    except Exception as e:
        print("❌ Error crítico en la gestión de la base de datos:", e)