import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "oracle.db"
SCHEMA_PATH = ROOT / "schema.sql"


def build_database():
    if not SCHEMA_PATH.exists():
        print("❌ schema.sql not found.")
        return

    with sqlite3.connect(DB_PATH) as conn:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()

    print("✅ Oracle database created successfully!")
    print(f"📁 Database: {DB_PATH}")


if __name__ == "__main__":
    build_database()
