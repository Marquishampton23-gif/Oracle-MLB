import glob
import os
import pandas as pd


class MasterLoader:

    def __init__(self):
        self.data_folder = "data"

    def load_all(self):

        csv_files = glob.glob(os.path.join(self.data_folder, "*.csv"))

        database = {}

        for file in csv_files:

            print(f"Loading {os.path.basename(file)}")

            try:

                df = pd.read_csv(file)

                database[os.path.basename(file)] = df

            except Exception as e:

                print(f"Failed: {file}")
                print(e)

        return database