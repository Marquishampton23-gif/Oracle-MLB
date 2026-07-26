from pathlib import Path
import sqlite3
import pandas as pd

DATA_FOLDER = Path("../data")
DB_PATH = Path("oracle.db")

def import_csvs():
    if not DATA_FOLDER.exists():
        print("No data folder found.")
        return

    conn = sqlite3.connect(DB_PATH)

    for csv_file in DATA_FOLDER.glob("*.csv"):
        print(f"Importing {csv_file.name}...")
        df = pd.read_csv(csv_file)
        table_name = csv_file.stem.replace("-", "_").replace(" ", "_")
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()
    print("✅ All CSV files imported.")

if __name__ == "__main__":
    import_csvs()
