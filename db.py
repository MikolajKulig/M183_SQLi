import os
import psycopg2


def _load_dotenv(path=".env"):
    """Lightweight .env loader: sets variables into os.environ if not present.

    This avoids adding an external dependency while letting developers use a
    local `.env` file during development. The file should contain lines like
    DB_PASSWORD=secret
    """
    if not os.path.exists(path):
        return
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                os.environ.setdefault(key, val)
    except Exception:
        # If reading .env fails for any reason, don't crash here; require env var later.
        return


def get_conn():
    # Try loading a local .env for development convenience, but require
    # DB_PASSWORD to be set in the environment. No hard-coded default is kept.
    _load_dotenv()
    password = os.environ.get("DB_PASSWORD")
    if not password:
        raise RuntimeError(
            "DB_PASSWORD is not set. Set the DB_PASSWORD environment variable or create a local .env file (see .env.example)."
        )

    return psycopg2.connect(
        dbname="m183",
        user="postgres",
        password=password,
        host="localhost",
        port="5432",
    )


def get_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]
