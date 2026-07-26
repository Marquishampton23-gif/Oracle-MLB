import sqlite3
from pathlib import Path

DATABASE = Path("database/oracle.db")

def start_oracle():
    print("=" * 50)
    print("⚾ ORACLE MLB INTELLIGENCE ENGINE")
    print("Version: Alpha 0.1")
    print("=" * 50)

    if DATABASE.exists():
        print("✅ Database found:", DATABASE)
    else:
        print("⚠️ Database not found.")
        print("Run build_database.py to create it.")

    print("\nOracle is ready for development.")

if __name__ == "__main__":
    start_oracle()
