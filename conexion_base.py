import psycopg2
from psycopg2 import sql
import subprocess
import os


def inicializar_base():
    print("🔎 Verificando base de datos...")

    database = "plantas_db"
    host = "localhost"
    user = "postgres"
    password = "plantas_db1234567890_*"
    port = "5432"

    try:
        # =========================
        # CONEXIÓN A POSTGRES (DB ADMIN)
        # =========================
        conexion = psycopg2.connect(
            host=host,
            database="postgres",
            user=user,
            password=password,
            port=port
        )

        conexion.autocommit = True
        cursor = conexion.cursor()

        # =========================
        # VERIFICAR SI EXISTE DB
        # =========================
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (database,)
        )

        existe = cursor.fetchone()

        if not existe:
            print("⚠️ Base no existe, creando...")

            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(database)
                )
            )

            print("✅ Base de datos creada")

            cursor.close()
            conexion.close()

            # =========================
            # EJECUTAR SQL AUTOMÁTICAMENTE
            # =========================
            ruta_sql = os.path.join(os.getcwd(), "plantas_db.sql")

            env = os.environ.copy()
            env["PGPASSWORD"] = password

            subprocess.run([
                "psql",
                "-U", user,
                "-d", database,
                "-f", ruta_sql
            ], env=env, check=True)

            print("✅ Base inicializada con SQL")

        else:
            print("ℹ️ La base ya existe, no se ejecuta el SQL")

            cursor.close()
            conexion.close()

    except Exception as e:
        print("❌ Error:", e)