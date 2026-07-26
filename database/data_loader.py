"""
Oracle Data Loader
Version 1.0
"""

import csv
from pathlib import Path


class DataLoader:

    def __init__(self):
        self.database = Path(__file__).parent

    def load_csv(self, filename):

        file_path = self.database / filename

        with open(file_path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            return list(reader)

    def available_files(self):

        return [
            file.name
            for file in self.database.glob("*.csv")
        ]


if __name__ == "__main__":

    loader = DataLoader()

    print(loader.available_files())